from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'password',
        ]

    def create(self, validated_data):
        user = User(email=validated_data['email'], role='subscriber')
        user.set_password(validated_data['password'])
        user.save()
        return user