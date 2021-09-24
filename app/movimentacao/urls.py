from django.urls import path

from . import views


movimentacao_list = views.MovimentacoesListView.as_view()

urlpatterns = [
    path("", movimentacao_list, name="movimentacao_list"),
    path(
        "upload/", 
        views.upload_movimentacao_view, 
        name="upload_movimentacao_view"
    ),
]