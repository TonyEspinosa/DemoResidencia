from django.db import models

# Create your models here.
class m_lista(models.Model):
    id_lista = models.AutoField(primary_key = True, db_column='id_lista')

    nombre = models.CharField(max_length=250, null=True, verbose_name = "Nombre de la Lista")
    
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = "Creación")

    class Meta:
        verbose_name = "Lista"
        verbose_name_plural = "Listas"
        ordering = ["nombre"]
    
    def __str__(self) -> str:
        #return '%d %s %s' % (self.id_categoria, self.nombre, str(self.date_created))
        return self.nombre  # type: ignoree