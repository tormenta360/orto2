from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect	


from app.tipo_perfil.forms import Tipo_perfilForm,Tipo_perfilForm_consultar 
from app.tipo_perfil.models import TipoPerfil, FacialFrontal, PerfilTotal   
from app.tipo_perfil.models import PTercioInferioir, Sonrisa, CompetenciaLabial
from app.informacion.models import fichas

# Create your views here.

def tipo_perfil(request):
	return render(request, 'tipo_perfil/tipo_perfil.html')



def tipo_perfil_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:	
			if request.method == 'POST':
				form = Tipo_perfilForm(request.POST,initial={'fichas':ids.id})
				if form.is_valid():
					form.save()

				return HttpResponseRedirect('/denticion/aspectos/nuevo/%s/%s/' %(codi,num))
			else: 
				form = Tipo_perfilForm(initial={'fichas':ids.id})
				
		return render(request,'tipo_perfil/form_tipo_perfil.html', {'form':form,'codi':codi,'num':num})
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")




def tipo_perfil_list(request):
	tipo_perfil = TipoPerfil.objects.all().order_by('fichas')
	contexto = {'tipo_perfiles': tipo_perfil}
	return render(request,'tipo_perfil/tipo_perfil_list.html', contexto)




def tipo_perfil_edit(request,codi,num):
	str(codi)
	#try:
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	if ids:
		datos = TipoPerfil.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form = Tipo_perfilForm(instance=datos)
		else: 
			form = Tipo_perfilForm(request.POST, instance=datos)
			if form.is_valid():
				form.save()
			return redirect('/denticion/sagitales/editar/%s/%s' %(codi,num))
		return render(request, 'tipo_perfil/form_tipo_perfil.html',{'form':form,'num':num,'codi':codi})
	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	#except Exception, e:
	#	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

	



def tipo_perfil_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			datos = TipoPerfil.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = Tipo_perfilForm_consultar(instance=datos)
			else: 
				form = Tipo_perfilForm_consultar(request.POST, instance=datos)
				
				return HttpResponseRedirect('/denticion/aspectos/consultar/%s/%s/' %(codi,num))
			return render(request, 'tipo_perfil/form_tipo_perfil.html',{'form':form,'num':num,'codi':codi})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")





