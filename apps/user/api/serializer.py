from rest_framework import serializers

from apps.user.models import User, Role, Permission


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'last_login', 'is_superuser', 'is_staff', 'is_active')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


# Role Serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = ('create_date', 'modified_date')


# Permission Serializer
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        exclude = ('create_date', 'modified_date')
