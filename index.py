from features.compress import compress
from features.decompress import decompress

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Compactar texto (Sobrescreve saida.huf)")
        print("2 - Descompactar texto (Sobrescreve entrada.txt)")
        print("0 - Sair")
        
        choice = input("Digite sua escolha: ")

        if choice == "1":
            compress()
        elif choice == "2":
            decompress()
        elif choice == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
