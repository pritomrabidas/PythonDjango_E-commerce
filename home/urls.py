from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('update', update, name='update'),
]

