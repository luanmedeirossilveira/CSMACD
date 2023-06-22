import threading
import time
import random


class Transmitter(threading.Thread):

  def __init__(self, id):
    super(Transmitter, self).__init__()
    self.id = id

  def run(self):
    while True:
      # Verificar se o meio de transmissão está ocupado
      if self.is_medium_busy():
        print(
          f'Transmitter {self.id}: Meio de transmissão ocupado. Realizando backoff...'
        )
        self.perform_backoff()
      else:
        print(
          f'Transmitter {self.id}: Meio de transmissão livre. Enviando quadro...'
        )
        # Simulando o envio de um quadro
        self.send_frame()
        # Aguardar um intervalo de tempo antes de enviar novamente
        self.wait_interval()

  def is_medium_busy(self):
    # Simulando a detecção do meio de transmissão ocupado
    busy = random.choice([True, False])
    if busy:
      print(f'Transmitter {self.id}: O meio de transmissão está ocupado.')
    return busy

  def perform_backoff(self):
    # Simulando o algoritmo de backoff com tempo exponencial truncado
    backoff_time = 2 ** random.randint(1, 6)
    print(
      f'Transmitter {self.id}: Aguardando backoff por {backoff_time} unidades de tempo.'
    )
    time.sleep(backoff_time)

  def send_frame(self):
    print(f'Transmitter {self.id}: Quadro enviado.')

  def wait_interval(self):
    # Aguardar um intervalo de tempo antes de enviar novamente
    interval = random.randint(1, 5)
    print(
      f'Transmitter {self.id}: Aguardando {interval} unidades de tempo antes de enviar novamente.'
    )
    time.sleep(interval)


# Criar transmissores
transmitter1 = Transmitter(1)
transmitter2 = Transmitter(2)

# Iniciar as threads dos transmissores
transmitter1.start()
transmitter2.start()
