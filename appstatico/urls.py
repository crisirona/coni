from django.urls import path
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('creardemanda/',login_required(views.crearDemanda),name='creardemanda'),
    path('right/',views.sidebarright, name='sidebarright'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('accounts/login/',LoginView.as_view(template_name='appstatico/login.html'),name='login'),
    path("logout", LogoutView.as_view(), name="logout"),
    path('crud/',login_required(views.crud),name='crud'),
    path('eliminardemanda/',login_required(views.eliminardemanda),name='eliminardemanda'),
    path('busqueda/',login_required(views.busqueda),name='busqueda'),
    path('eliminar/<int:id>/',login_required(views.eliminar),name='eliminar'),
    path('editar/<int:id>/',login_required(views.editar),name='editar'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)