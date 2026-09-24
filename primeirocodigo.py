
nome_completo = input("Digite seu nome completo: ")
idade = int(input("Digite a sua idade: "))
# 3. Solicitar a lista de desejos separada por vírgula
desejos_input = input("Digite a sua lista de desejos/sonhos (separados por vírgula): ")

# Transforma a frase numa lista de itens limpos (sem espaços no início/fim)
lista_desejos = [item.strip() for item in desejos_input.split(",")]

# 4. Criar uma lista de produtos disponíveis
produtos = ["Carro", "Celular", "Livro", "Computador", "Viagem"]

# 5. Criar uma lista de preços para cada produto
precos = [50000.00, 3000.00, 50.00, 4500.00, 2000.00]

# 6. Exibir o primeiro nome e o último sobrenome
nomes = nome_completo.strip().split()
primeiro_nome = nomes[0]
ultimo_sobrenome = nomes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último sobrenome: {ultimo_sobrenome}")

# 7. Verificar itens da lista de desejos que existem na lista de produtos
print("\n--- Itens da lista de desejos encontrados ---")
for desejo in lista_desejos:
    # Usamos .title() para evitar problemas se o utilizador digitou em minúsculas
    desejo_formatado = desejo.strip().title()
    
    if desejo_formatado in produtos:
        indice = produtos.index(desejo_formatado)
        preco = precos[indice]
        print(f"Produto: {desejo_formatado} | Preço: R$ {preco:.2f}")

# 8. Verificar condição de idade e oferta de produto ganho
if idade <= 20:
    for desejo in lista_desejos:
        desejo_formatado = desejo.strip().title()
        if desejo_formatado in produtos:
            print(f"\nParabéns! Você acaba de ganhar o produto: {desejo_formatado}!")
            break  # Interrompe o loop ao encontrar o primeiro produto ganho