# ตามวิดีโอ ไฟล์นี้จะชื่อ serializers.py
# แต่สร้างให้ชื่อ มัน Unique หน่อยจะดีกว่า !!

from rest_framework import serializers

from profiles_api import models

# HelloSerializer
#---------------------------------------------------
class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing out APIView """
    name = serializers.CharField(max_length=10)


# UserProfileSerializer
#---------------------------------------------------
class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


# ProfileFeedItemSerializer
#---------------------------------------------------
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
