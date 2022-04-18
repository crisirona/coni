from django.shortcuts import render,redirect
from django.db.models import Q
from .forms import DemandaForm,Registro,CustomUserCreationForm
from .models import Demanda


# Create your views here.
def index(request):
    return render(request,'appstatico/inicio.html')

def crearDemanda(request):
    
    if request.method == 'POST':
        demanda = DemandaForm(request.POST)
        # demandado = DemandadoForm(request.POST)
        # demandante = DemandanteForm(request.POST)
        
        if demanda.is_valid() :

          
            # demandado.demanda = Demanda.objects.last
            # demandado.demanda = Demanda.objects.last
            demanda.save()
            # demandado.save()
            # demandante.save()
            return redirect('index')
    else:
        demanda = DemandaForm()
        # demandado = DemandadoForm()
        # demandante = DemandanteForm()
    contexto={
        'demanda':demanda, 
        # 'demandado':demandado, 
        # 'demandante':demandante,
    }
    return render(request,'appstatico/creardemanda.html',contexto)

def sidebarright(request):
    return render(request,'appstatico/sidebar-right.html')

def signin(request):
    return render(request,'appstatico/login.html')
def signup(request):
    # contexto={
    #     'registro':CustomUserCreationForm()
    # }
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('index')
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request,'appstatico/registro.html',context)

def crud(request):
    demanda = Demanda.objects.all()
    contexto={
        'demanda':demanda
    }
    return render(request,'appstatico/crud.html',contexto)


def eliminardemanda(request):
    demanda = Demanda.objects.all()
    contexto={
        'demanda':demanda
    }
    return render(request,'appstatico/eliminardemanda.html',contexto)

def eliminar(request,id):
    demanda = Demanda.objects.get(id=id)
    demanda.delete()
    return redirect('index')

def editar(request,id):
    demanda = Demanda.objects.get(id=id)
    formulario = DemandaForm(request.POST or None, request.FILES or None, instance=demanda)
    contexto={
        'demanda':demanda,
        'formulario':formulario
    }
    return render(request,'appstatico/modificar.html',contexto)

def busqueda(request):
    busqueda = request.GET.get("buscar")
    demanda = Demanda.objects.all()
    if busqueda:
        demanda = Demanda.objects.filter(
            Q(id_demanda__icontains= busqueda)
        ).distinct()
        
    
    contexto={
        'demanda':demanda,
        
    }
    return render(request,'appstatico/busqueda.html',contexto)