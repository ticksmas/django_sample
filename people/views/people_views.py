from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader

from ..models import Pessoa, Endereco

@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	result = Pessoa.objects.all()
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	return HttpResponse(pessoa)

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def cadastrar(request):
	p = Pessoa(nome="Juca", idade="39")
	p.save()

	end = Endereco(pessoa=p, logradouro="Av do Contorno",
			numero=200, bairro="Centro", cep="31456-789")
	end.save()

	return HttpResponse(f"{p.nome} cadastrado com sucesso (id={p.endereco})")