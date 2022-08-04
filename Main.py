#small:
#medium:
#big:99 20x20
import os
from random import randint
from copy import copy,deepcopy
from guizero import App,Waffle,CheckBox
from time import sleep,time
app=App()
c=[(0,0,255),(0,255,0),(255,0,0),(102,0,102),(153,76,0),(0,255,255),(0,0,0),(100,100,100),(150,150,150),(255,255,0),(255,255,255)]
y=15
m=49
gg=False
first=True
f=False
start=time()
x=[['('+str(i).rjust(2,'0')+')' for i in range(y+1)]]

def px(x):
    print('')
    for i in range(len(x)):
        print(x[i])

x.extend([['[??]' for ii in range(y+1)] for i in range(y)])
for i in range(1,len(x)):
    x[i][0]='('+str(i).rjust(2,'0')+')'
xo=list(x)
px(x)
x2=deepcopy(x)
def ff():
    global f
    if f:
        f=False
    else:
        f=True

def colour(x3):
    for b in range(1,y+1):
        for a in range(y,0,-1):
            if not(x3[a][b]=='[FF]' or x3[a][b]=='[??]' or x3[a][b]=='[  ]' or x3[a][b]=='[XX]'):
                grid.pixel(b-1,a-1).color=c[int(x3[a][b][1:3])-1]
            elif x3[a][b]=='[  ]':
                grid.pixel(b-1,a-1).color=c[8]
            elif x3[a][b]=='[FF]':
                grid.pixel(b-1,a-1).color=c[9]
            elif x3[a][b]=='[XX]' or x3[a][b]=='[??]':
                grid.pixel(b-1,a-1).color=c[10]

def fin():
    global x2,y,m
    i=0
    for a in x2:
        for b in a:
            if (b[2].isdigit() and b[0]=='[') or b=='[  ]':
                i+=1
    if (y**2)-m==i:
        return True

def press(a,b):
    global gg
    global first
    global x2
    global f
    global start
    if first or gg:
        first=False
    else:
        print(a,b)
        a+=1
        b+=1
        if x2[b][a]=='[??]' or x2[b][a]=='[FF]': 
            if f:
                if x2[b][a]=='[FF]':
                    x2[b][a]='[??]'
                else:
                    x2[b][a]='[FF]'
                colour(x2)
            else:
                if x[b][a]=='[XX]':
                    print('XXXXX')
                    px(x)
                    gg=True
                    colour(x)
                    app.error('Error','Task_Manager_Failed_error_code_0555643210000')
                elif x[b][a]=='[  ]':
                    se(b,a)
                    colour(x2)
                    if fin():
                        app.info('Success','You survived the mines, have a gold star'+str((time()-start))+'s')
                        gg=True
                else:
                    x2[b][a]=x[b][a]
                    colour(x2)
                    if fin():
                        app.info('Success','You survived the mines, have a gold star, completed in '+str((time()-start))+'s')
                        gg=True
        px(x2)
        

grid=Waffle(app,height=y,width=y,command=press)
flag=CheckBox(app,text='Flag?',command=ff)
for i in range(m):
    a=randint(1,y)
    b=randint(1,y)
    while x[a][b] =='[XX]' or (a in range((y//2)-2,(y//2)+3) and b in range((y//2)-2,(y//2)+3)):
        a=randint(1,y)
        b=randint(1,y)
    x[a][b]='[XX]'
px(x)
for a in range(1,y+1):
    for b in range(1,y+1):
        n=0
        if x[a][b]!='[XX]': 
            for i in range(a-1,a+2):
                for ii in range(b-1,b+2):
                    if i<=y and ii<=y:
                        if x[i][ii]=='[XX]':
                            n+=1
            x[a][b]='['+str(n).rjust(2,' ')+']'
            if x[a][b]=='[ 0]':
                x[a][b]='[  ]'

for a in range(1,y+1):
    for b in range(1,y+1):
        if x[a][b]=='[  ]':
            for i in range(a-1,a+2):
                for ii in range(b-1,b+2):
                    if i<=y and ii<=y:
                        if x[i][ii]=='[  ]':
                            if i==a-1 and ii==b-1:
                                continue

px(x)

def se(a,b):
    global x,x2 
    for i in range(a-1,a+2):
        for ii in range(b-1,b+2):
            if i<=y and ii<=y:
                if x[i][ii]=='[  ]' and x2[i][ii]=='[??]':
                    x2[i][ii]=x[i][ii]
                    se(i,ii)
                elif x2[i][ii]=='[??]':
                    x2[i][ii]=x[i][ii]
x2[y//2][y//2]='[  ]'
se(y//2,y//2)
px(x2)
colour(x2)

