from django.db import models
from django.contrib.auth.models import User


class Equipe(models.Model):
    nome = models.CharField(max_length=100)

    imagem = models.ImageField(null=True, blank=True, upload_to='equipes')
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

class Regional(models.Model):
    nome = models.CharField(max_length=100)
    loja_atual = models.CharField(max_length=100,blank=True,null=True,default=None)
    equipe = models.ForeignKey(Equipe,blank=True,null=True, on_delete=models.CASCADE, related_name='regional')
    ativa = models.BooleanField(default=False)

    def __str__(self):          
        return self.nome
    
    def loja_atual_valida(self):
        if self.loja_atual is None:
            return '---'
        return self.loja_atual
    
    
    class Meta:
        verbose_name = 'Regional'
        verbose_name_plural = 'Regionais'


class Loja(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    concluida = models.BooleanField(default=False)
    regiao = models.ForeignKey(Regional, blank=True, null=True, on_delete=models.CASCADE, related_name='lojas')
    equipe = models.ForeignKey(Equipe, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    def concluidas(self):
        total = Loja.objects.filter(concluida=True).filter(regiao__nome=self.regiao).count()
        return total
    
    def total_lojas_regiao(self):
        total_lojas = Loja.objects.all().filter(regiao__nome=self.regiao).count()
        return total_lojas
    
    def lojas_concluidas(self):
        lojas_concluidas = Loja.objects.all().filter(regiao__nome=self.regiao).filter(concluida=True)
        return lojas_concluidas
    
    def lojas_nao_concluidas(self):
        lojas_nao_concluidas = Loja.objects.filter(regiao__nome=self.regiao).filter(concluida=False)
        return lojas_nao_concluidas
    
    def percentual_concluido(self):
        total = Loja.objects.filter(concluida=True).filter(regiao__nome=self.regiao).count()
        total_lojas = Loja.objects.all().filter(regiao__nome=self.regiao).count()
        percentual = ((total/total_lojas)*100)
        return percentual
    
    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'

class Dashboard(models.Model):
    nome = models.CharField(max_length=100)
    regionais = models.ManyToManyField(Regional, blank=True)

    def __str__(self):
        return self.nome
    
    def percentual_concluidas(self):
        total_concluidas = Loja.objects.all().filter(concluida=True).count()
        total_nao_concluidas = Loja.objects.all().filter(concluida=False).count()
        percentual_geral = ((total_concluidas/total_nao_concluidas)*100)
        return percentual_geral
    
    class Meta:
        verbose_name = 'Dashboard'
        verbose_name_plural = 'Dashboards'

class Suporte(models.Model):
    nome = models.CharField(max_length=100)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    regiao = models.ForeignKey(Regional,blank=True, null=True, on_delete=models.CASCADE, related_name='suporte')
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Suporte'
        verbose_name_plural = 'Suportes'
    
    
    




