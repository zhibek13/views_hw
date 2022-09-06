from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Company, Category, Item
from .serializers import CategorySerializer, ItemSerializer, CompanySerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class ItemGenericViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CompanyGenericViewSet(GenericViewSet, CreateModelMixin, ListModelMixin,UpdateModelMixin,
                            DestroyModelMixin, RetrieveModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer