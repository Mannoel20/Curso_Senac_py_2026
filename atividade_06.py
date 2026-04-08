praias = {}
continua = 70000

while continua == 70000:
    nome_praia = input("informe o nome da praia: ")
    distancia_centro = float(input("informe a distancia da praia ao centro da cidade: "))
    media_veranistas = float(input("iforme o numero medio de veranistas na pra: "))
    tipo_acesso = float(input("informe o tipo de acesso a praia( 0 - acesso nao asfaltado; 1 - acesso asfaltado): "))
     
    praias[nome_praia] = [distancia_centro, media_veranistas, tipo_acesso]

    continua = int(input("\nDeseja cadastar nova praia (0 - Sim / 1 - nao): "))    
    print()

print(praias)

numero_praias_15km = 0
numero_veranistas_praia_nao_asfaltado = 0
quantidade_numero_de_praias_acesso_nao_asfaltado = 0 
praias_acesso_asfaltado_menos_1000_veranistas = {}

nomes_praia = praias.keys()
for nome in nomes_praia:
    elemento = praias.get(nome)
    print(elemento)

    distancia_centro = elemento [0]
    quantidade_veranistas = [1]
    tipo_acesso = [2]

    if distancia_centro > 15:
        numero_praias_15km =numero_praias_15km +1

    if tipo_acesso == 0:
        numero_veranistas_praia_nao_asfaltado = numero_veranistas_praia_nao_asfaltado +1
        quantidade_numero_de_praias_acesso_nao_asfaltado = quantidade_numero_de_praias_acesso_nao_asfaltado +1

    if tipo_acesso == 1 and quantidade_veranistas < 100:
        praias_acesso_asfaltado_menos_1000_veranistas[nome] = distancia_centro

media_veranistas = numero_veranistas_praia_nao_asfaltado / quantidade_numero_de_praias_acesso_nao_asfaltado  

print( f"numero de praias mais de 15 km do centro: {numero_praias_15km} ")
print(f"media de veranistas de praias com acesso nao asfaltado: {media_veranistas} ")
print(f"prais com acesso asfaltado e com menos de 1000 veranistas: {praias_acesso_asfaltado_menos_1000_veranistas}")

