from rest_framework import serializers

from .models import Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = (
            "pk",
            "content",
            "is_active",
            "start_date",
            "end_date",
        )
