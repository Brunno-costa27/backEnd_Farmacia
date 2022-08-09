from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from funcionarios.api import viewsets
from funcionarios.api import viewsets as funcionariosviewsets
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

schema_view = get_schema_view(
   openapi.Info(
      title="Pharmacy API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

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
    # path('teste', viewsets.buscar_dados),
    # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
