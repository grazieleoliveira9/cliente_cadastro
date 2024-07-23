from datetime import datetime



def cadastro():
    msg = "Cadastro de cliente"
    data = datetime.now()
    print(data)  
    nome = str(input("Digite o nome do cliente: "))
    cliente = str(input("Cliente Pessoa Física ou Juridica: "))
    cpf_cnpj = str(input("Digite o CPF ou CNPJ: "))
    telefone = str(input("Digite o número para contato: "))
    email = str(input("Digite o email: "))
    endereco = str(input("Digite o endereço(rua/avenida, bairro, número, CEP, estado ou compl.): "))


    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg + "\n"), 
        arquivo.write("Data: " + str(data) + "\n"), 
        arquivo.write("Nome: " + nome + "\n"), 
        arquivo.write("Cliente: " + cliente + "\n"),
        arquivo.write("CPF" + cpf_cnpj + "\n"),
        arquivo.write("Número para contato:" +telefone + "\n"), 
        arquivo.write("Email: " + email + "\n"), 
        arquivo.write(endereco + "\n")


def servico():
    msg_entrega = "Tipo de serviço e data da entrega"

    servico_tipo = input("Qual o tipo de serviço: ")
    entrega_data = input("Data da entrega prevista do serviço: ")

    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg_entrega + "\n"), 
        arquivo.write("Tipo de Serviço: " + servico_tipo + "\n"), 
        arquivo.write("Data de entrega do serviço:" + entrega_data + "\n")




def pagamento():

    msg_pagamento = "Forma de Pagamento"

    pgto_valor = input("Valor do serviço: ")
    pgto_prazo = input("Pagamento à vista, prazo ou pix?  ")
    x = input("Forma de pagamento:")
    y = input("Se a prazo, quantidade de parcelas(se não houver, aperte enter) :")
    print("Cadastro de cliente concluído e pedido concluído!")
        

    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg_pagamento + "\n"), 
        arquivo.write("Valor do serviço: " + pgto_valor + "\n"), 
        arquivo.write("Prazo/Vista: " +pgto_prazo + "\n"), 
        arquivo.write("Modo de pagamento: " + x + "\n") ,
        arquivo.write("Quantidade de parcelas: " + y + "\n"), 
        arquivo.write("---------------------------------------------------------------" + "\n")

    


def main():
    cadastro()
    servico()
    pagamento()

main()
# if __name__ == "__main__":
#      cadastro(),servico(), pagamento() 