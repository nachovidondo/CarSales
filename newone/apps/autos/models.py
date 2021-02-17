from apps.base.models import BaseModel
from django.db import models

# Create your models here.
class Category(BaseModel):
    description = models.CharField(max_length=50,verbose_name="Descripcion",blank=True,null=True)
    class Meta:
        verbose_name ="Categoria"
        verbose_name_plural= "Categorias"
    def __str__(self):
        return self.description
    
class Importation(BaseModel):
    country= models.CharField(max_length=100,verbose_name="País de Origen",blank=True,null=True)
    class Meta:
        verbose_name ="Importacion"
        verbose_name_plural="Importaciones"
    def __str__(self):
        return self.country
    
class Car(BaseModel):
    brand = models.CharField(max_length=150, verbose_name ="Marca")
    model = models.IntegerField(verbose_name="Modelo")
    colour = models.CharField(verbose_name="Color",max_length=100)
    price = models.IntegerField(verbose_name="Precio",default="error")
    category_car = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Categoria",blank=True,null=True)
    importation_car = models.ForeignKey(Importation,on_delete=models.CASCADE,verbose_name="Importacion",blank=True,null=True)
    class Meta:
        verbose_name ="Auto"
        verbose_name_plural ="Autos"
    def __str__(self):
        return self.brand