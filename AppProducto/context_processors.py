from AppProducto.models import Categoria

def menu_categorias(request):
    categorias = Categoria.objects.all()
    
    return{'menu_categorias': categorias}