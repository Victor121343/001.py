# Pregunta diferentes datos, aunque no esten validados.

# Importa el módulo requerido para usar datos de tipo Date.
import datetime
# Los datos se tienen, se preguntan o se calculan
# Notación húngara utilizada:
#   str   string
#   i     int
#   f     float
#   dt    date


def main():
 # Los datos str solo se preguntan y procesan sin intermediación.
 strDato = input("Dame un dato string: ")
 # Los datos numéricos se preguntan por intermediación.
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)
 # Los datos date (fecha) se preguntan por intermediación.
 _dtDato = input("fecha yyyy/mm/dd: ")

 año=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 print(año)
 print(mes)
 print(dia)

 dtDato = datetime.datetime(int(año), int(mes), int(dia))

 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))