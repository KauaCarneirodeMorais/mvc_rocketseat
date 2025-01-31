
class Algumacoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou Saindo")

with Algumacoisa() as something:
    # a açao da funcao algumacoisa
    print("estou no meio")
