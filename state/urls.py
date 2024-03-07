from django.contrib import admin
from django.urls import path, include

from .views import home, FlatList, FlatCategoryDetail, FlatCreate, FlatUpdate, FlatDelete, ManagerList, ManagerDelete, \
    ManagerCreate, ManagerUpdate



urlpatterns = [
    path('', home, name='home'),
    path('flats/', FlatList.as_view(), name='flat_list'),
    path('flats/<int:pk>/', FlatCategoryDetail.as_view(), name='flat_detail'),
    path('flats/create/', FlatCreate.as_view(), name='create-flat'),
    path('flat/<int:pk>/update/', FlatUpdate.as_view(), name='update-flat'),
    path('flat/<int:pk>/delete/', FlatDelete.as_view(), name='delete-flat'),
    path('managers/', ManagerList.as_view(), name='manager_list'),
    path('managers/create/', ManagerCreate.as_view(), name='create-manager'),
    path('manager/<int:pk>/update/', ManagerUpdate.as_view(), name='update-manager'),
    path('manager/<int:pk>/delete/', ManagerDelete.as_view(), name='delete-manager')
]
