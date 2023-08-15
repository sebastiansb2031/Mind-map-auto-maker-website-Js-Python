import random
import numpy as np
import svgwrite

def crear_matriz (matriz,Escala_radio,pcentralx,pcentraly,ancho_elipse,largo_elipse,ancho_elipse_ttl,colores):
 pi,cos,sin=np.pi ,np.cos ,np.sin 
 def angulos_limite(matriz,jerarquia,num):
  conta=0
  for i in range(len(matriz)):
   if matriz[i]==jerarquia:
    conta=conta+1
    if conta==num+1:
     i_actual=i
  conta2=0
  for i in range(i_actual):
   if matriz[i]==2:
    conta2=conta2+1
  angulon= (conta2-1)*(360/(np.bincount(matriz)[2]))*pi/180
  return angulon

 def primer_radio(qf,ancho_elipse,largo_elipse,radio_min,radio_min0,Escala_radio,pcentralx,pcentraly,colores):
  radiof=((qf)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*((2*(k)))+radio_min0)*Escala_radio
  res=360/(qf)
  for i in range(qf):
     globals()["Angulo"+str(2)+str(i)]=res*i*pi/180
     globals()["Centrox"+str(2)+str(i)]=(radiof+radio_min/2)*cos(res*i*pi/180)+pcentralx
     globals()["Centroy"+str(2)+str(i)]=( radiof+radio_min/2)*sin(res*i*pi/180)+pcentraly
     globals()["Color"+str(2)+str(i)]=random.choice(list(colores.values()))
  radio=radiof
  return radio
 
 solape=0
 Tamaño=np.bincount(matriz)
 radio=0
 for k in range(len(Tamaño)-2) :
  q=Tamaño[k+1]
  qf=Tamaño[k+2]
  radio_min0=ancho_elipse_ttl
  radio_min=2*2*max(ancho_elipse/2,largo_elipse)
  nactual=0
  aux1=0
  if k==0:
   radiof=primer_radio(qf,ancho_elipse,largo_elipse,radio_min,radio_min0,Escala_radio,pcentralx,pcentraly,colores)
  if k>0:
   radio=radiof
   radiof=((qf)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*((1*(k)+1)))*Escala_radio
   while radiof<radio+2*radio_min:
    radiof=radiof+radio_min  
   
   qhf=2*pi*radiof/(max(ancho_elipse,largo_elipse))
   resf=360/(qhf)
   for i in range(q): #num. de elementos de la jerarquia anterior
    for n in range(globals()["Nelementos"+str(k+1)+str(i)]): #numero de elementos jerarquia superior de cada elementos de jerarquia anterior
      globals()["Angulo"+str(k+2)+str(nactual+n)]=round((angulos_limite(matriz,k+2,n+nactual)+resf*(n)*pi/180)/(resf*pi/180))*(resf*pi/180)
      if nactual>0: 
       while globals()["Angulo"+str(k+2)+str(nactual+n)]-globals()["Angulo"+str(k+2)+str(nactual+n-1)]<(resf*pi/(180*2)):
        globals()["Angulo"+str(k+2)+str(nactual+n)]=round((angulos_limite(matriz,k+2,n+nactual)+resf*(n+aux1)*pi/180)/(resf*pi/180))*(resf*pi/180)
        aux1=aux1+1
        if globals()["Angulo"+str(k+2)+str(nactual+n)]+(resf*pi)/180>(angulos_limite(matriz,k+2,n+nactual)+((360/(Tamaño[2]))*pi)/(180)):
         solape=1   
      aux1=0   
      globals()["Centrox"+str(k+2)+str(nactual+n)]=(radiof)*cos(globals()["Angulo"+str(k+2)+str(nactual+n)])+pcentralx
      globals()["Centroy"+str(k+2)+str(nactual+n)]=(radiof)*sin(globals()["Angulo"+str(k+2)+str(nactual+n)])+pcentraly
      globals()["Color"+str(k+2)+str(nactual+n)]=random.choice(list(colores.values()))
      if k==len(Tamaño)-3:
       Radiomax=radiof
    nactual=nactual+globals()["Nelementos"+str(k+1)+str(i)] 
 return solape,Radiomax  
    

