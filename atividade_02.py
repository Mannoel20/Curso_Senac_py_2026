def calcular_taxa_servico(diarias):
    """Retorna o valor da taxa baseado na quantidade de dias."""
    if diarias < 15:
        return 8.00
    elif diarias == 15:
        return 6.30
    return 5.00

def processar_hotel():
    valor_base = 150.00
    total_hotel = 0
    
    while True:
        nome = input("\nNome do cliente (ou 'fim'): ").strip()
        if nome.lower() == 'fim':
            break
            
        dias = int(input(f"Quantidade de diárias de {nome}: "))
        
        # Lógica centralizada
        taxa = calcular_taxa_servico(dias)
        conta_individual = dias * (valor_base + taxa)
        
        total_hotel += conta_individual
        
        print(f">> Cliente: {nome} | Total: R$ {conta_individual:.2f}")

    print(f"\nFATURAMENTO TOTAL: R$ {total_hotel:.2f}")

# Executa o programa
processar_hotel()
