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


vaojuew = ItemBiblioteca("Scarlet", 2020, False)

print(vaojuew.obter_info())