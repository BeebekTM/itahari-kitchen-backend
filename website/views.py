from rest_framework import viewsets
from .models import ContactUs
from .serializers import ContactSerializer
# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
     queryset = ContactUs.objects.all().order_by('-id')
     serializer_class = ContactSerializer
