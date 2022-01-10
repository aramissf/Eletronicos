from eletro import Eletronico
from logMixin import LogMixin
class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            Info = f'{self._nome}, nao esta ligado'
            print(Info)
            self.log_Error(Info)
            return
        if self._conectado:
            Info = f'{self._nome}, ja esta concetado'
            print(Info)
            self.log_Error(Info)
        Info = f'{self._nome},concetado'
        print(Info)
        self.log_Info(Info)
        self._conectado = True

    def desconectar(self):
        if not self._ligado:
            Info = f'{self._nome}, nao esta ligado'
            print(Info)
            self.log_Error(Info)
            return

        if not self._conectado:
            Info = f'{self._nome}, nao esta conectado'
            print(Info)
            self.log_Error(Info)
            return

        Info = f'{self._nome}, desconectado'
        print(Info)
        self.log_Info(Info)
        self._conectado = False




