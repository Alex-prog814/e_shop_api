from rest_framework import viewsets


from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        parent_slug = self.request.query_params.get('parent')
        if parent_slug is not None:
            parent_slug = parent_slug.rstrip('/')
            queryset = queryset.filter(parent_id=parent_slug)
        return queryset



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}








#TODO related_product_in_category_details
#TODO add views for images
#TODO pagination
#TODO filtering
#TODO add_to_cart