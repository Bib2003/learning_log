from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    # Include the URLs for user authentication
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html', next_page='learning_logs:index'),
        name='logout'),
    
]