
from django.contrib import admin
from django.urls import path
from Trombinoscoop.views import *

app_name="Trombinoscoop"
urlpatterns = [
    path('', login),
    path('login/', login),
    path('welcome/', welcome),
    path('admin/', admin.site.urls),
]