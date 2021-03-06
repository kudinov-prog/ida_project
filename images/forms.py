import os
from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django import forms
from django.core.exceptions import ValidationError
from django.core.files import File

from .models import Picture


class ImageForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['image_url', 'image_file']

    def clean(self):
        super().clean()
        content = self.cleaned_data
        url = content['image_url']
        file_im = content['image_file']

        if not url and not file_im:
            raise ValidationError('Заполните хотя бы одно поле')

        if url and file_im:
            raise ValidationError('Заполните только одно из полей')

        if not file_im and url:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(url).read())
            content['image_file'] = File(img_temp, name=os.path.basename(url))
            content['image_url'] = url
            img_temp.flush()

        return content


class ImageSizeForm(forms.Form):
    width = forms.IntegerField(label='Ширина', required=False, min_value=1)
    height = forms.IntegerField(label='Высота', required=False, min_value=1)

    def clean(self):
        super().clean()
        if not self.cleaned_data['width'] and not self.cleaned_data['height']:
            raise ValidationError('Заполните хотя бы одно поле')
