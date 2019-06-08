"""djangoencuestas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path



from django.contrib.auth.models import User
from testing.models import Ticket, Category


from testing.views import UserViewSet, TicketViewSet, CategoryViewSet

from encuestas.views import UserViewSet, EncuestasViewSet, ProcedimientosViewSet, PacientesViewSet

from rest_framework import routers

from rest_framework_simplejwt import views as jwt_views



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'apitesting/users', UserViewSet)

# router.register(r'apitesting/tickets', TicketViewSet)

# router.register(r'apitesting/category', CategoryViewSet)


router.register(r'api/users', UserViewSet)

router.register(r'api/encuestas', EncuestasViewSet)

router.register(r'api/procedimientos', ProcedimientosViewSet)

router.register(r'api/pacientes', PacientesViewSet)



urlpatterns = [
    path('', include('nucleo.urls')),
    path('qr/', include('qr.urls')),
    path('encuestas/', include('encuestas.urls')),
    path('contactar/', include ('contactar.urls')), 
    path('push/', include ('notificaciones_push.urls')), 
    path('estadisticas/', include ('estadisticas.urls')), 
    path('admin/', admin.site.urls),

    #PARA LA APP REGISTROS

    path('accounts/', include('django.contrib.auth.urls')),
   
   
    
    # path('api/', include('encuestas.urls')),
    path(r'', include(router.urls)),
    # path(r'apitesting/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   
]







