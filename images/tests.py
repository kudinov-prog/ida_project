from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from django.test import Client, TestCase

from .models import Picture


class TestImages(TestCase):

    def setUp(self):

        self.client = Client()
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        self.picture = Picture.objects.create(
            image_url=None,
            image_file=uploaded
        )

    def test_check_img_tag(self):
        """ Проверяет страницу конкретной записи с
            картинкой: на странице есть тег <img>
        """
        url = reverse('edit_image', kwargs={'image_id': self.picture.id})
        response = self.client.get(url, follow=True)
        self.assertContains(response, text='<img', status_code=200, count=1)
