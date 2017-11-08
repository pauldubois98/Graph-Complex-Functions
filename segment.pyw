from calcFunctions import *
from plot import *
from tkinter import *
import webbrowser


def segment(f):
    #we ask for the segment properties
    print("Put 'j' for the imaginary part eg: z0=1+2j")
    print("Image of a segment from z0 to z1:")
    z0=complex(ask('z0=', '-1-1j'))
    z1=complex(ask('z1=', '2+2j'))
    #we ask for the computer boundaries
    print("""As I am a computer, \
I will create N "random" points""")
    N=int(ask('N=', 1000))

    #creating the list of points
    listz=createRandomFromSegment(z0, z1, N)

    #plot function
    myPlot(f, listz)




class Segment(Frame):
    def __init__(self, boss=None, **arg):
        #class __init__
        Frame.__init__(self, boss, **arg)
        #name the window:
        boss.title("Images of discs by a complex function")
        
        #plot variables
        self.z0=None
        self.z1=None
        self.N=None
        self.f=None
        
        ##graph objects
        Label(self, text='{ z: z = z0 + (z1 - z0) * a;   0 < a < 1 }', \
              font=('Times', -30, 'bold'), fg='red').pack()
        #z0
        Label(self, text='Starting point of the segment (z0)', \
              font=('Times', -20, 'bold')).pack()
        self.z0Input=Entry(self, width=25)
        self.z0Input.pack(anchor='w')
        self.z0Input.insert(0, '1+2j')
        Label(self, text='(use j for imaginary part)').pack(anchor='w')
        #z1
        Label(self, text='Ending point of the segment (z1)', \
              font=('Times', -20, 'bold')).pack()
        self.z1Input=Entry(self, width=25)
        self.z1Input.pack(anchor='w')
        self.z1Input.insert(0, '1-1j')
        Label(self, text='(use j for imaginary part)').pack(anchor='w')
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
            listz=createRandomFromSegment(self.z0, self.z1, self.N)
            #plot function
            myPlot(self.f, listz)

    def updateVals(self, event=None):
        #z0
        try:
            self.z0=complex(self.z0Input.get())
        except:
            self.info.config(text="Invalid z0", fg='red')
        else:
            #z1
            try:
                self.z1=complex(self.z1Input.get())
            except:
                self.info.config(text="Invalid z1", fg='red')
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
    Segment(root).pack(anchor='w', padx=5, pady=5)
    root.mainloop()
    
