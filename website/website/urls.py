"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home, name="Home"),
    path('denoise/', view.denoise, name="denoise"),
    path('dehaze/', view.dehaze, name="dehaze"),
    path('process_video/', view.process_video, name="process_video"),
    path('process_video/denoise_vid/', view.denoise_video, name="denoise_video"),
    path('process_video/dehaze_vid/', view.dehaze_video, name="dehaze_video")

    # path('download/', view.download_denoise, name="download_denoise"),
    # path('download/', view.download_dehaze, name="download_dehaze")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
