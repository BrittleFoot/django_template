from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    permissions = serializers.SerializerMethodField()
    first_name = serializers.CharField()

    def get_permissions(self, user):
        all_user_permissions = user.user_permissions.all()
        for g in user.groups.all():
            all_user_permissions |= g.permissions.all()

        return list(all_user_permissions.values_list("codename", flat=True))

    class Meta:
        model = User
        fields = [
            "public_id",
            "username",
            "email",
            "permissions",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
