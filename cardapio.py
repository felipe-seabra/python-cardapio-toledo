from time import sleep
from typing import List
from typing import Optional

arq = 'cardapio.txt' # Nomeia o arquivo .txt

# Cardápio com as pizzas já cadastradas
cardapio = [
    {
        "id": 1,
        "name": "Calabresa",
        "ingredients": ["calabresa", "queijo", "massa"],
        "price": 50
    },
    {
        "id": 2,
        "name": "Margherita",
        "ingredients": ["molho de tomate", "queijo mussarela", "manjericão", "massa"],
        "price": 55
    },
    {
        "id": 3,
        "name": "Pepperoni",
        "ingredients": ["pepperoni", "queijo", "massa"],
        "price": 60
    },
    {
        "id": 4,
        "name": "Quatro Queijos",
        "ingredients": ["queijo mussarela", "queijo provolone", "queijo gorgonzola", "queijo parmesão", "massa"],
        "price": 65
    },
    {
        "id": 5,
        "name": "Frango com Catupiry",
        "ingredients": ["frango desfiado", "queijo catupiry", "massa"],
        "price": 60
    },
    {
        "id": 6,
        "name": "Napolitana",
        "ingredients": ["molho de tomate", "queijo mussarela", "tomate", "azeitona", "cebola", "massa"],
        "price": 65
    },
    {
        "id": 7,
        "name": "Mussarela",
        "ingredients": ["queijo mussarela", "massa"],
        "price": 45
    },
    {
        "id": 8,
        "name": "Atum",
        "ingredients": ["atum", "queijo", "massa"],
        "price": 55
    },
    {
        "id": 9,
        "name": "Brócolis com Catupiry",
        "ingredients": ["brócolis", "queijo catupiry", "massa"],
        "price": 60
    },
    {
        "id": 10,
        "name": "Lombo com Champignon",
        "ingredients": ["lombo", "champignon", "queijo", "massa"],
        "price": 65
    },
    {
        "id": 11,
        "name": "Alho e Óleo",
        "ingredients": ["alho", "óleo", "queijo", "massa"],
        "price": 50
    },
    {
        "id": 12,
        "name": "Bacon",
        "ingredients": ["bacon", "queijo", "massa"],
        "price": 55
    },
    {
        "id": 13,
        "name": "Calabresa com Catupiry",
        "ingredients": ["calabresa", "queijo catupiry", "massa"],
        "price": 60
    }
]

# Menu de opções para ser exibido
menu = [
    'Adicionar pizza no cardápio',
    'Consultar pizza',
    'Alterar pizza do cardápio',
    'Excluir pizza do cardápio',
    'Exibir cardápio completo',
    'Exportar cardápio para arquivo texto',
    'SAIR'
]

def ler_int(text: str) -> int:
    """
    Lê um número inteiro e retorna o mesmo, tratando erros.
    """
    while True:
        try:
            return int(input(text.upper()))
        except ValueError:
            print('\033[31mOops! O valor deve ser um número inteiro. Favor digitar novamente...\033[0;0m')
            sleep(1)

def ler_float(text: str) -> float:
    """
    Lê um número flutuante e retorna o mesmo, tratando erros
    """
    while True:
        try:
            return float(input(text.upper()))
        except ValueError:
            print('\033[31mOops! O valor deve ser um número flutuante. Favor digitar novamente...\033[0;0m')
            sleep(1)

def ler_string(text: str) -> str:
    """
    Lê um string e retorna a mesma
    """
    return input(text.upper())

def input_para_sair() -> None:
    """
    Pausa a execução do programa até o usuário apertar enter.
    """
    input("Clique enter para sair!")

def imprimir_linha(value=45):
    """ 
    Imprime na tela uma linha separadora. 
    """
    print('-'*value)

def imprimir_cabecalho(text= '', color = '\033[31m') -> None:
    """ 
    Imprime na tela um cabeçalho formatado.
    """
    print('\n' * 10)
    imprimir_linha()
    print(f'{color}\033[1m{text.center(42).upper()}\033[0;0m')
    imprimir_linha()
    print()

def exibir_menu(options: List[str]) -> None:
    """
    Imprime na tela um menu de opções.
    """
    for i, option in enumerate(options, start=1):
        print(f'[{i}] - {option.upper()}')
    print('\n\n')

def ler_lista() -> list:
    """
    Lê uma lista de ingredientes.
    """
    lista_ingredientes = []
    contador = 1
    print('\n\nIngredientes...\n\n')
    while True:
        print('DIGITE 0 (ZERO) CASO QUEIRA FINALIZAR!')
        ingrediente = ler_string(f'\n{contador}º ingrediente da pizza: ')
        if ingrediente != '0':
            lista_ingredientes.append(ingrediente)
            contador += 1
        else:
            print('\n')
            break
    return lista_ingredientes

def exibir_ingredientes(ingredients: List[str]) -> None:
    """
    Percorre uma lista de ingredientes e os mostra na tela.
    """
    print('INGREDIENTES: ')
    for i in range(len(ingredients)):
        print(f'{i + 1}º - {ingredients[i].upper()}')

