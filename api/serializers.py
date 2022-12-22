from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


'''Using Serializer type of serializer'''
# class ArticleSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     description=serializers.CharField(max_length=400) 
#     # since serializers dont have text field

#     def create(self, validated_data=None):
#         return Article.objects.create(validated_data=validated_data)

#     def update(self, instance, validated_data=None):
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title', 'description')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        token=Token.objects.create(user=user)
        print("key=",token.key)
        return user