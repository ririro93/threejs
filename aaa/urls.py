from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    index,
    line,
)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('line/', line, name='line'),
]