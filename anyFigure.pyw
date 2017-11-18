from calcFunctions import *
from plot import *

from sector import *
from segment import *
from disc import *
from circle import *
from shape import *
from path import *



def anyFigure():
    #we ask for the function
    #with this technic, the user can put anything :D
    print("Please type in the (complex) function that you want to plot:")
    func=ask('f(z)=', 'pow(z-1, 3)+10')
    f=lambda z: eval(func)

    #we ask for the plotting figure
    print("\nWhat would you like to plot?\n\
    0)Quit :{\n\
    1)A sector of the complex plane :)\n\
    2)A segment in the complex plane :}\n\
    3)A disc in the complex plane :o\n\
    4)A circle in the complex plane :D\n\
    5)A more complex shape :$")
    choice=input('>>> ')
    if choice=='':
        choice=4
        print("Default choice: 4) circle\n")
    else:
        choice=int(choice)%7
        print("")

    #execute the right plotting function
    if choice==0:
        pass
    elif choice==1:
        sector(f)
    elif choice==2:
        segment(f)
    elif choice==3:
        disc(f)
    elif choice==4:
        circle(f)
    elif choice==5:
        shape(f)
    elif choice==6:
        path(f)



class AnyFigure(Frame):
    #init method
    def __init__(self, boss=None, **arg):
        #class __init__
        Frame.__init__(self, boss, **arg)
        #name the window:
        boss.title("Images of figures by a complex function")

        #ABOUT ME ;)
        Button(self, text='About Me...', bg='black', fg='white', \
               command=self.about).pack(pady=0, side=TOP)
        #Title label
        Label(self, text="Select a figure to plot :", \
              fg='red', font=('Times', -20, 'bold')).pack(pady=10)
        #website link (explanation of the shape)
        Button(self, text='Shapes explanations', bg='grey',\
               command=lambda e=None: webbrowser.open_new("shapes.html"), \
               width=15).pack(pady=10)

        
        #circle
        Button(self, text='Circle', bg='green', \
               command=self.circle, width=20).pack(pady=5)
        #disc
        Button(self, text='Disc', bg='blue', \
               command=self.disc, width=20).pack(pady=5)
        #segment
        Button(self, text='Segment', bg='purple', \
               command=self.segment, width=20).pack(pady=5)
        #sector
        Button(self, text='Sector', bg='orange', \
               command=self.sector, width=20).pack(pady=5)
        #more complicated shape
        Button(self, text='Other Shape', bg='yellow', \
               command=self.shape, width=20).pack(pady=5)
        #more complicated shape
        Button(self, text='Other Path', bg='white', \
               command=self.path, width=20).pack(pady=5)

        
        #quit
        Button(self, text='Quit', bg='red', \
               command=boss.destroy, width=5).pack(pady=20)

    #about me method
    def about(self):
        webbrowser.open("https://pauldubois98.github.io/prgm.html")
    #circle method
    def circle(self):
        root=Tk()
        Circle(root).pack(anchor='w', padx=5, pady=5)
    #disc method
    def disc(self):
        root=Tk()
        Disc(root).pack(anchor='w', padx=5, pady=5)
    #segment method
    def segment(self):
        root=Tk()
        Segment(root).pack(anchor='w', padx=5, pady=5)
    #sector method
    def sector(self):
        root=Tk()
        Sector(root).pack(anchor='w', padx=5, pady=5)
    #complicated shape method
    def shape(self):
        root=Tk()
        Shape(root).pack(anchor='w', padx=5, pady=5)
    #complicated path method
    def path(self):
        root=Tk()
        Path(root).pack(anchor='w', padx=5, pady=5)
    






if __name__=='__main__':
    root=Tk()
    AnyFigure(root).pack(padx=5, pady=0)
    root.mainloop()
