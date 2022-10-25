from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from articles import serializers
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

# @api_view(['GET', 'POST'])
# def articleAPI(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         # article = articles[0]
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # print(request.data['title'])
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # article_data = {
    #     "title":article.title,
    #     "content":article.content,
    #     "created_at":article.created_at,
    #     "updated_at":article.updated_at
    # }
    # return Response(article_data)


class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def articleDetailAPI(request, article_id):
#     if request.method == 'GET':
#         # article = Article.objects.get(id=article_id)
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleSerializer(article, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         article = get_object_or_404(Article, id=article_id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class articleDetail(APIView):
    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)