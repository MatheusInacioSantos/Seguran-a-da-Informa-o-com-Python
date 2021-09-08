import random, string
tamanho =int(input('Digite o tamanho da senha que deseja: '))

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'

rnd = random.SystemRandom() # pega da biblioteca os a seguinte classe = os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))