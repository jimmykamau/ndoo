from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from bucketlist.views import (
    IndexView, DashboardView,
    CreateBucketlistView, EditBucketlistView, DeleteBucketlistView,
    CreateBucketlistItemView, EditBucketlistItemView, DeleteBucketlistItemView)


urlpatterns = [
    url(r'^login/$', auth_views.login,
        {'template_name': 'index.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/$', CreateView.as_view(
        template_name='register.html',
        form_class=UserCreationForm,
        success_url='/login/'
    )),
    url(r'^$', IndexView.as_view()),
    url(r'^dashboard/$', DashboardView.as_view()),
    url(r'^create-bucketlist/$', CreateBucketlistView.as_view()),
    url(r'^edit-bucketlist/$', EditBucketlistView.as_view()),
    url(r'^delete-bucketlist/$', DeleteBucketlistView.as_view()),
    url(r'^bucketlist/(?P<id>[0-9]+)/items/$',
        CreateBucketlistItemView.as_view()),
    url(r'^bucketlist/items/(?P<item_id>[0-9]+)/$',
        EditBucketlistItemView.as_view()),
    url(r'^bucketlist/items/(?P<item_id>[0-9]+)/delete/$',
        DeleteBucketlistItemView.as_view()),
]
