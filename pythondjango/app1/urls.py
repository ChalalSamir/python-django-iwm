from django.urls import path
from . import views


app_name = 'app1'
urlpatterns = [
    path('' , views.index, name='index'),
    path('create' , views.create, name='create'),
    path('<id>/delete', views.delete, name='delete' ),
    path('<id>/update' , views.update, name='update'),
    path('<id>', views.detail_view, name='view_detail'),
]