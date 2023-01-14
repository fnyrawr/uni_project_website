"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("users/", include("User.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='about.html'), name='about'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('home', TemplateView.as_view(template_name='about.html'), name='home'),
    path('howto', TemplateView.as_view(template_name='howto.html'), name='howto'),
    path('downloads', TemplateView.as_view(template_name='downloads.html'), name='downloads'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
