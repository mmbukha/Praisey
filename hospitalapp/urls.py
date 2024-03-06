from django.contrib import admin
from django.urls import path, include
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('details/', views.details, name='details'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('uploadimage/', views.uploadimage, name='upload'),
    path('show_image/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
