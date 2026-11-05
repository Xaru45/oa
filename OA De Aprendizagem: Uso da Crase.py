import os

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        "pergunta": "(Banespa) Assinale a alternativa que preenche corretamente as lacunas do texto ao lado: Recorreu ___ irmã \ne ___ ela se apegou como ___ uma tábua de salvação.",
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
com a(s) ou à(s).\n“Ao reconhecer aos povos indígenas o
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
        "opções": [
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
        "opções": [
            "A) Ninguém gosta de pegar mais trânsito as sextas-feiras.",
            "B) No convite estava bem claro que eram trajes à rigor",
            "C) Preferimos os políticos que fazem àqueles que só prometem.",
            "D) Com os indícios abundantes,chegaram a rápida resolução do caso."
            ],
            "correta": "C"
    },
    {
        "pergunta": "(OBJETIVA) Há ERRO no uso da crase em:",
        "opções": [
            "A) O filho terminou de almoçar às pressas.",
            "B) A família está esperando desde às 2h.",
            "C) Todos chegaram à confraternização a tempo.",
            "D) Às vezes as coisas acontecem como gostamos."
            ],
            "correta": "B"
    },
    {
        "pergunta": """Leia o texto para responder à questão.
“A Natureza da Mordida” é mistério que
se lê com prazer de Carla Madeira
A escritora Carla Madeira virou um
fenômeno editorial em 2021. Seu Tudo é
rio, publicado originalmente em 2014 e
reeditado, foi do boca
boca listas de mais
vendidos no país, beirando os 150 mil
exemplares. Foi a autora brasileira mais
lida do ano.
Véspera, seu romance mais recente,

deu continuidade ao caminho bem-
sucedido. E agora a expectativa está

sobre A Natureza da mordida, seu livro
do meio, que acaba de ser reeditado.
Alguns elementos do conteúdo
talvez ajudem entender a
acolhida do leitorado. O interesse pela
subjetividade das personagens, a
curiosidade para explorar a condição
humana, a ambiguidade e a autonomia
das mulheres retratadas, o direito
entregue essas personagens
de errarem e de serem más. Na forma,
as construções fluidas, o trabalho
cuidadoso com a palavra, a prosa
poética com frases altamente tatuáveis
também ajudam.
A Natureza da mordida repete um
formato já conhecido na obra da autora
– os fragmentos. Capítulos curtos,
alguns brevíssimos, alternam a voz das
duas protagonistas.

(Gabriela Mayer.
https://www.folha.uol.com.br/ilustrada/,
27.01.2023. Adaptado)
De acordo com a norma-padrão, as
lacunas do texto devem ser
preenchidas, respectivamente, com:""",

            "opções": [
                "A) a ... a ... à ... à",
                "B) à ... às ... a ... a",
                "C) a ... às ... a ... a",
                "D) à ... à ... à ... à"
                ],
                "correta": "C"
    },
    {
        "pergunta": """(BRB) Leia: 
        
“O cenário esportivo atual é favorável
____ um patamar de profissionalismo
muito mais inclinado ____ performance
de alto nível. Os atletas têm tido
compromissos comerciais e profissionais
muito maiores,
____ medida que elevam suas marcas
pessoais e se mostram mais voltados
____  prática de suas atividades em alto grau
de exigência de mercado.”
Pode-se dizer, quanto ao uso adequado
ou não do acento grave, que completam
os espaços do texto acima
respectivamente os seguintes vocábulos:""",

            "opções": [
                "A) A – a – à – à.",
                "B) A – à – à – à.",
                "C) A – à – a – à.",
                "D) À – a – a – a."
                ],
                "correta": "C"
    },
    {
        "pergunta": "(MS CONCURSOS) Assinale a alternativa, onde o acento indicador de crase, não tem cabimento.",
        "opções": [
            "A) A desnutrição abre caminho às doenças.",
            "B) Devemos aliar a teoria à prática.",
            "C) A chuva reteve-o na escola e só mais tarde regressou à casa.",
            "D) Fui à Casa Glória comprar uma roupa."
            ],
            "correta": "C"
    },
    {
        "pergunta": """(UFPR) Quais as formas que completam, pela ordem, as lacunas das frases seguintes?

Daqui ___ pouco vai começar o exame; Compareci ___ cerimônia de posse do novo governador;
Não tendo podido ir ___ faculdade hoje, prometo assistir ___ todas as aulas amanhã.""",
            "opções": [
                "A)  à - a - a - à",
                "B) há - na - à - a",
                "C) a - há - na - à",
                "D) a - à - à - a"
                ],
                "correta": "D"

    },
    {
        "pergunta": "(Unifor) Marque a alternativa em que o sinal de crase está empregado em todos os casos que é necessário.",
        "opções": [
            "A) A família ficou à mercê do frio, a despeito do fogo que estava a arder.",
            "B) O vento entrava à vontade restando a família a expectativa de que acontecesse logo.",
            "C) Falavam à beça, mas talvez não se entendessem à contento.",
            "D)  A cachorra ficou à porta, à olhar as brasas."
            ],
            "correta": "A"
    },
    {
        "pergunta": """ (OBJETIVA)
“Terrível”, ela diz, aos prantos. “Sabe
aquele cara, Michael, com quem eu
estava saindo? Bem, ele é o primeiro
homem por quem eu me interessei
desde o meu divórcio. Ontem ______
noite ele me disse que eu estava
pressionando muito e que ele só quer
amizade. Estou devastada.”
Você suspira e diz: “Bom, para ser bem
honesta, isso provavelmente aconteceu ______
você é velha, feia e
chata, sem falar que é carente e
dependente. E está pelo menos 10 quilos
acima do peso. Eu simplesmente
desistiria agora _____ de fato
não há esperança de que você encontre
alguém que vá amá-la. Francamente,
você não merece!”. Você falaria assim
com alguém de quem gosta? É claro
que não. Mas, estranhamente, esse é
exatamente o tipo de coisa que dizemos _____
nós mesmos em tais situações
- ou ainda pior. Com autocompaixão,
aprendemos a falar com nós mesmos

como um bom amigo. “Sinto muito.
Você está bem? Deve estar muito
chateada. Lembre-se de que eu estou
sempre aqui e que gosto muito de você.
Há alguma coisa que eu possa fazer
para ajudar?”
Embora uma maneira simples de
pensar sobre autocompaixão seja tratar
a si mesmo como você trataria um bom
amigo, a definição mais completa
envolve três elementos essenciais que
mobilizamos quando estamos sofrendo:
autobondade, humanidade
compartilhada e mindfulness.
(Fonte: Manual de Mindfulness e
Autocompaixão − adaptado.)\n
Assinalar a alternativa que preenche as
lacunas do texto CORRETAMENTE:""",
            "opções": [
                "A) a | porque | por que | à",
                "B) a | por que | porque | à",
                "C) à | por que | por que | a",
                "D) à | porque | porque | a"
                ],
                "correta": "D"
    },
    {
        "pergunta": """(FUNDEPES) Marechal Deodoro é um município
brasileiro do estado de Alagoas. Sua
população estimada em 2016 era de
51.715 habitantes de acordo com o IBGE.
O município faz parte da Região
Metropolitana de Maceió.
Foi fundada em 05 de agosto de 1591
com a denominação de Sesmaria de
Santa Madalena do Sumaúma, foi
doado a Diogo de Melo Castro com os
seguintes limites: Cinco léguas do litoral
da Pajuçara ao porto do Francês; Sete
léguas de frente a fundos para o sertão
e mais quatro léguas da boca do rio
Paraíba. Em 12 de abril de 1636 passou a
ser denominada de Vila Santa Madalena
da Lagoa do Sul. Em 16 de setembro de
1817 a mesma passou a ser a Capital da
província das Alagoas. Em 08 de março
de 1823 foi elevada a cidade. O
município foi criado em 09 de novembro
de 1939, com a denominação de
Marechal Deodoro, em homenagem ao
Marechal Deodoro da Fonseca,
alagoano que foi o primeiro presidente
da república do Brasil. Em 16 de
setembro de 2006, foi considerada pelo
Ministério da Cultura como Patrimônio
Histórico Nacional, em virtude do seu
passado e de ter sido berço do Marechal
Deodoro da Fonseca, proclamador da
República Brasileira.
Disponível em:
<https://www.marechaldeodoro.al.gov.b
r/a-cidade/historia/>. Acesso em: 21
mar. 2023.\n
Em relação às regras formais do uso do
acento indicativo de crase, dadas as
afirmativas
I. No trecho: “Sete léguas de
frente a fundos para o sertão e mais
quatro léguas da boca do rio Paraíba”,
há uma infração quanto à ausência do
sinal de crase em “a", já que o
enunciado apresenta uma locução
adverbial feminina.\n
II. Na frase: “Em 08 de março de 1823 foi
elevada a cidade" ocorrência do sinal
indicativo de crase no “a” é obrigatória.\n
III. Em: “foi doado a Diogo de Melo Castro
com os seguintes limites”, não ocorre
crase, porque o “a” está diante de uma
palavra masculina.\n
verifica-se que está/ão correta/s""",
            "opções": [
                "A) I, apenas.",
                "B) III, apenas.",
                "C) I e II, apenas.",
                "D) II e III, apenas."
                ],
                "correta": "D"
    },
    {
        "pergunta": "(Unicenp-PR) Qual a alternativa que aponta a frase incorreta quanto ao acento indicativo da crase?",
        "opções": [
            "A) Uma mulher deu à luz sobre uma pia enquanto o dinheiro do SUS (Sistema Único de Saúde) é desviado para comprar chope e salgadinhos.",
            "B) Esse expediente levou à lastimável aprovação do IPMF.",
            "C) À absoluta ineficiência do sistema de arrecadação, soma-se a má aplicação dos recursos públicos.",
            "D) A questão social continua prioritária demais para ser relegada à segundo plano."
            ],
            "correta": "D"
    },
    {
        "pergunta": """Analise as frases.

I. Ontem, fui até a escola para visitar velhos amigos.
Ontem, fui até à escola para visitar velhos amigos.

II. Ontem, passei a noite na casa da minha prima.
Ontem, passei à noite na casa da minha prima.

III. Ontem, entreguei o relatório a minha supervisora.
Ontem, entreguei o relatório à minha supervisora.

Dentre os pares de frases apresentados, a estrutura frasal em que se verifica alteração de sentido da segunda frase em relação à primeira está contida em:""",

            "opções": [
                "A) I, apenas.",
                "B) II, apenas.",
                "C) I e III, apenas.",
                "D) II e III, apenas."
                ],
                "correta": "B"

    },
    {
        "pergunta": "(UFPR) Em qual alternativa o vocábulo a deve receber acento grave?",
        "opções": [
            "A) Pintou o quadro a óleo.",
            "B) Fomos a uma aldeia.",
            "C) Dirigiram-se a Vossa Excelência.",
            "D) Voltou a casa paterna."
            ],
            "correta": "B"
    },
    {
        "pergunta": """(UFPR) Quais as formas que completam, pela ordem, as lacunas das frases seguintes?

Daqui ___ pouco vai começar o exame; Compareci ___ cerimônia de posse do novo governador; 
Não tendo podido ir ___ faculdade hoje, prometo assistir ___ todas as aulas amanhã.""",
            "opções": [
                "A)  a - à - à - a",
                "B) há - na - à - a",
                "C) a - há - na - à",
                "D) à - a - a - à"
                ],
                "correta": "A"
    }

]

