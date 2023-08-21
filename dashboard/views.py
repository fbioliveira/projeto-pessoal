from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dashboard.models import Equipe, Regional, Loja, Suporte, Dashboard

def index(request):

    context = {
        'projeto': Dashboard.objects.all(),
    }
    
    return render(request, 'index.html', context)

@login_required
def manutencao(request):
    
    projetos = Dashboard.objects.all()
    regiao = Regional.objects.filter(equipe__nome=request.user.suporte.equipe, ativa=True)
    lojas_regiao = []

    for loja in regiao[0].lojas.all():
        lojas_regiao.append(loja.nome)

    if regiao[0].loja_atual in lojas_regiao:
        return redirect('encerrar-manutencao')
    

    if request.method == 'POST':
        regiao = Regional.objects.get(equipe__nome=request.user.suporte.equipe, ativa=True)
        loja_ativa = request.POST['lojas']
        regiao.loja_atual = loja_ativa
        regiao.save()
        return redirect('encerrar-manutencao')

    return render(request, 'manutencao.html', {'projetos': projetos})

@login_required
def encerrar_manutencao(request):

    if request.method == 'POST':
        regiao = Regional.objects.get(equipe__nome=request.user.suporte.equipe, ativa=True)
        loja_encerrada = Loja.objects.get(nome=regiao.loja_atual)
        loja_encerrada.concluida = True
        print(loja_encerrada)
        loja_encerrada.save()
        regiao.loja_atual = None
        regiao.save()
        return redirect('manutencao') 


    return render(request, 'encerrar-manutencao.html')  

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Usuário não Existe.')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('Usuário ou senha está incorreto.')

    return render(request, 'login.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('index')