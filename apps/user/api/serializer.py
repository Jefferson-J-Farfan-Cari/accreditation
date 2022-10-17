from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.user.models import User, Role, Permission, CurriculumVitae


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name
        token['lastname'] = user.last_name
        token['email'] = user.email
        token['role'] = user.role.name
        token['role_id'] = user.role_id
        # token['permissions'] = list(user.role.permissions.values('id', 'name', 'path'))

        return token


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

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['role'] = RoleSerializer(obj, many=False)
        return super(UserSerializer, self).to_representation(obj)


# Role Serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = ('create_date', 'modified_date')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['permissions'] = PermissionSerializer(obj, many=True)
        return super(RoleSerializer, self).to_representation(obj)


# Permission Serializer
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        exclude = ('create_date', 'modified_date')


class CurriculumVitaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumVitae
        exclude = ('create_date', 'modified_date')
