from rest_framework import serializers

from movimentacao.models import Movimentacao


class MovimentacaoSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source="get_tipo_display")
    natureza = serializers.SerializerMethodField()
    saldo = serializers.SerializerMethodField()

    def get_natureza(self, instance):
        return instance.natureza

    def get_saldo(self, instance):
        return instance.saldo
    class Meta:
        model = Movimentacao
        fields = "__all__"

