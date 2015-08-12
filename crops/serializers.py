from rest_framework import serializers

from .models import Crop, Category


class CropSerializer(serializers.ModelSerializer):

    # category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Crop
        fields = ('name', 'pk', 'plant_start_date', 'plant_end_date',
            'tier', 'transplant', 'direct_seed', 'category', 'notes')


class CategorySerializer(serializers.ModelSerializer):

    crops = CropSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'crops')

