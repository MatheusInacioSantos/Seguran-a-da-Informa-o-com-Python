import ctypes

atributo_ocultar = 0x02

pasta = input('Digite o caminho da pasta ou arquivo ex.: (c:/pasta/arquivo.txt): ')

retorno = ctypes.windll.Kernel32.SetFileAttributesW(pasta, atributo_ocultar)

# ou passe o nome do arquivo direto
# retorno = ctypes.windll.Kernel32.SetFileAttributesW('teste.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado!')
else:
    print('Arquivo não foi ocultado')