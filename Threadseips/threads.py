import time
from threading import Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {} \n' .format(piloto, trajeto))

# def carro1(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print('Carro1: ', trajeto)
#         trajeto += velocidade
#
# def carro2(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print('Carro2: ', trajeto)
#         trajeto += velocidade
#

if __name__ == '__main__':
    # carro1(10)
    # carro2(20)
    t_carro1 = Thread(target=carro, args=[1, 'Matheus'])
    t_carro2 = Thread(target=carro, args=[1.5, 'Thiago'])

    t_carro1.start()
    t_carro2.start()