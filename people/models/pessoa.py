from django.db import models
from django.apps import apps

class PessoaDAO(models.Manager):
	def retorna_C(self):
		return self.filter(nome__startswith="C")

	def nova(nome, idade, data_nascimento, cpf,
		logradouro, numero, bairro, cep):
		p = Pessoa(nome=nome, idade=idade,
			data_nascimento = data_nascimento, cpf = cpf)
		end = Endereco(pessoa=p,
			logradouro=logradouro, numero=numero,
			bairro=bairro, cep=cep)
		p.save()
		end.save()
		return p

class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.IntegerField(default=0)
	data_nascimento = models.DateField(null=True)
	cpf = models.CharField(max_length=14, null=True)

	def __str__(self):
		return f"{self.nome} (id={self.id})"

	def detalhar(self):
		result = Endereco.objects.get(pessoa__id=self.id)
		if(result):
			return result

	objects = PessoaDAO()

class Endereco(models.Model):
	pessoa = models.ForeignKey("Pessoa", on_delete=models.CASCADE)
	logradouro = models.CharField(max_length=200)
	numero = models.IntegerField()
	bairro = models.CharField(max_length=100,null=True)
	cep = models.CharField(max_length=9)
	
	def __str__(self):
		detalhe = f"""{self.logradouro}, {self.numero}.
			Bairro {self.bairro}. CEP: {self.cep}
		"""
		return detalhe