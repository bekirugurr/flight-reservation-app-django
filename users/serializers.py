from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators=[validate_password],
        style={
            'input_type' :'password'
        }
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style={
            'input_type' :'password'
        }
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        )
    
    def validate(self, attr):
        if attr['password'] != attr['password2']:
            raise serializers.ValidationError(
                {'password' : 'Password fileds do not match'}
            )
        return attr

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


#! login de normalde sadece token key döner. Login olunca token key ile birlikte user bilgilerini de dönmesi için aşağıdaki kodu ekledim
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):    #! Burası önemli. Bu parantez ile birlikte üzerine yazmanın yanı sıra önceden var olanları inherit ettik
        fields =(
            'key',
            'user'
        )

