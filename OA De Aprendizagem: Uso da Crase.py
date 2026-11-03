import os

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

# VETOR DE QUESTÕES
questoes = [
    {
        "pergunta": "O acento grave indicativo da crase está corretamente empregado em:",
        "opcoes": [
            "A) É preciso esta
            
            
            r atento \033[1màs\033[0m coisas boas da vida.",
            "B) Gostaria de poder viver melhor o meu dia \033[1mà\033[0m dia.",
            "C) As decisões \033[1màs\033[0m quais citei vão transformar minha vida.",
            "D) O parque ecológico localiza-se \033[1mà\033[0m três quilômetros daqui."
        ],
        "correta": "A"
    },
    {
        "pergunta": "resposta b teste",
        "opcoes": [
            "A) a",
            "B) b",
            "C) c",
            "D) d"
        ],
        "correta": "B"
    }
    
]

def jogar_em_ordem():
    limpa()
    print('Agora que você já aprendeu todas as regras de quando usar a crase, vamos testar seus conhecimentos com algumas questões!')
    input('\nAperte Enter para começar...')
    limpa()
    
    for numero, q in enumerate(questoes, 1):
        print(f"--- QUESTÃO NÚMERO {numero} DE {len(questoes)} ---")
        print(q["pergunta"] + "\n")
        
        for opcao in q["opcoes"]:
            print(opcao)
            
        resposta = input("\nSua resposta (A, B, C ou D): ").strip().upper()
        
        if resposta == q["correta"]:
            print("\033[32m\nCorreto!\033[0m")
        else:
            print(f"\033[31m\nErrou! A certa era {q['correta']}\033[0m")
            
        print("\n" + "-"*40)
        
        # VALIDAÇÃO: Só aceita S ou M
        opcao_continuar = ""
        while opcao_continuar not in ["S", "M"]:
            opcao_continuar = input("Deseja ir para a próxima questão? (S - Sim / M - Voltar ao Menu): ").strip().upper()
            
            if opcao_continuar not in ["S", "M"]:
                print("\033[31mOpção inválida! Digite 'S' para continuar ou 'M' para sair.\033[0m")
        
        if opcao_continuar == "M":
            limpa()
            print("Retornando ao menu principal...\n")
            return  # Sai da função e volta direto para o menu principal
        
        limpa()

    print("\033[1m=== FIM DAS QUESTÕES! ===\033[0m")
    input("Aperte Enter para voltar ao menu principal...")
    limpa()

def menu():
    print('\033[1m---USO DA CRASE---\033[0m')
    print('1. Revisão do assunto')
    print('2. Lista de questões')
    print('3. Encerrar')

opcao = ""
while opcao != "3":
    menu()
    opcao = input('\nSelecione a opção desejada: ')

    if opcao == "1":
        limpa()
        print('Vamos aprender de uma vez por todas o uso da crase!!!')
        print('\n\nA crase é a fusão da preposição \033[1ma\033[0m com o artigo definido feminino \033[1ma\033[0m (ou \033[1mas\033[0m), ou com o início dos pronomes demonstrativos \033[1maquele(s)\033[0m, \033[1maquela(s)\033[0m, \033[1maquilo\033[0m. O sinal gráfico que marca a crase é o acento grave (`).')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('\033[1mREGRAS DE QUANDO USAR CRASE\033[0m')
        print('A crase pode ser usada nas seguintes situações:')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('\n\nAntes de palavras femininas.\nExemplos:')
        print('Fui \033[1mà\033[0m escola.')
        print('Fomos \033[1mà\033[0m praia.')
        print('Você vai \033[1mà\033[0m padaria agora?')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Quando acompanham verbos que indicam destino \033[1m(ir, voltar, vir)\033[0m.\nExemplos:')
        print('Fui \033[1mà\033[0m padaria.')
        print('Voltei \033[1mà\033[0m loja')
        print('\nQuando o lugar tem nome próprio, usamos uma regra para determinar se tem ou não a crase: se você vai "a" e volta "da" há crase. Se você vai "a" e volta "de" não há crase.\nExemplos:')
        print('Vou \033[1mà\033[0m Bahia -> Voltei da Bahia (tem crase)')
        print('Vou a Brasília -> Voltei de Brasília (não tem crase)')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Nas locuções adverbiais, prepositivas e conjuntivas.\nExemplos:')
        print('Saímos \033[1mà\033[0m noite.')
        print('\033[1mÀ\033[0m medida que o tempo passa, aprendemos mais.')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Antes de pronomes demonstrativos \033[1m(aquela, aquele, aquilo)\033[0m.\nExemplos:')
        print('Nas férias, fui \033[1mà\033[0mquela cidade que você me indicou.')
        print('Refere-se \033[1mà\033[0mquilo que aconteceu ontem na festa')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Antes da locução "à moda de" quando ela estiver subentendida.\nExemplos:')
        print('Fez um gol \033[1mà\033[0m Pelé (faz um gol \033[1mà\033[0m moda de Pelé)')
        print('Escreve \033[1mà\033[0m Machado de Assis (escreve \033[1mà\033[0m moda de Machado de Assis)')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Uso da crase na indicação das horas.\nExemplos:')
        print('A reunião será \033[1màs\033[0m 10:40h.')
        print('Saio do IFAL \033[1màs\033[0m 12:20.')
        print('Por outro lado, quando acompanhadas de preposições \033[1m(para, desde, após, perante, com)\033[0m, não se utiliza a crase.')
        print('Ficamos na reunião desde \033[1mas\033[0m 11:00')
        print('Saímos do IFAL após \033[1mas\033[0m 18:00')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Diante dos Pronomes Relativos \033[1m"A qual" / "As quais"\033[0m.\nExemplos:')
        print('A cidade \033[1mà\033[0m qual fomos é linda. \033[1m(Quem vai, vai a algum lugar)\033[0m.')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Agora que vimos todas as regras do uso correto da crase, veremos a seguir as situações que \033[1mNÃO\033[0m devemos usar a crase!!!')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Antes de palavras masculinas.\nExemplos:')
        print('Eduardo tem um carro \033[1ma\033[0m álcool.')
        print('Bernardo comprou um jipe \033[1ma\033[0m diesel.')
        print('Carliane escreve \033[1ma\033[0m lápis.')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Antes de verbos.\nExemplos:')
        print('Ele estava disposto \033[1ma\033[0m estudar.')
        print('Ela passava o dia \033[1ma\033[0m cantar.')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Antes de pronomes pessoais do caso reto e do caso oblíquo.')
        print('Os pronomes do caso reto são: \033[1meu, tu, ele, nós, vós, eles\033[0m.\nOs pronomes do caso oblíquo são: \033[1mme, mim, comigo, te, ti, contigo, se, si, o, lhe\033[0m.\nExemplos:')
        print('Falamos \033[1ma\033[0m ela sobre o ocorrido')
        print('A professora se referiu \033[1ma\033[0m mim.')
        print('Deram o dinheiro \033[1ma\033[0m ele?')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Antes dos pronomes demonstrativos \033[1m(isso, esse, este, esta, essa)\033[0m\nExemplos:')
        print('Quando você aderir \033[1ma\033[0m esse plano, a mensalidade ficará com um preço menor')
        print('A professora se referiu \033[1ma\033[0m isso que aconteceu na aula.')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Entre palavras repetidas.\nExemplos:')
        print('Dia \033[1ma\033[0m dia')
        print('Cara \033[1ma\033[0m cara')
        input('\nAperte Enter para continuar...')
        limpa()
        
        print('Quando o \033[1m"A"\033[0m estiver no singular e a palavra seguinte no plural.\nExemplo:')
        print('Não me refiro \033[1ma\033[0m mulheres sem caráter.')
        input('\nAperte Enter para voltar ao menu principal...')
        limpa()

    elif opcao == "2":
        jogar_em_ordem()

    elif opcao == "3":
        limpa()
        print("Bons estudos. Até à próxima!")

    else:
        limpa()
        print("Opção inválida! Tente novamente.\n")
