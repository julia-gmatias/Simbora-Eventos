from django.shortcuts import render, get_object_or_404, redirect
from .models import Eventos

def listar_eventos(request):
    eventos = Eventos.objects.all().order_by('-data_criacao')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def detalhes_evento(request, pk):
    evento = get_object_or_404(Eventos, pk=pk)
    return render(request, 'eventos/detalhes_evento.html', {'evento': evento})

def criar_evento(request):
    if request.method == "POST":
        evento = Eventos(
            id_evento=request.POST.get('id_evento'),
            imagem_url=request.POST.get('imagem_url'),
            titulo=request.POST.get('titulo'),
            descricao=request.POST.get('descricao'),
            data_evento=request.POST.get('data_evento'),
            status=request.POST.get('status'),
            participantes=request.POST.get('participantes'),
            id_endereco_id=request.POST.get('id_endereco'),
            id_categoria_id=request.POST.get('id_categoria'),
        )
        evento.save()
        return redirect('lista-eventos')

    return render(request, 'eventos/form_evento.html')
