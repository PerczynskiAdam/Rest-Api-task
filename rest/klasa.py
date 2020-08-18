import requests
import json


r = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')
r_dict = r.json()


string = r_dict['items'][0]
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

   def __repr__(self):
      return self.title

book1 = Book.from_json(string)
book2 = Book.from_json(string)

book1.__dict__
print(book)


y = []
def proba():
   try:
      for x in r_dict['items']:
         book = Book.from_json(x)
         y.append(book)
   except Exception as e:
      print(str(e))

