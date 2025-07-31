from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accueil.urls' )),
    path('reservation/', include('reservation_en_ligne.urls', namespace='reservation_en_ligne')),
    path('commandes/', include('gestion_commande.urls', namespace='gestion_commande')),
    path('menu/', include('gestion_menus_plats.urls', namespace='gestion_menus_plats')),
    path('auth/', include('authentification.urls', namespace='authentification')),
    path('livraison/', include('livraison.urls', namespace='livraison')),




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)