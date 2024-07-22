from datetime import datetime



def cadastro():
    msg = "Cadastro de cliente"
    data = datetime.now()
    print(data)  
    nome = str(input("Digite o nome do cliente: "))
    cpf_cnpj = str(input("Digite o CPF ou CNPJ:"))
    telefone = str(input("Digite o número para contato: "))
    email = str(input("Digite o email: "))
    endereco = str(input("Digite o endereço: "))

    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg + "\n"), arquivo.write("Data: " + str(data) + "\n"), arquivo.write("Nome: " + nome + "\n"), arquivo.write("CPF/CNPJ: " + cpf_cnpj + "\n"), arquivo.write("Número para contato:" +telefone + "\n"), arquivo.write("Email: " + email + "\n"), arquivo.write(endereco + "\n")


def entrega():
    msg_entrega = "Tipo de serviço e data da entrega"

    servico = input("Qual o tipo de serviço: ")
    entrega_data = input("Data da entrega do serviço: ")

    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg_entrega + "\n"), arquivo.write("Tipo de Serviço: " + servico + "\n"), arquivo.write("Data de entrega do serviço:" + entrega_data + "\n")




def pagamento():

    msg_pagamento = "Forma de Pagamento"

    pgto_valor = input("Valor do serviço: ")
    pgto_prazo = input("Pagamento à vista ou a prazo?  ")
    data_pgto = input("Data do recebimento: ")
    forma_pagamento = input("Qual a forma de pagamento: ")

    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg_pagamento + "\n"), arquivo.write("Valor do serviço: " + pgto_valor + "\n"), arquivo.write("Prazo/Vista: " +pgto_prazo + "\n"), arquivo.write("Data do Pagamento: " + data_pgto + "\n"),  arquivo.write("Forma de Pagamento: " + forma_pagamento + "\n"), 
        arquivo.write("---------------------------------------------------------------" + "\n")

    print("Cadastro de cliente concluído!")




cadastro()
entrega()
pagamento()


if __name__ == "__main__":
     cadastro(),entrega(), pagamento() 