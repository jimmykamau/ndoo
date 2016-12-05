from django.contrib.auth.models import User
from rest_framework import serializers
from bucketlist.models import BucketList, BucketListItem


class BucketListSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = BucketList
        fields = '__all__'


class BucketListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketListItem
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer for User model having only the fields
    required for Registration"""

    # This field is not tied to any model. It is for server side authentication
    confirm_password = serializers.CharField(
        max_length=32, required=False, write_only=True)

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the
        # read-only fields
        fields = (
            'id', 'username',
            'password', 'confirm_password',
            'email', 'first_name', 'last_name'
        )
        required_fields = (
            'username',
            'password', 'confirm_password',
            'email', 'first_name', 'last_name'
        )
        read_only_fields = (
            'id', 'confirm_password'
        )

    def create(self, validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password')
        if password == confirm_password:
            user = User(
                email=validated_data['email'],
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        raise serializers.ValidationError(
            "Password and confirm_password don't match")
