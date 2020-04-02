from rest_framework import serializers
from .models import Post

class FormAPI(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content1', 'content2', 'note', 'image_title', 'image_1', 'image_2',)