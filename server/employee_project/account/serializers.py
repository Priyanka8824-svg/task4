from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

def UniqueEmailValidator( email ):
	if not User.objects.filter( email=email ).exists():
		return email
	raise ValidationError("User with this email already exists.")


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField( validators=[ UniqueEmailValidator ] )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'is_superuser')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)