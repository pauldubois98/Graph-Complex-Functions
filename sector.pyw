from calcFunctions import *
from plot import *
from tkinter import *
import webbrowser

def sector(f):
    #we ask for the sector properties
    print("Image of a sector: @1<arg(z)<@2")
    a1=pi*float(ask('@1=pi*', '0.25'))
    a2=pi*float(ask('@2=pi*', '0.75'))
    #we ask for the computer boundaries
    print("As I am a computer, \
I need an upper bound R for the lenght of the points")
    R=float(ask('R=', 1))
    print("""As I am a computer, \
I will create N "random" points""")
    N=int(ask('N=', 1000))

    #creating the list of points
    listz=createRandomFromSector(a1, a2, R, N)

    #plot function
    myPlot(f, listz)







class Sector(Frame):
    def __init__(self, boss=None, **arg):
        #class __init__
        Frame.__init__(self, boss, **arg)
        #name the window:
        boss.title("Images of discs by a complex function")
        
        #plot variables
        self.a0=None
        self.a1=None
        self.R=None
        self.N=None
        self.f=None
        
        ##graph objects
        Label(self, text='{ z: @0 < arg(z) < @1   (& | z | < R)}', \
              font=('Times', -30, 'bold'), fg='red').pack()
        #z0
        Label(self, text='Starting point of the segment (@0)', \
              font=('Times', -20, 'bold')).pack()
        self.a0Input=Entry(self, width=25)
        self.a0Input.pack(anchor='w')
        self.a0Input.insert(0, '1/4')
        Label(self, text='(will be multiplied by pi)').pack(anchor='w')
        #z1
        Label(self, text='Ending point of the segment (@1)', \
              font=('Times', -20, 'bold')).pack()
        self.a1Input=Entry(self, width=25)
        self.a1Input.pack(anchor='w')
        self.a1Input.insert(0, '3/4')
        Label(self, text='(will be multiplied by pi)').pack(anchor='w')
        #R
        Label(self, text='(due to computer) limit for | z | (R)', \
              font=('Times', -20, 'bold')).pack()
        self.RInput=Entry(self, width=25)
        self.RInput.pack(anchor='w')
        self.RInput.insert(0, '10')
        #N
        Label(self, text='Number of points randomly generated (N)', \
              font=('Times', -20, 'bold')).pack()
        self.NInput=Entry(self, width=25)
        self.NInput.pack(anchor='w')
        self.NInput.insert(0, '10000')
        #func
        Label(self, text='Complex function to graph ( f(z) )', \
              font=('Times', -20, 'bold')).pack()
        self.funcInput=Entry(self, width=40)
        self.funcInput.pack(anchor='w')
        self.funcInput.insert(0, '(z+1)/(z-1)')
        Label(self, text='Functions that you can use are listed here:', \
              justify='left').pack(anchor='w')
        url="https://docs.python.org/3.5/library/cmath.html"
        Button(self, text='Mathematical functions for complex numbers', \
               command=lambda e=None: webbrowser.open_new(url)).pack(anchor='w')

        #info label
        self.info=Label(self, text=">>> click 'GRAPH !' to draw the graph <<<",\
                        font=('Times', -20, 'bold'), fg='grey')
        self.info.pack(pady=10)
        #validation button
        Button(self, text='GARPH !', bg='green', \
               command=self.graph).pack(pady=10)

    def graph(self):
        if self.updateVals():
            #creating the list of points
            listz=createRandomFromSector(self.a0, self.a1, self.R, self.N)
            #plot function
            myPlot(self.f, listz)

    def updateVals(self, event=None):
        #a0
        try:
            self.a0=float(eval(self.a0Input.get()))*pi
        except:
            self.info.config(text="Invalid @0", fg='red')
        else:
            #a1
            try:
                self.a1=float(eval(self.a1Input.get()))*pi
            except:
                self.info.config(text="Invalid @1", fg='red')
            else:
                #R
                try:
                    self.R=float(self.RInput.get())
                except:
                    self.info.config(text="Invalid R", fg='red')
                else:
                    #N
                    try:
                        self.N=int(self.NInput.get())
                    except:
                        self.info.config(text="Invalid N", fg='red')
                    else:
                        #func
                        try:
                            self.f=lambda z: eval(self.funcInput.get())
                        except:
                            self.info.config(text="Invalid function", fg='red')
                        else:
                            self.info.config(text="Everything is valid", fg='green')
                            return True
        return False

                
        


if __name__=='__main__':
    root=Tk()
    Sector(root).pack(anchor='w', padx=5, pady=5)
    root.mainloop()

