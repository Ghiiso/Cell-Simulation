import matplotlib.pyplot as plt

def mostraGrafici(cell,pellet,ripr,vel,tempo):
    plt.plot(tempo,cell, label="cellule", color="blue")
    plt.plot(tempo,pellet, label="pellet", color = "red")
    #plt.plot(tempo,ripr, label="prob. riproduzione")
    plt.plot(tempo,vel, label="vel media")

    plt.xlabel('tempo (s)')
    plt.legend()
    plt.show()



