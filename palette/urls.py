

from django.urls import path,include
from .views import create_color_palette, public_color_palettes,add_to_favorites,home,create,check_auth_status

urlpatterns = [
    # for rest api
    path('create', create_color_palette, name='create-color-palette'),
    path('public/', public_color_palettes, name='public-color-palettes'),
    path('<int:palette_id>/favorite/', add_to_favorites, name='add-to-favorites'),
    path('api-auth/status/', check_auth_status, name='check-auth-status'),  
    # for htmlpage
    path('api/public/', home, name='index'),
    path('api/create', create, name='create_palette'),
]
