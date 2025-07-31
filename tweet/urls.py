from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),

      # ✅ ADDED: Route for logged-in user's own tweets
    path('my-account/', views.my_account, name='my_account'),

    # ✅ ADDED: Public profile for other users
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]


 