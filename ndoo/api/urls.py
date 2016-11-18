from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api.views import bucketlist_controls, bucketlistitem_controls, \
    UserRegisterAPIView


urlpatterns = [
    url(r'^auth/login/$', obtain_jwt_token),
    url(r'^auth/register/$', UserRegisterAPIView.as_view(), name='register'),
    url(r'^bucketlists/$', bucketlist_controls),
    url(r'^bucketlists/(?P<id>[0-9]+)/$', bucketlist_controls),
    url(r'^bucketlists/(?P<id>[0-9]+)/items/$',
        bucketlistitem_controls),
    url(r'^bucketlists/(?P<id>[0-9]+)/items/(?P<item_id>[0-9]+)/$',
        bucketlistitem_controls),
]
