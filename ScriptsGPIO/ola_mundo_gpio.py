#Projeto de Python3 para usar GPIO
import RPi.GPIO as gpio
import time

#Configura o modo de operação da porta
gpio.setmode(gpio.BCM)

#Configura a direção do pino
gpio.setup(17, gpio.OUT)

#Roda o loop principal e pega algum evento que interrompa a sua execução
try:
	#Loop principal
	while True:
		gpio.output(17, gpio.HIGH)
		time.sleep(0.5)
		gpio.output(17, gpio.LOW)
		time.sleep(0.5)
except:
	gpio.cleanup()
