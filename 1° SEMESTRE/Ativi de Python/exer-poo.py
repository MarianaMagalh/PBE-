


class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao, disponivel):
        if ano_publicacao <= 0:
            raise ValueError("O ano de publicação tem que ser maior que 0")
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            raise Exception("O livro já está emprestado.")
        self.disponivel = False

    def devolver(self):
        if self.disponivel:
            raise Exception("O livro já esta disponivel novamente.")
        self.disponivel = True

    def obter_info(self):
        status = "Sim" if self.disponivel else "Não"
        return f"Título:{self.titulo}\nAno: {self.ano_publicacao}\nDisponível:{status}"

livro1 = ItemBiblioteca("Hipotese do amor", 2019, True)

print(livro1.obter_info())

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel,colecao):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.colecao = colecao

    def adicionar_livro(self, livro):
        colecoes_livros = []
        livro = ItemBiblioteca

        livro.append(colecoes_livros)

    def verificar_disponibilidade_colecao(self):
        if not self.colecao:
            raise Exception("O livro da colecao já foi emprestado")
        self.colecao = True

    def obter_info(self):
        titulo_colecao = []

        for livro_c in self.titulo:
            titulo_colecao.append(livro_c)

class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel, n_edicao):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.n_edicao = n_edicao

    def atuaizar_edicao(self, nova_edicao):
        if self.n_edicao >= 0:
            if not self.nova_edicao:
                raise Exception("O número da edição é invalido!")
            
            self.n_edicao += nova_edicao
    
    def restringir_emprestimo(self, dias_max = 14):
        if self.ano_publicacao <= 2000:
            dias_max += 7
            dias_max = False
        
        dias_max = True


    def obter_info(self):
        return f"N° edição:{self.n_edicao}"
    
class Biblioteca():
    def __init__(self):
        self.livros = {}

    def adicionar_item(self, item:ItemBiblioteca):
        if not self.livros[item.titulo]:
            self.livros[item.titulo] = item
        else:
            raise Exception("Item já existe")

    def remover_item(self, titulo):
        self.livros.pop(titulo)

    def listar_itens_disponiveis(self):
        for livro in self.livros:
            print(livro)
        
