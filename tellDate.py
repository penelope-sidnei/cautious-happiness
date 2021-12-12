#print current date and time
import datetime
data=datetime.date.today()

print("Dia: ",data)
print("\n")
hora=datetime.datetime.now()
print("Dia e hora:")
print(hora.strftime("%Y-%m-%d %H:%M:%S"))