def percorrer_cardapio() -> Optional[dict]:
    cod = ler_int('digite o código da pizza: ')
    for pizza in cardapio:
        if cod == pizza["id"]:
            return pizza
    return None

def cardapio_cadastrar() -> None:
    """
    Adiciona uma nova pizza ao cardápio.
    """
    imprimir_cabecalho('cadastrando nova pizza')
    cardapio.append({
        'id': cardapio[-1]["id"] + 1,
        'name': ler_string('Digite o nome da PIZZA: '),
        'ingredients': ler_lista(),
        'price': ler_float('Digite o Preço: '),
    })
    imprimir_cabecalho('pizza cadastrada com sucesso', '\033[32m')
    sleep(2)

def cardapio_alterar() -> None:
    """
    Altera uma pizza já cadastrada no cardápio.
    """
    print('\n\n')
    pizza = percorrer_cardapio()
    if(pizza):
        imprimir_cabecalho('alterando pizza')
        pizza['name'] = ler_string('Digite o nome da PIZZA: ')
        pizza['ingredients'] = ler_lista()
        pizza['price'] = ler_float('Digite o Preço: ')
        imprimir_cabecalho('pizza alterada com sucesso', '\033[32m')
        sleep(2)
        return
    else:
        print('\033[31mO CÓDIGO NÃO EXISTE!!\033[0;0m')
        sleep(1)
    
def cardapio_consulta() -> None:
    """
    Faz a consulta de uma pizza pelo código.
    """
    print('\n\n')
    pizza = percorrer_cardapio()
    if(pizza):
        print('\n\n')
        imprimir_linha(80)
        print(f'\033[33m- CÓDIGO: \033[33m{pizza["id"]} \t\033[34m- NOME: {pizza["name"].upper(): <25} \t\t\033[31m\033[1m- PREÇO: R$ {pizza["price"]: >5.2f}\033[0;0m')
        exibir_ingredientes(pizza["ingredients"])
        imprimir_linha(80)
        print('\n\n')
        input_para_sair()
        return
    print('\033[31mO CÓDIGO NÃO EXISTE!!\033[0;0m')
    sleep(1)

def cardapio_remover() -> None:
    """
    Exclui uma pizza do cardapio.
    """
    print('\n\n')
    pizza = percorrer_cardapio()
    if(pizza):
        cardapio.remove(pizza)
        imprimir_cabecalho('pizza excluida com sucesso', '\033[32m')
        sleep(2)
        return
    else:
        print('O CÓDIGO NÃO EXISTE!!')
        sleep(1)

def cardapio_exibir() -> None:
    """
    Imprime o cardápio na tela
    """
    for pizza in cardapio:
        imprimir_linha(80)
        print(f'\033[33m- CÓDIGO: \033[33m{pizza["id"]} \t\033[34m- NOME: {pizza["name"].upper(): <25} \t\t\033[31m\033[1m- PREÇO: R$ {pizza["price"]: >5.2f}\033[0;0m')
        exibir_ingredientes(pizza["ingredients"])
        imprimir_linha(80)
    input_para_sair()

def arquivo_existe(name: str) -> bool:
    """ Verificação se arquivo existe """
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(name: str) -> None:
    """ Criar um novo arquivo """
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[0;0m')

def grava_arquivo() -> None:
    """ Função para gravar o 'cardapio.txt' (nome 'cardapio.txt' predefinido) """
    with open(arq, 'wt+', encoding='utf-8') as arquivo:
        for pizza in cardapio:
            arquivo.write(f'{pizza["id"]};{pizza["name"]};{pizza["ingredients"]};{pizza["price"]}\n')
    arquivo.close()

def cardapio_salvar() -> None:
    """ Exporta o cardapio para arquivo .txt """
    if not arquivo_existe(arq):
        criar_arquivo(arq)
    grava_arquivo()
    imprimir_cabecalho('cardápio exportado com sucesso', '\033[32m')
    sleep(1)

# Opções do menu
options = {
    1: cardapio_cadastrar,
    2: cardapio_consulta,
    3: cardapio_alterar,
    4: cardapio_remover,
    5: cardapio_exibir,
    6: cardapio_salvar,
}

def main() -> None:
    """ Função principal do programa. """
    while True:
        imprimir_cabecalho('menu de opções')
        exibir_menu(menu)
        op = ler_int('DIGITE UMA OPÇÃO: ')

        if op == 7:
            imprimir_cabecalho('saindo do sistema')
            sleep(1)
            break

        options.get(op, lambda: print('\033[31mOpção inválida.\033[0;0m'))()

if __name__ == '__main__':
    main()


""" Existe algumas coisas que estão diferentes do enunciado!!!

1 - O ID não está sendo usado para a manipulação do dict, mas o index do dict
sempre é igual ao ID, portanto da quase na mesma...

2 - As funções principais não recebem parâmetros, elas pedem quando são chamadas,
fiz isso pq achei mais confiável e mais fácil de tratar os erros, assim deixando
o código menor.

3 - Nome das variável e props de funções estão em inglês, se preferir trocar para
ficar tudo em português acho que ficaria melhor para o entendimento.

Se quiser modificar, fique a vontade.
"""