def ordem():
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
        
        continuar = ""
        while continuar not in ["S", "N"]:
            continuar = input("Deseja ir para a próxima questão? (S - Sim / N - Voltar ao Menu): ").strip().upper()
            
            if continuar not in ["S", "M"]:
                print("\033[31mOpção inválida! Digite 'S' para continuar ou 'N' para sair.\033[0m")
        
        if continuar == "N":
            limpa()
            print("Retornando ao menu principal...\n")
            return 
        
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
        print('A crase é a fusão da preposição \033[1ma\033[0m com o artigo definido feminino \033[1ma\033[0m (ou \033[1mas\033[0m), ou com o início dos pronomes demonstrativos\n \033[1maquele(s)\033[0m, \033[1maquela(s)\033[0m, \033[1maquilo\033[0m. O sinal gráfico que marca a crase é o acento grave (`).')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('\033[1mREGRAS DE QUANDO USAR CRASE\033[0m')
        print('A crase pode ser usada nas seguintes situações:')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Antes de palavras femininas.\nExemplos:')
        print('Fui \033[1mà\033[0m escola.')
        print('Fomos \033[1mà\033[0m praia.')
        print('Você vai \033[1mà\033[0m padaria agora?')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Quando acompanham verbos que indicam destino \033[1m(ir, voltar, vir)\033[0m.\nExemplos:')
        print('Fui \033[1mà\033[0m padaria.')
        print('Voltei \033[1mà\033[0m loja.')
        print('\nQuando o lugar tem nome próprio, usamos uma regra para determinar se tem ou não a crase: se você vai "a" e volta "da" há crase. Se você vai "a" e volta "de" não há crase.\nExemplos:')
        print('Vou \033[1mà\033[0m Bahia -> Voltei da Bahia (tem crase)')
        print('Vou a Brasília -> Voltei de Brasília (não tem crase)')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Nas locuções adverbiais, prepositivas e conjuntivas.\nExemplos:')
        print('Saímos \033[1mà\033[0m noite.')
        print('\033[1mÀ\033[0m medida que o tempo passa, aprendemos mais.')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Antes de pronomes demonstrativos \033[1m(aquela, aquele, aquilo)\033[0m.\nExemplos:')
        print('Nas férias, fui \033[1mà\033[0mquela cidade que você me indicou.')
        print('Refere-se \033[1mà\033[0mquilo que aconteceu ontem na festa.')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Antes da locução "à moda de" quando ela estiver subentendida.\nExemplos:')
        print('Fez um gol \033[1mà\033[0m Pelé. (fez um gol \033[1mà\033[0m moda de Pelé)')
        print('Escreve \033[1mà\033[0m Machado de Assis. (escreve \033[1mà\033[0m moda de Machado de Assis)')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Uso da crase na indicação das horas.\nExemplos:')
        print('A reunião será \033[1màs\033[0m 10:40h.')
        print('Saio do IFAL \033[1màs\033[0m 12:20.')
        print('Por outro lado, quando acompanhadas de preposições \033[1m(para, desde, após, perante, com)\033[0m, não se utiliza a crase.')
        print('Ficamos na reunião desde \033[1mas\033[0m 11:00.')
        print('Saímos do IFAL após \033[1mas\033[0m 18:00.')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Diante dos Pronomes Relativos \033[1m"A qual" / "As quais"\033[0m.\nExemplos:')
        print('A cidade \033[1mà\033[0m qual fomos é linda. \033[1m(Quem vai, vai a algum lugar)\033[0m.')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('\033[1mREGRAS DE QUANDO NÃO USAR CRASE\033[0m \nAgora que vimos todas as regras do uso correto da crase, veremos a seguir as situações que \033[1mNÃO\033[0m devemos usar a crase!!!')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Antes de palavras masculinas.\nExemplos:')
        print('Eduardo tem um carro \033[1ma\033[0m álcool.')
        print('Bernardo comprou um jipe \033[1ma\033[0m diesel.')
        print('Carliane escreve \033[1ma\033[0m lápis.')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Antes de verbos.\nExemplos:')
        print('Ele estava disposto \033[1ma\033[0m estudar.')
        print('Ela passava o dia \033[1ma\033[0m cantar.')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Antes de pronomes pessoais do caso reto e do caso oblíquo.')
        print('Os pronomes do caso reto são: \033[1meu, tu, ele, nós, vós, eles\033[0m.\nOs pronomes do caso oblíquo são: \033[1mme, mim, comigo, te, ti, contigo, se, si, o, lhe\033[0m.\nExemplos:')
        print('Falamos \033[1ma\033[0m ela sobre o ocorrido.')
        print('A professora se referiu \033[1ma\033[0m mim.')
        print('Deram o dinheiro \033[1ma\033[0m ele?')
        input('\nAperte Enter para continuar')
        limpa()
        
        print('Antes dos pronomes demonstrativos \033[1m(isso, esse, este, esta, essa)\033[0m\nExemplos:')
        print('Quando você aderir \033[1ma\033[0m esse plano, a mensalidade ficará com um preço menor.')
        print('A professora se referiu \033[1ma\033[0m isso que aconteceu na aula.')
        input('\nAperte Enter para continuar')
        limpa()
        
        
        print('Entre palavras repetidas.\nExemplos:')
        print('Dia \033[1ma\033[0m dia.')
        print('Cara \033[1ma\033[0m cara.')
        input('\nAperte Enter para continuar')
        limpa()
        
        
        print('Quando o \033[1m"A"\033[0m estiver no singular e a palavra seguinte no plural.\nExemplo:')
        print('Não me refiro \033[1ma\033[0m mulheres sem caráter.')
        input('\nAperte Enter para voltar ao menu principal')
        limpa()
        
        
        print('\033[1mREGRAS DE CRASE FACULTATIVA\033[0m \nE para finalizar, você vai ver os casos que a crase é meramente opcional!!!')
        input('\nAperte Enter para continuar')
        limpa()
        
        
        print('Diante de pronomes possessivos femininos.\nExemplos:')
        print('Pergunte \033[1ma\033[0m sua mãe. \n         ou\nPergunte \033[1mà\033[0m sua mãe.')
        input('\nAperte Enter para continuar')
        limpa()
        
        
        print('Depois da preposição \033[1m"ATÉ".\033[0m \nExemplos:')
        print('Fomos até \033[1ma\033[0m praça. \n          ou\nFomos até \033[1mà\033[0m praça.')
        input('\nAperte Enter para continuar')
        limpa()
        
        
        print('Antes de nomes próprios femininos.\nExemplos:')
        print('Obedeça \033[1ma\033[0m Joana! \n        ou\nObedeça \033[1mà\033[0m Joana!')
        input('\nAperte Enter para continuar')
        limpa()
        
        
    elif opcao == "2":
        ordem()

    elif opcao == "3":
        limpa()
        print('Bons estudos. Até à próxima!')

    else:
        limpa()
        print('\033[31mOpção inválida! Tente novamente.\033[0m\n')
