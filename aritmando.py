'''
Um jogo simples para praticar aritmética 
com números inteiros
'''
# bliblioteca para gerar número randômicos
import random
# bliblioteca para colorir palavras 
# caso não esteja instalada no sistema, entre com:
# 'pip install termcolor' no terminal
from termcolor import colored
# importa as mensagens do arquivo 'mensagens.py'
import mensagens as mg 
# variáveis que serão utilizadas em várias funções
# e terão seus acrescidos ou decrescidos conforme a necessidade
energia = 0   #inicializa o contador de energia (usando o método de emular ponteiros do C com funções)
rodadas = [0] #inicializa o contador de rodadas
acertos = [0] #inicializa o contador de acertos
erros = [0]   #inicializa o contador de erros

def altera_energia(e):
    '''
    A energia do jogador varia em conformidade com o desempenho
    '''
    global energia
    if e:
        energia += 1
    elif e == False:
        energia -= 1
    return energia

def game():
    ''' 
    Realiza várias operações:
    - encerra o game; 
    - sorteia o operador artmético;
    - ativa as funções necessárias, etc
    '''
    if altera_energia(None) == -3:
        mg.adeus()
        quit()
    elif altera_energia(None) == 10:
        mg.first10()

    # Sorteia o operador aritmético
    operador = ['+', '-', '*', '/']
    operador_escolhido = random.choice(list(operador))
    
    if operador_escolhido == "-":
        resp, a, b = subtracao()
        if resp == True:
            acertou(resp)
        else:
            erros[0] += 1
            print(colored("Você errou. :-(", "red"))
            print(f"A subtração de {a} - {b} = {a - b}")
            print(f"Energia: {altera_energia(resp)}")
            aborda_game()

    elif operador_escolhido == "+":
        resp, a, b = soma()
        if resp == True:
            acertou(resp)
        else:
            erros[0] += 1
            print(colored("Você errou. :-(","red"))
            print(f"A soma de {a} + {b} = {a + b}")
            print(f"Energia: {altera_energia(resp)}")
            aborda_game()

    elif operador_escolhido == "*":
        resp, a = multiplicacao()
        if resp == True:
            acertou(resp)
        else: 
            print(colored("Você errou. :-(","red"))
            print(f"Energia: {altera_energia(resp)}")
            print(f"Para recordar a tabuada do {a}") 
            erros[0] += 1
            tabela(a)
            aborda_game()

    elif operador_escolhido == "/":
        resp, a, b, resto = divisao()
        if resp == True:
            acertou(resp)
        else: 
            if resto == 0:
                erros[0] += 1
                print(colored("Você errou. :-(","red"))
                print(f"{a} / {b} = {int(a/b)}")

            else:
                erros[0] += 1
                print(colored("Você errou. :-(","red"))
                print(f"{a} / {b} = {int(a/b)}") 
                print(f"Resto = {resto}")

                print(f"Energia: {altera_energia(resp)}")
                aborda_game()
                
def acertou(resp):
    '''
    Retorna mensagem em caso de acerto
    '''
    acertos[0] += 1
    print(colored("Você acertou!!!", "green"))
    print(f"Energia: {altera_energia(resp)}")
    aborda_game()

def soma():
    '''
    Retorna o resultado da subtração com valor sempre positivo
    '''
    a = random.randint(1, 100) # inclui o número nove na randomizacao
    b = random.randint(1, 100)
    while True:
        try:
            resposta = int(input(f"O resultado de {a} + {b} é: "))
        except ValueError:
            print(colored("Ops! Entre com um número inteiro. Tente novamente", "red"))
            continue
        else:
            break

    resultado = a + b
    if resposta == resultado:
        return True, a, b
    else:
        return False, a, b

def subtracao():
    '''
    Retorna o resultado da subtração com valor sempre positivo
    '''
    a = random.randint(1, 100) # inclui o número nove na randomizaçao
    b = random.randint(1, 100) 
    if b > a:
        a, b = b, a
    while True:
        try:
            resposta = int(input(f"O resultado de {a} - {b} é: "))
        except ValueError:
            print(colored("Ops! Entre com um número inteiro. Tente novamente", "red"))
            continue
        else:
            break

    resultado = a - b
    if resposta == resultado:
        return True, a, b
    else:
        return False, a, b

def multiplicacao():
    '''
    Retorna o resultado de um multiplicação
    '''
    a = int(10 * (random.SystemRandom().random()))
    b = int(10 * (random.SystemRandom().random()))

    while True:
        try:
            resposta = int(input(f"O resultado de {a} * {b} é: "))
        except ValueError:
            print(colored("Ops! Entre com um número inteiro. Tente novamente", "red"))
            continue
        else:
            break
    resultado = a * b 
    if resposta == resultado:
        return True, a
    else:
        return False, a

def divisao():
    '''
    Retorna o resultado da subtração com valor sempre positivo
    '''
    a = 1 + int(100 * (random.SystemRandom().random())) 
    b = 1 + int(100 * (random.SystemRandom().random())) 
    
    divisivel = False

    if b > a : # a sempre será maior
        a, b = b, a
    if a % b == 0:
        divisivel = True

    while True:
        try:
            if divisivel: 
                resposta = int(input(f"O resultado de {a} / {b} é: "))
            else:
                resposta, resposta_resto = input(f"O resultado inteiro de {a} / {b} e o resto: ").split()
                resposta = int(resposta)
                resposta_resto = int(resposta_resto)

        except ValueError:
            print(colored("Ops! Entre com um número inteiro. Tente novamente","red"))
            continue
        else:
            break

    if divisivel:
        resultado = a / b
        resto = 0
        if resposta == resultado:
            return True, a, b, resto
        else:
            return False, a, b, resto
    else:
        resultado = int(a / b)
        resto = a % b
        if resultado == resposta and resto == resposta_resto:
            return True, a, b, resto
        else:
            return False, a, b, resto
         
def aborda_game():
    '''
    Encerra o game quando o jogador escolhe a opção 's'
    [ENTER] para continuar.
    Note a linha aonde a variável aborda está,
    antes tinha colocado dentro do if sair, e houve problemas.
    '''
    aborda = False    
    while aborda == False:
        # a depender do terminal ou no window, 'blink' não funcionar
        tecla_s = colored("s", "red", attrs=["blink"])
        tecla_enter = colored("ENTER", "green", attrs=["blink"])
        rodadas[0] += 1
        sair = input(f"Você quer sair do jogo? {tecla_s}AI / [{tecla_enter}](continua) > ")
        if sair == 's':
            print("Tchau... :-(")
            print("=======================")
            print(f"Energia: {altera_energia(None)}")
            print(f"Rodadas: {rodadas[0]}")
            print(f"Acertos: {acertos[0]}")
            print(f"Erros:   {erros[0]}")
            print(f"Aprov:   {(100 * acertos[0])/rodadas[0]:.2f}%")
            aborda = True
        elif sair == '':
            game()
        else:
            print(f"Tecle '{tecla_s}' ou a tecla [{tecla_enter}].")
            continue

        aborda = True

def tabela(n):
    '''
    Cria a tabela de multiplicação para relembrar o jogador em caso de erro na
    operação.
    '''
    for i in range(1,11):
        print(f"    {n} x {i} = {n*i}")

def main():
    mg.apresentacao()
    game()

if __name__ == "__main__":
    main()
