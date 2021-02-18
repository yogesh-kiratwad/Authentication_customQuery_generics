from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from blog.models import post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated

# Create your views here.

class PostMyPermission(BasePermission):
    def has_object_permission(self,request,view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author  == request.user

class PostView(viewsets.ModelViewSet):
    # permission_classes = [PostMyPermission]
    serializer_class = PostSerializer

    def get_object(self,queryset=None, **kwargs):  #argument is captured here
        item = self.kwargs.get('pk')               # its saved in item
        return get_object_or_404(post, title=item) # it will match with pk with its post_title

    def get_queryset(self):  #custom queryset
        return post.objects.all()






# class PostList(generics.ListCreateAPIView):
#     queryset = post.postobjects.all()
#     serializer_class = PostSerializer
#     pass

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostMyPermission):
#     permission_classes = [PostMyPermission]
#     queryset = post.objects.all()
#     serializer_class = PostSerializer
#     # pass