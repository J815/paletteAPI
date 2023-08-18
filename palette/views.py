from django.shortcuts import render,get_object_or_404


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import ColorPalette,UserFavorite
from .serializers import ColorPaletteSerializer


@api_view(['GET'])
def check_auth_status(request):
    if request.user.is_authenticated:
        return Response({"authenticated": True, "username": request.user.username})
    else:
        return Response({"authenticated": False})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_color_palette(request):
    if request.method == 'POST':
        data = request.data.copy()
        data['user'] = request.user.id  # Associate the logged-in user
        serializer = ColorPaletteSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        return render(request, 'create_palette.html')  # Render the HTML template

@api_view(['GET'])
def public_color_palettes(request):
    palettes = ColorPalette.objects.filter(is_public=True)
    serializer = ColorPaletteSerializer(palettes, many=True)
    return Response(serializer.data)

def home(request,*args,**kwargs):
    return render(request,"api/index.html")

def create(request,*args,**kwargs):
    return render(request,"api/create_palette.html")


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_favorites(request, palette_id):
    palette = get_object_or_404(ColorPalette, pk=palette_id)
    
    user_palette, created = UserFavorite.objects.get_or_create(user=request.user, palette=palette)
    
    if created:
        return Response({"detail": "Palette added to favorites."}, status=201)
    else:
        return Response({"detail": "Palette is already in favorites."}, status=400)