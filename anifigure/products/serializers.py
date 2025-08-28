from rest_framework import serializers

from products.models import Product, Category, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = ["image"]
        extra_kwargs = {
            "image": {"read_only": True},
        }


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "description",
            "price",
            "slug",
            "quantity",
            "images",
            "currency",
        )
        read_only_fields = ["slug", "quantity", "images"]
        exclude_fields = [
            "category",
            "order",
            "discount",
            "archived",
            "available",
            "created_by",
            "updated_at",
            "created_at",
            "cart",
        ]
        extra_kwargs = {
            "pk": {"read_only": False},
        }

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)

        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)

        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        instance.pk = validated_data.get("pk", instance.pk)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()

        instance.images.all().delete()
        for image_data in images_data:
            ProductImage.objects.create(product=instance, **image_data)

        return instance

    def validate_category(self, attrs):
        category_pk = attrs.pk
        if not Product.objects.get(category=category_pk):
            raise serializers.ValidationError(f"product with {category_pk} does not exists!")

    def validate_slug(self, attrs):
        slug = attrs.slug
        if not Product.objects.filter(slug=slug).exists():
            raise serializers.ValidationError(f"Product with slug {slug} does not exist!")
        return attrs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
