from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('reg/', reg, name='reg'),
    path('login/', login_user, name='login'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('logout/', logout , name='logout'),
    path('forget',forget ,name='forget'),
    path('forget_otp',forget_otp ,name='forget_otp'),
    path('forget_pass',forget_pass ,name='forget_pass'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)