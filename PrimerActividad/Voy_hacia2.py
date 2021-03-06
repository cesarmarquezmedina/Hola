import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from time import time

tiempo_ini=time()

def distancia(x,x1,y,y1):
    a=(x-x1)**2
    b=(y-y1)**2
    c=((a+b)**.5)*100000
    return c

def Checar(df1,df2):
    for indexx in range(min(df1.index.values),max(df1.index.values)):
        for indexy in range(min(df2.index.values),max(df2.index.values)):
            aprox=distancia(df1['X'][indexx],df2['X'][indexy],df1['Y'][indexx],df2['Y'][indexy])
            if (aprox<100):
                return(True,indexx,indexy)
                
    return (False,0,0)
                
            
    
df=pd.read_csv('Rutas_ok.csv')

Rut=[10,7,20,40,1,2]

salidax=[21.864067]
saliday=[-102.242734]

llegadax=[21.925291]
llegaday=[-102.298139]

num=0

dis=[]
dis2=[]
RutaSalida=[]
RutaSalida2=[]
RutaLlegada=[]
RutaLlegada2=[]

for index in range(df.shape[0]):
    dis.append(distancia(df['X'][index],salidax[num],df['Y'][index],saliday[num]))
    
    dis2.append(distancia(df['X'][index],llegadax[0],df['Y'][index],llegaday[0]))

df['Distancia']=pd.DataFrame(dis)
df['Distancia2']=pd.DataFrame(dis2)

for index in range(len(Rut)):
    aux=min(df[(df['Ruta']==Rut[index])&(df['Direccion']==1)]['Distancia'])
    aux2=min(df[(df['Ruta']==Rut[index])&(df['Direccion']==2)]['Distancia'])
    
    aux3=min(df[(df['Ruta']==Rut[index])&(df['Direccion']==1)]['Distancia2'])
    aux4=min(df[(df['Ruta']==Rut[index])&(df['Direccion']==2)]['Distancia2'])
    
    if(aux<100):
        RutaSalida.append(Rut[index])
    if(aux2<100):
        RutaSalida2.append(Rut[index])
        
    if(aux3<100):
        RutaLlegada.append(Rut[index])
    if(aux4<100):
        RutaLlegada2.append(Rut[index])
        
MismaRuta=False
TomarRuta=[]
hacia=[]

for index in range(len(RutaSalida)):
    for index2 in range(len(RutaLlegada)):
        if(RutaSalida[index]==RutaLlegada[index2]):
            MismaRuta=True
            TomarRuta.append(RutaSalida[index])
            hacia.append(1)
            
for index in range(len(RutaSalida2)):
    for index2 in range(len(RutaLlegada2)):
        if(RutaSalida2[index]==RutaLlegada2[index2]):
            MismaRuta=True
            TomarRuta.append(RutaSalida2[index])
            hacia.append(2)
                
if(MismaRuta):
    for index in range(len(TomarRuta)):
        aux=min(df[(df['Ruta']==TomarRuta[index])&(df['Direccion']==hacia[index])]['Distancia'])
        aux2=min(df[(df['Ruta']==TomarRuta[index])&(df['Direccion']==hacia[index])]['Distancia2'])
        num1=df[(df['Distancia']==aux)&(df['Ruta']==TomarRuta[index])].index.values[0]
        num2=df[(df['Distancia2']==aux)&(df['Ruta']==TomarRuta[index])].index.values[0]
        if(num1<num2):
            print('Tomar Ruta')
            print(TomarRuta[index])
            plt.plot(df['Y'][num1:num2+1],df['X'][num1:num2+1])

