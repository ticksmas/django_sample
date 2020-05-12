from django.db import models

class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.IntegerField(default=0)
	data_nascimento = models.DateField(null=True)
	cpf = models.CharField(max_length=14, null=True)

	def __str__(self):
		detalhe = f"{self.nome} (id={self.id})"
		result = Endereco.objects.filter(pessoa__id=self.id)
		print(result)
		if(result):
			end = result[0]
			detalhe+= f" - Logradouro: {end.logradouro}"
		return detalhe

class Endereco(models.Model):
	pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	logradouro = models.CharField(max_length=200)
	numero = models.IntegerField()
	bairro = models.CharField(max_length=100,null=True)
	cep = models.CharField(max_length=9)