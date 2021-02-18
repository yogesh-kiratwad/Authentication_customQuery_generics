from rest_framework import serializers
from blog.models import post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['id','title','content','slug','author','status']

