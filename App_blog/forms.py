from django import forms 
from App_blog.models import Blog, Comment, Likes

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("comment",)
