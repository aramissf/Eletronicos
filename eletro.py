from logMixin import LogMixin


class Eletronico(LogMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False



    def ligar(self):
        if self._ligado:
            Info = f'{self._nome}, Ja esta ligado'
            print(Info)
            self.log_Error(Info)
            return
        Info = f'{self._nome}, ligou'
        print(Info)
        self.log_Info(Info)
        self._ligado = True



    def desligar(self):
        if not self._ligado:
            Info = f'{self._nome}, nao esta ligado'
            print(Info)
            return

        Info = f'{self._nome}, esta desligado'
        print(Info)
        self.log_Info(Info)
        self._ligado = False



