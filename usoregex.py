# Da la opcion de preguntar un dato hasta que este sea correcto

# Importa el módulo requerido para usar Regular Expressions
import re

def main():
  # Infinty Loop: se corre hasta que se presenta un break
  # este seguira preguntando el dato hasta que se cumpla con el
  # requisito
  while True:
    strRFC = input("Dame el RFC: ")
    coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
    if (coincide):
      print("RFC Correcto!")
      break
    else:
      print("RFC incorrecto. Intenta de nuevo.")