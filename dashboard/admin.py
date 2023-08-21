from django.contrib import admin
from dashboard.models import Equipe, Regional, Loja, Suporte, Dashboard

# Register your models here.
@admin.register(Equipe)
class EquipesAdmin(admin.ModelAdmin):
    ...
@admin.register(Regional)    
class RegionaisAdmin(admin.ModelAdmin):
    list_display = 'nome', 'loja_atual', 'equipe', 'ativa'
    
@admin.register(Loja)
class LojasAdmin(admin.ModelAdmin):
    list_display = 'nome', 'concluida', 'regiao', 'equipe'
    list_per_page = 20
    

@admin.register(Suporte)
class SuporteAdmin(admin.ModelAdmin):
    ...

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    ...