from tkinter import *
from math import *
from time import *

root=Tk()
root.title("Зачетная работа")
root.geometry("1280x1024")
canv=Canvas(width=1280,height=1024,bg="white")
canv.pack()
x=0
pogdan=1.5
s=0
p=0
y=0
l=150
h=100
l2=125
h2=75
wis2=15
wis=15
stroka1="1.5_"
stroka2="_"
znachprog11=0
znachprog12=0
znachprog1=0
znachprog2=0
znachprog3=0
znachprog4=0
def autopog(e):
    global znachprog1,znachprog2,znachprog3,znachprog4
    m[0][0]=str(8)
    m[1][0]=str(8)
    m[2][0]=str(8)
    m[3][0]=str(8)
    m[0][1]=str(0.22)
    m[0][2]=str(0.15)
    m[0][3]=str(0.25)
    m[1][1]=str(0.21)
    m[1][2]=str(0.23)
    m[1][3]=str(0.24)
    m[2][1]=str(0.17)
    m[2][2]=str(0.22)
    m[2][3]=str(0.13)
    m[3][1]=str(0.15)
    m[3][2]=str(0.20)
    m[3][3]=str(0.22)
    canv.coords(kurT2,330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260)
    cell4=sreda(m,[[0,1],[0,2],[0,3]])
    oda5=sreda(m,[[1,1],[1,2],[1,3]])
    oda2=sreda(m,[[2,1],[2,2],[2,3]])
    oda3=sreda(m,[[3,1],[3,2],[3,3]])
    okrulnow(str(cell4))
                    

    m[0][4]=round(cell4,znak)
    if m[0][4]==0:
       m[0][4]=""
    okrulnow(str(oda5))
    m[1][4]=round(oda5,znak)
    if m[1][4]==0:
       m[1][4]=""
    okrulnow(str(oda2))
    m[2][4]=round(oda2,znak)
    if m[2][4]==0:
       m[2][4]=""
    okrulnow(str(oda3))
    m[3][4]=round(oda3,znak)
    if m[3][4]==0:
       m[3][4]=""
    if m[0][0] and cell4:
          tyt5=round(float(m[0][0])/cell4,2)
          m[0][5]=tyt5
          vivod(m)
    if m[1][0] and oda5:
          tyta5=round(float(m[1][0])/oda5,2)
          m[1][5]=tyta5
          vivod(m)
    if m[2][0] and oda2:
          tytaa5=round(float(m[2][0])/oda2,2)
          m[2][5]=tytaa5
          vivod(m)
    if m[3][0] and oda3:
          tytaaa5=round(float(m[3][0])/oda3,2)
          m[3][5]=tytaaa5
          vivod(m)
    vivod(m)
    if cell4!=0 and m[0][0]:
      canv.create_rectangle(1030,300,1070,318,fill="white",outline="white")
      oznachprog1=pogdan/float(m[0][0])
      znachprog1=round(tyt5*oznachprog1,2)
      okrulnow(str(znachprog1))
      znachprog1=round(znachprog1,znak)
      canv.create_text(1030,300,font='Arial 15',anchor='nw',text=znachprog1)
      canv.create_text(1017,300,font='Arial 15',anchor='nw',text="±")
      
      m[0][5]=round(tyt5,znak) 
      vivod(m)
      
    if oda5!=0 and m[1][0]:
      canv.create_rectangle(1030,375,1070,393,fill="white",outline="white")
      oznachprog2=pogdan/float(m[1][0])
      znachprog2=round(tyta5*oznachprog2,2)
      okrulnow(str(znachprog2))
      znachprog2=round(znachprog2,znak)
      canv.create_text(1030,375,font='Arial 15',anchor='nw',text=znachprog2)
      canv.create_text(1017,375,font='Arial 15',anchor='nw',text="±")
      m[1][5]=round(tyta5,znak) 
      vivod(m)
    if oda2!=0 and m[2][0]:
       canv.create_rectangle(1030,450,1070,468,fill="white",outline="white")
       oznachprog3=pogdan/float(m[2][0])
       znachprog3=round(tytaa5*oznachprog3,2)
       okrulnow(str(znachprog3))
       znachprog3=round(znachprog3,znak)
       canv.create_text(1030,450,font='Arial 15',anchor='nw',text=znachprog3)
       canv.create_text(1017,450,font='Arial 15',anchor='nw',text="±")
       m[2][5]=round(tytaa5,znak) 
       vivod(m)
    if oda3!=0 and m[3][0]:
       canv.create_rectangle(1030,525,1070,543,fill="white",outline="white")
       oznachprog4=pogdan/float(m[3][0])
       znachprog4=round(tytaaa5*oznachprog4,2)
       
       okrulnow(str(znachprog4))
       znachprog4=round(znachprog4,znak)
       canv.create_text(1030,525,font='Arial 15',anchor='nw',text=znachprog4)
       canv.create_text(1017,525,font='Arial 15',anchor='nw',text="±")
       m[3][5]=round(tytaaa5,znak) 
       vivod(m)
def f23(e):
            global x,k,a,y,wis,io,znachprog11,znachprog12,cell,oda,tyt,tyta
##    print(float(m[y][x]+e.char))
            vivod23(io)
            if (e.keysym.isdigit() or (e.char=="." and io[y][x].count(".")==0)) and len(io[y][x])<4:
                if float(io[y][x]+e.char)<100 and x>0:
    
                  io[y][x]+=e.char
                elif x==0 and float(io[y][x]+e.char)<1000:
                  io[y][x]+=e.char
        
        
                vivod23(io)
                canv.coords(k,240+x*l+(len(io[y][x])*wis),y*h+50+320,240+x*l+30+(len(io[y][x])*wis),y*h+50+320)
        #prosuma(m,[[0,1],[0,2],[0,3]])
                cell=sreda(io,[[0,1],[0,2],[0,3]])
                oda=sreda(io,[[1,1],[1,2],[1,3]])
                okrulnow(str(cell))
                io[0][4]=round(cell,znak)
                if io[0][4]==0:
                   io[0][4]=""
                okrulnow(str(oda))
                io[1][4]=round(oda,znak)
                if io[1][4]==0:
                   io[1][4]=""
                if io[0][0] and cell:
                      tyt=round(float(io[0][0])/cell,2)
                      io[0][5]=tyt
                if io[1][0] and oda:
                      tyta=round(float(io[1][0])/oda,2)
                      io[1][5]=tyta
        
       
        
               
        
           
