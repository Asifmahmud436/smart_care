from rest_framework import serializers
from .import models
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']

        def save(self):
            username = self.validate_data['username']
            email = self.validate_data['email']
            first_name = self.validate_data['first_name']
            last_name = self.validate_data['last_name']
            password = self.validate_data['password']
            password2 = self.validate_data['confirm_password']
            # password milailam ar dekhlam same email exists kore kina onno kono user er 
            if password != password2:
                raise serializers.ValidationError({'error':'Password does not match.'})
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'error':'Email already exists'})
            # jodi shobkisu thik thake taile notun ekta account create korbo
            account = User(username = username,email=email,first_name=first_name,last_name=last_name)
            account.set_password(password)
            account.is_active = False
            account.save()
            return account


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)