else:
    
    #Ruta Salida1
    for index in range(len(RutaSalida)):
        xs=df[(df['Ruta']==RutaSalida[index])&(df['Direccion']==1)]
              
        aux=min(df[(df['Ruta']==RutaSalida[index])&(df['Direccion']==1)]['Distancia'])
        num1=df[(df['Ruta']==RutaSalida[index])&(df['Distancia']==aux)].index.values[0]
        
        
        for index2 in range(len(RutaLlegada)):
            xll=df[(df['Ruta']==RutaLlegada[index2])&(df['Direccion']==1)]
                        
            aux2=min(df[(df['Ruta']==RutaLlegada[index2])&(df['Direccion']==1)]['Distancia2'])
            num2=df[(df['Ruta']==RutaLlegada[index2])&(df['Distancia2']==aux2)].index.values[0]
                                
            ok,index3,index4=Checar(xs,xll)
                        
            if((ok)&(num1<index3)&(index4<num2)):
                plt.plot(df['Y'][num1:index3+1],df['X'][num1:index3+1])
                plt.plot(df['Y'][index4:num2+1],df['X'][index4:num2+1])
                plt.scatter(df['Y'][index4],df['X'][index4],color=(1,0,0))
                break
            
        for index2 in range(len(RutaLlegada2)):
            xll=df[(df['Ruta']==RutaLlegada2[index2])&(df['Direccion']==2)]
                        
            aux2=min(df[(df['Ruta']==RutaLlegada2[index2])&(df['Direccion']==2)]['Distancia2'])
            num2=df[(df['Ruta']==RutaLlegada2[index2])&(df['Distancia2']==aux2)].index.values[0]
                                
            ok,index3,index4=Checar(xs,xll)
                        
            if((ok)&(num1<index3)&(index4<num2)):
                plt.plot(df['Y'][num1:index3+1],df['X'][num1:index3+1])
                plt.plot(df['Y'][index4:num2+1],df['X'][index4:num2+1])
                plt.scatter(df['Y'][index4],df['X'][index4],color=(1,0,0))
                break
    #Ruta Salida2
    for index in range(len(RutaSalida2)):
        xs=df[(df['Ruta']==RutaSalida2[index])&(df['Direccion']==2)]
              
        aux=min(df[(df['Ruta']==RutaSalida2[index])&(df['Direccion']==2)]['Distancia'])
        num1=df[(df['Ruta']==RutaSalida2[index])&(df['Distancia']==aux)].index.values[0]
        
        
        for index2 in range(len(RutaLlegada)):
            xll=df[(df['Ruta']==RutaLlegada[index2])&(df['Direccion']==1)]
                        
            aux2=min(df[(df['Ruta']==RutaLlegada[index2])&(df['Direccion']==1)]['Distancia2'])
            num2=df[(df['Ruta']==RutaLlegada[index2])&(df['Distancia2']==aux2)].index.values[0]
                                
            ok,index3,index4=Checar(xs,xll)
                        
            if((ok)&(num1<index3)&(index4<num2)):
                plt.plot(df['Y'][num1:index3+1],df['X'][num1:index3+1])
                plt.plot(df['Y'][index4:num2+1],df['X'][index4:num2+1])
                plt.scatter(df['Y'][index4],df['X'][index4],color=(1,0,0))
                break
            
        for index2 in range(len(RutaLlegada2)):
            xll=df[(df['Ruta']==RutaLlegada2[index2])&(df['Direccion']==2)]
                        
            aux2=min(df[(df['Ruta']==RutaLlegada2[index2])&(df['Direccion']==2)]['Distancia2'])
            num2=df[(df['Ruta']==RutaLlegada2[index2])&(df['Distancia2']==aux2)].index.values[0]
                                
            ok,index3,index4=Checar(xs,xll)
                        
            if((ok)&(num1<index3)&(index4<num2)):
                plt.plot(df['Y'][num1:index3+1],df['X'][num1:index3+1])
                plt.plot(df['Y'][index4:num2+1],df['X'][index4:num2+1])
                plt.scatter(df['Y'][index4],df['X'][index4],color=(1,0,0))
                break
                            
#plt.scatter([-102.221879,-102.366247,-102.366247,-102.221879],[21.840073,21.840073,21.951886,21.951886])

plt.scatter(saliday,salidax)
plt.scatter(llegaday,llegadax,color=(0,1,0))

plt.show()

tiempo_final=time()

print((tiempo_final-tiempo_ini))
        
        
