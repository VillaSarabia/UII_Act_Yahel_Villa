from django.shortcuts import render,HttpResponse
# Create your views here.
def index (request):
    productos = [
        {
            'nombre': 'Pikachu VMAX',
            'tipo': 'Eléctrico',
            'hp': 310,
            'rareza': 'Rara Secreta',
            'imagen': 'https://assets.pokemon.com/static-assets/content-assets/cms2-es-xl/img/cards/web/SWSH11/SWSH11_LA_TG17.png' # Reemplaza con URL de imagen real
        },
        {
            'nombre': 'Charizard VSTAR',
            'tipo': 'Fuego',
            'hp': 280,
            'rareza': 'Ultra Rara',
            'imagen': 'https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SWSH9/SWSH9_EN_18.png' # Reemplaza con URL de imagen real
        },
        {
            'nombre': 'Mewtwo V',
            'tipo': 'Psíquico',
            'hp': 220,
            'rareza': 'Rara Holo',
            'imagen': 'https://assets.pokemon.com/static-assets/content-assets/cms2-es-xl/img/cards/web/SWSHP/SWSHP_LA_SWSH223.png' # Reemplaza con URL de imagen real
        }
    ]
    contexto = {'productos': productos}
    return render(request, 'index.html', contexto)
