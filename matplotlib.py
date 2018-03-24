'''Lab 4: Matplotlib'''
'''Name: Bradley Sumoge'''

'''Problem 1'''
def rand(n):
    import numpy as np
    A = np.random.normal(size=(n,n))
    B = A.mean(axis=1)[:None]
    C = np.var(B)
    return C

def plot():
    import numpy as np
    from matplotlib import pyplot as plt
    Y = np.zeros(10)
    Y[0] = rand(100)
    Y[1] = rand(200)
    Y[2] = rand(300)
    Y[3] = rand(400)
    Y[4] = rand(500)
    Y[5] = rand(600)
    Y[6] = rand(700)
    Y[7] = rand(800)
    Y[8] = rand(900)
    Y[9] = rand(1000)
    plt.plot(Y)
    plt.show()
    return Y

'''Problem 2'''
def plot_trig():
    import numpy as np
    from matplotlib import pyplot as plt
    x = np.linspace(np.pi*-1,np.pi,100)
    plt.plot(x,np.sin(x))
    plt.show()
    plt.plot(x,np.cos(x))
    plt.show()
    plt.plot(x,np.arctan(x))
    plt.show()
    return

'''Problem 3'''
def plot_custom():
    import numpy as np
    from matplotlib import pyplot as plt
    x1 = np.linspace(-2,1,50)
    x2 = np.linspace(1,6,50)
    plt.plot(x1,1/(x1-1), 'm--', linewidth=4)
    plt.plot(x2,1/(x2-1), 'm--', linewidth=4)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    plt.show()
    return

'''Problem 4'''
def subplot():
    import numpy as np
    from matplotlib import pyplot as plt
    x = np.linspace(0,2*np.pi,100)

    ax1 = plt.subplot(2,2,1)
    ax1.plot(x, np.sin(x), 'g')
    ax1.set_title("sin(x)")
    plt.axis([0, 2*np.pi, -2, 2])

    ax2 = plt.subplot(2,2,2)
    ax2.plot(x, np.sin(2*x), 'r--')
    ax2.set_title("sin(2x)")
    plt.axis([0, 2*np.pi, -2, 2])

    ax3 = plt.subplot(2,2,3)
    ax3.plot(x, 2*np.sin(x), 'b--')
    ax3.set_title("2sin(x)")
    plt.axis([0, 2*np.pi, -2, 2])
    
    ax4 = plt.subplot(2,2,4)
    ax4.plot(x, 2*np.sin(2*x), 'm:')
    ax4.set_title("2sin(2x)")
    plt.axis([0, 2*np.pi, -2, 2])
        
    plt.suptitle("Sine Plots")
    plt.show()
    return
    
    