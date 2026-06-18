from rest_framework import serializers
from .models import User, Brand, Category, Product, Inquiry, Order, OrderItem, BlogPost, GalleryItem

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone', 'address', 'role']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'products']

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True) # Handles the array of cart items

    class Meta:
        model = Order
        fields = ['id', 'user', 'full_name', 'phone', 'email', 'shipping_address', 'total_amount', 'payment_method', 'status', 'items', 'created_at']

    def create(self, validated_data):
        # Pop out the items list from the validated request data
        items_data = validated_data.pop('items')

        # Create the master order record first
        order = Order.objects.create(**validated_data)

        # Loop through the array and create individual items attached to this order
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
    

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = '__all__'