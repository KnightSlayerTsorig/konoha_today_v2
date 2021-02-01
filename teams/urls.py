from django.urls import path
from . import views
from django.conf.urls.static import static
from konoha_today import settings


urlpatterns = [
    path('', views.teams, name="teams"),
    path('team_5', views.team_5, name='team_5'),
    path('team_7', views.team_7, name='team_7'),
    path('team_10', views.team_10, name='team_10'),
    path('team_15', views.team_15, name='team_15')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
