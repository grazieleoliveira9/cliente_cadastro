import time
from datetime import datetime


def boas_vindas():
    time.sleep(1)
    print("--------------------------------------------")
    time.sleep(1)
    print( "bem vindo ao sistema de cadastro de cliente")
    time.sleep(1)
    print("--------------------------------------------")


def cadastro():
    msg = "Cadastro de cliente"  
    nome = ("Digite o nome do cliente: ")
    cliente = ("Cliente Pessoa Física ou Juridica: ")
    cpf_cnpj = ("Digite o CPF ou CNPJ: ")
    telefone_celular = ("Digite o número para contato celuar: ")
    telefone_fixo = ("Digite o telefone fixo: ")
    email = ("Digite o email: ")
    endereco = ("Digite o endereço(rua/avenida, bairro, número, CEP, estado ou compl.): ")


    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg + "\n"), 
        arquivo.write("Nome: " + nome + "\n"), 
        arquivo.write("Cliente: " + cliente + "\n"),
        arquivo.write("CPF" + cpf_cnpj + "\n"),
        arquivo.write("Número para contato:" +telefone_celular + "\n"), 
        arquivo.write("Número para contato:" +telefone_fixo + "\n"), 
        arquivo.write("Email: " + email + "\n"), 
        arquivo.write(endereco + "\n")


def servico():
    msg_entrega = "Tipo de serviço e data da entrega"

    servico_tipo = input("Qual o tipo de serviço: ")
    tamanho = input("Qual o tamanho do projeto: ")
    entrega_data = input("Data da entrega prevista do serviço: ")

    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg_entrega + "\n"), 
        arquivo.write("Tipo de Serviço: " + servico_tipo + "\n"), 
        arquivo.write("Tamanho do projeto: " + tamanho + "\n"),
        arquivo.write("Data de entrega do serviço:" + entrega_data + "\n")




def pagamento():

    msg_pagamento = "Forma de Pagamento"

    pgto_valor = input("Valor do serviço: ")
    pgto_prazo = input("Pagamento à vista, prazo ou pix?  ")
    x = input("Forma de pagamento:")
    y = input("Se a prazo, quantidade de parcelas(se não houver, aperte enter) :")
    print("Cadastro de cliente concluído e pedido concluído!")
    data = datetime.now()
    print(data)
        

    with open("cadastro.txt", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.write(msg_pagamento + "\n"), 
        arquivo.write("Valor do serviço: " + pgto_valor + "\n"), 
        arquivo.write("Prazo/Vista: " +pgto_prazo + "\n"), 
        arquivo.write("Modo de pagamento: " + x + "\n") ,
        arquivo.write("Quantidade de parcelas: " + y + "\n"), 
        arquivo.write("Data: " + str(data) + "\n"), 
        arquivo.write("---------------------------------------------------------------" + "\n")

    


def main():
    boas_vindas()
    cadastro()
    servico()
    pagamento()

main()

if __name__ == "__main__":
     cadastro(),servico(), pagamento() 