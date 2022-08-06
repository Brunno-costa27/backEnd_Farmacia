from funcionarios import models
from rest_framework import serializers


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = ['cpf', 'nome', 'senha']

class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offers
        fields = ['id', 'medicament', 'type', 'price', 'status', 'id_request']

    