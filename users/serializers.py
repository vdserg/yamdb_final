from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role')
        model = User
        required_fields = ('username', 'email')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.email = self.validated_data['email']
        if user.role == 'moderator':
            user.is_staff = True
        elif user.role == 'admin':
            user.is_admin = True
        user.save()
        return user


class CreateAuthKeySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = ('email',)
        model = User


class CheckAuthKeySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    auth_code = serializers.CharField(required=True)

    class Meta:
        fields = ('email', 'auth_code')
        model = User
