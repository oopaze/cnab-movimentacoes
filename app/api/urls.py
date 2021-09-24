from re import U
from django.urls import path
from django.urls.conf import include

from .views import MovimentacaoListApiView


movimentacao_url = [
    path("", MovimentacaoListApiView.as_view(), name="movimentacao_api_list")
]

urlpatterns = [
    path("movimentacao/", include(movimentacao_url), name="movimentacao")
]