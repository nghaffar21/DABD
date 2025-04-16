from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('producte/', include('producte.urls')),
    path('admin/', admin.site.urls),
]
