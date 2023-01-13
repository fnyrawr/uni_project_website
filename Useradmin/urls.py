from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/useradmin/signup
    path('signup/', views.SignUp.as_view(), name='signup'),
]