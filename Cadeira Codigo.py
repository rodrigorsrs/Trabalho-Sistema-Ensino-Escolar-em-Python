import os
import json

class Pessoa:
    def __init__(self, codigo, nome, cpf):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf

class Estudante(Pessoa):
    def __init__(self, codigo, nome, cpf):
        super().__init__(codigo, nome, cpf)

class Professor(Pessoa):
    def __init__(self, codigo, nome, cpf):
        super().__init__(codigo, nome, cpf)

class Disciplina:
    def __init__(self, codigodisciplina, nome):
        self.codigodisciplina = codigodisciplina
        self.nome = nome

class Turma:
    def __init__(self, codigoturma, codigoprofessor, codigodisciplina):
        self.codigoturma = codigoturma
        self.codigoprofessor = codigoprofessor
        self.codigodisciplina = codigodisciplina

class Matricula:
    def __init__(self, codigomatricula, codigoturma, codigoestudante):
        self.codigomatricula = codigomatricula
        self.codigoturma = codigoturma
        self.codigoestudante = codigoestudante

class DataManager:
    @staticmethod
    def salvar_dados(nome_arquivo, lista_objetos):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump([vars(obj) for obj in lista_objetos], arquivo, indent=4)
        print(f"Lista de {nome_arquivo.split('.')[0].capitalize()} salva com sucesso")
        input("Pressione Qualquer Teclad para continuar....")

    @staticmethod
    def carregar_dados(nome_arquivo, classe_objeto):
        lista_objetos = []
        try:
            with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                for item in dados:
                    obj = classe_objeto(**item)
                    lista_objetos.append(obj)
            print("Carregado com sucesso!")
            return lista_objetos
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return []

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu_principal():
    limpar_tela()
    print("Sistema de Ensino Escolar")
    print("--------------------------------------")
    print("1 - Estudantes")
    print("2 - Professores")
    print("3 - Disciplinas")
    print("4 - Turmas")
    print("5 - Matrículas")
    print("0 - Sair")
    print("--------------------------------------")
    opcao_selecionada = input("Digite a opção desejada: ")
    if opcao_selecionada.strip() == '':
        return 0
    return int(opcao_selecionada)

def menu_operacoes(opcao_menu_principal):
    limpar_tela()
    print(f"Menu de Operações - Opção selecionada: {opcoes_menu_principal[opcao_menu_principal - 1]}")
    print("--------------------------------------")
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Excluir")
    print("5 - Salvar Lista")
    print("6 - Carregar Lista")
    print("0 - Voltar")
    print("--------------------------------------")
    opcao_selecionada = input("Digite a opção desejada: ")
    return int(opcao_selecionada)

def incluir(classe_objeto, lista_objetos):
    atributos = {}
    for chave in classe_objeto.__init__.__code__.co_varnames[1:]:
        if chave == 'codigoturma':
            mensagem = 'Digite o Código da Turma: '
        elif chave == 'codigoprofessor':
            mensagem = 'Digite o Código do Professor: '
        elif chave == 'codigoestudante':
            mensagem = 'Digite o Código do Estudante: '
        elif chave == 'codigomatricula':
            mensagem = 'Digite o Código da Matrícula: '
        elif chave == 'codigodisciplina':
            mensagem = 'Digite o Código da Disciplina: '
        else:
            mensagem = f'Digite o(a) {chave}: '
            
        valor = input(mensagem)
        atributos[chave] = valor
        
        if chave == 'codigoestudante':
            print("Código do Estudante:", valor)
        elif chave == 'codigoprofessor':
            print("Código do Professor:", valor)
        elif chave == 'codigoturma':
            print("Código da Turma:", valor)
        elif chave == 'codigomatricula':
            print("Código da Matrícula:", valor)
        elif chave == 'codigodisciplina':
            print("Código da Disciplina:", valor)
        elif chave != 'codigo' and chave != 'codigoprofessor' and chave != 'codigoestudante' and chave !='codigodisciplina' and chave !='codigomatricula' and chave !='codigoturma':
            print(f"{chave.capitalize()}: {valor}")
    novo_objeto = classe_objeto(**atributos)
    lista_objetos.append(novo_objeto)
    print("Informações Adicionadas com sucesso")
    input("Pressione qualquer tecla para continuar...")