def crear_lineas(matriz,dwg,pcentralx,pcentraly,color_e_ttl,mm):
 Tamaño=np.bincount(matriz)
 for k in range(len(Tamaño)-2) :
  nactual=0
  if k>0:   
   for i in range(Tamaño[k+1]):   
    for n in range(globals()["Nelementos"+str(k+1)+str(i)]):    
       globals()["linea"+str(k)+str(i)+str(n)]=dwg.add(dwg.line(start=(globals()["Centrox"+str(k+2)+str(nactual+n)],globals()["Centroy"+str(k+2)+str(nactual+n)]),end=(globals()["Centrox"+str(k+1)+str(i)],globals()["Centroy"+str(k+1)+str(i)]),stroke="#FFFFFF",stroke_width=3*mm))
       globals()["linea"+str(k)+str(i)+str(n)]=dwg.add(dwg.line(start=(globals()["Centrox"+str(k+2)+str(nactual+n)],globals()["Centroy"+str(k+2)+str(nactual+n)]),end=(globals()["Centrox"+str(k+1)+str(i)],globals()["Centroy"+str(k+1)+str(i)]),stroke=globals()["Color"+str(k+1)+str(i)],stroke_width=2*mm))
    nactual=nactual+globals()["Nelementos"+str(k+1)+str(i)]   
  else:
   for i in range(Tamaño[k+2]):
      globals()["linea"+str(nactual)]=dwg.add(dwg.line(start=(globals()["Centrox"+str(2)+str(i)],globals()["Centroy"+str(2)+str(i)]),end=(pcentralx,pcentraly),stroke="#FFFFFF",stroke_width=3*mm))
      globals()["linea"+str(nactual)]=dwg.add(dwg.line(start=(globals()["Centrox"+str(2)+str(i)],globals()["Centroy"+str(2)+str(i)]),end=(pcentralx,pcentraly),stroke=color_e_ttl,stroke_width=2*mm))
         


def crear_elipses(matriz,matrizcon,shapes,dwg,ancho_elipse,largo_elipse):
 Tamaño=np.bincount(matriz)
 for k in range(len(Tamaño)-2) :
  nactual=0
  if k>0:   
   for i in range(Tamaño[k+1]):   
    for n in range(globals()["Nelementos"+str(k+1)+str(i)]):         
      if matrizcon[np.where(matriz==k+2)[0][nactual+n]]=="1" :
       globals()["e" + str(nactual+n+1)+str(k+2)]=shapes.add(dwg.ellipse(center=(globals()["Centrox"+str(k+2)+str(nactual+n)],globals()["Centroy"+str(k+2)+str(nactual+n)]), r=(ancho_elipse/2, largo_elipse), stroke_width= 1,stroke='#FFFFFF',fill=globals()["Color"+str(k+2)+str(nactual+n)] ) )
      else:
       globals()["e" + str(nactual+n+1)+str(k+2)]=shapes.add(dwg.ellipse(center=(globals()["Centrox"+str(k+2)+str(nactual+n)],globals()["Centroy"+str(k+2)+str(nactual+n)]), r=(ancho_elipse/2, largo_elipse), stroke_width= 0,fill='#FFFFFF' ))
    nactual=nactual+globals()["Nelementos"+str(k+1)+str(i)]
  else:
   for i in range(Tamaño[k+2]):
     if matrizcon[np.where(matriz==k+2)[0][i]]=="1" :
      globals()["e" + str(i+1)+str(k+2)] = shapes.add(dwg.ellipse(center=(globals()["Centrox"+str(2)+str(i)], globals()["Centroy"+str(2)+str(i)]), r=(ancho_elipse/2, largo_elipse),stroke_width= 1,stroke='#FFFFFF',fill=globals()["Color"+str(2)+str(i)]))
     else:
      globals()["e" + str(i+1)+str(k+2)] = shapes.add(dwg.ellipse(center=(globals()["Centrox"+str(2)+str(i)], globals()["Centroy"+str(2)+str(i)]), r=(ancho_elipse/2, largo_elipse),stroke_width=0,fill='#FFFFFF'))
         
    
