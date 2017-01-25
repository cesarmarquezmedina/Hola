import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector


cnx = mysql.connector.connect(user='cesarmarquez', password='CESAR_2606952_*cmarquez',
                              host='urban-srv.isavanzados.com.mx',
                              database='Scripts'
                              )
cursor=cnx.cursor()

cursor.execute('Select * from Ruta40')
df=cursor.fetchall()
cnx.close()

df=pd.DataFrame(df)
df.columns=['Ruta','Hora','X','Y','Id']

#df=pd.read_csv('Rutas_ok.csv')
#df1=df1.dropna()
#x=df[(df['Direccion']==1)&(df['Ruta']==7)][['X','Y']]



#y2=x2['X']
#x2=x2['Y']

#background=plt.imread('Map.png')
#plt.plot(x,y,linewidth=2)

#plt.scatter(x2,y2)
plt.scatter([-102.221879,-102.366247,-102.366247,-102.221879],[21.840073,21.840073,21.951886,21.951886])

#x=[21.854529]
#y=[-102.259909]
#df=df.tail(7)
#df=df.head(2)

y=df['X']
x=df['Y']


#plt.scatter(x,y)
plt.plot(x,y)

#y=x2['X']
#x=x2['Y']
#plt.plot(x,y)

#x=[21.855951] 
#y=[-102.253258]
#plt.scatter(y,x)
plt.show()#,extent=[-102.366247, -102.221879, 21.840073, 21.951886])