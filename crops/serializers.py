from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Crop, Category


class CropSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Crop
        fields = ('name', 'pk', 'plant_start_date', 'plant_end_date',
            'tier', 'transplant', 'direct_seed', 'category', 'notes',
            'image', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('rest:crop-retrieve',
                kwargs={'pk': obj.pk}, request=request)
        }


class CategorySerializer(serializers.ModelSerializer):

    crops = CropSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'crops')