##        tyt=cell/ad
##        tyta=oda/ada
##        m[0][4]=tyt
##        m[1][4]=tyta
                vivod23(io)
                if cell!=0 and io[0][0]:
                       canv.create_rectangle(1040,375,1090,393,fill="white",outline="white")
                       
                       oznachprog11=pogdan/float(io[0][0])
                       
                       znachprog11=round(tyt*oznachprog11,2)
                       okrulnow(str(znachprog11))
                       znachprog11=round(znachprog11,znak)
                       canv.create_text(1040,375,font='Arial 15',anchor='nw',text=znachprog11)
                       canv.create_text(1030,375,font='Arial 15',anchor='nw',text="±")
                       
                       io[0][5]=round(tyt,znak)
                       vivod23(io)
                if oda!=0 and io[1][0]:
                    canv.create_rectangle(1040,475,1090,493,fill="white",outline="white")
                    oznachprog12=pogdan/float(io[1][0])
                    znachprog12=round(tyta*oznachprog12,2)
                    okrulnow(str(znachprog12))
                    znachprog12=round(znachprog12,znak)
                    canv.create_text(1040,475,font='Arial 15',anchor='nw',text=znachprog12)
                    canv.create_text(1030,475,font='Arial 15',anchor='nw',text="±")
                    
                    io[1][5]=round(tyta,znak)
                    vivod23(io)
            if e.keysym=="Right":
                if x>=3:
                    x=-1
                x+=1
                canv.coords(k,240+x*l+len(io[y][x])*wis,y*h+50+320,240+x*l+30+len(io[y][x])*wis,y*h+50+320)
        
        

            if e.keysym=="Left":
                if x<=0:
                    x=4
                x-=1
                canv.coords(k,240+x*l+len(io[y][x])*wis,y*h+50+320,240+x*l+30+len(io[y][x])*wis,y*h+50+320)

            if e.keysym=="Up":
                if y<=1:
                    y=1
                y-=1
                canv.coords(k,240+x*l+len(io[y][x])*wis,y*h+50+320,240+x*l+30+len(io[y][x])*wis,y*h+50+320)

            if e.keysym=="Down":
                if y>=1:
                    y=-1
                y+=1
                canv.coords(k,240+x*l+len(io[y][x])*wis,y*h+50+320,240+x*l+30+len(io[y][x])*wis,y*h+50+320)
            if e.keysym=="BackSpace":
                   io[y][x]=io[y][x][:-1]
                   vivod23(io)

                   canv.coords(k,240+x*l+len(io[y][x])*wis,y*h+50+320,240+x*l+30+len(io[y][x])*wis,y*h+50+320)
                   cell=sreda(io,[[0,1],[0,2],[0,3]])
                   oda=sreda(io,[[1,1],[1,2],[1,3]])
                   okrulnow(str(cell))
                   io[0][4]=round(cell,znak)
                   if io[0][4]==0:
                      io[0][4]=""
                   okrulnow(str(oda))
                   io[1][4]=round(oda,znak)
                   if io[1][4]==0:
                      io[1][4]=""
                   if io[0][0] and cell:
                         tyt=round(float(io[0][0])/cell,2)
                         io[0][5]=tyt
                   if io[1][0] and oda:
                         tyta=round(float(io[1][0])/oda,2)
                         io[1][5]=tyta
                   vivod23(io)
                   if cell!=0 and io[0][0]:
                       canv.create_rectangle(1040,375,1090,393,fill="white",outline="white")
                       
                       oznachprog11=pogdan/float(io[0][0])
                       
                       znachprog11=round(tyt*oznachprog11,2)
                       okrulnow(str(znachprog11))
                       znachprog11=round(znachprog11,znak)
                       canv.create_text(1040,375,font='Arial 15',anchor='nw',text=znachprog11)
                       canv.create_text(1030,375,font='Arial 15',anchor='nw',text="±")
                       
                       io[0][5]=round(tyt,znak)
                       vivod23(io)
                   if oda!=0 and io[1][0]:
                    canv.create_rectangle(1040,475,1090,493,fill="white",outline="white")
                    oznachprog12=pogdan/float(io[1][0])
                    znachprog12=round(tyta*oznachprog12,2)
                    okrulnow(str(znachprog12))
                    znachprog12=round(znachprog12,znak)
                    canv.create_text(1040,475,font='Arial 15',anchor='nw',text=znachprog12)
                    canv.create_text(1030,475,font='Arial 15',anchor='nw',text="±")
                    
                    io[1][5]=round(tyta,znak)
                    vivod23(io)

def vivod(m):
                 global t
                 for i in range(0,len(m)):
                    for j in range(0,len(m[i])):
                        canv.delete(t[i][j])

                        t[i][j]=canv.create_text(j*l2+330,40+260+i*h2,text=m[i][j],font="Arial 20",anchor="w")
def vivod23(m):
    global ik
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            canv.delete(ik[i][j])

            ik[i][j]=canv.create_text(j*l+240,40+320+i*h,text=m[i][j],font="Arial 20",anchor="w")
m=[""]*4
for g in range(0,len(m)):
              m[g]=[""]*6
t=[""]*4
for g in range(0,len(t)):
                t[g]=[""]*6
ik=[""]*2
for g in range(0,len(ik)):
    ik[g]=[""]*6
io=[""]*2
for g in range(0,len(io)):
    io[g]=[""]*6
def sreda(m, v):
                  s=0
                  q=0
                  for i in range(0,len(m)):
         
         
                    for j in range(1,len(m[i])):
                      if m[i][j] and [i,j] in v:
                        d=float(m[i][j])
                        s+=d
                        q+=1
                
                  if q:
                   k=s/q
                  else:
                    k=0      
                  return k
canv.create_text(640,300,text="Проектная работа по информатике",font="Verdana 20")
canv.create_text(640,360,text="ПРОВЕРКА ПОСТОЯНСТВА СКОРОСТИ ДВИЖЕНИЯ ТЕЛЕЖКИ ",font="Verdana 20")


canv.create_text(640,450,text="2022 год",font="Verdana 15")

canv.create_text(900,800,text="Для перехода нажмите ENTER",font="Verdana 15")
def f2(e):
 root.unbind("<Next>")
 root.unbind("<Prior>")
 root.unbind("<Return>")
 root.unbind("<KeyRelease>")
 root.unbind("<BackSpace>")
 root.unbind("<F3>")
 root.bind("<Button-1>",r)
 canv.delete("all")
 canv.create_rectangle(200,150,1080,230)
 canv.create_rectangle(200,280,1080,360)
 canv.create_rectangle(200,410,1080,490)
 canv.create_rectangle(200,540,1080,620)
 canv.create_rectangle(200,670,1080,750)
 canv.create_rectangle(200,790,1080,870)
 canv.create_text(600,120,text="МЕНЮ",font="Verdana 30")
 canv.create_text(600,190,text="Описание",font="Verdana 20")
 canv.create_text(600,320,text="Анимация",font="Verdana 20")
 canv.create_text(600,450,text="Погрешности",font="Verdana 20")
 canv.create_text(600,580,text="Таблица",font="Verdana 20")
 canv.create_text(600,700,text="Диаграмма",font="Verdana 20")
 canv.create_text(600,820,text="Помощь",font="Verdana 20")
 canv.create_text(260,20,text="Для того,чтобы перейти вo вкладку в меню",font="Verdana 15")
 canv.create_text(490,40,text="надо навести курсор на прямоугольник с нужным названием и нажать левой кнопкой мыши",font="Verdana 15")   
def f1(e):
 canv.delete("all")
 root.unbind("<Return>")
 root.bind("<Button-1>",r)
 canv.create_rectangle(200,150,1080,230)
 canv.create_rectangle(200,280,1080,360)
 canv.create_rectangle(200,410,1080,490)
 canv.create_rectangle(200,540,1080,620)
 canv.create_rectangle(200,670,1080,750)
 canv.create_rectangle(200,790,1080,870)
 canv.create_text(600,120,text="МЕНЮ",font="Verdana 30")
 canv.create_text(600,190,text="Описание",font="Verdana 20")
 canv.create_text(600,320,text="Анимация",font="Verdana 20")
 canv.create_text(600,450,text="Погрешности",font="Verdana 20")
 canv.create_text(600,580,text="Таблица",font="Verdana 20")
 canv.create_text(600,700,text="Диаграмма",font="Verdana 20")
 canv.create_text(600,820,text="Помощь",font="Verdana 20")
 canv.create_text(260,20,text="Для того,чтобы перейти вo вкладку в меню",font="Verdana 15")
 canv.create_text(490,40,text="надо навести курсор на прямоугольник с нужным названием и нажать левой кнопкой мыши",font="Verdana 15")
def f(e):
                global x,k,a,y,wis2,m,kurT2,pogdan,znachprog1,znachprog2,znachprog3,znachprog4,cell4,oda5,oda2,oda3,tyt5,tyta5,tytaa5,tytaaa5
                if (e.keysym.isdigit() or (e.char=="." and m[y][x].count(".")==0)) and len(m[y][x])<4:
                    if float(m[y][x]+e.char)<100 and x>0:
    
                      m[y][x]+=e.char
                    elif x==0 and float(m[y][x]+e.char)<1000:
                      m[y][x]+=e.char
##                    m[y][x]+=e.char
                    vivod(m)
        
                    canv.coords(kurT2,330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260)
