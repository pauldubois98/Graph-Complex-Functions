from cmath import *
from random import uniform, random


def createRandomFromSector(a1, a2, R, N, z0=0):
    return [z0+rect(uniform(0, R), uniform(a1, a2)) for i in range(N)]

def createRandomFromDisc(z0, R, N):
    return [z0+rect(uniform(0, R), uniform(-pi, pi)) for i in range(N)]

def createRandomFromSegment(z0, z1, N):
    return [z0+(random()*(z1-z0)) for i in range(N)]

def createRandomFromCircle(z0, R, N):
    return [z0+rect(R, uniform(-pi, pi)) for i in range(N)]

def apply(function, listNumbers):
    return [function(z) for z in listNumbers]

def ask(txt, default):
    a=input(txt)
    if a=='':
        a=default
        print('> '+txt+str(default))
    return a

def takeRe(listNumbers):
    return [z.real for z in listNumbers]

def takeIm(listNumbers):
    return [z.imag for z in listNumbers]

def cprint(z, length=5):
    return str(z.real)[:length]+'+'+str(z.imag)[:length]+'i'

def lprint(z, fz):
    for i in range(len(z)):
        print('f(' + cprint(z[i]) + ')=' + cprint(fz[i]))
