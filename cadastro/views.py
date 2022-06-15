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
    
    form = UnidadeForm()
    context = {'form': form}
    
    if request.method == 'POST':

        sigla = request.POST.get('sigla')
        nome = request.POST.get('nome')
    
        unidade = Unidade()
        unidade.sigla = sigla
        unidade.nome = nome
        unidade.created_by = request.user
        unidade.edited_by = request.user
        unidade.save()
    
        messages.add_message(request, messages.SUCCESS, "Unidade salva com sucesso.")

        return redirect(reverse("unidade-read"))

    return render(request, 'cadastro/unidade-create.html', context)



#@login_required
def editar_unidade(request, id):
    unidade = get_object_or_404(Unidade, pk=id)
    form = UnidadeForm(instance=unidade)
    context = {'unidade': unidade, 'form': form}
    erros = False

    if request.method == 'POST':
        
        sigla = request.POST.get('sigla')
        nome = request.POST.get('nome')

        if Unidade.objects.filter(nome=nome).exists():
            messages.add_message(request, messages.ERROR, "Este nome já existe.")
            erros = True
        
        if Unidade.objects.filter(sigla=sigla).exists():
            messages.add_message(request, messages.ERROR, "Esta sigla já existe.")
            erros = True

        if not erros:
            unidade.sigla = sigla
            unidade.nome = nome
            unidade.edited_at = timezone.now()
            #Somente quem criou poderá editar
            #if unidade.owner == request.user:
            unidade.save()
            form = UnidadeForm(instance=unidade)
            context['form'] = form

            messages.add_message(request, messages.SUCCESS, "Unidade atualizada com sucesso.")

            return redirect(reverse("unidades"))

        return render(request, 'unidade-update.html', context)

    return render(request, 'unidade-update.html', context)