def listar(classe_objeto, lista_objetos):
    for objeto in lista_objetos:
        atributos = vars(objeto)
        if 'codigo' in atributos:  # Verifica se 'codigo' está presente nos atributos
            print(f"Código da {classe_objeto.__name__}: {atributos['codigo']}")
        for chave, valor in atributos.items():
            if chave == 'codigoestudante':
                print("Código do Estudante:", valor)
            if chave == 'codigoprofessor':
                print("Codigo do Professor:", valor)
            if chave == 'codigoturma':
                print("Codigo da Turma:", valor)
            if chave == 'codigomatricula':
                print("Codigo de Matricula:", valor)
            if chave == 'codigodisciplina':
                print("Codigo da Disciplina:", valor)
            elif chave != 'codigo' and chave != 'codigoprofessor' and chave != 'codigoestudante' and chave !='codigodisciplina' and chave !='codigomatricula' and chave !='codigoturma':
                print(f"{chave.capitalize()}: {valor}")
        print("--------------------------------------")

def editar(classe_objeto, lista_objetos):
    codigo = input("Digite o código do objeto que deseja editar: ")
    for objeto in lista_objetos:
        if objeto.codigo == codigo:
            nome = input("Novo nome: ")
            cpf = input("Novo CPF: ")
            objeto.nome = nome
            objeto.cpf = cpf
            print("Objeto editado com sucesso!")
            return
    print("Objeto não encontrado.")

def excluir(classe_objeto, lista_objetos):
    codigo = input("Digite o código do objeto que deseja excluir: ")
    for objeto in lista_objetos:
        if objeto.codigo == codigo:
            lista_objetos.remove(objeto)
            print("Objeto excluído com sucesso!")
            return
    print("Objeto não encontrado.")

def salvar(nome_arquivo, lista_objetos):
    DataManager.salvar_dados(nome_arquivo, lista_objetos)

def carregar(nome_arquivo, classe_objeto, lista_objetos):
    lista_objetos.clear()
    lista_objetos.extend(DataManager.carregar_dados(nome_arquivo, classe_objeto))

opcoes_menu_principal = ["Estudantes", "Professores", "Disciplinas", "Turmas", "Matrículas"]
lista_estudante = []
lista_professor = []
lista_disciplina = []
lista_turma = []
lista_matricula = []

def main():

    while True: 
        opcao_menu_principal = menu_principal()

        if opcao_menu_principal == 0:
            break 
        else:
            lista_objetos = None
            if opcao_menu_principal == 1:
                lista_objetos = lista_estudante
                classe_objeto = Estudante
            elif opcao_menu_principal == 2:
                lista_objetos = lista_professor
                classe_objeto = Professor
            elif opcao_menu_principal == 3:
                lista_objetos = lista_disciplina
                classe_objeto = Disciplina
            elif opcao_menu_principal == 4:
                lista_objetos = lista_turma
                classe_objeto = Turma
            elif opcao_menu_principal == 5:
                lista_objetos = lista_matricula
                classe_objeto = Matricula

            while True:
                opcao_menu_operacoes = menu_operacoes(opcao_menu_principal) 
                if opcao_menu_operacoes == 0:
                    break 
                elif opcao_menu_operacoes == 1:
                    incluir(classe_objeto, lista_objetos)
                elif opcao_menu_operacoes == 2:
                    listar(classe_objeto, lista_objetos)
                    input("Pressione qualquer tecla para continuar...")
                elif opcao_menu_operacoes == 3:
                    editar(classe_objeto, lista_objetos)
                elif opcao_menu_operacoes == 4:
                    excluir(classe_objeto, lista_objetos)
                elif opcao_menu_operacoes == 5:
                    salvar(classe_objeto, lista_objetos)
                elif opcao_menu_operacoes == 6:
                    carregar(classe_objeto, lista_objetos)
                else:
                    limpar_tela()
                    print("Opção inválida!")
                    input("Pressione qualquer tecla para continuar...")

if __name__ == "__main__":
    main()