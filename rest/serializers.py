from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
   authors = serializers.JSONField()
   categories = serializers.JSONField(allow_null=True)
   class Meta:
      model = Post
      fields = '__all__'

