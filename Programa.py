import random


class Cuestionador:

    def __init__(self):

        self.questions=[
            "¿Qué es el ALMICANTARAT?",
            "¿Dónde se encuentra el Zenit?",
            "¿Cuántos órdenes existen en la taxonomía de suelos?"
        ]

        self.answers=[
            "Círculo imaginario en la esfra celeste",
            "90 grados respecto al horizonte",
            12
        ]

    def jugar(self):
        #Generar un númerp aleatorio entre 0 y n-1 siendo n el tamaño
        #de la lista de preguntas
        n=len(self.questions)
        number= random.randint(0, n-1)
        print(self.questions[number])

        #solicitar la respuesta al usuario
        respuesta=input("¿Cuál es tu respuesta?")

        #verificar di la respuesta es correcta
        if respuesta== self.answers[number]:
            print("Qué chimba so")
        else:
            print("palo de bruto")