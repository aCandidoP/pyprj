class Contato():
    id = 1
    def __init__(self, id, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.id = Contato.id
        Contato.id += 1

class Agenda():
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, id, nome, email, telefone):
        novo_contato = Contato(nome, email, telefone, id)
        self.contatos.append(novo_contato)

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None
    
    def exibir_contatos(self):
        for contato in self.contatos:
            print(f'{contato.id} {contato.nome} {contato.telefone} {contato.email}')

# Adicionando Contatos

agenda = Agenda()
agenda.adicionar_contato(Contato.id, "André", 'andre@gmail', '9999-9999')
agenda.exibir_contatos()
agenda.adicionar_contato(Contato.id, "André", 'andre@gmail', '9999-9999')
agenda.exibir_contatos()