##                    summas(m)
                    cell4=sreda(m,[[0,1],[0,2],[0,3]])
                    oda5=sreda(m,[[1,1],[1,2],[1,3]])
                    oda2=sreda(m,[[2,1],[2,2],[2,3]])
                    oda3=sreda(m,[[3,1],[3,2],[3,3]])
                    okrulnow(str(cell4))
                    

                    m[0][4]=round(cell4,znak)
                    if m[0][4]==0:
                       m[0][4]=""
                    okrulnow(str(oda5))
                    m[1][4]=round(oda5,znak)
                    if m[1][4]==0:
                       m[1][4]=""
                    okrulnow(str(oda2))
                    m[2][4]=round(oda2,znak)
                    if m[2][4]==0:
                       m[2][4]=""
                    okrulnow(str(oda3))
                    m[3][4]=round(oda3,znak)
                    if m[3][4]==0:
                       m[3][4]=""
                    if m[0][0] and cell4:
                          tyt5=round(float(m[0][0])/cell4,2)
                          m[0][5]=tyt5
                    if m[1][0] and oda5:
                          tyta5=round(float(m[1][0])/oda5,2)
                          m[1][5]=tyta5
                    if m[2][0] and oda2:
                          tytaa5=round(float(m[2][0])/oda2,2)
                          m[2][5]=tytaa5
                    if m[3][0] and oda3:
                          tytaaa5=round(float(m[3][0])/oda3,2)
                          m[3][5]=tytaaa5
                    vivod(m)
                    if cell4!=0 and m[0][0]:
                      canv.create_rectangle(1030,300,1070,318,fill="white",outline="white")
                      oznachprog1=pogdan/float(m[0][0])
                      znachprog1=round(tyt5*oznachprog1,2)
                      okrulnow(str(znachprog1))
                      znachprog1=round(znachprog1,znak)
                      canv.create_text(1030,300,font='Arial 15',anchor='nw',text=znachprog1)
                      canv.create_text(1017,300,font='Arial 15',anchor='nw',text="±")
                      
                      m[0][5]=round(tyt5,znak) 
                      vivod(m)
                      
                    if oda5!=0 and m[1][0]:
                      canv.create_rectangle(1030,375,1070,393,fill="white",outline="white")
                      oznachprog2=pogdan/float(m[1][0])
                      znachprog2=round(tyta5*oznachprog2,2)
                      okrulnow(str(znachprog2))
                      znachprog2=round(znachprog2,znak)
                      canv.create_text(1030,375,font='Arial 15',anchor='nw',text=znachprog2)
                      canv.create_text(1017,375,font='Arial 15',anchor='nw',text="±")
                      m[1][5]=round(tyta5,znak) 
                      vivod(m)
                    if oda2!=0 and m[2][0]:
                       canv.create_rectangle(1030,450,1070,468,fill="white",outline="white")
                       oznachprog3=pogdan/float(m[2][0])
                       znachprog3=round(tytaa5*oznachprog3,2)
                       okrulnow(str(znachprog3))
                       znachprog3=round(znachprog3,znak)
                       canv.create_text(1030,450,font='Arial 15',anchor='nw',text=znachprog3)
                       canv.create_text(1017,450,font='Arial 15',anchor='nw',text="±")
                       m[2][5]=round(tytaa5,znak) 
                       vivod(m)
                    if oda3!=0 and m[3][0]:
                       canv.create_rectangle(1030,525,1070,543,fill="white",outline="white")
                       oznachprog4=pogdan/float(m[3][0])
                       znachprog4=round(tytaaa5*oznachprog4,2)
                       okrulnow(str(znachprog4))
                       znachprog4=round(znachprog4,znak)
                       canv.create_text(1030,525,font='Arial 15',anchor='nw',text=znachprog4)
                       canv.create_text(1017,525,font='Arial 15',anchor='nw',text="±")
                       m[3][5]=round(tytaaa5,znak) 
                       vivod(m)
                    
                    
                if e.keysym=="Right":
                    if x>=3:
                        x=-1
                    x+=1
                    #print(x,y)
                    #canv.create_line(330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260)
                    canv.coords(kurT2,330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260)
        
        

                if e.keysym=="Left":
                    if x<1:
                        x=4
                    x-=1
                    canv.coords(kurT2,330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260)

                if e.keysym=="Up":
                    if y<=0:
                        y=4
                    y-=1
                    canv.coords(kurT2,330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260)

                if e.keysym=="Down":
                    if y>=3:
                        y=-1
                    y+=1
                    canv.coords(kurT2,330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260)
                if e.keysym=="BackSpace":
           
                       m[y][x]=m[y][x][:-1]
                       vivod(m)
                       canv.coords(kurT2,330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260)
                       cell4=sreda(m,[[0,1],[0,2],[0,3]])
                       oda5=sreda(m,[[1,1],[1,2],[1,3]])
                       oda2=sreda(m,[[2,1],[2,2],[2,3]])
                       oda3=sreda(m,[[3,1],[3,2],[3,3]])
                       okrulnow(str(cell4))
                        

                       m[0][4]=round(cell4,znak)
                       if m[0][4]==0:
                           m[0][4]=""
                       okrulnow(str(oda5))
                       m[1][4]=round(oda5,znak)
                       if m[1][4]==0:
                           m[1][4]=""
                       okrulnow(str(oda2))
                       m[2][4]=round(oda2,znak)
                       if m[2][4]==0:
                           m[2][4]=""
                       okrulnow(str(oda3))
                       m[3][4]=round(oda3,znak)
                       if m[3][4]==0:
                           m[3][4]=""
                       if m[0][0] and cell4:
                              tyt5=round(float(m[0][0])/cell4,2)
                              m[0][5]=tyt5
                       if m[1][0] and oda5:
                              tyta5=round(float(m[1][0])/oda5,2)
                              m[1][5]=tyta5
                       if m[2][0] and oda2:
                              tytaa5=round(float(m[2][0])/oda2,2)
                              m[2][5]=tytaa5
                       if m[3][0] and oda3:
                              tytaaa5=round(float(m[3][0])/oda3,2)
                              m[3][5]=tytaaa5
                       vivod(m)
                       if cell4!=0 and m[0][0]:
                          canv.create_rectangle(1030,300,1070,318,fill="white",outline="white")
                          oznachprog1=pogdan/float(m[0][0])
                          znachprog1=round(tyt5*oznachprog1,2)
                          okrulnow(str(znachprog1))
                          znachprog1=round(znachprog1,znak)
                          canv.create_text(1030,300,font='Arial 15',anchor='nw',text=znachprog1)
                          canv.create_text(1017,300,font='Arial 15',anchor='nw',text="±")
                          
                          m[0][5]=round(tyt5,znak) 
                          vivod(m)
                          
                       if oda5!=0 and m[1][0]:
                          canv.create_rectangle(1030,375,1070,393,fill="white",outline="white")
                          oznachprog2=pogdan/float(m[1][0])
                          znachprog2=round(tyta5*oznachprog2,2)
                          okrulnow(str(znachprog2))
                          znachprog2=round(znachprog2,znak)
                          canv.create_text(1030,375,font='Arial 15',anchor='nw',text=znachprog2)
                          canv.create_text(1017,375,font='Arial 15',anchor='nw',text="±")
                          m[1][5]=round(tyta5,znak) 
                          vivod(m)
                       if oda2!=0 and m[2][0]:
                           canv.create_rectangle(1030,450,1070,468,fill="white",outline="white")
                           oznachprog3=pogdan/float(m[2][0])
                           znachprog3=round(tytaa5*oznachprog3,2)
                           okrulnow(str(znachprog3))
                           znachprog3=round(znachprog3,znak)
                           canv.create_text(1030,450,font='Arial 15',anchor='nw',text=znachprog3)
                           canv.create_text(1017,450,font='Arial 15',anchor='nw',text="±")
                           m[2][5]=round(tytaa5,znak) 
                           vivod(m)
                       if oda3!=0 and m[3][0]:
                           canv.create_rectangle(1030,525,1070,543,fill="white",outline="white")
                           oznachprog4=pogdan/float(m[3][0])
                           znachprog4=round(tytaaa5*oznachprog4,2)
                           okrulnow(str(znachprog4))
                           znachprog4=round(znachprog4,znak)
                           canv.create_text(1030,525,font='Arial 15',anchor='nw',text=znachprog4)
                           canv.create_text(1017,525,font='Arial 15',anchor='nw',text="±")
                           m[3][5]=round(tytaaa5,znak) 
                           vivod(m)
