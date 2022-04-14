from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.db import models


class UserCreationSerializer(serializers.ModelSerializer):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(
            username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(
                detail="User with username exists")

        email_exists = User.objects.filter(username=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")

        phonenumber_exists = User.objects.filter(
            username=attrs['phone_number']).exists()

        if phonenumber_exists:
            raise serializers.ValidationError(
                detail="User with phonenumber exists")

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
        )

        user.set_password(validated_data['password'])

        user.save()

        return user
