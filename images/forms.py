from django import forms
from .models import Addimage

from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

from urllib import request
import os


class ImageForm(forms.ModelForm):

    class Meta:
        model = Addimage
        fields = ['image_url', 'image_file']  


class ImageSizeForm(forms.Form):
    width = forms.IntegerField(label='Ширина')
    height = forms.IntegerField(label='Высота')
