from django.shortcuts import render

# Paginas
def v_inicio(request):
	return render(request,'inicio.html', {})