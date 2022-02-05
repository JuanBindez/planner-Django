from django.contrib import admin
from django.urls import path, include
from .views import teste_planer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste_planer),
    path('planer/', include('planercasa.urls')),
    path('', include('planercasa.urls')),
    path('', include('planercasa.urls')),
]
