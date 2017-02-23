from django.conf.urls import url, include
from rest_framework import routers
from Teams import views

router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'teams/(?P<team_id>[0-9]+)/players', views.PlayerViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]