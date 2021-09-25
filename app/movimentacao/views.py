from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from .forms import MovimentacoesUploadForm
from .handlers.movimentacoes_reader import MovimentacoesFileHandle
from .models import Movimentacao


class MovimentacoesListView(ListView):
    model = Movimentacao
    template_name = "movimentacao/movimentacao_list.html"
    context_object_name = 'movimentacoes'
    ordering = ("cpf", "data")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        valores = ctx['movimentacoes'].first().get_valor_entradas_saidas()
        
        ctx.update({
            "recebido": valores['entradas'],
            "pago": valores['saidas']
        })
        return ctx


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


def get_movimentacao_info(request, id):
    movimentacao = get_object_or_404(Movimentacao, id=id)

    valores = movimentacao.get_valor_entradas_saidas()

    json_object = {
        "dono_loja": movimentacao.dono_loja,
        "nome_loja": movimentacao.nome_loja,
        "valor": movimentacao.valor,
        "cartao": movimentacao.cartao,
        "cpf": movimentacao.cpf_formatado,
        "data": movimentacao.data.strftime("%d/%m/%y %H:%M"),
        "natureza": movimentacao.natureza,
        "saldo": f"{movimentacao.saldo:.2f}",
        "recebido": valores['entradas'],
        "pago": valores['saidas']
    }

    return JsonResponse({
        "object": json_object,
        "status_code": 200,
        "success": True
    })