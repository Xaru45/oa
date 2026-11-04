import os

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

# VETOR DE QUESTÕES
questoes = [
    {
        "pergunta": "(Oficial de Justiça/SP) Assinale a alternativa onde o sinal indicativo da crase foi usado inadequadamente:",
        "opções": [
            "A) Prefiro esta bolsa àquela.",
            "B) Isto é prejudicial à saúde.",
            "C) Escrevia à Machado de Assis.",
            "D) As lágrimas caíam uma à uma de seus olhos."
        ],
        "correta": "A"
    },
    {
        "pergunta": "(Banco do Brasil) Opção que preenche corretamente as lacunas: O gerente dirigiu-se ___ sua sala e pôs-se ___ falar ___ todas as pessoas convocadas.",
        "opções": [
            "A) à - à - à",
            "B) a - à - à",
            "C) à - a - a",
            "D) a - a - à"
        ],
        "correta": "C"
    },
    {
        "pergunta": "(Banespa) Assinale a alternativa que preenche corretamente as lacunas do texto ao lado: Recorreu ___ irmã e ___ ela se apegou como ___ uma tábua de salvação.",
        "opções": [
            "A) à - à - a",
            "B) à - a - à",
            "C) a - a - a",
            "D)  à - a - a"
        ],
        "correta": "D"
    },
    {
        "pergunta": "(Cesgranrio) Assinale a frase em que à ou às está mal empregado.",
        "opções": [
            "A) Amores à vista.",
            "B) Referi-me às sem-razões do amor.",
            "C) Submeteram o amor à provações difíceis.",
            "D) Estava meu coração à mercê das paixões."
        ],
        "correta": "C"
    },
    {
        "pergunta": "(FEI) Assinalar a alternativa que preenche corretamente as lacunas das seguintes orações:\n\nI. Precisa falar ___ cerca de três mil operários.\nII. Daqui ___ alguns anos tudo estará mudado.\nIII. ___ dias está desaparecido.\nIV. Vindos de locais distantes, todos chegaram ___ tempo ___ reunião.",
        "opções": [
        "A) a - a - há - a - à",
        "B) à - a - a - há - a",
        "C) a - à - a - a - há",
        "D) há - a - à - a - a"
        ],
        "correta": "A"
    },
    {
        "pergunta": "(FGV) Assinale a alternativa em que está correto o uso do acento indicativo de crase:",
        "opções": [
        "A) O autor se comparou à alguém que tem boa memória.",
        "B) Ele se referiu às pessoas de boa memória.",
        "C) As pessoas aludem à uma causa específica.",
        "D) Ele passou a ser entendido à partir de suas reflexões sobre a memória."
        ],
        "correta": "B"
    },
    {
        "pergunta": "(Escrivão.Pol./SP) A alternativa em que o sinal de crase não procede é:",
        "opções": [
        "A) À exceção da Bandeirantes, as outras emissoras de televisão detêm a ampla liderança com percentuais fabulosos.",
        "B)  Está presente a cineasta das cidades brasileiras à quem a porcentagem de 7% surpreendeu.",
        "C) Os dados da pesquisa referem-se às cenas, certamente sem paralelo, em qualquer outro lugar no mundo.",
        "D) Cresce, às escondidas, o número de cidades recebendo imagens de televisão, ameaçadoras dos valores ético-culturais."
        ],
        "correta": "B"
    },
    {
        "pergunta": "(FASP) Assinale a alternativa com erro de crase:",
        "opções": [
        "A) Refiro-me à Roma antiga, na qual viveu César.",
        "B) Fui à Lisboa de meus avós, pois gosto da Lisboa de meus avós.",
        "C) Já não agrada ir a Brasília. A gasolina…"
        "D) Nenhuma das alternativas está errada."
        ], 
        "correta": "B"
    },
    {
        "pergunta": "(ITA) Analisando as sentenças:\n\nI. A vista disso, devemos tomar sérias medidas.\nII. Não fale tal coisa as outras.III.\n Dia a dia a empresa foi crescendo.\nIV. Não ligo aquilo que me disse.\n\nPodemos deduzir que:",
        "opções": [
        "A) Apenas a sentença III não tem crase.",
        "B) As sentenças III e IV não têm crase.",
        "C) Todas as sentenças têm crase.",
        "D) Nenhuma sentença tem crase."
        ],
        "correta": "A"
    },
    {
        "pergunta": """(MARANATHA) No excerto abaixo, complete as lacunas
com a(s) ou à(s).\n
“Ao reconhecer aos povos indígenas o
direito ___ terras que habitam, ___
Constituição Federal de 1988 favoreceu
processos de demarcação e
delimitação de territórios, que
continuam ___ ser feitos até hoje. Em
todas ___ regiões do Brasil, ___
reivindicações geraram uma profusão
de relatórios, laudos e pareceres,
produzidos pelos grupos técnicos (GT)

que realizam os estudos etno-
históricos, antropológicos, ambientais e

cartográficos exigidos pela legislação.
Em cada uma dessas iniciativas, consta
um elemento em comum: os mapas.
[...]”
VIANA, Diego. Mapas ajudam a
reconhecer terras indígenas e
quilombolas. Pesquisa Fapesp, maio de
2023. Disponível
em: https://revistapesquisa.fapesp.br/m

apas-ajudam-a-reconhecer-terras-
indigenas-equilombolas/. Acesso em: 14

mai. 2023.
A sequência que preenche
adequadamente as lacunas é: """,
        "opções": [
            "A) as | à | à | às | às",
            "B) às | a | a | as | as",
            "C) às | à | a | às | as",
            "D) as | a | à | as | às"
            ],
            "correta": "A"
    },
    {
        "pergunta": """(OBJETIVA) Quantas crases devem ser usadas na
frase: “A noite, fez tudo as pressas para
logo ir a praça.”?""",
        "opções": [
            "A) Uma",
            "B) Duas",
            "C) Três",
            "D) Nenhuma"
            ],
            "correta": "C"
    },
    {
        "pergunta": """(INSTITUTO MAIS) Declaram-se favor da
medida e alinhados
que perguntaram sobre a alteração da
tarifa partir do
próximo mês.\n
De acordo com a norma-padrão da
Língua Portuguesa e quanto ao uso da
crase, assinale a alternativa que
preenche correta e respectivamente as
lacunas.""",
        "opção": [
            "A) à / àqueles / à",
            "B) a / aqueles / à",
            "C) à / àqueles / a§",
            "D) a / àqueles / a"
            ],
            "correta": "D"
    },
    {
        "pergunta": """De acordo com a norma-padrão da
Língua Portuguesa e quanto ao uso ou
não da crase, assinale a alternativa
correta.""",
        "opção": [
            "A) Ninguém gosta de pegar mais trânsito as sextas-feiras.",
            "B) No convite estava bem claro que eram trajes à rigor",
            "C) Preferimos os políticos que fazem àqueles que só prometem.",
            "D) Com os indícios abundantes,chegaram a rápida resolução do caso."
            ],
            "correta": "C"
    }

]

def jogar_em_ordem():
    limpa()
    print('Agora que você já aprendeu todas as regras de quando usar a crase, vamos testar seus conhecimentos com algumas questões!')
    input('\nAperte Enter para começar')
    limpa()
    
    for numero, q in enumerate(questoes, 1):
        print(f"--- QUESTÃO NÚMERO {numero} DE {len(questoes)} ---")
        print(q["pergunta"], flush=True)
        
        for opcao in q["opções"]:
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
