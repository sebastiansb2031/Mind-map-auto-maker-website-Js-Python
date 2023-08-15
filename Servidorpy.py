from flask import Flask, render_template,request,jsonify
import Control_archivo_2 as CA
import json
globals()["editando"]=0
globals()["Mascara1"]=[1,2,3]
globals()["Mascara1_txt"]=["Titulo","Subtitulo1","Subtitulo2"]
globals()["Mascara1_txt_aux"]=["11Titulo","12Subtitulo1","13Subtitulo2"]
globals()["Hipervinculo1"]=["nulo","nulo","nulo"]
globals()["Mascaracon"]=["1","1","1"]

globals()["posaux"]=0
'''
El folder estático es el que contiene el archivo html, css y las imágenes, los scripts están en una carpeta aparte o en otro lugar
Este script permite a construcción de un sitio web sencillo usado como método de estudio
representando toda la información tanto académica como personal del usuario en un solo lugar
gracias a la integración de hipervinculos y visualizaciones en minuatura para que
pueda hacer la mayoría de acciones sin salir del sitio 
'''
app = Flask(__name__,static_folder='/home/sebastian/Mapas/Maps/static', template_folder='/home/sebastian/Mapas/Maps/') #Creamos una instancia de flask y especificamos la ruta donde buscará el archivo HTML



def crear_menu(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c):

  
  Bloques=dict()
  editando=globals()["editando"]
  if c=="1" and editando==0:
   globals()["editando"]=1 

   c="Escriba el título del mapa mental  :"
   return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  if c=="2" and editando==0:
   globals()["editando"]=2
   c="Indique el nombre del archivo,debe estar en el mismo directorio    :"
   return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  if editando==1:
    Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux=CA.editar_mapa_nuevo(c)  
    Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)
    globals()["editando"]=3   
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    return Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  if editando==2:
    Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux=CA.editar_mapa_existente(c)
    Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)
    globals()["editando"]=3   
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    return Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  if editando==3: 
   Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)
   
   for i in range(len(Mascara1_txt)):
      if Mascara1_txt_aux[i]==c:
       globals()["posaux"]=i
       i=len(Mascara1_txt)+1
   if c=="g":
    CA.guardar_txt(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux)
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques


   if c=="q":
    globals()["editando"]=0
    c= "1:Crear un nuevo mapa 2:Modificar un mapa existente q :para salir g:guardar mapa: :"
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
   for i in range(len(Mascara1_txt)):
     if Mascara1_txt_aux[i]==c:
      globals()["posaux"]=i
      i=len(Mascara1_txt)+1
   if c=="hh" :
     c="Ingrese el hipervinculo, puede ser un archivo local o un link de la web"
     
     globals()["editando"]=4
     return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
   if c=="d" :
    Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,globals()["posaux"]=CA.borrar_posicion(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,globals()["posaux"])
    Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques

   if c=="c" :
    c="Ingrese el nuevo termino a reemplazar"
    globals()["editando"]=5
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
   if c=="cc" :
    c="Ingrese el nuevo termino a reemplazar"
    globals()["editando"]=6
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
   if c=="nw":
    c="Ingrese el nuevo termino "
    globals()["editando"]=7
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
   if c=="cnw":
    c="Ingrese el nuevo termino "
    globals()["editando"]=8
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
    
   #if c0=="-1":
   if str(c)[0]=="-" or str(c)[0]=="+":
    globals()["posaux"]=globals()["posaux"]+int(c)
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)

  if editando==4:
    globals()["editando"]=3
    Hipervinculo1=CA.ingresar_hipervinculo(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,globals()["posaux"],c)
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  if editando==5:
    globals()["editando"]=3
    Mascara1_txt,Mascaracon,Mascara1_txt_aux=CA.cambiar_nodo(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,globals()["posaux"],c) 
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  if editando==6:
    globals()["editando"]=3
    Mascara1_txt,Mascaracon,Mascara1_txt_aux=CA.cambiar_conexion(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,globals()["posaux"],c)  
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  if editando==7:
    globals()["editando"]=3
    Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,globals()["posaux"]=CA.crear_nodo(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,globals()["posaux"],c)
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques

  if editando==8:  
    globals()["editando"]=3 
    Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,globals()["posaux"]=CA.crear_conexion(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,globals()["posaux"],c)
    c= str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[globals()["posaux"]])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo : nw:Nuevo conceptos  cnw:Nuevo conector c:Cambiar cc:Cambiar conector  d:Borrar texto cd:Borrar texto de conector -1:Concepto anterior :"
    Bloques=CA.organizar(Mascara1,Mascara1_txt_aux)
    return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques
  return  Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1,Mascara1_txt_aux,c,Bloques



@app.route('/', methods=['POST']) #Función de ruta que se ejecuta al haber una solicitud HTTP POST desde el HTML 
def my_form_post():
  Bloques=dict()
  c= request.form['texto']
  c=c.strip()
  globals()["Mascara1"],globals()["Mascara1_txt"],globals()["Mascaracon"],globals()["Hipervinculo1"],globals()["Mascara1_txt_aux"],c1,Bloques=crear_menu(globals()["Mascara1"],globals()["Mascara1_txt"],globals()["Mascaracon"],globals()["Hipervinculo1"],globals()["Mascara1_txt_aux"],c)
  return render_template('Inicio.html',x=str(c1),Mascara1txt=json.dumps(globals()["Mascara1_txt_aux"]), Mascara1=json.dumps(globals()["Mascara1"]),Bloques1=json.dumps(Bloques))  #Devuelve lo que se envío en el form
  
@app.route('/') #Función que se inicializa apenas se corre la app web  
def my_form():
    Bloques=dict()
    return render_template('Inicio.html', x="1:Crear un nuevo mapa 2:Modificar un mapa existente q :para salir g:guardar mapa: :",Mascara1txt=globals()["Mascara1_txt_aux"], Mascara1=json.dumps(globals()["Mascara1"]) ,Bloques1=json.dumps(Bloques))
    #return render_template('Inicio.html', x="")
  
      
if __name__ == "__main__":
    app.run(debug=True)