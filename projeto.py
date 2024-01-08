from datetime import date
while True:
    print('''ESCOLHA UMA DAS OPCOES
    [1] CALCULAR MEDIA
    [2] TABUADA
    [3] CALCULADORA
    [4] CALCULAR DESCONTO
    [5] CONVERSOR DE TEMPERATURA'
    [6] CONVERSOR DE MOEDA
    [7] CALCULAR DESCONTO E AUMENTO DO FUNCIONARIO
    [8] DETECTAR PALINDROMO
    [9] VER MAIOR PESSOA E MENOR PESSOA
    [10] ANALISADOR COMPLETO
    [11] ANALISADOR DE TRIANGULO
    [12] NUMEROS PRIMOS
    [13] CALCULAR FATORIAL
    [14] PROGRESSAO ARITIMÉTICA
    [15] SEQUENCIA DE FIBONACCI
    [16] TRATANDO VALORES
    [17] DESCOBRIR MAIOR E MENOR 2.0
    [18] LOJA DO FERNANDAO
    [19] CAIXA ELETRONICO''')

    opcao = input("Qual opcao escolhe? ")
    
    if opcao.isdigit() and opcao in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14','15', '16', '17', '18', '19'):
        if opcao == '1':
            print("VOCE DECIDIU CALCULAR A MEDIA!!")
            n1 = int(input("Digite o 1 nota: "))
            n2 = int(input("Digite o 2 nota: "))
            n3 = int(input("Digite a 3 nota: "))
            media = (n1 + n2 + n3) / 3
            print(f"A media das notas {n1}, {n2} e {n3} eh {media}")
            calcularMedia = input("Deseja continuar? (s/n)")
            if calcularMedia.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
                break

        elif opcao == '2':
            print("VOCE ESCOLHEU TABUADA!!")
            tabuada = int(input("Digite o numero que deseja fazer a tabuada: "))
            for i in range(1, 11):
                resultado = tabuada * i
                print(f"{tabuada} x {i} = {resultado}")
                
            calcularTabuada = input("Deseja continuar? (s/n)")
            if calcularTabuada.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
                break
        elif opcao == '3':
            print("VOCE ESCOLHEU CALCULADORA!!")
            while True:
                print('''ESCOLHA O QUE DESEJA
                [1] SOMA
                [2] SUBSTRACAO
                [3] MULTIPLICACAO
                [4] DIVISAO
                [5] POTENCIA''')
                
                opcaoCalculadora = input("Qual sua opcao? ")
                
                if opcaoCalculadora.isdigit() and opcaoCalculadora in ('1', '2', '3', '4', '5'):
                    if opcaoCalculadora == '1':
                        n1 = float(input("Digite o 1 valor: "))
                        n2 = float(input("Digite o 2 valor: "))
                        soma = n1 + n2
                        print(f"A soma de {n1:.0f} + {n2:.0f} = {soma:.:.0f}")
                    if opcaoCalculadora == '2':
                        n1 = float(input("Digite o 1 valor: "))
                        n2 = float(input("Digite o 2 valor: "))
                        substracao = n1 - n2
                        print(f"A substracao de {n1:.0f} - {n2:.0f} = {substracao:.0f}")
                    if opcaoCalculadora == '3':
                        print("oi")
                        n1 = float(input("Digite o 1 valor: "))
                        n2 = float(input("Digite o 2 valor: "))
                        multiplocaxcao = n1 * n2
                        print(f"A multiplocacao de {n1:.0f} * {n2:.0f} = {multiplocaxcao:.0f}")
                    if opcaoCalculadora == '4':
                        print("divisao")
                        n1 = float(input("Digite o 1 valor: "))
                        n2 = float(input("Digite o 2 valor: "))
                        divisao = n1 / n2
                        print(f"A divisao de {n1:.0f} / {n2:.0f} = {divisao:.0f}")
                    if opcaoCalculadora == '5':
                        n1 = float(input("Digite o 1 valor: "))
                        n2 = float(input("Digite o 2 valor: "))
                        potencia = n1 ** n2
                        print(f"A potenciacao de {n1:.0f} e {n2:.0f} = {potencia:.0f}")
                else:
                    print("Opcao invalida! Tente Novamente... ")
                
                continuarCalculadora = input("Deseja continuar? (s/n)")
                if continuarCalculadora.lower()  == 's':
                    print("Tudo bem...")
                else:
                    print("Saindo. Ate logo!")
                    break
                
        elif opcao == '4':
            produto = int(input("Digite o valor do produto: "))
            desconto = produto * 0.15
            print(f"O desconto do produto com 15% eh de {desconto:.0f}")
            
            continuarDesconto = input("Deseja continuar? (s/n)")
            if continuarDesconto.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
                break
        elif opcao == '5':
            while True:
                print('''ESCOLHA A OPCAO
                [1] CONVERTER CELSIUS PARA FAHRANHEIT
                [2] CONVERTER FAHRANHEIT PARA CELSIUS''')
                
                opcaoConversao = input("Escolha a opcao: ")
                
                if opcaoConversao.isdigit() and opcaoConversao in ('1', '2'):
                    print("VOCE ESCOLHEU O CONVERSOR DE MEDIDA")
                    if opcaoConversao == '1': # celsius para fahrenheit
                        grau = int(input("Diite o valor para converter de celsius para fahranheir: "))
                        fahrenheit = (grau * 9/5) + 32
                        print(f"A conversao de {grau}ºC para {fahrenheit}°F ")
                    elif opcaoConversao == '2':
                        fahrenheit1 = float(input("Diite o valor para converter de fahranheir para celsius : "))
                        celsius1 = (fahrenheit1 - 32 ) / 1.8
                        print(f"A conversao de {fahrenheit1}°F para {celsius1:.0f}ºC")
                else:
                    print("Opcao invalida! Tente Novamente... ")
                    
                continuarconversao = input("Deseja continuar? (s/n)")
                if continuarconversao.lower()  == 's':
                    print("Tudo bem...")
                else:
                    print("Saindo. Ate logo!")
                    break
        elif opcao == '6':
            while True:
                print("VOCE ESCOLHEU A CONVERSAO DE MOEDA")
                print('''ESCOLHA A OPCAO
                [1] CONVERTER REAL PARA DOLAR
                [2] CONVERTER DOLAR PARA EURO
                [3] CONVERTER REAL PARA EURO''')
                
                opcaoMoeda = input("Qual opcao voce escolhe? ")
                
                if opcaoMoeda.isdigit() and opcaoMoeda in ('1', '2', '3'):
                    if opcaoMoeda == "1":
                        moeda = float(input("Digite o valor de real que quer converter para dolar: R$ "))
                        dolar = moeda * 4.85
                        print(f"O valor da conversao de R${moeda} para dolar eh de {dolar:.2f}")
                    elif opcaoMoeda == '2':
                        dolar1 = float(input("Digite o valor de dolar que quer converter para euro: $ "))
                        euro = dolar1 * 0.90
                        print(f"O valor da conversao de ${dolar1} para euro eh de €{euro:.2f}")
                    elif opcaoMoeda == '3':
                        real =  float(input("Digite o valor de real que quer converter para euro: R$"))
                        euroReal = real * 0.19
                        print(f"O valor da conversao de ${real} para euro eh de €{euroReal:.2f}")
                else:
                    print("Opcao invalida! Tente Novamente... ")
                
                continuarMoeda = input("Deseja continuar? (s/n)")
                if continuarMoeda.lower()  == 's':
                    print("Tudo bem...")
                else:
                    print("Saindo. Ate logo!")
                    break
        elif opcao == '7':
            print("VOCE ESCOLHEU CALCULAR DESCONTO E AUMENTO DO FUNCIONARIO")
            funcionario = int(input("Digite o valor do funcionario: ß"))
            desconto = funcionario - (funcionario * 0.5)
            aumento = funcionario + (funcionario * 0.15)
            print(f"O desconto do funcionario eh de {desconto:.2f}")
            print(f"O aumento do funcionario eh de {aumento:.2f}")
            
            continuarAumentoDesconto= input("Deseja continuar? (s/n)")
            if continuarAumentoDesconto.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
                break
        elif opcao == '8':
            print("VOCE ESCOLHEU DETECTAR PALINDROMO")
            frase = str(input("Digite sua frase: ")).strip().upper()
            palavras = frase.split()
            juntar = ''.join(palavras)
            inverso = ''
            
            inverso = juntar[::-1]
            print(f"O inverso de {juntar} eh {inverso}")
            if inverso == juntar:
                print("EH um palindromo")
            else:
                print("Nao eh palindromo")
            continuarPalindromo= input("Deseja continuar? (s/n)")
            if continuarPalindromo.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
                break
        elif opcao == '9':
            print("VOCE ESCOLHEU VER MAIOR PESSOA E MENOR PESSOA")
            atual = date.today().year
            totmaior = 0
            totmenor = 0
            
            for p in range(1, 8):
                nasc = int(input(f"Em que ano {p} nasceu? "))
                idade = atual - nasc
                if idade >=21:
                   totmaior += 1 
                   media = (totmaior + totmenor) / 2
                else:
                   totmenor += 1
                   media = (totmaior + totmenor) / 2
           
            print(f"Ao todo tivemos {totmaior} pessoas maiores de idade...")
            print(f"E também tivemos {totmenor} pessoas menores de idade...")
            print(f"A media que tivemos de pessoas maiores e menores de idade eh de {media}...")
            continuarPalindromo= input("Deseja continuar? (s/n)")
            if continuarPalindromo.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
                break
        elif opcao == '10':
            print("VOCE ESCOLHEU O ANALISADOR COMPELTO")
            mediaIdade = 0
            nomeVelho = 0
            maiorIdadeVelho = 0
            totMulher20 = 0
            somarIdade = 0
            for pess in range(1, 5):
                print(f"---- {pess} PESSOA ----")
                nome = str(input("Nome: "))
                idade = int(input("Idade: "))
                sexo = str(input("Sexo: [F/M] "))
                somarIdade += 1 # FAZER A MEDIA DAS IDADES
                
                if pess == 1 and sexo == 'Mm':
                    maiorIdadeVelho = idade
                    nomeVelho = nome
                if sexo in 'Mm' and idade > maiorIdadeVelho:
                    maiorIdadeVelho = idade
                    nomeVelho = nome
                if sexo in 'Ff' and idade < 20:
                    totMulher20 += 1
                
            mediaIdade = somarIdade / 4
            print(f"A media de idade do grupo eh de {mediaIdade} anos")
            print(f"O homem mais velho tem {maiorIdadeVelho} anos e se chama {nomeVelho}")
            print(f"Ao todo sao/e {totMulher20} mulheres com menos de 20 anos")
            
            continuarPalindromo= input("Deseja continuar? (s/n)")
            if continuarPalindromo.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
                break
        elif opcao == '11':
            print("VOCE ESCOLHEU O ANALISADOR DE TRIANGULO")
            while True:
                print('''Escolha'qual dos triangulos quer saber
                [1] TRIANGULO EQUILATERO
                [2] TRIANGULO ISOCLES
                [3] TRINAGULO ESCALENO''')
                
                opcao = input("Qual opcao? ")
                
                if opcao.isdigit() and opcao in ('1', '2', '3'):
                    if opcao == '1':
                        print("Voce escolheu verificar se forma um triangulo equilatero.")
                        lado1 = int(input("Lado 1: "))
                        lado2 = int(input("Lado 2: "))
                        lado3 = int(input("Lado 3:"))
                        
                        if lado1 == lado2 == lado3:
                            print("Ele forma um triangulo equilatero")
                        else:
                            print("Ele NAO egh um triangulo equilatero")
                    elif opcao == '2':
                        print("Você escolheu verificar se forma um triângulo escaleno.")
                        lado1 = float(input("Digite o comprimento do lado 1: "))
                        lado2 = float(input("Digite o comprimento do lado 2: "))
                        lado3 = float(input("Digite o comprimento do lado 3: "))
                        if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
                           print("É um triângulo isósceles.")
                        else:
                            print("Não é um triângulo isósceles. Deve ter pelo menos 2 lados iguais.")
                    elif opcao == '3':
                        print("Você escolheu verificar se forma um triângulo escaleno.")
                        lado1 = float(input("Digite o comprimento do lado 1: "))
                        lado2 = float(input("Digite o comprimento do lado 2: "))
                        lado3 = float(input("Digite o comprimento do lado 3: "))
                        if lado1 != lado2 != lado3:
                            print("É um triângulo escaleno.")
                        else:
                            print("Não é um triângulo escaleno. Deve ter todos os lados diferentes.")
                else:
                    print("Opcao invalida... Tente novamente...")
        elif opcao == '12':
            print("VOCE ESCOLHEU VER SE EH NUMERO PRIMO")
            n = int(input("Digite um valor... "))
            tot = 0
            for i in range(1, n+1):
                if n % i == 0:
                    print('\033[33m', end=' ')
                    tot += 1
                else:
                    print('\033[31m', end=' ')
            print(f"{i}", end=' ')
            if tot == 2:
                print("Ele eh um nuemro primo!")
            else:
                print("Ele nao eh um nuemro primo")
        elif opcao == '13':
            num = int(input("Digite o valor para descobrir seu fatorial: "))
            cont = num
            f = 1
            print(f"Calculando {num}")
            while cont > 0:
                print(f"{cont}", end=' ')
                print(f" x " if cont > 1 else " = ", end=' ')
                f = f * cont
                cont -= 1
            print(f"O fatorial eh {f}")
            continuarFatorial= input("Deseja continuar? (s/n)")
            if continuarFatorial.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
                break
        elif opcao == '14':
            print("VOCE ESCOLHUE A PROGRESSAO ARITIMÉTICA!")
            termo = int(input("Digite o 1 numero: "))
            razao = int(input("Digite a razao: "))
            i = termo
            cont = 1
            total = 0
            mais = 10
            while mais != 0:
                total = total + mais
                while cont <= total:
                    print(f"{i}", end=' -> ')
                    i += razao
                    cont += 1
                print("PAUSA")
                mais = int(input("Quantos temrmos voce quer mostrar? "))
            print(f"Progressao finalizada {total} termos mostrados ")
            continuarProgressao= input("Deseja continuar? (s/n)")
            if continuarProgressao.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
        elif opcao == '15':
            print("VOCE ESCO,HEU A SEQUENCIA DE FIBONACCI")
            num = int(input("Quantos termos você quer mostrar? "))

            t1, t2 = 0, 1
            
            print(f"{t1} -> {t2}", end='')

            cont = 3
            while cont <= num:
                t1, t2 = t2, t1 + t2
                print(f" -> {t2}", end='')
                cont += 1

            print(" -> FIM")
            continuarFibo= input("Deseja continuar? (s/n)")
            if continuarFibo.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
        elif opcao == '16':
            print("VOCE ESCOLHEU TRATAR VALORES!")
            num = contator = soma = 0
            num = int(input("Digite um valor [999 para parar]: "))

            while num != 999:
                soma += num
                contator += 1
                num = int(input("Digite um valor [999 para parar]: "))
                
            print(f"Voce digitou {contator} e asoma entre eles foi {soma}")
            
            continuarTrat= input("Deseja continuar? (s/n)")
            if continuarTrat.lower()  == 's':
                print("Tudo bem...")
            else:
                print("Saindo. Ate logo!")
        elif opcao == '17':
            print("VOCE ESCOLHEU ACHAR O MENOR E MAIOR!")
            resp = 'S'
            soma = media = quant = maior = menor = 0
            while resp in 'Ss':
                valor = int(input("Digite um valor: "))
                soma += valor
                quant += 1
                if quant == 1:
                    maior = menor = valor
                else:
                    if valor > maior:
                        maior = valor
                    if valor < menor:
                        menor = valor
                resp = str(input("Voc deseja continuar? (S/N) "))
            media = soma / quant
            print(f"Voce digitou {quant} numeros e a media foi {media}")
            print(f"O maior valor foi {maior} e o menor eh {menor} ")
        elif opcao == '18':
            print("=" * 10)
            print("LOJA DO FELIPE")
            print("=" * 10)
            mais1000 = menor = contador = soma = 0
            while True:
                nomeProduto = str(input("Nome do produto: "))
                preco = float(input("Preco: R$ "))
                soma += preco
                contador += 1
                if preco > 1000:
                    mais1000 += 1
                if contador == 1:
                    menor = preco
                else:
                    if preco < menor:
                        menor = preco
                continuarCaixa = str(input("Deseja continuar? (s/n) "))
                if continuarCaixa == 's':
                    print("Tudo bem...")
                else:
                    break
            print(f"Existe {mais1000} total de produtos que custam mais de 1000")
            print(f"O total gasto na compra foi de  {soma}")
            print(f"O produto mais barato custa {menor:.2f} e custa {nomeProduto}.. ")
        elif opcao == '19':
            print("=" * 10)
            print("BANCO DO FELIPE")
            print("=" * 10)
            valor = int(input("Qual o valor a ser sacado? "))
            total = valor
            ced = 50
            totalCed = 0
            while True:
                if total >= ced:
                    total -= ced
                    totalCed += 1
                else:
                    if totalCed > 0:
                        print(f"O total de {totalCed} cedulas de R$ {ced}")
                    if ced == 50:
                        ced = 20
                    elif ced == 20:
                        ced = 10
                    elif ced == 10:
                        ced = 1
                    totalCed = 0
                    if total == 0:
                        break              
    else:
        print("Opcao invalida! Tente Novamente... ")