from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .serializers import PostSerializer
from .models import Post
from django_filters.rest_framework import DjangoFilterBackend
from .custom_filters import PostFilter

import requests
import json


r_post = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')
r_update = requests.get('https://www.googleapis.com/books/v1/volumes?q=war')
json_post = r_post.json()
json_update = r_update.json()


class Book:
   def __init__(self, volumeInfo, **kwargs):
      self.title = volumeInfo.get('title')
      self.authors = volumeInfo.get('authors')
      self.published_date = volumeInfo.get('publishedDate')
      self.categories = volumeInfo.get('categories')
      self.average_rating = volumeInfo.get('averageRating')
      self.ratings_count = volumeInfo.get('ratingsCount')
      self.thumbnail = volumeInfo.get('imageLinks').get('thumbnail')

   @classmethod
   def from_json(cls, json_string):
      return cls(**json_string)#**json_string - passing everything from dict

data_post = []
def post_data():
   try:
      for x in json_post['items']:
         book = Book.from_json(x)
         data_post.append(book.__dict__)
      return data_post
   except Exception as e:
      print(str(e))

data_update = []
def update_data():
   try:
      for x in json_update['items']:
         book = Book.from_json(x)
         data_update.append(book.__dict__)
      return data_update
   except Exception as e:
      print(str(e))
# Create your views here.
class PostBooks(APIView):
   def get(self, request, *arg, **kwargs):
      data = post_data()
      serializer = PostSerializer(data = data, many = True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)

class UpdateBooks(APIView):
   def get(self, request, *arg, **kwargs):
      data = update_data()
      serializer = PostSerializer(data = data, many = True)
      print(serializer)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)

class AllBooks(generics.ListAPIView):
   serializer_class = PostSerializer
   queryset = Post.objects.all()
   filter_backends = [DjangoFilterBackend, OrderingFilter]
   filterset_class = PostFilter
   ordering_fields = ['published_date']



class FilteredBooksId(generics.ListAPIView):
   serializer_class = PostSerializer
   def get_queryset(self):
      id = self.kwargs['id']
      return Post.objects.filter(id=id)
   


# r_post = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')
# json_post = r_post.json()

# class Book:
#    def __init__(self, volumeInfo, **kwargs):
#       self.title = volumeInfo.get('title')
#       self.authors = volumeInfo.get('authors')
#       self.published_date = volumeInfo.get('publishedDate')
#       self.categories = volumeInfo.get('categories')
#       self.average_rating = volumeInfo.get('averageRating')
#       self.ratings_count = volumeInfo.get('ratingsCount')
#       self.thumbnail = volumeInfo.get('imageLinks').get('thumbnail')

#    @classmethod
#    def from_json(cls, json_string):
#       return cls(**json_string)

# data_post = []
# def post_data():
#    try:
#       for x in json_post['items']:
#          book = Book.from_json(x)
#          data_post.append(book.__dict__)
#       return data_post
#    except Exception as e:
#       print(str(e))


# class PostBooks(APIView):
#    def get(self, request, *arg, **kwargs):
#       data = post_data()
#       serializer = PostSerializer(data = data, many = True)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data)
#       return Response(serializer.errors)