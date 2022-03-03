
import random
clientes = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
diccionario_descuentos = {cliente:random.randint(1,100) for cliente in clientes}
print(diccionario_descuentos)