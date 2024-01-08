
from django.contrib import admin
from django.urls import path
from Trombinoscoop.views import welcome

app_name="Trombinoscoop"
urlpatterns = [
    path('welcome/', welcome),
    path('admin/', admin.site.urls),
]