def r(e):
    global m,t,k,pogdan,x,y,znachprog11,znachprog12,znachprog1,znachprog2,znachprog3,znachprog4,cell4,oda5,oda2,oda3,tyt5,tyta5,tytaa5,tytaaa5
    if 200<e.x<1080 and 150<e.y<230:
       root.unbind("<Prior>")
       root.unbind("<Next>")
       root.unbind("<Button-1>")
       canv.delete("all")
       canv.create_text(250,100,font='Arial 25', anchor='w', text='Проверка постоянства скорости движения тележки')
       canv.create_text(50,130,font='Arial 15', anchor='nw', text="""
Приборы и материалы: Дорога с металлическим стержнем для крепления фотодатчиков и тормозной стенкой,
электронный секундомер с фотодатчиками, тележка с флажком, пенопластовые пластинки, измерительная лента (рулетка).
Цель работы:
    1. Приобрести навыки работы с электронным секундомером и фотодатчиками.
    2. Проверить, является ли движение тележки равномерным при компенсации силы трения.

Задание 1. Измерение средней скорости движения тележки.
1. Соберите установку, согласно рисунку.
2. Добейтесь равномерного движения тележки вниз по дороге. Для этого расположите дорогу на поверхности стола,
подложив под её начало пластинку из пенопласта. Слегка толкнете тележку вниз, по дороге. Наблюдайте за
движением тележки. Если наклоном удалось скомпенсировать силу сопротивления движению, то тележка доедет до
конца дороги без заметного на глаз изменения скорости. В противном случае необходимо подложить полоску
большей толщины или переместить её ближе к середине дороги.""")
       canv.create_text(50,30,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
       canv.create_text(500,30,text="Чтобы перейти на 2 страницу,нажмите PgDown",anchor="w",font="Arial 15")
       canv.create_rectangle(625,755,725,630,fill='grey',outline='black',width=1.5)
       canv.create_rectangle(635,660,715,640,fill='light grey',outline='black',width=1.5)
       
       canv.create_polygon(200,705,205,755,1105,661,1100,611,fill='red',outline='black',width=1.5)
       canv.create_polygon(240,701,260,699,252,619,232,621,fill="black")
       canv.create_polygon(1100,611,1080,613,1072,533,1092,531,fill="black")
       canv.create_line(232,621,1092,531,width=15)
       canv.create_polygon(456+616,529-64+100,436+616,531-64+100,436+614,531-64-20+100,456+614,529-64-20+100,fill="purple")
       canv.create_polygon(433,500+100,453,498+100,456,529+100,436,531+100,fill="light gray")#1датчик
       canv.create_polygon(433+616,500-64+100,453+616,498-64+100,456+616,529-64+100,436+616,531-64+100,fill="light gray")#2датчик
       canv.create_oval(1005,618,1035,589,fill='grey')
       canv.create_oval(1105,581,1075,611,fill='grey')
       canv.create_polygon(1005,591.5,1105,581,1103,561,1003,571.5,fill='green',outline='black')
       canv.create_line(205,755,1105,755)
       canv.create_rectangle(1005,671,1105,755,fill='red',outline='black',width=1.5)
       canv.create_polygon(200,705,210,704,206,664,196,665,fill="yellow",outline='black')
       canv.create_text(50,800,font='Arial 15', anchor='nw',text="""
3. Установите разгонную доску под минимальным углом к дороге.
4. Фотодатчик "пуск" расположите за разгонной доской так, чтобы флажок пересекал луч тогда, когда тележка
отъедет от разгонной доски на 4-5 см. Второй фотодатчик расположите ближе к концу дороги. Измерьте расстояние
s между фотодатчиками. Результат занести таблицу 1.
""")
       def pervch(e):
          canv.delete("all")
          canv.create_text(250,100,font='Arial 25', anchor='w', text='Проверка постоянства скорости движения тележки')
          canv.create_text(50,30,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
          canv.create_text(500,30,text="Чтобы перейти на 2 страницу,нажмите PgDown",anchor="w",font="Arial 15")
          canv.create_text(50,130,font='Arial 15', anchor='nw', text="""
Приборы и материалы: Дорога с металлическим стержнем для крепления фотодатчиков и тормозной стенкой,
электронный секундомер с фотодатчиками, тележка с флажком, пенопластовые пластинки, измерительная лента (рулетка).
Цель работы:
    1. Приобрести навыки работы с электронным секундомером и фотодатчиками.
    2. Проверить, является ли движение тележки равномерным при компенсации силы трения.

Задание 1. Измерение средней скорости движения тележки.
1. Соберите установку, согласно рисунку.
2. Добейтесь равномерного движения тележки вниз по дороге. Для этого расположите дорогу на поверхности стола,
подложив под её начало пластинку из пенопласта. Слегка толкнете тележку вниз, по дороге. Наблюдайте за
движением тележки. Если наклоном удалось скомпенсировать силу сопротивления движению, то тележка доедет до
конца дороги без заметного на глаз изменения скорости. В противном случае необходимо подложить полоску
большей толщины или переместить её ближе к середине дороги.""")
       
          canv.create_rectangle(625,755,725,630,fill='grey',outline='black',width=1.5)
          canv.create_rectangle(635,660,715,640,fill='light grey',outline='black',width=1.5)
          canv.create_polygon(200,705,205,755,1105,661,1100,611,fill='red',outline='black',width=1.5)
          
          canv.create_polygon(240,701,260,699,252,619,232,621,fill="black")
          canv.create_polygon(1100,611,1080,613,1072,533,1092,531,fill="black")
          canv.create_line(232,621,1092,531,width=15)
          canv.create_polygon(456+616,529-64+100,436+616,531-64+100,436+614,531-64-20+100,456+614,529-64-20+100,fill="purple")
          canv.create_polygon(433,500+100,453,498+100,456,529+100,436,531+100,fill="light gray")#1датчик
          canv.create_polygon(433+616,500-64+100,453+616,498-64+100,456+616,529-64+100,436+616,531-64+100,fill="light gray")#2датчик
          canv.create_oval(1005,618,1035,589,fill='grey')
          canv.create_oval(1105,581,1075,611,fill='grey')
          canv.create_polygon(1005,591.5,1105,581,1103,561,1003,571.5,fill='green',outline='black')#osnova
          canv.create_line(205,755,1105,755)
          canv.create_rectangle(1005,671,1105,755,fill='red',outline='black',width=1.5)
          canv.create_polygon(200,705,210,704,206,664,196,665,fill="yellow",outline='black')
          canv.create_text(50,800,font='Arial 15', anchor='nw',text="""
3. Установите разгонную доску под минимальным углом к дороге.
4. Фотодатчик "пуск" расположите за разгонной доской так, чтобы флажок пересекал луч тогда, когда тележка
отъедет от разгонной доски на 4-5 см. Второй фотодатчик расположите ближе к концу дороги. Измерьте расстояние
s между фотодатчиками. Результат занести таблицу 1.
""")
       def vtorch(e):
          canv.delete("all")
          canv.create_text(50,30,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
          canv.create_text(500,30,text="Чтобы перейти на 1 страницу,нажмите PgUp",anchor="w",font="Arial 15")
          canv.create_text(50,50,font='Arial 15', anchor='nw', text="""
5. Расположите тележку на разгонной доске. Освободите тележку. После прохождения тележки мимо обоих
фотодатчиков результат измерения времени занести в таблицу 1.
6. Повторяйте измерения несколько раз следя за тем, чтобы каждый очередной запуск тележки осуществляется с
одного и того же места разгонной доски. Результаты измерения времени занести в таблицу 1.
7. Подсчитайте среднее значение времена движения и приближенное значение скорости. Резyльтат занести в таблицу 1.
8. Установите разгонную доску под другим углом к дороге. Повторите измерения по пунктам 4-7.
9. Рассчитайте погрешность измерения скорости для каждого угла наклона разгонной доски.

Задание 2. Проверка постоянства скорости при движении тележки.
1. Соберите установку, согласно рисунку. Установите разгонную доску под минимальным углом к дороге.
2. На стержень неанесите мелом 3-4 метки по всей его длине.
3. Расположите фотодатчики около первой метки так, чтобы она оказалась приблизительно посредине между ними.
При этом расстояние между датчиками должно быть 70-80 мм. Занесите значение расстояния в таблицу 2.
4. Запустите тележку. Измерьте время t прохождение тележки мимо фотодатчиков. Произведя насколько опытов,
определите среднее время. Не забывайте, что запускать тележку необходимо с одного и того же места
разгонной доски.
5.Переместите датчики к следующей метке. Повторите измерения по пунктам 3 и 4, каждый раз занося в таблицу 2
значения ℓ и t
6. Рассчитайте мгновенную скорость тележки при прохождении мимо каждой метки. Результат занесите в таблицу 2.
7. Рассчитайте погрешность измерения мгновенной скорости при прохождении около каждой метки.
8. Нанесите на числовую ось результаты измерения скорости с учётом погрешности измерений.""")
          root.bind("<Prior>",pervch)


       root.bind("<Escape>",f2)
       root.bind("<Next>",vtorch)
       
    if 200<e.x<1080 and 280<e.y<360:
       canv.delete("all")
       root.unbind("<Button-1>")
##       canv.create_rectangle(625,655,725,530,fill='grey',outline='black',width=1.5)
##       canv.create_rectangle(635,560,715,540,fill='light grey',outline='black',width=1.5)#секундомер
       canv.create_rectangle(625,655,725,530,fill='grey',outline='black',width=1.5)
       canv.create_rectangle(635,600,715,550,fill='light grey',outline='black',width=1.5)
       canv.create_rectangle(1005,571,1105,655,fill='red',outline='black',width=1.5)
       canv.create_polygon(200,605,210,604,206,564,196,565,fill="yellow",outline='black')
       
       canv.create_polygon(200,605,205,655,1105,561,1100,511,fill='red',outline='black',width=1.5)
       canv.create_text(430,200,font='Arial 20', anchor='nw',text="Для запуска нажмите ENTER")
       canv.create_text(100,900,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
       
       
       canv.create_polygon(240,601,260,599,252,519,232,521,fill="black")
       canv.create_polygon(1100,511,1080,513,1072,433,1092,431,fill="black")
       canv.create_line(232,521,1092,431,width=15)
       
       canv.create_line(205,655,1105,655)
       canv.create_rectangle(1005,571,1105,655,fill='red',outline='black',width=1.5)
       
       flag=canv.create_polygon(456+616,529-64,436+616,531-64,436+614,531-64-20,456+614,529-64-20,fill="yellow")
       canv.create_polygon(433,500,453,498,456,529,436,531,fill="light gray")#1датчик
       canv.create_polygon(433+616,500-64,453+616,498-64,456+616,529-64,436+616,531-64,fill="light gray")#2датчик
       koleso1 = canv.create_oval(1005,518,1035,489,fill='grey')
       koleso2 = canv.create_oval(1105,481,1075,511,fill='grey')
       osnova = canv.create_polygon(1005,491.5,1105,481,1103,461,1003,471.5,fill='black',outline='black')
       def zapusk(e):
        canv.delete("all")
        canv.create_text(430,200,font='Arial 20', anchor='nw',text="Для запуска нажмите ENTER")
        canv.create_text(100,900,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
##       canv.create_rectangle(625,655,725,530,fill='grey',outline='black',width=1.5)
##       canv.create_rectangle(635,560,715,540,fill='light grey',outline='black',width=1.5)#секундомер
        canv.create_rectangle(625,655,725,530,fill='grey',outline='black',width=1.5)
        canv.create_rectangle(635,560,715,550,fill='light grey',outline='black',width=1.5)
        canv.create_rectangle(1005,571,1105,655,fill='red',outline='black',width=1.5)
        canv.create_polygon(200,605,210,604,206,564,196,565,fill="yellow",outline='black')
       
        canv.create_polygon(200,605,205,655,1105,561,1100,511,fill='red',outline='black',width=1.5)
        canv.create_polygon(240,601,260,599,252,519,232,521,fill="black")
        canv.create_polygon(1100,511,1080,513,1072,433,1092,431,fill="black")
        canv.create_line(232,521,1092,431,width=15)
        
        canv.create_line(205,655,1105,655)
        canv.create_rectangle(1005,571,1105,655,fill='red',outline='black',width=1.5)
        
        flag=canv.create_polygon(456+616,529-64,436+616,531-64,436+614,531-64-20,456+614,529-64-20,fill="yellow")
        canv.create_polygon(433,500,453,498,456,529,436,531,fill="light gray")#1датчик
        canv.create_polygon(433+616,500-64,453+616,498-64,456+616,529-64,436+616,531-64,fill="light gray")#2датчик
        koleso1 = canv.create_oval(1005,518,1035,489,fill='grey')
        koleso2 = canv.create_oval(1105,481,1075,511,fill='grey')
        osnova = canv.create_polygon(1005,491.5,1105,481,1103,461,1003,471.5,fill='black',outline='black')
        for i in range(0,130):
           canv.update()
           canv.move(koleso1,-(i/30)**2,((i/30)**2)/9.3)
           canv.move(koleso2,-(i/30)**2,((i/30)**2)/9.3)
           canv.move(osnova,-(i/30)**2,((i/30)**2)/9.3)
           canv.move(flag,-(i/30)**2,((i/30)**2)/9.3)
           canv.create_polygon(433,500,453,498,456,529,436,531,fill="light gray")#1датчик
           canv.create_polygon(433+616,500-64,453+616,498-64,456+616,529-64,436+616,531-64,fill="light gray")#2датчик
           sleep(0.02)

       root.bind("<Escape>",f2)
       root.bind("<Return>",zapusk)
    if 200<e.x<1080 and 410<e.y<490:
       schet=0
       root.unbind("<Button-1>")
       canv.delete("all")
       root.unbind("<BackSpace>")
       stroka11=canv.create_text(600,300,text=stroka1,anchor="w",font="Arial 15")
       canv.create_text(450,100,text="ПОГРЕШНОСТЬ",anchor="w",font="Arial 30")
       canv.create_text(250,150,text="С помощью клавиатуры введите общую погрешность измерительного прибора(линейки).",anchor="w",font="Verdana 15")
       canv.create_text(280,175,text="Значение погрешности,при котором выполнялась работа равна 1.5мм",anchor="w",font="Verdana 15")
       canv.create_rectangle(580,321,700,280,outline="black")
       canv.create_text(510,300,text="∆ =",anchor="w",font="Arial 15")
       canv.create_text(710,300,text="мм",anchor="w",font="Arial 15")
       canv.create_text(10,900,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")

       def vvod(e):
        global stroka1,stroka11,k,pogdan
        
        if len(stroka1)<5:
            if e.char.isdigit()or (e.char=="-" and len(stroka1)==0 or e.char=="." and stroka1.count(".")==0):
                if float(stroka1[0:-1]+e.char)<10:
                       stroka1=stroka1[:-1]+e.char+"_"
                       canv.create_rectangle(600,320,650,300,fill="white",outline="white")
                       stroka11=canv.create_text(600,300,text=stroka1,anchor="w",font="Arial 15")
                       pogdan=float(stroka1[0:-1])
                       print(pogdan)
                       
       def BS(e):
                 global stroka1
                 stroka1=stroka1[:-2]+"_"
                 canv.create_rectangle(600,320,650,290,fill="white",outline="white")
                 canv.create_text(600,300,text=stroka1,anchor="w",font="Arial 15")
                 if stroka1!="_":
                     pogdan=float(stroka1[0:-1])
                     print(pogdan)
                    
       root.bind("<KeyRelease>",vvod)
    
       root.bind("<BackSpace>", BS)
       root.bind("<Escape>",f2)
    if 200<e.x<1080 and 540<e.y<620:
        canv.delete("all")
        
        root.unbind("<Button-1>")
        x=0
        y=0
        canv.create_text(600,80,font='Arial 30',anchor='c',text='Таблица для задания 1')
        for i in range(8):
              canv.create_line(90 + 150 * i, 200, 90 + 150 * i, 100 + 100 * 4)
        for i in range(4):
              canv.create_line(90, 198+100*i, 1140, 198 + 100 * i)
##canv.create_rectangle(840,100,990,300,fill='white',outline='black')
##canv.create_rectangle(90,100,240,300,fill='white',outline='black')
##canv.create_rectangle(240,100,390,300,fill='white',outline='black')
##canv.create_rectangle(990,100,1140,300,fill='white',outline='black')
##canv.create_rectangle(390,100,840,200,fill='white',outline='black')
        canv.create_rectangle(390,250,840,198,fill='white',outline='black')
        canv.create_text(165,250,font='Arial 20',anchor='c',text='Угол \nНаклона')
        canv.create_text(615,220,font='Arial 20',anchor='c',text='t, c')
        canv.create_text(765,270,font='Arial 20',anchor='c',text='t')
        canv.create_text(615,270,font='Arial 20',anchor='c',text='t')
        canv.create_text(465,270,font='Arial 20',anchor='c',text='t')
        canv.create_text(315,250,font='Arial 20',anchor='c',text='s, см')
        canv.create_text(470,270,font='Arial 10',anchor='nw',text='1')
        canv.create_text(620,270,font='Arial 10',anchor='nw',text='2')
        canv.create_text(770,270,font='Arial 10',anchor='nw',text='3')
        canv.create_text(915,250,font='Arial 20',anchor='c',text='t  , c')
        canv.create_text(897,250,font='Arial 10',anchor='nw',text='ср')
        canv.create_text(1015,265,font='Arial 20',anchor='sw',text='ϑ')
        canv.create_text(1085,250,font='Arial 20',anchor='c',text=',')
        canv.create_text(1055,275,font='Arial 20',anchor='c',text='cм/с')
        canv.create_text(1030,250,font='Arial 10',anchor='nw',text='пр')
        canv.create_text(1048,240,font='Arial 13',anchor='nw',text="±")
        canv.create_text(1057,240,text="∆",anchor="nw",font="Arial 15")
        canv.create_text(1068,265,text="ϑ",anchor="sw",font="Arial 20")
        canv.create_text(50,30,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
        canv.create_text(50,550,text="""Чтобы ввести данные в таблицу,используйте
цифры с клавиатуры и точку для дробных значений""",anchor="w",font="Arial 15")
        canv.create_text(50,600,text="""Чтобы перейти к 2 таблице,используйте PgDown""",anchor="w",font="Arial 15")
        canv.create_text(600,550,text="""Чтобы перемещаться между пунктами таблицы,
используйте срелочки на клавиатуре""",anchor="w",font="Arial 15")
        canv.create_text(175,340,font='Arial 20',anchor='c',text='α')
        canv.create_text(175,440,font='Arial 20',anchor='c',text='α')
        canv.create_text(185,340,font='Arial 10',anchor='nw',text='1')
        canv.create_text(185,440,font='Arial 10',anchor='nw',text='2')
        if znachprog11!=0:
         
          
                       canv.create_rectangle(1040,375,1090,393,fill="white",outline="white")
                       
                       oznachprog11=pogdan/float(io[0][0])
                       
                       znachprog11=round(tyt*oznachprog11,2)
                       okrulnow(str(znachprog11))
                       znachprog11=round(znachprog11,znak)
                       canv.create_text(1040,375,font='Arial 15',anchor='nw',text=znachprog11)
                       canv.create_text(1030,375,font='Arial 15',anchor='nw',text="±")
                       
                       io[0][5]=round(tyt,znak)
                       vivod23(io) 
        if znachprog12!=0:
            
                    canv.create_rectangle(1040,475,1090,493,fill="white",outline="white")
                    oznachprog12=pogdan/float(io[1][0])
                    znachprog12=round(tyta*oznachprog12,2)
                    okrulnow(str(znachprog12))
                    znachprog12=round(znachprog12,znak)
                    canv.create_text(1040,475,font='Arial 15',anchor='nw',text=znachprog12)
                    canv.create_text(1030,475,font='Arial 15',anchor='nw',text="±")
                    
                    io[1][5]=round(tyta,znak)
                    vivod23(io)
        global k
        print(x,y)
        print(io)
        k=canv.create_line(240+x*l+(len(io[y][x])*wis),y*h+50+320,240+x*l+30+(len(io[y][x])*wis),y*h+50+320,width=5)
        vivod23(io)

        root.bind("<KeyRelease>",f23)
        def perelistvniz(e):
            root.unbind("<KeyRelease>")
            root.unbind("<Next>")
            canv.delete("all")
            
            global x,y,pogdan,znachprog1,znachprog2,znachprog3,znachprog4,cell4,oda5,oda2,oda3,tyt5,tyta5,tytaa5,tytaaa5
            x=0
            y=0
            def sreda(m, v):
                  s=0
                  q=0
                  for i in range(0,len(m)):
         
         
                    for j in range(1,len(m[i])):
                      if m[i][j] and [i,j] in v:
                        d=float(m[i][j])
                        s+=d
                        q+=1
                
                  if q:
                   k=s/q
                  else:
                    k=0      
                  return k
            for i in range(8):
                canv.create_line(200 + 125 * i, 170, 200 + 125 * i, 96 + 75 * 6)

            for i in range(6):
                canv.create_line(200, 170+75*i, 1075, 170 + 75* i)

            canv.create_line(450,190,826,190)
            canv.create_rectangle(450,210,825,170,fill='white',outline='black')
            canv.create_text(620,50,font='Arial 30',anchor='c',text='Таблица для задания 2')
            canv.create_text(262,200,font='Arial 20',anchor='c',text='№ метки')
            canv.create_text(262,287,font='Arial 20',anchor='c',text='1')
            canv.create_text(262,362,font='Arial 20',anchor='c',text='2')
            canv.create_text(262,437,font='Arial 20',anchor='c',text='3')
            canv.create_text(262,512,font='Arial 20',anchor='c',text='4')
            canv.create_text(388,200,font='Arial 20',anchor='c',text='ℓ, cм')
            canv.create_text(637,190,font='Arial 20',anchor='c',text='t, c')
            canv.create_text(512,225,font='Arial 20',anchor='c',text='t')
            canv.create_text(637,225,font='Arial 20',anchor='c',text='t')
            canv.create_text(762,225,font='Arial 20',anchor='c',text='t')
            canv.create_text(517,225,font='Arial 10',anchor='nw',text='1')
            canv.create_text(642,225,font='Arial 10',anchor='nw',text='2')
            canv.create_text(767,225,font='Arial 10',anchor='nw',text='3')
            canv.create_text(887,200,font='Arial 20',anchor='c',text='t  , c')
            canv.create_text(869,200,font='Arial 10',anchor='nw',text='ср')
            canv.create_text(960,200,font='Arial 20',anchor='c',text='ϑ')
            canv.create_text(1013,185,font='Arial 20',anchor='nw',text=',см/с')
            canv.create_text(965,200,font='Arial 10',anchor='nw',text='пр')
            canv.create_text(980,195,font='Arial 13',anchor='nw',text='±')
            canv.create_text(990,193,text="∆",anchor="nw",font="Arial 15")
            canv.create_text(1000,218,text="ϑ",anchor="sw",font="Arial 20")
            canv.create_text(50,20,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
            canv.create_text(50,600,text="""Чтобы ввести данные в таблицу,используйте
цифры с клавиатуры и точку для дробных значений""",anchor="w",font="Arial 15")
            canv.create_text(50,650,text="""Чтобы перейти к 1 таблице,используйте PgUp""",anchor="w",font="Arial 15")
            canv.create_text(600,590,text="""Чтобы использовать автозаполнение таблицы,нажмите F3""",anchor="w",font="Arial 15")
            canv.create_text(600,660,text="""Чтобы перемещаться между пунктами таблицы,
используйте срелочки на клавиатуре""",anchor="w",font="Arial 15")
##            t=[""]*4
##            for g in range(0,len(t)):
##                t[g]=[""]*6
##            m=[""]*4
##            for g in range(0,len(m)):
##              m[g]=[""]*6
           
            if znachprog1!=0:
                          cell4=sreda(m,[[0,1],[0,2],[0,3]])
                          if m[0][0] and cell4:
                              tyt5=round(float(m[0][0])/cell4,2)
                              m[0][5]=tyt5
                          canv.create_rectangle(1030,300,1070,318,fill="white",outline="white")
                          oznachprog1=pogdan/float(m[0][0])
                          znachprog1=round(tyt5*oznachprog1,2)
                          okrulnow(str(znachprog1))
                          znachprog1=round(znachprog1,znak)
                          canv.create_text(1030,300,font='Arial 15',anchor='nw',text=znachprog1)
                          canv.create_text(1017,300,font='Arial 15',anchor='nw',text="±")
                          
                          m[0][5]=round(tyt5,znak) 
                          vivod(m)
            if znachprog2!=0:
                          oda5=sreda(m,[[1,1],[1,2],[1,3]])
                          if m[1][0] and oda5:
                              tyta5=round(float(m[1][0])/oda5,2)
                              m[1][5]=tyta5
                          canv.create_rectangle(1030,375,1070,393,fill="white",outline="white")
                          oznachprog2=pogdan/float(m[1][0])
                          znachprog2=round(tyta5*oznachprog2,2)
                          okrulnow(str(znachprog2))
                          znachprog2=round(znachprog2,znak)
                          canv.create_text(1030,375,font='Arial 15',anchor='nw',text=znachprog2)
                          canv.create_text(1017,375,font='Arial 15',anchor='nw',text="±")
                          m[1][5]=round(tyta5,znak) 
                          vivod(m)
            if znachprog3!=0:
                       oda2=sreda(m,[[2,1],[2,2],[2,3]])
                       if m[2][0] and oda2:
                              tytaa5=round(float(m[2][0])/oda2,2)
                              m[2][5]=tytaa5
                       canv.create_rectangle(1030,450,1070,468,fill="white",outline="white")
                       oznachprog3=pogdan/float(m[2][0])
                       znachprog3=round(tytaa5*oznachprog3,2)
                       okrulnow(str(znachprog3))
                       znachprog3=round(znachprog3,znak)
                       canv.create_text(1030,450,font='Arial 15',anchor='nw',text=znachprog3)
                       canv.create_text(1017,450,font='Arial 15',anchor='nw',text="±")
                       m[2][5]=round(tytaa5,znak) 
                       vivod(m)
            if znachprog4!=0:
                       oda3=sreda(m,[[3,1],[3,2],[3,3]])
                       if m[3][0] and oda3:
                              tytaaa5=round(float(m[3][0])/oda3,2)
                              m[3][5]=tytaaa5
                       canv.create_rectangle(1030,525,1070,543,fill="white",outline="white")
                       oznachprog4=pogdan/float(m[3][0])
                       znachprog4=round(tytaaa5*oznachprog4,2)
                       okrulnow(str(znachprog4))
                       znachprog4=round(znachprog4,znak)
                       canv.create_text(1030,525,font='Arial 15',anchor='nw',text=znachprog4)
                       canv.create_text(1017,525,font='Arial 15',anchor='nw',text="±")
                       m[3][5]=round(tytaaa5,znak) 
                       vivod(m)
            global kurT2
            kurT2=canv.create_line(330+x*l2+len(m[y][x])*wis2,y*h2+50+260,330+x*l2+30+len(m[y][x])*wis2,y*h2+50+260,width=5)
            vivod(m)
            
    
##            def vivod(m):
##                 global t
##                 for i in range(0,len(m)):
##                    for j in range(0,len(m[i])):
##                        canv.delete(t[i][j])
##
##                        t[i][j]=canv.create_text(j*l2+330,40+260+i*h2,text=m[i][j],font="Arial 20",anchor="w")
##def summas(m):
## if len(m[y][1])>=1 and len(m[y][2])>=1 and len(m[y][3])>=1:
##    for i in range(0,len(m)):
##        s=0
##        for j in range(0,len(m[i])):
##            s+=float(m[i][j])
##        k=s/3
##        m.append(k)
##        vivod(m)
            
            root.bind("<Prior>",perelistvverh)
            root.bind("<KeyRelease>",f)
            root.bind("<F3>",autopog)
        def perelistvverh(e):
            root.unbind("<Prior>")
            root.unbind("<KeyRelease>")
            root.unbind("F3")
            canv.delete("all")
            print("verh")
            global x,y,k,znachprog11,znachprog12
            x=0
            y=0
            canv.create_text(600,80,font='Arial 30',anchor='c',text='Таблица для задания 1')
            for i in range(8):
              canv.create_line(90 + 150 * i, 200, 90 + 150 * i, 100 + 100 * 4)
            for i in range(4):
              canv.create_line(90, 198+100*i, 1140, 198 + 100 * i)
##canv.create_rectangle(840,100,990,300,fill='white',outline='black')
##canv.create_rectangle(90,100,240,300,fill='white',outline='black')
##canv.create_rectangle(240,100,390,300,fill='white',outline='black')
##canv.create_rectangle(990,100,1140,300,fill='white',outline='black')
##canv.create_rectangle(390,100,840,200,fill='white',outline='black')
            canv.create_rectangle(390,250,840,198,fill='white',outline='black')
            canv.create_text(165,250,font='Arial 20',anchor='c',text='Угол \nНаклона')
            canv.create_text(615,220,font='Arial 20',anchor='c',text='t, c')
            canv.create_text(765,270,font='Arial 20',anchor='c',text='t')
            canv.create_text(615,270,font='Arial 20',anchor='c',text='t')
            canv.create_text(465,270,font='Arial 20',anchor='c',text='t')
            canv.create_text(315,250,font='Arial 20',anchor='c',text='s, см')
            canv.create_text(470,270,font='Arial 10',anchor='nw',text='1')
            canv.create_text(620,270,font='Arial 10',anchor='nw',text='2')
            canv.create_text(770,270,font='Arial 10',anchor='nw',text='3')
            canv.create_text(915,250,font='Arial 20',anchor='c',text='t  , c')
            canv.create_text(897,250,font='Arial 10',anchor='nw',text='ср')
            canv.create_text(1015,265,font='Arial 20',anchor='sw',text='ϑ')
            canv.create_text(1085,250,font='Arial 20',anchor='c',text=',')
            canv.create_text(1055,275,font='Arial 20',anchor='c',text='cм/с')
            canv.create_text(1030,250,font='Arial 10',anchor='nw',text='пр')
            canv.create_text(1048,240,font='Arial 13',anchor='nw',text="±")
            canv.create_text(1057,240,text="∆",anchor="nw",font="Arial 15")
            canv.create_text(1068,265,text="ϑ",anchor="sw",font="Arial 20")
            canv.create_text(50,30,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
            canv.create_text(50,550,text="""Чтобы ввести данные в таблицу,используйте
цифры с клавиатуры и точку для дробных значений""",anchor="w",font="Arial 15")
            canv.create_text(50,600,text="""Чтобы перейти к 2 таблице,используйте PgDown""",anchor="w",font="Arial 15")
            canv.create_text(600,550,text="""Чтобы перемещаться между пунктами таблицы,
используйте срелочки на клавиатуре""",anchor="w",font="Arial 15")
            canv.create_text(175,340,font='Arial 20',anchor='c',text='α')
            canv.create_text(175,440,font='Arial 20',anchor='c',text='α')
            canv.create_text(185,340,font='Arial 10',anchor='nw',text='1')
            canv.create_text(185,440,font='Arial 10',anchor='nw',text='2')
            if znachprog11!=0:
                 if cell!=0 and io[0][0]:
                       canv.create_rectangle(1040,375,1090,393,fill="white",outline="white")
                       
                       oznachprog11=pogdan/float(io[0][0])
                       
                       znachprog11=round(tyt*oznachprog11,2)
                       okrulnow(str(znachprog11))
                       znachprog11=round(znachprog11,znak)
                       canv.create_text(1040,375,font='Arial 15',anchor='nw',text=znachprog11)
                       canv.create_text(1030,375,font='Arial 15',anchor='nw',text="±")
                       
                       io[0][5]=round(tyt,znak)
                       vivod23(io)
            if znachprog12!=0:
               if oda!=0 and io[1][0]:
                    canv.create_rectangle(1040,475,1090,493,fill="white",outline="white")
                    oznachprog12=pogdan/float(io[1][0])
                    znachprog12=round(tyta*oznachprog12,2)
                    okrulnow(str(znachprog12))
                    znachprog12=round(znachprog12,znak)
                    canv.create_text(1040,475,font='Arial 15',anchor='nw',text=znachprog12)
                    canv.create_text(1030,475,font='Arial 15',anchor='nw',text="±")
                    
                    io[1][5]=round(tyta,znak)
                    vivod23(io)

            k=canv.create_line(240+x*l+(len(io[y][x])*wis),y*h+50+320,240+x*l+30+(len(io[y][x])*wis),y*h+50+320,width=5)
            vivod23(io)
            root.bind("<Next>",perelistvniz)
            root.bind("<KeyRelease>",f23)
        root.bind("<Next>",perelistvniz)
            
        root.bind("<Escape>",f2)
    if 200<e.x<1080 and 670<e.y<750:
       canv.delete("all")
       root.unbind("<Button-1>")

       root.unbind('<Key>')
       canv.create_text(50,30,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
       canv.create_text(640,150,font='Arial 30', anchor='c',text='Диаграмма для второго задания')
       canv.create_line(100,560,1210,560,arrow=LAST,width=3)
       canv.create_text(1220,560,font='Arial 30', anchor='nw',text='ϑ,')
       canv.create_text(1215,600,font='Arial 15', anchor='nw',text='см/с')
       
       
       
       if m[0][5]!="" and m[1][5]!="" and m[2][5]!="" and m[3][5]!="":
        cell4=sreda(m,[[0,1],[0,2],[0,3]])
        oda5=sreda(m,[[1,1],[1,2],[1,3]])
        oda2=sreda(m,[[2,1],[2,2],[2,3]])
        oda3=sreda(m,[[3,1],[3,2],[3,3]])
        
        if m[0][0] and cell4:
              tyt5=round(float(m[0][0])/cell4,2)
              m[0][5]=tyt5
        if m[1][0] and oda5:
              tyta5=round(float(m[1][0])/oda5,2)
              m[1][5]=tyta5
        if m[2][0] and oda2:
              tytaa5=round(float(m[2][0])/oda2,2)
              m[2][5]=tytaa5
        if m[3][0] and oda3:
              tytaaa5=round(float(m[3][0])/oda3,2)
              m[3][5]=tytaaa5
        
        if cell4!=0 and m[0][0]:
          canv.create_rectangle(1030,300,1070,318,fill="white",outline="white")
          oznachprog1=pogdan/float(m[0][0])
          znachprog1=round(tyt5*oznachprog1,2)
          okrulnow(str(znachprog1))
          znachprog1=round(znachprog1,znak)
          
          
          m[0][5]=round(tyt5,znak) 
         
          
        if oda5!=0 and m[1][0]:
          canv.create_rectangle(1030,375,1070,393,fill="white",outline="white")
          oznachprog2=pogdan/float(m[1][0])
          znachprog2=round(tyta5*oznachprog2,2)
          okrulnow(str(znachprog2))
          znachprog2=round(znachprog2,znak)
          
          m[1][5]=round(tyta5,znak) 
          
        if oda2!=0 and m[2][0]:
           canv.create_rectangle(1030,450,1070,468,fill="white",outline="white")
           oznachprog3=pogdan/float(m[2][0])
           znachprog3=round(tytaa5*oznachprog3,2)
           okrulnow(str(znachprog3))
           znachprog3=round(znachprog3,znak)
           
           m[2][5]=round(tytaa5,znak) 
           
        if oda3!=0 and m[3][0]:
           canv.create_rectangle(1030,525,1070,543,fill="white",outline="white")
           oznachprog4=pogdan/float(m[3][0])
           znachprog4=round(tytaaa5*oznachprog4,2)
           okrulnow(str(znachprog4))
           znachprog4=round(znachprog4,znak)
           
           m[3][5]=round(tytaaa5,znak)
        minimal=float(min(float(float(m[0][5])-float(znachprog1)),float(float(m[1][5])-float(znachprog2)),float(float(m[2][5])-float(znachprog3)),float(float(m[3][5])-float(znachprog4))))
        maximal=float(max(float(float(m[0][5])+float(znachprog1)),float(float(m[1][5])+float(znachprog2)),float(float(m[2][5])+float(znachprog3)),float(float(m[3][5])+float(znachprog4))))
        razniha=maximal-minimal
        hoha=1080/20
        hoha1=1100/razniha
        pp=float(m[0][5])-float(znachprog1)-minimal
        ppp=float(m[1][5])-float(znachprog2)-minimal
        pppp=float(m[2][5])-float(znachprog3)-minimal
        ppppp=float(m[3][5])-float(znachprog4)-minimal
        z=2*float(znachprog1)
        zz=2*float(znachprog2)
        zzz=2*float(znachprog3)
        zzzz=2*float(znachprog4)
        obshee=[]
        
        canv.create_line(100+pp*hoha1,520,100+(z+pp)*hoha1,520)
        canv.create_line(100+ppp*hoha1,480,100+(zz+ppp)*hoha1,480)
        canv.create_line(100+pppp*hoha1,440,100+(zzz+pppp)*hoha1,440)
        canv.create_line(100+ppppp*hoha1,400,100+(zzzz+ppppp)*hoha1,400)
        for i in range(0,21):
            canv.create_text(100+55*i,575,font='Arial 15',text=round(minimal+(55/hoha1)*i,1))
        for aba in range(int(100+pp*hoha1),int(101+(z+pp)*hoha1)):
            if  int(100+ppp*hoha1)<=aba<=int(100+(zz+ppp)*hoha1):
                if int(100+pppp*hoha1)<=aba<=int(100+(zzz+pppp)*hoha1):
                    if int(100+ppppp*hoha1)<=aba<=int(100+(zzzz+ppppp)*hoha1):
                        obshee.append(aba)
        
                        
                        
        if obshee!=[]:
         canv.create_line(min(obshee, key=lambda i: int(i)),400,min(obshee, key=lambda i: int(i)),520,width=1.5)
         canv.create_line(max(obshee, key=lambda i: int(i)),400,max(obshee, key=lambda i: int(i)),520,width=1.5)
         canv.create_text(600,700,text='Вывод: Значения скорости совпали \n в пределах погрешности, поэтому \n движение является равномерным.  ',font="Verdana 20")
         for superk in range(min(obshee, key=lambda i: int(i)),max(obshee, key=lambda i: int(i))+1,2):
             canv.create_line(superk,400,superk,520,width=1.2,fill="grey")
         canv.create_text(100+pp*hoha1+float(znachprog1)*hoha1-5,515,text='ϑ',font="Verdana 20",anchor="sw")
         canv.create_text(100+pp*hoha1+float(znachprog1)*hoha1+5,518,text='1',font="Verdana 10",anchor="sw")
         canv.create_text(100+ppp*hoha1+float(znachprog2)*hoha1-5,475,text='ϑ',font="Verdana 20",anchor="sw")
         canv.create_text(100+ppp*hoha1+float(znachprog2)*hoha1+5,478,text='2',font="Verdana 10",anchor="sw")
         canv.create_text(100+pppp*hoha1+float(znachprog3)*hoha1-5,435,text='ϑ',font="Verdana 20",anchor="sw")
         canv.create_text(100+pppp*hoha1+float(znachprog3)*hoha1+5,438,text='3',font="Verdana 10",anchor="sw")
         canv.create_text(100+ppppp*hoha1+float(znachprog4)*hoha1-5,395,text='ϑ',font="Verdana 20",anchor="sw")
         canv.create_text(100+ppppp*hoha1+float(znachprog4)*hoha1+5,398,text='4',font="Verdana 10",anchor="sw")
        else:
         canv.create_text(600,700,text='Вывод: Значения скорости не совпали \n в пределах погрешности, поэтому \n движение является неравномерным.  ',font="Verdana 20")
       else:
           canv.create_text(650,350,text='Введите значения в таблицу под номером 2',font="Verdana 40",fill="red")
         
            
       for i in range (0,21):
        canv.create_line(100+55*i,555,100+55*i,565,width=1.5)
       root.bind("<Escape>",f2)
    if 200<e.x<1080 and 790<e.y<870:
       canv.delete("all")
       root.unbind("<Button-1>")
       canv.create_text(50,30,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
       canv.create_text(580,400,text="1)Для перехода из вкладок в меню надо нажать ESCAPE",font="Verdana 15")
       canv.create_text(614,440,text="2)Для перехода с титульного листа в меню надо нажать ENTER",font="Verdana 15")
       canv.create_text(593,480,text="3)Для того,чтобы запустить анимацию, надо нажать ENTER",font="Verdana 15")
       canv.create_text(523,520,text="4)Для того,чтобы перейти вo вкладку в меню,",font="Verdana 15")
       canv.create_text(720,560,text="надо навести курсор на прямоугольник с нужным названием и нажать левой кнопкой мыши",font="Verdana 15")
       canv.create_text(280,615,text="5)Для того,чтобы вбить значения в таблицу, используйте цифры с клавиатуры",font="Verdana 15",anchor="sw")
       canv.create_text(280,670,text="6)Для того,чтобы перелистывать условие и сменять таблицы, используйте PgUp и PgDown",font="Verdana 15",anchor="sw")
       
       root.bind("<Escape>",f2)

def okrulnow(pogresh):
    global znak
    znak=0
    for i in range(len(pogresh)):
        if pogresh[i] in '123456789':
            if '.' not in pogresh:
                znak = len(value) - i - 1
            elif float(pogresh) > 1:
                znak = -(pogresh.index('.') - i - 1)
            else:
                znak = -(pogresh.index('.') - i)
            break
    if pogresh[znak] == "1":
        znak += 1
    pogresh = round(float(pogresh), znak)
    if '.' in str(pogresh) and str(pogresh)[str(pogresh).find('.') + 1:] == '0':
        pogresh = int(pogresh)
    return pogresh, znak

root.bind("<Return>",f1)
##root.bind("<Button-1>",r)
root.mainloop()
