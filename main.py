from registrar import RegistrarDia

historico = []

while True:
    print (f'''
1 - Registrar atividade diária.
2 - Ver histórico.
0 - Sair.
''')
    
    opc = int(input("Digite o código da sua opção: "))

    if opc == 1:
        dados = RegistrarDia()

        dia = {
            "passos": dados.passos,
            "academia": dados.academia,
            "alimentacao": dados.alimentacao,
            "hidratacao": dados.hidratacao,
            "sono": dados.sono,
            "pontos": dados.somarPontos()
        }

        # dia = [dados.passos, dados.academia, dados.alimentacao, dados.hidratacao, dados.sono, dados.somarPontos()]

        historico.append(dia)
        print(historico)

    if opc == 2:
        for dia in historico:
            print(dia)

    if opc == 0:
        break