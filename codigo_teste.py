# Arquivo de teste com erros para o nosso revisor encontrar

numero_global = 10

def calcular_total(preco, imposto):
    global numero_global
    resultado = (preco * imposto) + numero_global
    return resultado

def saudar_usuario(nome):
    print(f"Olá, {nome}")
