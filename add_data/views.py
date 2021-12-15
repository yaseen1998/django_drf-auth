from django.shortcuts import render
from rest_framework import generics, permissions
from .serializer import AddSerializer
from .models import Add_data
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class AddListView(generics.ListCreateAPIView):
    serializer_class = AddSerializer
    queryset = Add_data.objects.all()

class DetailAddView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddSerializer
    queryset = Add_data.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    