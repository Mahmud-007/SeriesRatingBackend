from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True,'required':True}
                      }

        def create(self,validated_data):
            user=User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Series
        fields=('id','title','genre','description','rated_times','avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=('id','stars','user','series')