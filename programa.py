from os import system
from urllib.request import urlopen
import ssl
import json
from windowstoast import Toast

notificationID = '-12061987'

t = Toast('Sunat comprobantes', notificationID, Duration='Long')
t.add_image('sunat.jpg', 'logo', 'square')
#t.add_image('paisaje.png', None, 'square') #pone un cuadro largo de imágen


system('cls')

url="https://infocatsoluciones.com/"

context = ssl._create_unverified_context()

response = urlopen(url, context=context)

jData= json.loads(response.read())

print(jData)

if int( jData['cantidad'] ) == 0 :
	print('no hay comprobantes')
	t.add_text('No hay comprobantes por enviar')

else:
	print('hay comprobates')

	if jData['cantidad']==1:
		letra = 'Hay 1 comprobante'
	else:
		letra = 'Existen '+ jData['cantidad'] + 'comprobantes'
	
	t.add_text(letra)
	if int(jData['diferencia'])<=1:
		subCaso= "Antigüedad de 1 día"
	else:
		subCaso= "Antigüedad de " + jData['diferencia'] + ' días' 

	ultimo = 'Último comprobante {}'.format( jData['comprobante'])
	subCaso += "\n"+ultimo

	#t.add_text(subCaso)
	t.add_text(subCaso, attribution=True)
	


t.show()


sleep(20)