def Escribir_texto(matriz,matriztxt,dwg,ancho_fuente,mm):
 mm=mm
 def Quitar_espacio_arreglo(matriz):
  def Quitar_espacio(termino):
   aux=termino
   for j in range(len(str(termino))):
    if str(termino)[j]=='_':
     aux=str(str(aux)[:j])+" "+str(str(aux)[j+1:])
   return aux
  arr_aux=matriz
  for i in range(len(matriz)):
    arr_aux[i]=Quitar_espacio(arr_aux[i])
  return arr_aux

 Tamaño=np.bincount(matriz)
 for i in range(2,len(Tamaño),1):
  for j in range(Tamaño[i]):
   matriz2=Quitar_espacio_arreglo(matriztxt)
   globals()["Texto"+str(i)+str(j)]=dwg.add(dwg.text(matriz2[np.where(matriz==i)[0][j]] ,insert=(globals()["Centrox"+str(i)+str(j)]-len(matriz2[np.where(matriz==i)[0][j]])*ancho_fuente/2,globals()["Centroy"+str(i)+str(j)]),font_size=2*mm ,fill="black"))


def Escribir_hipervinculos(matriz,matrizhyperlk,dwg,e0):

 def Crear_hipervinculo(objeto,linkd,dwg,k,l):
    globals()["link"+str(k)+str(l)] = dwg.a(linkd)
    globals()["link"+str(k)+str(l)].add(objeto)
    dwg.add(globals()["link"+str(k)+str(l)])
 
 Tamaño=np.bincount(matriz)
 if matrizhyperlk[0]=="nulo":
  link0=dwg.a(href='javascript:false',target="_self", style="cursor:default")
  link0.add(e0)
  dwg.add(link0)
 else:
  Crear_hipervinculo(e0,matrizhyperlk[0],dwg,0,0)
 for i in range(2,len(Tamaño),1):
  for j in range(Tamaño[i]):
   if matrizhyperlk[np.where(matriz==i)[0][j]]!="nulo":  
    Crear_hipervinculo(globals()["e" + str(j+1)+str(i)],str(matrizhyperlk[np.where(matriz==i)[0][j]]),dwg,i,j)
   else:
    globals()["link"+str(j+1)+str(i)] = dwg.a(href='javascript:false',target="_self", style="cursor:default")
 # Añadir la elipse al hipervínculo
    globals()["link"+str(j+1)+str(i)].add(globals()["e" + str(j+1)+str(i)])
 # Añadir el hipervínculo al dibujo
    dwg.add(globals()["link"+str(j+1)+str(i)])
   

