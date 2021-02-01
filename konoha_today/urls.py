from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from konoha_today import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('teams/', include('teams.urls')),
                  path('activities', include('activities.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
