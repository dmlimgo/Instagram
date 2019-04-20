from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('list/', views.list, name="list"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_update, name='profile_update'),
    path('<int:user_pk>/', views.detail, name="detail"),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('search/', views.search, name='search'),
]