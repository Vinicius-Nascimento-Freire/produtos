def lin() :
    print('-' * 30)

def li() :
    print('-' * 60)

#Calculo para saber o lucro
def calculo_lucro(preco_venda, preco_custo, quant) :
    return (preco_venda - preco_custo) * quant

#Função para armazenar os dados dos produtos
def dados_produtos(nome, preco_custo, preco_venda, quant) :  
    lucro = calculo_lucro(preco_venda, preco_custo, quant)
    return (nome, preco_custo, preco_venda, quant, lucro)

lin()
print('Analisador de Portfólio de Produtos')
lin()

produtos = []
while True : 
    analise = input('Deseja seguir com a análise ? (S/N)').strip().upper()
    if analise == 'N' :
        print('Encerrando análise...')
        break
    
    if analise == 'S' :
        nome = input('Digite o nome do produto : ')
        preco_custo = float(input('Digite o preço de custo : '))
        preco_venda = float(input('Digite o preco de venda : '))
        quant = int(input('Qual a quantidade ? : '))
        #Adicionando os dados armazenados a lista
        ficha_pronta = dados_produtos(nome, preco_custo, preco_venda, quant)
        produtos.append(ficha_pronta)

        novo_produto = input('Deseja adiicionar outro produto ? (S/N)')
        if novo_produto == 'N' :
            break
        
li()       
for p in produtos : 
    print(f'NOME: {p[0]:<12} CUSTO: {p[1]:<11} PREÇO(VENDA): {p[2]:<11} QUANTIDADE: {p[3]:<11} LUCRO: {p[4]:<11}')   
li()         