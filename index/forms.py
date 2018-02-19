from django import forms

from .models import Post
from .models import Images


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)

    class Meta:
        model = Post
        fields = ('title', )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required = False)
    class Meta:
        model = Images
        fields = ('image', )
