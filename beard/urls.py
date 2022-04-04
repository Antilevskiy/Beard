from django.contrib import admin
from django.urls import path, include
from api.views import default_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', default_view),
    path('api/v1/', include('api.urls'))
]
