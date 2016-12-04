from django.forms import ModelForm

from bucketlist.models import (
    BucketList, BucketListItem)


class BucketListForm(ModelForm):
    class Meta:
        model = BucketList
        fields = ('name', 'description')


class BucketListItemForm(ModelForm):
    class Meta:
        model = BucketListItem
        fields = ('name', 'description')