def crear_elementos_svg(m1,m1txt,m1con,m1hyplk,ancho_fuente,ancho_elipse,largo_elipse,largo_elipse_ttl,largo_ttl,MedidaU,ma):
 mm=ma
 Colorespastel2 ={'Rojo1' : '#E6B0AA', 'Rojo2' : '#F5B7B1', 'Morado1' : '#D7BDE2' , 'Morado2' : '#D2B4DE','Azul1' : '#A9CCE3' , 'Azul2' : '#AED6F1','Verde_azul1' : '#A3E4D7' , 'Verde_azul2' : '#A2D9CE','Verde1' : '#A9DFBF' , 'Verde2' : '#ABEBC6','Amarillo1' : '#F9E79F' , 'Amarillo2' : '#FAD7A0','Naranja1' : '#F5CBA7' , 'Naranja2' : '#EDBB99','Blanco1' : '#F7F9F9' , 'Blanco2' : '#E5E7E9','Gris1' : '#D5DBDB' , 'Gris2' : '#CCD1D1','Negro1' : '#AEB6BF' , 'Negro2' : '#ABB2B9'}
 Colorespastel1 ={'Rojo1' : '#E6B0AA', 'Morado1' : '#D7BDE2' ,'Azul1' : '#A9CCE3'  ,'Verde1' : '#A9DFBF' ,'Amarillo1' : '#F9E79F' ,'Naranja1' : '#F5CBA7 ' ,'Gris1' : '#D5DBDB'  }
 color_e_ttl=random.choice(list(Colorespastel1.values()))
 
 def prevenir_solape(matriz,MedidaU,ancho_elipse,largo_elipse,ancho_elipse_ttl):
  pcentralx_aux=MedidaU
  pcentraly_aux=MedidaU
  Escala_aux=1
  solape,Radiomax= crear_matriz(matriz,Escala_aux,pcentralx_aux,pcentraly_aux,ancho_elipse,largo_elipse,ancho_elipse_ttl,Colorespastel1)
  while solape>0 or Radiomax>pcentralx_aux or Radiomax>pcentraly_aux:
   Escala_aux=Escala_aux+0.1
   pcentralx_aux=Escala_aux*pcentralx_aux
   pcentraly_aux=Escala_aux*pcentraly_aux
   solape,Radiomax= crear_matriz(matriz,Escala_aux,pcentralx_aux,pcentraly_aux,ancho_elipse,largo_elipse,ancho_elipse_ttl,Colorespastel1) 
  return pcentralx_aux,pcentraly_aux
 
 
 def crear_angulos(matriz): ##Funcion que 
  Tamaño=np.bincount(matriz)
  matrizres=[]
  matrizang=[]
  for i in range(2,len(Tamaño),1):  ##Vectores de posicion de jerarquías y resoluciones de ángulos
   matrizres.append(360/(Tamaño[i]+Tamaño[i]%2))
   globals()["conta"+str(i)]=0
   globals()["pos"+str(i)]=np.where(matriz==i)[0]
  for i in range(2,len(Tamaño)-1,1):
   globals()["Nelementosmax"+str(i)]=0
   for j in range(len(globals()["pos"+str(i)])):
    if j<len(globals()["pos"+str(i)])-1:
     globals()["Nelementos"+str(i)+str(j)]=len(globals()["pos"+str(i+1)][np.where((globals()["pos"+str(i+1)]>globals()["pos"+str(i)][j]) & (globals()["pos"+str(i+1)]<globals()["pos"+str(i)][j+1]))[0]])
    else:
     globals()["Nelementos"+str(i)+str(j)]=len(globals()["pos"+str(i+1)][np.where((globals()["pos"+str(i+1)]>globals()["pos"+str(i)][j]))[0]])
  
 crear_angulos(m1)
 pcentralx,pcentraly=prevenir_solape(m1,MedidaU,ancho_elipse,largo_elipse,largo_ttl)
 dwg = svgwrite.Drawing(filename='mapa_actual.svg', size=(str(2*pcentralx+10)+"px", str(2*pcentraly+10)+"px"),  debug=True)
 shapes = dwg.add(dwg.g(id='shapes', fill='red'))
 crear_lineas(m1,dwg,pcentralx,pcentraly,color_e_ttl,mm)
 crear_elipses(m1,m1con,shapes,dwg,ancho_elipse,largo_elipse)
 e0 = shapes.add(dwg.ellipse(center=(pcentralx, pcentraly), r=(largo_ttl,   largo_elipse_ttl),stroke_width=1*mm,stroke='#FFFFFF',fill=color_e_ttl))
 Escribir_hipervinculos(m1,m1hyplk,dwg,e0)
 Escribir_texto(m1,m1txt,dwg,ancho_fuente,mm)
 dwg.add(dwg.text(m1txt[0] ,insert=(pcentralx-largo_ttl/2,pcentraly+ancho_fuente),font_size=6*mm ,fill="black"))
 dwg.saveas('/home/sebastian/Mapas/Maps/static/mapa_actual.svg')


def crear_svg(M1,M1txt,M1con,M1hyplk):
 #Se convierten los arreglos en arreglos numpy
 def crear_numpyarr(M1,M1txt,M1con,M1hyplk): #Convertimos los arreglos a svg
  m1=np.array(M1)
  m1txt=np.array( M1txt)
  m1con=np.array(M1con)
  m1hyplk=np.array(M1hyplk)
  return m1,m1txt,m1con,m1hyplk

 m1,m1txt,m1con,m1hyplk=crear_numpyarr(M1,M1txt,M1con,M1hyplk)
 #Se inicializan las variables del mapa mental 
 mm=1
 entrada = 'Esternocleidomastoideo'
 ancho_fuente = 1 * mm 
 largo_msj,largo_ttl = len(entrada) * ancho_fuente,len(m1txt[0])*3*ancho_fuente 
 ancho_elipse ,largo_elipse ,largo_elipse_ttl= largo_msj, ancho_fuente * 4 ,ancho_fuente * 12
 radioxinicial ,radioyinicial= ancho_elipse / 2 , largo_elipse
 Tamaño = np.bincount(m1)
 radio_min=2*2*max(radioxinicial,radioyinicial)
 MedidaU = (Tamaño[-1] * max(ancho_elipse, largo_elipse) / (2 * np.pi) +  radio_min * len(Tamaño) + 2*largo_ttl )
 crear_elementos_svg(m1,m1txt,m1con,m1hyplk,ancho_fuente,ancho_elipse,largo_elipse,largo_elipse_ttl,largo_ttl,MedidaU,mm)
 
 


