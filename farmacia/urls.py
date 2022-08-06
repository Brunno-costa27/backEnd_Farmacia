from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from funcionarios.api import viewsets
from funcionarios.api import viewsets as funcionariosviewsets
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

route = routers.DefaultRouter()

route.register(r'autentication', funcionariosviewsets.FuncionariosViewSet, basename='autentication')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(route.urls)),
    path('employees', viewsets.employeesAll),
    path('create', viewsets.createEmployees),
    path('offers', viewsets.add_offers),
    path('email', viewsets.patient_message),
    path('detail/<int:pk>/', viewsets.employeeDetail),
    path('update/<int:pk>/', viewsets.updateEmployees),
    path('employee/<int:pk>/', viewsets.deleteEmployees),
    path('teste', viewsets.buscar_dados)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
