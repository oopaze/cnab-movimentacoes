from django.urls import path

from . import views


movimentacao_list = views.MovimentacoesListView.as_view()

urlpatterns = [
    path("", movimentacao_list, name="movimentacao_list"),
    path("<int:id>/", views.get_movimentacao_info, name="movimentacao_info"),
    path(
        "upload/", 
        views.upload_movimentacao_view, 
        name="upload_movimentacao_view"
    ),
]