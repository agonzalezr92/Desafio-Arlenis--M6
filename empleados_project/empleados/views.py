from django.shortcuts import render

def lista_empleados(request):
    empleados = ['Juan González', 'María Pérez', 'Angelina Fernández', 'Ana Torres','Emilio Ponce', 'Diego Torres', 'Julian Rodríguez']
    return render(request, 'empleados/lista.html', {'empleados': empleados})
