


from django.conf.urls import url, include

from rest_framework import  routers

from asset.rest_views import *
from asset.views import  eventlog_detail,eventlog_list

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'assets', AssetViewSet)
router.register(r'manufactories', ManufactoryViewSet)
router.register(r'userprofile', UserProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^eventlog_list/$', eventlog_list),
    url(r'^eventlog_detail/(\d+)/$', eventlog_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




