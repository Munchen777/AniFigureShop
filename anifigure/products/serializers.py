from rest_framework import serializers


from products.models import Product, Category, ProductImage


"""

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product name")
    description = models.TextField(verbose_name="Product description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Product category")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product price")
    slug = models.SlugField(max_length=80, unique=True, db_index=True, verbose_name="Product slug")
    discount = models.SmallIntegerField(default=0, verbose_name="Product discount")
    archived = models.BooleanField(default=False, verbose_name="Product archived")
    available = models.BooleanField(default=True, verbose_name="Product available")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name="Product created by")
    updated_at = models.DateTimeField(verbose_name="Product updated at", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Product created at", auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity of product")

def product_images_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename
    )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_images_directory_path, default=None, blank=True, null=True,
                              verbose_name="Product Image")

"""


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
            # "category",
            # "order",
            # "discount",
            # "archived",
            # "available",
            # "created_by",
            # "updated_at",
            # "created_at",
            # "cart",
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
