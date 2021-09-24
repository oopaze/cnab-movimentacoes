from rest_framework.generics import ListAPIView
from django.shortcuts import render

from movimentacao.models import Movimentacao
from .serializers import MovimentacaoSerializer


class MovimentacaoListApiView(ListAPIView):
    serializer_class = MovimentacaoSerializer
    queryset = Movimentacao.objects.all().order_by("cpf", "data")