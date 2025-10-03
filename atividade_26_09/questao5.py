class DispositivoEletronico:
    def ligar(self):
        print(f"Dispositivo ligado")
    def desligar(self):
        print(f"Dispositivo desligado")
    
class Computador(DispositivoEletronico):
    def instalar_software(self):
        print(f"Instalando software")

class Notebook(Computador):
    def verificar_bateria(self):
        print(f"Verificado a bateria")

meu_notebook = Notebook()
meu_notebook.ligar()
meu_notebook.instalar_software()
meu_notebook.verificar_bateria()