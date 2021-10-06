from django.urls import path

from . import views
# Create your views here.
urlpatterns = [
  path('', views.index, name='index'),
  path('add', views.form_create, name='form_create'),
  path('<int:id>/add_user', views.add_user, name='add_user'),
  path('create_travel', views.create_travel, name='create_travel'),
  path('destination/<int:id>', views.show_travel, name='show_travel'),

]