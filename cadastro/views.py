from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import UnidadeForm
from .models import Unidade


#@login_required
def unidade_read(request):
    return render(request, "cadastro/unidade-read.html", {"unidades": Unidade.objects.all()})


#@login_required
def cadastrar_unidade(request):
    if request.method=="POST":
        form=UnidadeForm(request.POST)
        if form.is_valid():
            unidade=form.save(commit=False)
            unidade.sigla = request.POST.get('sigla')
            unidade.nome = request.POST.get('nome')
            unidade.created_by = request.user
            unidade.edited_by = request.user
            unidade.save()
            messages.add_message(request, messages.SUCCESS, "Unidade cadastrada com sucesso.")
            return(redirect("unidade-read"))        
    else:
        form=UnidadeForm()
    return render(request, 'cadastro/unidade-create.html', {'form': form})

def editar_unidade(request, id):
     unidade = get_object_or_404(Unidade, pk=id)
     if request.method == "POST":
         form = UnidadeForm(request.POST, instance=unidade)
         if form.is_valid():
             unidade = form.save(commit=False)
             unidade.sigla = request.POST.get('sigla')
             unidade.nome = request.POST.get('nome')
             unidade.edited_by = request.user
             unidade.save()
             return redirect('unidade-read')
     else:
         form = UnidadeForm(instance=unidade)
     return render(request, 'cadastro/unidade-update.html', {'unidade': unidade, 'form': form})
