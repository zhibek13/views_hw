"""my_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_app import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('item', views.ItemGenericViewSet, basename='item')
router.register('company', views.CompanyGenericViewSet, basename='company')
# router.register('category', views.CategoryGenericViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', views.CompanyGenericViewSet.as_view({
        'get':'list',
        'post':'create',
    })),
    path('<int:pk>/', views.CompanyGenericViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    path('create/', views.CategoryCreateAPIView.as_view()),
    path('list/', views.CategoryListAPIView.as_view()),
    path('update/<int:pk>/', views.CategoryUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', views.CategoryDestroyAPIView.as_view()),
    path('retrieve/<int:pk>/', views.CategoryRetrieveAPIView.as_view()),
]
