from re import search


class Cliente:
    def __init__(self, nome: str, cpf: str, idade: str, telefone: str, email: str):
        self._nome = nome.title()
        self._cpf = Cliente.validar_cpf(cpf)
        self._idade = Cliente.validar_idade(idade)
        self._telefone = Cliente.validar_telefone(telefone)
        self._email = Cliente.validar_email(email)

    @classmethod
    def validar_cliente(self, cliente):
        dados_cliente = (cliente.nome, cliente.cpf, cliente.idade,
                         cliente.telefone, cliente.email)
        for dado in dados_cliente:
            if(dado == 'Dado invalido'):
                return False
        return True

    def validar_cpf(cpf):
        if('.' in cpf and '-' in cpf):
            cpf_formatado = cpf.replace('.', '').replace('-', '')
            return cpf_formatado if len(cpf_formatado) == 11 else 'Dado invalido'
        else:
            return cpf if len(cpf) == 11 else 'Dado invalido'

    def validar_telefone(telefone):
        telefone_com_caracteres = '(' in telefone and ')' in telefone and ' ' in telefone and '-' in telefone

        if (telefone_com_caracteres):
            telefone_formatado = telefone.replace(
                '(', '').replace(')', '').replace(' ', '').replace('-', '')

            return telefone_formatado if len(telefone_formatado) == 11 or len(telefone_formatado) == 10 else 'Dado invalido'
        elif(len(telefone) == 11 or len(telefone) == 10):
            return telefone
        else:
            return 'Dado invalido'

    def validar_email(email):
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(search(email_regex, email)):
            return email
        else:
            return 'Dado invalido'

    def validar_idade(idade):
        idade_int = int(idade)
        limite_idade = idade_int >= 18 and idade_int <= 70
        return str(idade_int) if limite_idade else 'Dado invalido'

    def __str__(self):
        return(f'Nome: {self._nome}\nCPF: {self._cpf}\nIdade: {self._idade}\nTelefone: {self._telefone}\nEmail: {self._email}')

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def idade(self):
        return self._idade

    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email

    @idade.setter
    def idade(self, idade):
        self._idade = Cliente.validar_idade(idade)

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = Cliente.validar_telefone(telefone)

    @email.setter
    def email(self, email):
        self._email = Cliente.validar_email(email)
