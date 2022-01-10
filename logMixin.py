class LogMixin:
    #Como não será preciso saber a instancia do metodo ele será definido como statci
    @staticmethod
    def write(msg):
        #Crinando um arquivo novo com o nome de log.lo, usando o 'a+' para indicar que e para sempre acrescentar
        #uma linha nova e passando o as f para pegar o nome do arquivo no parametro('log.log'
        with open('log.log', 'a+') as f:
            #pagando o parametro f para indicar o arquivo e mandando escrever a mensagem contida no parametro msg
            f.write(msg)
            #usando o f.write(/n) para quebrar uma linha toda vez que for escrever uma nova msg
            f.write('\n')

    def log_Info(self,msg):
        self.write(f'INFO: {msg}')

    def log_Error(self,msg):
        self.write(f'ERROR : {msg}')
