from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import mixins, serializers
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework import generics

# Create your views here.

class GenericArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class GenericArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class MixinArticleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class MixinArticleDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ArticleList(APIView):
    def get(self, request,format=None ):
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles,many=True)
        return Response(serializers.data)
    
    def post(self, request,format=None):
        serializers = ArticleSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get_object(self,pk):
        try:
            return Article.objects.get(pk=pk)
    
        except Article.DoesNotExist:
            raise Http404

    def get(self, request,pk,format=None ):
        article = self.get_object(pk)
        serializers = ArticleSerializer(article)
        return Response(serializers.data)

    def put(self,request,pk,format=None):
        article = self.get_object(pk)
        serializers = ArticleSerializer(article,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        article = self.get_object(pk)
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET","POST"])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles,many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = ArticleSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializers = ArticleSerializer(article)
        return Response(serializers.data)

    elif request.method == "PUT":
        serializers = ArticleSerializer(article,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)