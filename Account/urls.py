from django.conf.urls import url, include
from rest_framework import routers
from Account import views
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', obtain_jwt_token),
    url(r'^users/', views.UserViewSet.as_view()),
]
