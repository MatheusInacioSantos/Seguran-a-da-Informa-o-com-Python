import os # importa o modulo ou biblioteca os (integra os programas e recursos do sistema operacional)

print('#' * 60) # imprimindo o # sessenta vezes

ip_ou_host = input('Digite o ip ou host que sera verificado: ') # criamos uma variavel que vai receber do usuario um io
print('-' * 60)  # imprimindo o - sessenta vezes
os.system('ping -n 6 {}' .format(ip_ou_host)) # chamando system da biblioteca os - comando ping
# -n -nu de pacotes que serão 6 {}
print('-' * 60) # imprimindo o - sessenta vezes