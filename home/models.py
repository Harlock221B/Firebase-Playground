from django.db import models
import main

class Games(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250)

def inserir_dados(self):
    conexao.child('vendas').push(games)

def deletar_dados(self):
    conexao.child('vendas').delete(games)

def editar_dados(self):
    conexao.child('vendas').update(games)

def exibir_dados(self):
    dados = conexao.child('vendas').get()
    for linhas in valores.each():
        print(linhas.name())
        print(linhas.id())