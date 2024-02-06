from django.contrib import admin
from django.urls import path
from currency.views import get_current_usd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_current_usd/', get_current_usd, name='get_current_usd')
]
