from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/', include('firstapp.urls'))
    path(route='',view=views.index, name='index')
]
