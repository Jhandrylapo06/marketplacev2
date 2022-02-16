from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from AppUsuario.models import Usuario
# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.titulo

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='productos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='subidas/',blank=True, null=True)
    miniatura =  models.ImageField(upload_to='subidas/',blank=True, null=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self) :
        return self.titulo

    def get_miniatura(self):
        if self.miniatura:
            return self.miniatura.url
        else:
            if self.imagen:
                self.miniatura = self.make_miniatura(self.imagen)
                self.save()

                return self.miniatura.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_miniatura(self, imagen, size=(300, 200)):
        img = Image.open(imagen)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        miniatura = File(thumb_io, name=imagen.name)

        return miniatura
