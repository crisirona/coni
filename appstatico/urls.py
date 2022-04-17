from django.urls import path
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('creardemanda/',views.crearDemanda,name='creardemanda'),
    path('right/',views.sidebarright, name='sidebarright'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('login/',LoginView.as_view(template_name='appstatico/login.html'),name='login'),
    path("logout", LogoutView.as_view(), name="logout"),
    path('crud/',views.crud,name='crud'),
    path('eliminardemanda/',views.eliminardemanda,name='eliminardemanda'),
    path('busqueda/',views.busqueda,name='busqueda'),
    path('eliminar/<int:id>/',views.eliminar,name='eliminar'),
    path('editar/<int:id>/',views.editar,name='editar'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)