from django.shortcuts import render
from Appentrega.models import *
from django.http import *
from Appentrega.forms import form_bcen , form_btor , form_beng

# Create your views here.
def inicio(request):
    return render(request, "Appentrega/padre.html")

def agregar_bcen(request):

    if request.method == "POST":

        nformu = form_bcen(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            Bomba_Cen = BCentri(
                modelo=info_ok["modelo"],
                materiales_carcaza=info_ok["materiales_carcaza"],
                materiales_voluta=info_ok["materiales_voluta"],
                presion=info_ok["presion"],
                caudal=info_ok["caudal"],
                altura=info_ok["altura"],
                temp=info_ok["temp"],
            )

            Bomba_Cen.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_bcen()

    return render(request, "Appentrega/NuevaBCent.html", {"MiFormulario":nformu})

def agregar_btor(request):
    
    if request.method == "POST":

        nformu = form_btor(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            Bomba_tor = Btornillo(
                modelo=info_ok["modelo"],
                materiales_carcaza=info_ok["materiales_carcaza"],
                materiales_tornillo=info_ok["materiales_tornillo"],
                presion=info_ok["presion"],
                caudal=info_ok["caudal"],
                altura=info_ok["altura"],
                temp=info_ok["temp"],
            )

            Bomba_tor.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_btor()
        
    return render(request, "Appentrega/NuevaBTor.html", {"MiFormulario2":nformu})

def agregar_beng(request):
    
    if request.method == "POST":

        nformu = form_beng(request.POST)

        if nformu.is_valid():

            info_ok = nformu.cleaned_data

            Bomba_eng = Bengranajes(
                modelo=info_ok["modelo"],
                materiales_carcaza=info_ok["materiales_carcaza"],
                materiales_engranajes=info_ok["materiales_engranajes"],
                presion=info_ok["presion"],
                caudal=info_ok["caudal"],
                altura=info_ok["altura"],
                temp=info_ok["temp"],
            )

            Bomba_eng.save()

            return render(request, "Appentrega/padre.html")
    else:

        nformu = form_beng()

    return render(request, "Appentrega/NuevaBEng.html",{"MiFormulario3":nformu})


def busqueda(request):
    return render(request, "Appentrega/busqueda.html")

def buscar_modelo(request):

    if request.method=="GET":

        presion_dada = request.GET["presion"]
        resultados_modelos = BCentri.objects.filter(presion__icontains=presion_dada)
    
        return render(request, "Appentrega/resultadobusqueda.html", {'DBusqueda':resultados_modelos})
    
    else:

        respuesta = "No enviaste datos"
        
    return HttpResponse(respuesta)
