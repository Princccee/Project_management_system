from django.urls import path
from . import views # from the currenct directory import views.py file
from django.conf import settings 
from django.conf.urls.static import static

app_name = 'core' # Set the app name i.e. core

# Design the URLs pattern
urlpatterns = [
    path('', views.index, name='index'), # to home page
    path('dashboard/', views.dashboard, name='dashboard'), # to dashboard page
    path('login/', views.login_view, name='login'),  # to login page
    path('logout/', views.logout_view, name='logout'), # to logout
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)