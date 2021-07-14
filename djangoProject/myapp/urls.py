from django.urls import include, path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('uploads/', FileUpload.as_view(), name='upload'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)