from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from rest_framework import exceptions

'''Declaration'''
# class ArticleSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     description=serializers.CharField(max_length=400)

'''Serializing Shell'''
# from api.models import Article
# from api.serializers import ArticleSerializer
# article=Article(title='Devbits',decription='web dev event')
# serialized=ArticleSerializer(article)
# serialized.data

# from rest_framework.renderers import JSONRenderer
# json=JSONRenderer().render(serialized.data)
# print(json)

'''Deserializing Shell'''
# import io
# from rest_framework.parsers import JSONParser
# stream=io.BytesIO(json)
# data=JSONParser().parse(stream)
# data


'''Using Serializer type of serializer'''
'''saving model instances'''
# class ArticleSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     description=serializers.CharField(max_length=400) 
    # since serializers dont have text field

    # def create(self, validated_data=None):
    #     return Article.objects.create(**validated_data)

    # def update(self, instance, validated_data=None):
    #     print("update started")
    #     instance.title = validated_data.get('title',instance.title)
    #     instance.description = validated_data.get('description',instance.description)
    #     instance.save()
    #     return instance

'''Creation Shell'''
# from api.models import Article
# from api.serializers import ArticleSerializer
# serialized1=ArticleSerializer(data={'title':'Devbits1','description':'Web dev1'})
# serialized1.is_valid()
# serialized1.save()

'''Updating shell'''
# article=serialized1.save()
# serialized2=ArticleSerializer(article,data={'title':'Devbits2','description':'Web dev2'})
# serialized2.is_valid()
# serialized2.save()

# '''Using Model Serializer'''
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title', 'description')

#     '''validation'''
#     def validate_title(self, value):
#         if "#" in value:
#             raise exceptions.ValidationError(detail="can not include '#' in title")  
#         return value

#     '''serializer method field'''
#     # thumbnail=serializers.SerializerMethodField()
#     # def get_thumbnail(self,instance):
#     #         return 'Devbits workshop'
#     # class Meta:
#     #     model = Article
#     #     fields = '__all__'
    
# '''validation'''
# # serialized=ArticleSerializer(data={'title':'#Devbits','description':'Web dev'})
# # serialized.is_valid()
# # serialized.errors

'''Using HyperLinkedModelSerializer'''
# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Article
#         fields = ('__all__')

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