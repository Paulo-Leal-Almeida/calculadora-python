def calculadora():
    print("=== Calculadora Simples ===")
    print("Operações disponíveis: +  -  *  /")
    print("Digite 'sair' para encerrar.\n")

    while True:
        num1 = input("Digite o primeiro número: ")
        if num1.lower() == "sair":
            print("Encerrando a calculadora. Até mais!")
            break

        num2 = input("Digite o segundo número: ")
        if num2.lower() == "sair":
            print("Encerrando a calculadora. Até mais!")
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("⚠️ Entrada inválida! Digite números válidos.\n")
            continue

        operacao = input("Escolha a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("⚠️ Erro: divisão por zero não é permitida!\n")
                continue
            resultado = num1 / num2
        else:
            print("⚠️ Operação inválida! Tente novamente.\n")
            continue

        print(f"Resultado: {resultado}\n")

# Executa a calculadora
calculadora()
