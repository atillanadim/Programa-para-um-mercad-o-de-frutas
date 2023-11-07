#Exercicio em Python 

#Vende 4 tipos de fruta: Bananas 0,99 Euros por kg, Kiwis 2,22 Euros por kg, Laranjas 1,25 Euros por kg e 1,75 euros por kg.
#para cada cliente ler o nome, onumero de frutas que comprou e a quantidade de cada uma
#calcular o valor total da compra e o valor a pagar
# acabar com o cliente fim 
#escrever o nome do cliente que mais pagou e o valor que ele pagou, quantos clientes foram processados e qual foi a media em kg

#####print("***Algoritmo Frutaria***")
print("**AlgoritmoFrutaria***")

frutas = {
    "banana": 0.99,
    "kiwi": 2.22,
    "laranja": 1.25,
    "pessego": 1.75
}
#iniciar clientes e total da compra 
clientes = []
total_compra_clientes = []

while True:
    nome = input("Qual o nome do cliente (ou 'Fim' para encerrar): ")
    if nome == "Fim":
        break

    total_cliente = 0
    quantidade_kg_total = 0

    numero_frutas = int(input("Quantas frutas o cliente comprou?"))

    for _ in range(numero_frutas):
        nome_fruta = input("Qual o nome da fruta?").lower()
        quantidade = float(input(f"Quantos kgs de {nome_fruta} o cliente comprou?"))
        #caso o nome da fruta estiver no dicionario faça assim
        if nome_fruta in frutas:
          #guardar o custo da fruta com o nome na variavel custo
            custo_fruta = frutas[nome_fruta]
          #somando o total da compra do cliente
            total_cliente += quantidade * custo_fruta
            quantidade_kg_total += quantidade
    #colocar o total da compra do cliente no final da lista       
    total_compra_clientes.append(total_cliente)

    #criando o dicionario para cliente com o nome do cliente e o total da compra e a quantidade em kg
    clientes.append({
        "nome": nome,
        "total_compra": total_cliente,
        "quantidade_kg": quantidade_kg_total
    })
  #para cada cliente que passar adicionar no dicionario clientes 
    for cliente in clientes:
                  print(f"{cliente['nome']} pagou €{cliente['total_compra']:.2f}")
# Encontre o cliente que mais pagou
if total_compra_clientes:
    cliente_mais_pago = clientes[total_compra_clientes.index(max(total_compra_clientes))]
    print(f"O cliente que mais pagou foi {cliente_mais_pago['nome']} com um total de €{cliente_mais_pago['total_compra']:.2f}")
else:
    print("Nenhum cliente processado.")

# Calcule a média em kg
total_kg = sum(cliente["quantidade_kg"] for cliente in clientes)
numero_clientes = len(clientes)
media_kg = total_kg / numero_clientes if numero_clientes > 0 else 0
#mostrar o total na tela
print(f"Foram processados {numero_clientes} cliente(s)")
print(f"A média em kg foi de {media_kg:.2f} kg")

