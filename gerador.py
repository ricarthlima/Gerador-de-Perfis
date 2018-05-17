"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (https://cin.ufpe.br)

Autor: Ricarth Ruan da Silva Lima (http://cin.ufpe.br/~rrsl)
Email: rrsl@cin.ufpe.br
Data: 2018-05-17

The MIT License 2018 Ricarth Lima
"""

import random

LISTA_NOMES_MASCULINOS = ["Ricarth", "Nicolas","João", "José", "Pedro",
                          "Gustavo", "Ricardo", "Bernado", "Bruno", "Davi",
                          "Eduardo", "Felipe", "Heitor", "Henrique","Rodrigo",
                          "Samuel","Vinicius"]

LISTA_NOMES_FEMININOS = ["Monalisa","Amanda","Ana","Beatriz","Bruna",
                         "Camila","Julia","Lara", "Leticia", "Maria",
                         "Sofia", "Valentina", "Yasmin"]

LISTA_SOBRENOMES = ["Silva","Santos","Oliveira","Souza","Sousa",
                    "Lima","Pereira","Ferreira","Alves","Almeida",
                    "Costa","Rodrigues","Nascimento","Carvalho",
                    "Araújo","Ribeiro","Muller","Smith","Gomes",
                    "Wang","Johnson","Bernard","Taylor","Rossi",
                    "Sato","Ali"]

LISTA_PROVEDORES = ["gmail.com","hotmail.com","live.com","outlook.com",
                    "yahoo.com", "gmail.com.br", "uol.com.br"]

LISTA_OCUPACAO = ["Estudante","Advogado","Empreendedor","Professor",
                  "Economsita","Engenheiro","Médico","Enfermeiro","Psicologo",
                  "Gestor","Auditor","Locutor","Amigo Contratado", "Ladrão",
                  "Político", "Pedreiro", "Assistente", "Empregado", "Mordomo",
                  "Cozinheiro", "Veterinário", "Dono de Casa", "Super-Heroi",
                  "Apresentador", "Youtuber", "Instagramer", "Pro player",
                  "Analista de Sistemas", "Gerente de Marketing", "Suporte",
                  "Soldado", "Policial"]

LISTA_CIDADES = ["Rio Branco","Maceió","Macapá","Manaus","Salvador",
                 "Fortaleza","Brasília","Vitória","Goiânia","São Luís",
                 "Cuiabá","Campo Grande","Belo Horizonte", "Belém", "João Pessoa",
                 "Curitiba", "Recife", "Teresina","Rio de Janeiro", "Natal","Porto Alegre",
                 "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]

class Gerador:
    def __init__(self):
        self.__IDs = []
        self.__emails = []
        self.__usuarios = []
        self.__BD = {}
        self.__nomesM = LISTA_NOMES_MASCULINOS
        self.__nomesF = LISTA_NOMES_FEMININOS
        self.__sobrenomes = LISTA_SOBRENOMES
        self.__provedores = LISTA_PROVEDORES
        self.__chars = [".","-","_"]
        self.__gen = ["M","F","O"]
        self.__ocupacao = LISTA_OCUPACAO
        self.__cidade = LISTA_CIDADES
        
    def getBD(self):
        return self.__BD

    def geraID(self):
        iD = random.randint(10000,99999)
        if iD in self.__IDs:
            return self.geraID()
        else:
            return iD

    def geraEmail(self,nome,ano):
        carac = self.__chars[random.randint(0,2)]
        provedor = self.__provedores[random.randint(0,len(self.__provedores)-1)]
        email = nome.lower() + carac + str(ano) + "@" + provedor
        if email in self.__emails:
            return self.geraEmail(nome,ano)
        else:
            return email

    def geraUsuario(self,nome):
        usu = nome + str(random.randint(111,999))
        if usu in self.__usuarios:
            return self.geraUsuario(nome)
        else:
            return usu

    def geraSenha(self):
        lista = []
        lista.append(chr(random.randint(65,90)))    #Maiusculas
        lista.append(chr(random.randint(97,122)))   #Minusculas
        lista.append(chr(random.randint(48,57)))    #Numeros
        lista.append(chr(random.randint(33,47)))    #Caracteres
        lista.append(chr(random.randint(91,95)))    #Mais caracteres
        lista.append(chr(random.randint(65,90)))    #Maiusculas
        lista.append(chr(random.randint(97,122)))   #Minusculas
        lista.append(chr(random.randint(48,57)))    #Numeros
        lista.append(chr(random.randint(33,47)))    #Caracteres
        lista.append(chr(random.randint(91,95)))    #Mais caracteres

        senha = ""
        while lista != []:
            pos = random.randint(0,len(lista)-1)
            senha = senha + lista[pos]
            del lista[pos]

        return senha

    def geraNome(self,gen):
        nome = ""
        if gen == "M":
            nome = self.__nomesM[random.randint(0,len(self.__nomesM)-1)]
        elif gen == "F":
            nome = self.__nomesF[random.randint(0,len(self.__nomesF)-1)]
        else:
            lista = self.__nomesM[:] + self.__nomesF[:]
            nome = lista[random.randint(0,len(lista)-1)]

        sobrenome1 = self.__sobrenomes[random.randint(0,len(self.__sobrenomes)-1)]
        sobrenome2 = self.__sobrenomes[random.randint(0,len(self.__sobrenomes)-1)]

        return nome + " " + sobrenome1 + " " + sobrenome2

    def geraOcupacao(self):
        return self.__ocupacao[random.randint(0,len(self.__ocupacao)-1)]

    def geraCidade(self):
        return self.__cidade[random.randint(0,len(self.__cidade)-1)]

    def geraGenero(self):
        return self.__gen[random.randint(0,2)]

    def geraData(self):
        dia = random.randint(10,29)
        mes = random.randint(1,9)
        ano = random.randint(1945,2010)
        return(dia,mes,ano)
    
    def adiciona(self):
        iD = self.geraID()
        gen = self.geraGenero()
        nomeComp = self.geraNome(gen)
        nome = nomeComp.split()[0]        
        nas = self.geraData()
        
        email = self.geraEmail(nome,nas[2])
        usuario = self.geraUsuario(nome)
        senha = self.geraSenha()

        ocup = self.geraOcupacao()
        cidade = self.geraCidade()

        dataSTR = str(nas[0])+"/0"+str(nas[1])+"/"+str(nas[2])
        
        self.__IDs.append(iD)
        self.__emails.append(email)
        self.__usuarios.append(usuario)
        self.__BD[iD] = [email,usuario,senha,nomeComp,dataSTR,gen,ocup,cidade,[]]

    def geraAmizade(self):
        id1 = random.choice(self.__IDs)
        id2 = random.choice(self.__IDs)
        if id1 != id2:
            if (id2 in self.__BD[id1][8]) == False:
                self.__BD[id1][8].append(id2)
                self.__BD[id2][8].append(id1)
            else:
                return self.geraAmizade()
        else:
            return self.geraAmizade()
        
    def grava(self,arq="bd.txt"):
        file = open(arq,"w")
        for chave in self.__BD:
            file.write(str(chave)+";")
            file.write(self.__BD[chave][0]+";")
            file.write(self.__BD[chave][1]+";")
            file.write(self.__BD[chave][2]+";")
            file.write(self.__BD[chave][3]+";")
            file.write(self.__BD[chave][4]+";")
            file.write(self.__BD[chave][5]+";")
            file.write(self.__BD[chave][6]+";")
            file.write(self.__BD[chave][7]+";")
            for iD in self.__BD[chave][8]:
                file.write(str(iD)+" ")
            file.write("\n")
        file.close()

if __name__ == '__main__':
    ger = Gerador()
    perf = int(input("Quantos perfis?\n>>> "))
    
    for i in range(0, perf):
        ger.adiciona()
    amiz = int(input("Quantas amizades?\n>>> "))
    
    for i in range(0, amiz):
        ger.geraAmizade()
        
    try:
        ger.grava(input("Nome do arquivo de gravação\n>>>")+".txt")
        print("Done!")
    except:
        print("Erro de diretório.")
    
