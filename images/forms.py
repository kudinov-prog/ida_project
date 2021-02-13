from django import forms
from .models import Addimage

from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.core.files import File

from urllib import request
import os

from django.core.exceptions import ValidationError

class ImageForm(forms.ModelForm):

    class Meta:
        model = Addimage
        fields = ['image_url', 'image_file']  

    def clean(self):
        super().clean()
        all_data = self.cleaned_data
        url = all_data['image_url']
        file_im = all_data['image_file']

        if not self.cleaned_data['image_url'] and not self.cleaned_data['image_file']:
            raise ValidationError('Заполните хотя бы одно поле')

        if self.cleaned_data['image_url'] and self.cleaned_data['image_file']:
            raise ValidationError('Заполните только одно из полей')
        
        
        if not file_im and url:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(url).read())
            all_data['image_file'] = File(img_temp, name=os.path.basename(url))
            all_data['image_url'] = url
            img_temp.flush()

        return all_data


class ImageSizeForm(forms.Form):
    width = forms.IntegerField(label='Ширина', required=False, min_value=1)
    height = forms.IntegerField(label='Высота', required=False, min_value=1)

    def clean(self):
        super().clean()
        if not self.cleaned_data['width'] and not self.cleaned_data['height']:
            raise ValidationError('Заполните хотя бы одно поле')
