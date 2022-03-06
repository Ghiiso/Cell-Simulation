from cProfile import label
import matplotlib.pyplot as plt

def mostraGrafici(cell,pellet,tempo):
    plt.plot(tempo,cell, label="cellule", color="blue")
    plt.plot(tempo,pellet, label="pellet", color = "red")

    plt.xlabel('tempo')
    plt.legend()
    plt.show()



