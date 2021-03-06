from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import ListView
from PIL import Image
from sorl.thumbnail import get_thumbnail

from .forms import ImageForm, ImageSizeForm
from .models import Picture


class IndexListView(ListView):
    """ Вывод главной страницы со списком изображений
    """
    template_name = 'index.html'
    context_object_name = 'index'

    def get_queryset(self):
        images = Picture.objects.all()
        return images


def new_image(request):
    """ Страница добавления нового изображения
    """
    form = ImageForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        image = form.save(commit=False)
        image.save()
        image_url = reverse('edit_image', args=(image.id,))
        return redirect(image_url)

    return render(request, 'new_image.html', {'form': form})


def edit_image(request, image_id):
    """ Страница изображения с формой изменения размеров
    """
    image = get_object_or_404(Picture, id=image_id)

    form = ImageSizeForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        width = form.cleaned_data.get('width')
        height = form.cleaned_data.get('height')

        image_url = image.image_file

        img = Image.open(image_url)
        img_ratio = float(img.size[0]) / img.size[1]

        if width is None:
            width = height * img_ratio
        elif height is None:
            height = width / img_ratio

        resized = get_thumbnail(image_url, f"{int(width)}x{int(height)}")
        image.image_file.save(resized.name, ContentFile(resized.read()), True)

        return render(
            request, 'single_image.html', {'item': image, 'form': form}
        )

    return render(
        request, 'single_image.html', {'item': image, 'form': form}
        )
