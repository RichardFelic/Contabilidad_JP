from django.db import models
from django.utils import timezone
from SistCont.Enums import Season
from django.contrib import messages

# Create your models here.
   
class TipoMoneda(models.Model):
    descripcion = models.CharField(max_length=50)
    ultima_tasa_cambiaria = models.FloatField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
class TipoCuenta(models.Model):
    descripcion = models.CharField(max_length=50)
    origen = models.CharField(max_length=2, choices=[('DB', 'DB'), ('CR', 'CR')])
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
class CatalogoAuxiliares(models.Model):
    id_EC = models.CharField(max_length=10, unique=True, blank=True)
    descripcion= models.CharField(max_length=50)
    id_aux= models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], null=True)
    cuenta = models.CharField(max_length=50, null=True)
    origen = models.CharField(max_length=2, choices=[('DB', 'DB'), ('CR', 'CR')], null=True)
    fecha = models.DateField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.identificador
    
    def save(self, *args, **kwargs):
        if not self.id_EC:
            ult_obj = CatalogoAuxiliares.objects.order_by('-id').first()
            if ult_obj:
                ult_cod = ult_obj.id_EC
                num = int(ult_cod[2:])
                self.id_EC = 'EC{}'.format(num +1)
            else:
                self.id_EC = 'EC1'
        super(CatalogoAuxiliares, self).save(*args, **kwargs)


class Auxiliar(models.Model):
    id_EC = models.CharField(max_length=10, unique=True, default="EC1")
    id_aux = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], default=1)
    nombre_aux = models.CharField(max_length=50)
    cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, null=True)
    origen = models.CharField(max_length=2, choices=[('DB', 'DB'), ('CR', 'CR')], null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateField(default=timezone.now)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.id_EC:
            ult_obj = Auxiliar.objects.order_by('-id').first()
            if ult_obj:
                ult_cod = ult_obj.id_EC
                num = int(ult_cod[2:])
                self.id_EC = 'EC{}'.format(num +1)
            else:
                self.id_EC = 'EC1'
        super(Auxiliar, self).save(*args, **kwargs)

    
class CatalogoCuentas(models.Model):
    descripcion = models.CharField(max_length=50)
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)
    permite_transacciones = models.BooleanField(default=True)
    nivel = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])
    cuenta_mayor = models.CharField(max_length=50)
    balance = models.FloatField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

