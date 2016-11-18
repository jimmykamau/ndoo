from django.contrib import admin
from django.contrib.auth.models import User
from bucketlist.models import BucketList, BucketListItem


admin.site.register(
    (BucketList, BucketListItem))
