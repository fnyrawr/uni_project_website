from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.blogpost_list, name='blogpost-list'),
    path('show/<int:pk>/', views.blogpost_detail, name='blogpost-detail'),
    path('create/', views.BlogpostCreateView.as_view(), name='blogpost-create'),
    path('delete/<int:pk>/', views.BlogpostDeleteView.as_view(), name='blogpost-delete'),
    path('edit/<int:pk>', views.blogpost_edit, name='blogpost-edit'),
    path('delete/<int:pk>/image/<int:id>', views.image_delete, name='image-delete'),
]