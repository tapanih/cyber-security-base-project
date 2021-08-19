from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('add', views.add_post, name='add'),
    path('delete/<int:post_id>', views.delete_post, name='delete')
]
