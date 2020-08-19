from rest_framework import serializers

from product.models import Product, Category

from e_shop.product.models import ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ProductSerializer, self).to_representation(instance)
        representation['image'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage

    def _get_image_url(self, obj):
        if object.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super(ProductImageSerializer, self).to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'