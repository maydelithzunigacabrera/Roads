from tkinter import *
import tkinter as tk
import time
import random
class Circulo:
    def __init__(self,canvas,x,y,d,vX,vY,color):
        self.canvas=canvas
        self.image=canvas.create_oval(x,y,x+d,y+d,fill=color)
        self.vX=vX
        self.vY=vY
        self.x=x
        self.y=y
    def movimiento(self):
        coord=self.canvas.coords(self.image)
        if(coord[2]>=(self.canvas.winfo_width()-10)or coord[0]-10<0):
            self.vX=-self.vX
        if(coord[3]>=(self.canvas.winfo_height()-10)or coord[1]-10<0):
            self.vY=-self.vY
        self.canvas.move(self.image,self.vX,self.vY)
    def retX(self):
        self.x
        return self.x
    def retY(self):
        self.y
        return self.y
class Graf:

    def __init__(_graf, graf):
        _graf.graf = graf
        _graf. Col = len(graf)

    def algoritmo_busqueda(_graf, s, t, nodo_padre):

        nodos_NoRecorridos = [False] * (_graf.Col)
        cola = []
        cola.append(s)
        nodos_NoRecorridos[s] = True
        while cola:
            u = cola.pop(0)
            for i, v in enumerate(_graf.graf[u]):
                if nodos_NoRecorridos[i] == False and v > 0:
                    cola.append(i)
                    nodos_NoRecorridos[i] = True
                    nodo_padre[i] = u
        return True if nodos_NoRecorridos[t] else False

    def ffulker(_graf, fuente, destino):
        nodo_padre = [-1] * (_graf.Col)
        flujo_max = 0
        while _graf.algoritmo_busqueda(fuente, destino, nodo_padre):
            camino = float("Inf")
            d = destino
            while(d != fuente):
                camino = min(camino, _graf.graf[nodo_padre[d]][d])
                d = nodo_padre[d]

            flujo_max += camino
            v = destino
            while(v != fuente):
                u = nodo_padre[v]
                _graf.graf[u][v] -= camino
                _graf.graf[v][u] += camino
                v = nodo_padre[v]

        return flujo_max
