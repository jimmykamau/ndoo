from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class TimeStampMixin(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True)
    date_modified = models.DateTimeField(
        auto_now=True)

    class Meta:
        abstract = True


class BucketList(TimeStampMixin):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        User, related_name='bucketlists')

    def __str__(self):
        return '{}'.format(self.name)


class BucketListItem(TimeStampMixin):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    bucketlist_id = models.ForeignKey(
        BucketList, related_name='items')

    def __str__(self):
        return '{}'.format(self.name)
