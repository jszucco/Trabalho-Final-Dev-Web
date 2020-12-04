from django.db import models

# Create your models here.


class Promocao(models.Model):
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    loja = models.ForeignKey('lojas.Loja', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    cupom = models.CharField(max_length=30)
    destaque = models.BooleanField(default=False)

    class Meta:
        unique_together = ('produto', 'loja')

    def __str__(self):
        return str(self.produto)
