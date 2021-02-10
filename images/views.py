from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.views.generic import ListView

from .models import Image
from .forms import ImageForm


class IndexListView(ListView):
    """ Вывод главной страницы с картинками
    """
    template_name = 'index.html'
    context_object_name = 'index'

    def get_queryset(self):
        images = Image.objects.all()
        return images


def new_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
            image_url = reverse('edit_image', args=(image.id,))
            return redirect(image_url)
        return render(request, 'new_image.html', {'form': form})
    form = ImageForm()
    return render(request, 'new_image.html', {'form': form})


def edit_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    form = ImageForm()
    return render(request, 'single_image.html', 
                 {'item': image, 'form': form})
