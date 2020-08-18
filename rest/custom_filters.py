from django_filters import rest_framework as filters
from .models import Post

# class CustomSearchFilter(filters.SearchFilter):
#    def get_search_fields(self, view, request):
#       if request.query_params.get('authors', 'id'):
#          return ['authors', 'id']
#       return super(CustomSearchFilter, self).get_search_fields(view, request)

class PostFilter(filters.FilterSet):
   authors = filters.CharFilter(lookup_expr='icontains')
   class Meta:
      model = Post
      fields = ['published_date']