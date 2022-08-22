from funcionarios import models
from rest_framework import serializers


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = ['id', 'nome', 'email']

class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offers
        fields = ['id', 'medicament', 'type', 'price', 'status', 'id_request', 'quant']

    
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = ['id', 'email', 'nome', 'id_request']
