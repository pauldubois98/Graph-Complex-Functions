import matplotlib.pyplot as plt
from calcFunctions import *


def boundaries(mini, maxi):
    if mini>1.1*mini:
        mini*=1.1
    else:
        mini*=0.9
    if maxi<1.1*maxi:
        maxi*=1.1
    else:
        mini*=0.9
        
    
    if mini==maxi:
        mini-=1
        maxi+=1
    return (mini, maxi)

def boundariesX(listfx, listx):
    mini=min(min(listfx), min(listx))
    maxi=max(max(listfx), max(listx))
    return boundaries(mini, maxi)
    
def boundariesY(listfy, listy):
    mini=min(min(listfy), min(listy))
    maxi=max(max(listfy), max(listy))
    return boundaries(mini, maxi)


def myPlot(f, listz):
    #calculations over the complex
    listfz=apply(f, listz)

    #print the first 10 calculations
    print('\n\n\tCalculating random points on the figure (z), \
and their images (w=f(z))')
    lprint(listz[:10], listfz[:10])
    print('...')

    ##making the real & imaginary parts
    #for the z
    listfx=takeRe(listfz)
    listfy=takeIm(listfz)
    #for the f(z)
    listx=takeRe(listz)
    listy=takeIm(listz)

    #plotting z in blue and f(z) in red
    plt.scatter(listx, listy, color='blue')
    plt.scatter(listfx, listfy, color='red')

    #making inteligent boundaries of the plot
    plt.xlim(boundariesX(listfx, listx))
    plt.ylim(boundariesY(listfy, listy))
    
    #label axis
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    #grid
    plt.grid(True, which='both')
    #axis
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    #title
    #plt.title('blue: shape; red: image of the shape')

    #get the user know the colors
    print("\n\n\twith w=f(z):\n")
    print("Points in blue: figure in z-plane")
    print("Points in red: image of the figure in w-plane")

    #finally, we show the result ;)
    plt.show()

