from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('movimentacao/', include('movimentacao.urls'), name="movimentacao"),
    path('api/v1/', include('api.urls'), name="api"),
]
