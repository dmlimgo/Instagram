from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name="list"),
    path('new/', views.create, name="create"),
    path('<int:posts_pk>/', views.detail, name="detail"),
    path('<int:posts_pk>/edit', views.edit, name="edit"),
    path('<int:posts_pk>/delete', views.delete, name="delete"),
]