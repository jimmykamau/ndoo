from bucketlist.models import BucketList, BucketListItem
import factory


class BucketListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BucketList


class BucketListItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BucketListItem
