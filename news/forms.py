from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content1','content2','note','image_title','image_1','image_2',)