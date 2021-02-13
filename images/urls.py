from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('new', views.new_image, name='new_image'),
    path('edit_image/<int:image_id>', views.edit_image, name='edit_image'),
]
