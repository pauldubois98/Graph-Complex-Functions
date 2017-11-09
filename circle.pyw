from calcFunctions import *
from plot import *
from tkinter import *
import webbrowser

def circle(f):
    #we ask for the circle properties
    print("Put 'j' for the imaginary part eg: z0=1+2j")
    print("Image of a circle: |z-z0|=R")
    z0=complex(ask('z0=', '0'))
    R=float(ask('R=', 1))
    #we ask for the computer boundaries
    print("""As I am a computer, \
I will create N "random" points""")
    N=int(ask('N=', 10000))

    #creating the list of points
    listz=createRandomFromCircle(z0, R, N)

    #plot function
    myPlot(f, listz)


class Circle(Frame):
    def __init__(self, boss=None, **arg):
        #class __init__
        Frame.__init__(self, boss, **arg)
        #name the window:
        boss.title("Images of circles by a complex function")
        
        #plot variables
        self.z0=None
        self.R=None
        self.N=None
        self.f=None
        
        ##graph objects
        Label(self, text='{ z: | z - z0 | = R }', \
              font=('Times', -30, 'bold'), fg='red').pack(pady=15)
        #website link (explanation of the shape)
        Button(self, text='Shapes explanations', \
               command=lambda e=None: webbrowser.open_new("shapes.html")).pack()
        #z0
        Label(self, text='Center of the circle (z0)', \
              font=('Times', -20, 'bold')).pack()
        self.z0Input=Entry(self, width=25)
        self.z0Input.pack(anchor='w')
        self.z0Input.insert(0, '1+2j')
        Label(self, text='(use j for imaginary part)').pack(anchor='w')
        #R
        Label(self, text='Radius of the circle (R)', \
              font=('Times', -20, 'bold')).pack()
        self.RInput=Entry(self, width=25)
        self.RInput.pack(anchor='w')
        self.RInput.insert(0, '1')
        #N
        Label(self, text='Number of points randomly generated (N)', \
              font=('Times', -20, 'bold')).pack()
        self.NInput=Entry(self, width=25)
        self.NInput.pack(anchor='w')
        self.NInput.insert(0, '10000')
        #func
        Label(self, text='Complex function to graph (f(z))', \
              font=('Times', -20, 'bold')).pack()
        self.funcInput=Entry(self, width=40)
        self.funcInput.pack(anchor='w')
        self.funcInput.insert(0, 'pow(z-1, 3)+5')
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
            listz=createRandomFromCircle(self.z0, self.R, self.N)
            #plot function
            myPlot(self.f, listz)

    def updateVals(self, event=None):
        #z0
        try:
            self.z0=complex(self.z0Input.get())
        except:
            self.info.config(text="Invalid z0", fg='red')
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
    Circle(root).pack(anchor='w', padx=5, pady=5)
    root.mainloop()

