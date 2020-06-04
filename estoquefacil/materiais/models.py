from django.db import models
from django.core.validators import MinValueValidator


class Materiais(models.Model):
    material = models.CharField(max_length=300)
    datacompra = models.DateField()
    datavalidade = models.DateField()
    quantidade = models.IntegerField(validators=[MinValueValidator(0)])
    custo = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )

    def __str__(self):
        return self.material

    def custo_unitario(self):
        cu = self.custo/self.quantidade
        return cu
