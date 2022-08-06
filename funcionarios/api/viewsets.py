import email.message
import json
import smtplib
from re import U

import requests
from django.shortcuts import get_object_or_404
from funcionarios import models
from funcionarios.api import serializers
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from twilio.rest import Client

from ..models import Employees


class FuncionariosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.FuncionariosSerializer
    queryset = models.Employees.objects.all()
  
# Mostra todos os funcionários
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
@api_view()
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
@api_view(http_method_names=['POST'])
def add_offers(request):
    serializer = serializers.OffersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(http_method_names=['POST'])
def patient_message(request):
    # corpo_email = """
    # <p>Olá, Brunno</p>
    # <p>Mensagem da Farmácia xxxxx</p>
    # """
    data = request.data
    print(data['email'])
    corpo_email = """
    <p>Olá, Brunno</p>
    <p>Mensagem da Farmácia xxxxx</p>
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
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.login("sbrunno.costa@gmail.com", "neppkrhchairkaet")
    # server.sendmail(
    # "sbrunno.costa@gmail.com",
    # email['email'],
    # "Deu certo!")
    # server.quit()
    return Response({"sucess": "email"}, status=status.HTTP_200_OK)
    
