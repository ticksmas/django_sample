from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import Pessoa, Endereco

@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	lista = Pessoa.objects.all()
	html = "<ul>"
	for p in lista:
		html+=f"<li>{p.nome} (id={p.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def detalhar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	return HttpResponse(f"Detalhou {pessoa.nome} (id={pessoa.id})")

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def cadastrar(request):
	p = Pessoa(nome="Matheus", idade=21)
	p.save()
	return HttpResponse(f"{p.nome} cadastrado com sucesso (id={p.id})")