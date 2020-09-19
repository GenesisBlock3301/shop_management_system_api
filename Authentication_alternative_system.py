
###### Model ########
class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_salesman = models.BooleanField(default=False)
    created_by = models.ForeignKey("self", on_delete=None, null=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.name

#------------------------------------------------------------------------------#

###### Serializer ########

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User object"""

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "name",
            "password",
            "is_owner",
            "is_manager",
            "is_salesman",
        )

        read_only_fields = ("id",)

    def create(self, validated_data):
        """creates user with encrypted password and retruns the user"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthtokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""

    username = serializers.CharField()
    password = serializers.CharField(
        style={
            "input_type": "password",
        },
        trim_whitespace=False,
    )

    def validate(self, data):
        """validate and authticate the user"""
        username = data.get("username")
        password = data.get("password")

        user = authenticate(
            request=self.context.get("request"), username=username, password=password
        )

        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        data["user"] = user
        return data

#------------------------------------------------------------------------------#

###### View ########
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from serializers import AuthtokenSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthtokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Retrive and return authenticated user"""
        return self.request.user