class Estoque(object):
    """
    """

    global total_produtos
    total_produtos = []

    def __init__(self,
                 id_produto=None
):
        self.id_produto = 0
        self.produto = {}


    def adicionarProduto(self,
                         nome_produto,
                         valor,
                          
):
        """
        

        Parameters
        ----------
        nome_produto : TYPE
            DESCRIPTION.
        valor : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        produtos = {} # Cria o dicionario
        str_nome = str(nome_produto) # Certifica que o nome do produto é uma str
        
        produtos[str_nome] = [valor, self.id_produto] # Adiciona o produto ao dicionário
        total_produtos.append(produtos) # Cria uma lista de produtos
        print(total_produtos)
        print('-'*50)
        self.id_produto += 1 # Aumenta o id do próximo item
        return total_produtos


    def checarPreços(self):
        """
        

        Returns
        -------
        None.

        """
        contagem = 0 # Índice numérico para organizar o print dos produtos
        for i in total_produtos: # Acessando todos os produtos cadastrados na lista
            contagem +=1 
            for j, k in i.items(): # Acessa os dicionários e pega os nome (key) e os valores (k[0])
                print(f'{contagem}. Nome: {j};  Preço: {k[0]} reais \n')
        print('-'*50)
 
    def checarId(self):
        """
        

        Returns
        -------
        None.

        """
        for produtos in total_produtos:
            for nome, value in produtos.items():
                print(f'O id de {nome.capitalize()} é {value[1]}')


    def modificarPreço(self, novo_valor=None):
        """


        Returns
        -------
        None.

        """
        print('Os produtos cadastrados no momento são: \n')
        self.checarPreços() # Mostra todos os produtos

        posicao = int(input('Digite o número do produto que você quer alterar: '))
        novoValor = int(input('Digite o novo valor do produto: '))

        for indice, produto  in enumerate(total_produtos):# Acessando todos os produtos cadastrados na lista
            if (indice +1) == posicao: # Checa o indice do produto a ser mudado
                for nome, value in produto.items(): # Entra nos values do dicionário do índice acima
                    value[0] = novoValor # Modifica o valor do produto
                    print(f'O preço do produto {nome.capitalize()} ', end='')
                    print(f'foi alterado para {novoValor} reais!')
                    return total_produtos
                    break
            else:
                continue

a = Estoque()
a.adicionarProduto('paoDeQueijo', 10)
a.adicionarProduto('chiclete', 20)

