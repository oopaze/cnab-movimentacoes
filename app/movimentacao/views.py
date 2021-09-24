from django.shortcuts import render

from .forms import MovimentacoesUploadForm
from .handlers.movimentacoes_reader import MovimentacoesFileHandle
from .models import Movimentacao


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

            # return redirect()

    context = {'form': form}

    return render(request, "movimentacao/movimentacao_form.html", context)