Bucle=True
Letras=list(map(chr, range(65, 80)))
while Bucle:
    
    window=Tk()
    W=1000
    H=700
    window.wm_attributes('-transparentcolor', '#ab23ff')
    canvas=Canvas(window,width=W,height=H)
    canvas.pack()
    ListaC=list()
    v=0
    Sf=""
    Sd=""
    f=16
    d=16
    respuesta=0
    print('1: Matriz al azar','2: Matriz hecha por el usuario','3: Cerrar',)
    q=input('Ingrese su opción:')
    try:
        q=int(q)
        if(q>3 or q<1):
            print('Fuera de rango')
    except:
        print('Opcion incorrecta')
    n=0
    if(q==1):     
        try:
            n=int(input("ingrese tamaño de matriz: "))
            if n%2==0:
               if not n%3==0:
                  v=int(n/3-0.33)
               else:
                   v=int(n/2)
            if n%2==0 and n%3==0:
                v=int(n/4)   
            else:
                v=int(n/3)
            for i in range(n):
                if n<16:
                    if i==0:
                       ListaC.append(Circulo(canvas,10,350,50,0,0,"green"))
                       tk.Label(window,text=Letras[i],bg="green",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                    if not i==0 and not i==n-1:
                      if n==5:  
                         if i%2==1:
                             ListaC.append(Circulo(canvas,300+(100*i),250,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         else:
                             ListaC.append(Circulo(canvas,400+(50*i),450,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==6:
                         if i<=int(n/2)-1:
                             ListaC.append(Circulo(canvas,100+(250*i),250,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>int(n/2)-1:
                             ListaC.append(Circulo(canvas,(250*i)-400,450,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==7:
                         if i%2==0:
                             ListaC.append(Circulo(canvas,200+(100*i),450,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i%2==1:
                             ListaC.append(Circulo(canvas,200+(100*i),250,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==8:
                         if i%2==0:
                             ListaC.append(Circulo(canvas,50+(100*i),250,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i%2==1:
                             ListaC.append(Circulo(canvas,150+(100*i),450,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==9:
                          if i<=v:
                             ListaC.append(Circulo(canvas,(300*i)-150,150,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                          if i>v and i<=v*2:
                             ListaC.append(Circulo(canvas,(300*i)-1050,350,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                          if i>v*2:
                             ListaC.append(Circulo(canvas,(100*i)-250,550,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n>=10 and n<=14:
                         if i<=v:
                             if n<13:
                                ListaC.append(Circulo(canvas,50+(200*i),100,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             else:
                                ListaC.append(Circulo(canvas,(200*i),100,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>v and i<=v*2:
                             if n<13:
                                ListaC.append(Circulo(canvas,(200*i)-550,350,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             else:
                                ListaC.append(Circulo(canvas,(200*i)-v*200,350,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>v*2:
                             if n==10:
                                ListaC.append(Circulo(canvas,(200*i)-1050,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             if n==11:
                                ListaC.append(Circulo(canvas,(200*i)-1150,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             if n==12:
                                ListaC.append(Circulo(canvas,(200*i)-1200,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             if n==13:
                                ListaC.append(Circulo(canvas,(200*i)-1500,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             if n==14:
                                ListaC.append(Circulo(canvas,(200*i)-1600,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==15:
                         if i<=v:                   
                             ListaC.append(Circulo(canvas,(170*i)-25,100,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>v and i<=v*2:
                             ListaC.append(Circulo(canvas,(170*i)-875,350,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>v*2:
                             ListaC.append(Circulo(canvas,(170*i)-1550,550,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                    if i==n-1:
                        ListaC.append(Circulo(canvas,W-50,350,50,0,0,"red"))
                        tk.Label(window,text=Letras[i],bg="red",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
            if(n>=5 and n<=15):
                while(respuesta<1 or respuesta>2):
                    respuesta=int(input("¿Desea ingresar nodos especificos? 1: Si  2: No "))
                if(respuesta==1):
                    try:              
                        print("Nodos para escoger", end=' ')
                        for x in range(n):
                            print(Letras[x],end=' ')
                        print("")
                        while (f<0 or d<0 or f>=n or d>=n) and (d==f) :
                            Sf=input("ingrese su nodo escogido para la fuente: ").upper()
                            Sd=input("ingrese su nodo escogido para el destino: ").upper()
                            try:
                                f=Letras.index(Sf)
                                d=Letras.index(Sd)
                                if(f==d):
                                    print("Nodos iguales no permitidos. Reintente")
                                    Sf=""
                                    Sd=""
                                    f=-16
                                    d=-16
                                if(f>=n or d>=n):
                                    print("Nodo fuera de rango")
                                    f=-16
                                    d=-16
                            except:
                                print("Valores no permitidos. Reintente")
                                f=-16
                                d=-16
                            if(Sf==Sd):
                                print("No puede escoger los mismos nodos, reingrese")
                                Sf=""
                        
                    except:
                        f=0
                        d=n-1
                if(respuesta==2):
                    f=0
                    d=n-1               
                graf=list()
                fuente = f
                destino = d
                i=n/2
                i1=n/2
                if(n%2==1):
                    i=int(n/2-0.6)+1
                    i1=int(n/2+0.6)-1
                else:
                    i=int(i)
                    i1=int(i1)-1
                for x in range(n-1):
                    a=list()
                    graf.append(a)    
                    if x==0:
                            a.append(0)         
                            for w in range(i):
                                a.append(random.randint(1,10))
                            for w in range(i1):
                                a.append(0)
                    else:
                        a.append(0)
                        for y in range(n-1):
                            if not (y+1==x):
                                a.append(random.randint(0,10))
                            else:
                                a.append(0)
                l=list()
                for x in range(n):
                    l.append(0)
                
                graf.append(l)
                g = Graf(graf)
                for x in range(n):                  
                    print("   "+Letras[x],end='')
                nl=0
                for x in graf:
                    print("")
                    print(Letras[nl],end='  ')
                    for y in x:
                        print(y,end='   ')
                    nl+=1
                print("")
                for i in range(len(graf)):
                    for j in range(len(graf)):
                        if graf[i][j]>0:
                           if i<=j:
                              if graf[i][j]!=graf[j][i]:
                                 canvas.create_line(ListaC[i].retX()+50, ListaC[i].retY()+25, ListaC[j].retX(), ListaC[j].retY()+25,fill='orange',arrow=tk.LAST,arrowshape=(14,20,10),width=6)
                                 tk.Label(window,text=graf[i][j],font=("Helvetica", 12,"bold")).place(x=int((ListaC[i].retX()+ListaC[j].retX())/2)+25,y=int((ListaC[i].retY()+ListaC[j].retY())/2))
                              else:
                                 canvas.create_line(ListaC[i].retX(), ListaC[i].retY()+25, ListaC[j].retX()+50, ListaC[j].retY()+25,fill='orange',arrow=tk.LAST,arrowshape=(14,20,10),width=6)
                                 tk.Label(window,text=graf[i][j],font=("Helvetica", 12,"bold")).place(x=int((ListaC[i].retX()+ListaC[j].retX())/2),y=int((ListaC[i].retY()+ListaC[j].retY())/2))
                           if i>j:
                              if graf[i][j]!=graf[j][i]:
                                 canvas.create_line(ListaC[i].retX(), ListaC[i].retY()+25, ListaC[j].retX()+50, ListaC[j].retY()+25,fill='orange',arrow=tk.LAST,arrowshape=(14,20,10),width=6)
                                 tk.Label(window,text=graf[i][j],font=("Helvetica", 12,"bold")).place(x=int((ListaC[i].retX()+ListaC[j].retX())/2)-15,y=int((ListaC[i].retY()+ListaC[j].retY())/2)+20)
                              else:
                                 canvas.create_line(ListaC[i].retX()+50, ListaC[i].retY()+25, ListaC[j].retX(), ListaC[j].retY()+25,fill='orange',arrow=tk.LAST,arrowshape=(14,20,10),width=6)  
                a=g.ffulker(fuente,destino)
                tk.Label(window,text=("El flujo máximo es: "+str(a)),font=("Helvetica", 12,"bold")).place(x=10,y=5)
            else: 
                print("Valor muy pequeño escoja entre 5 a 15")
        except:
            print("No es un numero")
    if(q==2):
        try:
            n=int(input("ingrese tamaño de matriz: "))
            if n%2==0:
               if not n%3==0:
                  v=int(n/3-0.33)
               else:
                   v=int(n/2)
            if n%2==0 and n%3==0:
                v=int(n/4)   
            else:
                v=int(n/3)
            for i in range(n):
                if n<16:
                    if i==0:
                       ListaC.append(Circulo(canvas,10,350,50,0,0,"green"))
                       tk.Label(window,text=Letras[i],bg="green",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                    if not i==0 and not i==n-1:
                      if n==5:  
                         if i%2==1:
                             ListaC.append(Circulo(canvas,300+(100*i),250,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         else:
                             ListaC.append(Circulo(canvas,400+(50*i),450,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==6:
                         if i<=int(n/2)-1:
                             ListaC.append(Circulo(canvas,100+(250*i),250,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>int(n/2)-1:
                             ListaC.append(Circulo(canvas,(250*i)-400,450,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==7:
                         if i%2==0:
                             ListaC.append(Circulo(canvas,200+(100*i),450,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i%2==1:
                             ListaC.append(Circulo(canvas,200+(100*i),250,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==8:
                         if i%2==0:
                             ListaC.append(Circulo(canvas,50+(100*i),250,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i%2==1:
                             ListaC.append(Circulo(canvas,150+(100*i),450,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==9:
                          if i<=v:
                             ListaC.append(Circulo(canvas,(300*i)-150,150,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                          if i>v and i<=v*2:
                             ListaC.append(Circulo(canvas,(300*i)-1050,350,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                          if i>v*2:
                             ListaC.append(Circulo(canvas,(100*i)-250,550,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n>=10 and n<=14:
                         if i<=v:
                             if n<13:
                                ListaC.append(Circulo(canvas,50+(200*i),100,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             else:
                                ListaC.append(Circulo(canvas,(200*i),100,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>v and i<=v*2:
                             if n<13:
                                ListaC.append(Circulo(canvas,(200*i)-550,350,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             else:
                                ListaC.append(Circulo(canvas,(200*i)-v*200,350,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>v*2:
                             if n==10:
                                ListaC.append(Circulo(canvas,(200*i)-1050,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             if n==11:
                                ListaC.append(Circulo(canvas,(200*i)-1150,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             if n==12:
                                ListaC.append(Circulo(canvas,(200*i)-1200,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             if n==13:
                                ListaC.append(Circulo(canvas,(200*i)-1500,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                             if n==14:
                                ListaC.append(Circulo(canvas,(200*i)-1600,550,50,0,0,"blue"))
                                tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                      if n==15:
                         if i<=v:                   
                             ListaC.append(Circulo(canvas,(170*i)-25,100,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>v and i<=v*2:
                             ListaC.append(Circulo(canvas,(170*i)-875,350,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                         if i>v*2:
                             ListaC.append(Circulo(canvas,(170*i)-1550,550,50,0,0,"blue"))
                             tk.Label(window,text=Letras[i],bg="blue",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
                    if i==n-1:
                        ListaC.append(Circulo(canvas,W-50,350,50,0,0,"red"))
                        tk.Label(window,text=Letras[i],bg="red",font=("Helvetica", 12,"bold")).place(x=int(ListaC[i].retX()+17),y=int(ListaC[i].retY()+13))
            if(n>=5 and n<=15):
                while(respuesta<1 or respuesta>2):
                    respuesta=int(input("¿Desea ingresar nodos especificos? 1: Si  2: No"))
                if(respuesta==1):
                    try:              
                        print("Nodos para escoger", end=' ')
                        for x in range(n):
                            print(Letras[x],end=' ')
                        print("")
                        while (f<0 or d<0 or f>=n or d>=n) and (d==f):
                            Sf=input("ingrese su nodo escogido para la fuente: ").upper()
                            Sd=input("ingrese su nodo escogido para el destino: ").upper()
                            try:
                                f=Letras.index(Sf)
                                d=Letras.index(Sd)
                                if(f==d):
                                    print("Nodos iguales no permitidos. Reintente")
                                    Sf=""
                                    Sd=""
                                    f=-16
                                    d=-16
                                if(f>=n or d>=n):
                                    print("Nodo fuera de rango")
                                    f=-16
                                    d=-16
                            except:
                                print("Valores no permitidos. Reintente")
                                f=-16
                                d=-16
                            if(Sf==Sd):
                                print("No puede escoger los mismos nodos, reingrese")
                                Sf=""                                                    
                    except:
                        f=0
                        d=n-1
                if(respuesta==2):
                    f=0
                    d=n-1
                graf=list()
                fuente = f
                destino = d
                i=n/2
                i1=n/2
                if(n%2==1):
                    i=int(n/2-0.6)+1
                    i1=int(n/2+0.6)-1
                else:
                    i=int(i)
                    i1=int(i1)-1
                for x in range(n-1):
                    a=list()
                    a.append(0)  
                    for y in range(n):                                                                                                   
                        try:
                            if not (x==y or y==0):
                                m=int(input('Ingrese capacidad desde '+ Letras[x]+ ' hasta '+Letras[y]+' si no desea una conexion ingrese 0: '))
                                a.append(m)
                            if x==y and x>0:
                                a.append(0)
                        except:
                            print('No es un numero')
                    graf.append(a)
                l=list()
                for x in range(n):
                    l.append(0)               
                graf.append(l)
                g = Graf(graf)                    
                for x in range(n):                  
                    print("   "+Letras[x],end='')
                nl=0
                for x in graf:
                    print("")
                    print(Letras[nl],end='  ')
                    for y in x:
                        print(y,end='   ')
                    nl+=1
                print("")
                for i in range(len(graf)):
                    for j in range(len(graf)):
                        if graf[i][j]>0:
                           if i<=j:
                              if graf[i][j]!=graf[j][i]:
                                 canvas.create_line(ListaC[i].retX()+50, ListaC[i].retY()+25, ListaC[j].retX(), ListaC[j].retY()+25,fill='orange',arrow=tk.LAST,arrowshape=(14,20,10),width=6)
                                 tk.Label(window,text=graf[i][j],font=("Helvetica", 12,"bold")).place(x=int((ListaC[i].retX()+ListaC[j].retX())/2)+25,y=int((ListaC[i].retY()+ListaC[j].retY())/2))
                              else:
                                 canvas.create_line(ListaC[i].retX(), ListaC[i].retY()+25, ListaC[j].retX()+50, ListaC[j].retY()+25,fill='orange',arrow=tk.LAST,arrowshape=(14,20,10),width=6)
                                 tk.Label(window,text=graf[i][j],font=("Helvetica", 12,"bold")).place(x=int((ListaC[i].retX()+ListaC[j].retX())/2),y=int((ListaC[i].retY()+ListaC[j].retY())/2))
                           if i>j:
                              if graf[i][j]!=graf[j][i]:
                                 canvas.create_line(ListaC[i].retX(), ListaC[i].retY()+25, ListaC[j].retX()+50, ListaC[j].retY()+25,fill='orange',arrow=tk.LAST,arrowshape=(14,20,10),width=6)
                                 tk.Label(window,text=graf[i][j],font=("Helvetica", 12,"bold")).place(x=int((ListaC[i].retX()+ListaC[j].retX())/2)-15,y=int((ListaC[i].retY()+ListaC[j].retY())/2)+20)
                              else:
                                 canvas.create_line(ListaC[i].retX()+50, ListaC[i].retY()+25, ListaC[j].retX(), ListaC[j].retY()+25,fill='orange',arrow=tk.LAST,arrowshape=(14,20,10),width=6)  
                a=g.ffulker(fuente,destino)
                tk.Label(window,text=("El flujo máximo es: "+str(a)),font=("Helvetica", 12,"bold")).place(x=10,y=5)              
            else:
                print("Valor debe ser entre 5 y 15")
        except:
            print("No es un numero")
    if(q==3):
        Bucle=False
    if n%2==0:
       if not n%3==0:
          v=int(n/3-0.33)
       else:
           v=int(n/2)
    if n%2==0 and n%3==0:
        v=int(n/4)   
    else:
        v=int(n/3)
    window.update()
    l=list()
    input("continuar")
    window.destroy()
    window.update()
window.mainloop()

            
    
    


