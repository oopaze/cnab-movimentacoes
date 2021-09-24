from django.urls import path

from . import views


urlpatterns = [
    path("upload/", views.upload_movimentacao_view, name="upload_cnab_view")
]