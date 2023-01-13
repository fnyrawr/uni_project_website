from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.CustomSignUpView.as_view(), name='signup'),
    path('show/', views.UserListView.as_view(), name='userlist'),
    path('verify-email/<uidb64>/<token>',
         views.verify_email, name='verify'),
]