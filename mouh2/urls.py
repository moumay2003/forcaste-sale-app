from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path('chat/', views.chat_view, name='chat'),
    path('', views.loginPage, name='log'),
    path('logout/', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('home', views.index, name='home'),
    path('stat', views.stat, name='stat'),
    path('display/', views.display_image, name='display_image'),
    path('predict/', views.predict, name='predict'),
    path('display2/', views.display_image2, name='display_image2'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)