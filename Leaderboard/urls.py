from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("api", views.LeaderboardView, basename="LeaderboardViewRoute")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('show/', views.leaderboard_list, name='leaderboard-list'),
    path('delete/<int:pk>/', views.LeaderboardDeleteView.as_view(), name='leaderboard-delete'),
]