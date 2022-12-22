from django.shortcuts import render,HttpResponse
from .models import Article
from .serializers import ArticleSerializer
import io,json

#  for serializing and deserializing
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

#  for simple request methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#  for api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# for APIView
from rest_framework.decorators import APIView

# for mixins
from rest_framework import mixins,generics

#  for viewsets
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



#  for authentication of each api
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#  for user registration
from django.contrib.auth.models import User
from .serializers import UserSerializer






# Create your views here.

def Index(request):
    return HttpResponse('The server is runnning')

# using the serializer to serialize the data
def new(request):
    a=Article(title="New Article",description="New Description")
    a.save()
    serialized=ArticleSerializer(a)
    print("Serializer Data=",serialized.data)

    return HttpResponse("Done")

#  using serializer to deserialize the data
def new1(request):
    a=Article(title="New Article part2",description="New Description part 2")
    a.save()
    serialized=ArticleSerializer(a)

    #  JSONRwenderer converts the serizlized dta (dictionary) into json format
    y= JSONRenderer().render(serialized.data)
    # y is now a json 


    #  JSONParser is used to convert json to dictionary 
    stream=io.BytesIO(y)
    data=JSONParser().parse(stream)
    deserialized=ArticleSerializer(data=data)

    print("validated=",deserialized.is_valid())
    print("validated=",deserialized._validated_data)

    print("Serialized=",serialized)
    print("Deserialized=",deserialized)

    return HttpResponse(y)




'''using simple request.method way to create apis'''
# @csrf_exempt
# def article_list(request):
    
#     #  get all articles
#     if request.method == 'GET':
#         print("Request=",request)
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
#     elif request.method == 'POST':
#         print("Request=",request)
#         data=JSONParser().parse(request)
#         serializer=ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save() 
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)




# @csrf_exempt
# def article_details(request,id=None):
#     try:
#         article=Article.objects.get(pk=id)
    
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer=ArticleSerializer(article)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         data=JSONParser().parse(request)
#         serializer=ArticleSerializer(article,data=data)

#         if serializer.is_valid():
#             serializer.save() 
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse("Deletion done",status=204)




'''using api_view functional component'''

# @api_view(['GET','POST'])
# def article_list(request):
    
#     #  get all articles
#     if request.method == 'GET':
#         print("Request=",request)
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         print("Request=",request)
#         # data=JSONParser().parse(request)
#         serializer=ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def article_details(request,id=None):
#     try:
#         article=Article.objects.get(pk=id)
    
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer=ArticleSerializer(article,data=request.data)

#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response("Deletion done")


'''using APIView class based component'''

# class ArticleList(APIView):
#     def get(self, request):
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer=ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetails(APIView):
#     def get_object(self,id):
#         try:
#             article=Article.objects.get(pk=id)
#             return article
        
#         except Article.DoesNotExist:
#             # print("Do not exist")
#             return None

#     def get(self,request,id):
#         article=self.get_object(id)    
#         if article is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def put(self,request,id):
#         article=self.get_object(id)
#         if article is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=ArticleSerializer(article,data=request.data)

#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         article=self.get_object(id)
#         if article is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         article.delete()
#         return Response("Deletion done")



'''using mixins(generics) for api writing'''

# class ArticleList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)


'''method 1'''
# class ArticleDetails(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer

#     lookup_field='id'

#     def get(self,request,id):
#         return self.retrieve(request,pk=id)

#     def put(self,request,id):
#         return self.update(request,pk=id)

#     def delete(self,request,id):
#         return self.destroy(request,pk=id)

'''method 2'''
# class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer

#     lookup_field='id'

#     def get(self,request,id):
#         return self.retrieve(request,pk=id)

#     def put(self,request,id):
#         return self.update(request,pk=id)

#     def delete(self,request,id):
#         return self.destroy(request,pk=id)


'''viewsets.Viewset method'''

# class ArticleViewSet(viewsets.ViewSet):

#     def list(self,request):
#         article=Article.objects.all()
#         serializer=ArticleSerializer(article,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def create(self,request):
#         serializer=ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self,request,pk=None):
#         '''m1'''
#         # try:
#         #     article=Article.objects.get(pk=pk)
#         # except Article.DoesNotExist:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)

#         '''m2'''
#         queryset=Article.objects.all()
#         article=get_object_or_404(queryset,pk=pk)

#         serializer=ArticleSerializer(article)
#         return Response(serializer.data,status=status.HTTP_200_OK)


'''viewsets.GenericViewSet'''
# class ArticleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer

'''viewsets.ModelViewSet'''
class ArticleViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)






'''user viewset for registration'''

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer