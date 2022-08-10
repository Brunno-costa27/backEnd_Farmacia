import email.message
import json
import smtplib
from re import U

import requests
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from funcionarios import models
from funcionarios.api import serializers
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Employees

# from twilio.rest import Client



class FuncionariosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.FuncionariosSerializer
    queryset = models.Employees.objects.all()
  
# Mostra todos os funcionários
# @swagger_auto_schema()
@api_view(http_method_names=['GET'])
def employeesAll(request):
    # Código que manda email para os pacientes
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.login("sbrunno.costa@gmail.com", "neppkrhchairkaet")
    # server.sendmail(
    # "sbrunno.costa@gmail.com",
    # "sbrunno.costa@gmail.com",
    # "Deu certo!")
    # server.quit()
    users = Employees.objects.all()
    serializer = serializers.FuncionariosSerializer(instance=users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Busca um funcionario
@api_view(http_method_names=['GET'])
def employeeDetail(request, pk):
    # user = get_object_or_404(
    #     User.objects.all(), pk=pk
    # )
    # serializer = serializers.FuncionarioSerializer(instance=user)
    # print(serializer.data)
    # return Response(serializer.data)
    user = Employees.objects.all().filter(pk=pk).first()
    # print(user)
    if user:
        serializer = serializers.FuncionariosSerializer(instance=user, many=False)
        return Response(serializer.data)
    else:
        return Response({
            'message': 'errou'
        },status=status.HTTP_400_BAD_REQUEST)

# Cria um funcionario
@swagger_auto_schema(method='POST', request_body=serializers.FuncionariosSerializer)
@api_view(http_method_names=['POST'])
def createEmployees(request):
    serializer = serializers.FuncionariosSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

# Atualiza um funcionário
@api_view(http_method_names=['POST'])
def updateEmployees(request, pk):
    print(request.data)
    user = Employees.objects.all().filter(pk=pk).first()
    serializer = serializers.FuncionariosSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

# Deleta um funcionário
@api_view(http_method_names=['DELETE'])
def deleteEmployees(request, pk):
    user = Employees.objects.get(pk=pk)
    # print(user)
    # serializer = serializers.FuncionariosSerializer(instance=user, data=request.data)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    # user = Employees.objects.get(pk=pk)
    # user.delete
    # return Response("deu certo", status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def buscar_dados(request):
    request = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    todos = json.loads(request.content)
    print(todos)
    return Response(todos, status=status.HTTP_200_OK)

# adicionar ofertas no banco da farmácia
@swagger_auto_schema(method='POST', request_body=serializers.OffersSerializer)
@api_view(http_method_names=['POST'])
def add_offers(request):
    serializer = serializers.OffersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

# @swagger_auto_schema(method='POST', request_body=)
@api_view(http_method_names=['POST'])
def patient_message(request):
    # corpo_email = """
    # <p>Olá, Brunno</p>
    # <p>Mensagem da Farmácia xxxxx</p>
    # """
    data = request.data
    nome = data['nome']
    medicament = data['medicament']
    print(data['email'])
    print(data['nome'])
    print(data['medicament'])
    corpo_email = f"""
    <p>Olá, {nome}</p>
    <p>Você solicitou o medicamento {medicament}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Solicitações de remédio"
    msg['From'] = 'sbrunno.costa@gmail.com'
    msg['To'] = data['email']
    password = 'neppkrhchairkaet' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

    serializer = serializers.EmailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({"sucess": "email"}, status=status.HTTP_200_OK)
    
