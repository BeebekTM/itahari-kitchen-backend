from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, SAFE_METHODS, BasePermission
from .models import User, Brand, Category, Product, Inquiry, Order, BlogPost, GalleryItem
from .serializers import (UserRegistrationSerializer, BrandSerializer, CategorySerializer, 
                        ProductSerializer, InquirySerializer, OrderSerializer, BlogPostSerializer,
                        GalleryItemSerializer)
from .permissions import IsAdminOrReadOnly

class AuthViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account registered cleanly!"})
        return Response(serializer.errors, status=400)

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    # Custom action to quickly fetch your frontend's active deal banner items
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def deals(self, request):
        active_deals = Product.objects.filter(is_deal_of_the_day=True, is_available=True)
        serializer = self.get_serializer(active_deals, many=True)
        return Response(serializer.data)
    

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all().order_by('-created_at')
    serializer_class = InquirySerializer

    # Security: Anyone can submit an inquiry, but only the admin can view the list
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()] # Public checkout submission
        return [IsAdminUser()]  # Only admin can view all order histories globally
    

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    

# Add these at the very bottom of restaurant/views.py

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminOrReadOnly]


class GalleryItemViewSet(viewsets.ModelViewSet):
    queryset = GalleryItem.objects.all().order_by('-created_at')
    serializer_class = GalleryItemSerializer
    permission_classes = [IsAdminOrReadOnly]