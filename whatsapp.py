import pywhatkit as pw
from pandas import read_csv
from datetime import datetime, timedelta

number = read_csv('Listanumeros.csv', header=0)

data = number.values

for j in range(len(data)):
    day = datetime.now()
    new_day = day + timedelta(minutes=1)
    mensaje = "Hola "+data[j,0]+" buenas tardes como estas?"
    numero = "+"+str(data[j,1])
    pw.sendwhatmsg(numero,mensaje, day.hour,new_day.minute)
