from calcFunctions import *
from plot import *
from tkinter import *
import webbrowser

def path(f):
    #we ask for the shape properties
    print("Image of a shape: {z=x+iy: x0<x<x1, y=f*(x)}")
    x0=float(ask('x0=', '0'))
    x1=float(ask('x1=', '1'))
    print("Please type in the (real) function for the path of the plot:")
    func1=ask('f*(x)=', '0')
    f1=lambda x: eval(func1)
    #we ask for the computer boundaries
    print("""As I am a computer, \
I will create N "random" points""")
    N=int(ask('N=', 10000))

    #creating the list of points
    listz=createRandomFromPath(x0, x1, f1, N)

    #plot function
    myPlot(f, listz)



class Path(Frame):
    def __init__(self, boss=None, **arg):
        #class __init__
        Frame.__init__(self, boss, **arg)
        #name the window:
        boss.title("Images of complicated shapes by a complex function")
        
        #plot variables
        self.x0=None
        self.x1=None
        self.fPath=None
        self.N=None
        self.f=None
        
        ##graph objects
        Label(self, text='{ z = x + iy :   x0 < x < x1 & y = f*(x) }', \
              font=('Times', -30, 'bold'), fg='red').pack(pady=15)
        #website link (explanation of the shape)
        Button(self, text='Shapes explanations', \
               command=lambda e=None: webbrowser.open_new("shapes.html")).pack()
        #x0
        Label(self, text='Lower bound for x (x0)', \
              font=('Times', -20, 'bold')).pack()
        self.x0Input=Entry(self, width=25)
        self.x0Input.pack(anchor='w')
        self.x0Input.insert(0, '-1.5')
        Label(self, text='(x0 should be real)').pack(anchor='w')
        #x1
        Label(self, text='Upper bound for x (x1)', \
              font=('Times', -20, 'bold')).pack()
        self.x1Input=Entry(self, width=25)
        self.x1Input.pack(anchor='w')
        self.x1Input.insert(0, '2')
        Label(self, text='(x1 should be real)').pack(anchor='w')
        #f*
        Label(self, text='Function of y in terms of x ( f*(x) )', \
              font=('Times', -20, 'bold')).pack()
        self.func1Input=Entry(self, width=25)
        self.func1Input.pack(anchor='w')
        self.func1Input.insert(0, '-x*x*x + x*x')
        Label(self, text='(f*(x) should be real, \
I will take the modulus if not)').pack(anchor='w')
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
        self.funcInput.insert(0, '-1j-2*z')
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
            listz=createRandomFromPath(self.x0, self.x1, \
                                        self.f1, self.N)
            #plot function
            myPlot(self.f, listz)

    def updateVals(self, event=None):
        #x0
        try:
            self.x0=complex(self.x0Input.get())
        except:
            self.info.config(text="Invalid x0", fg='red')
        else:
            #x1
            try:
                self.x1=complex(self.x1Input.get())
            except:
                self.info.config(text="Invalid x1", fg='red')
            else:
                #N
                try:
                    self.N=int(self.NInput.get())
                except:
                    self.info.config(text="Invalid N", fg='red')
                else:
                    #func*
                    try:
                        self.f1=lambda x: eval(self.func1Input.get())
                    except:
                        self.info.config(text="Invalid function f*", fg='red')
                    else:
                        #func
                        try:
                            self.f=lambda z: eval(self.funcInput.get())
                        except:
                            self.info.config(text="Invalid function f", \
                                             fg='red')
                        else:
                            self.info.config(text="Everything is valid", \
                                             fg='green')
                            return True
        return False
        


if __name__=='__main__':
    root=Tk()
    Path(root).pack(anchor='w', padx=5, pady=5)
    root.mainloop()




