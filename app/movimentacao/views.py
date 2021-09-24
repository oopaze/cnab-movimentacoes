from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import MovimentacoesUploadForm
from .handlers.movimentacoes_reader import MovimentacoesFileHandle
from .models import Movimentacao


class MovimentacoesListView(ListView):
    model = Movimentacao
    template_name = "movimentacao/movimentacao_list.html"
    paginate_by = '10'
    context_object_name = 'movimentacoes'
    ordering = "cpf"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx

    def get_queryset(self):
        return super().get_queryset()


def upload_movimentacao_view(request):
    form = MovimentacoesUploadForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            file = request.FILES.get("file")
            file_handle = MovimentacoesFileHandle(file)
            movimentacoes = file_handle.handle_movimentacoes()

            instances = []

            for movimentacao in movimentacoes:
                instances.append(
                    Movimentacao(**movimentacao)
                )

            Movimentacao.objects.bulk_create(instances)

            return redirect("movimentacao_list")

    context = {'form': form}

    return render(request, "movimentacao/movimentacao_form.html", context)