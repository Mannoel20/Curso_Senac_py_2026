class Cao:
    def __init__(self, peso, raca):
        self.peso = peso
        self.raca = raca

    def __str__(self):
        # Corrigido: Fechamento das aspas e chaves
        return f"{self.raca} ({self.peso} kg)"

# Criando a instância (Objeto)
meu_cao = Cao(10, "poodle")

# Acessando atributos diretamente
print(f"Meu {meu_cao.raca} pesa {meu_cao.peso} kg")

# Chamando o método __str__ automaticamente ao printar o objeto
print(meu_cao)