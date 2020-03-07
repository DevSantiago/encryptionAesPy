#-*- coding: utf-8 -*-

from Crypto.Cipher import AES
from base64 import b64encode
import Padding
import hashlib
import sys
import binascii


val = '1121941866'
password = 'Claro-Firebase2019*'
ival = 10


plaintext = str(val) #parseo la cadena de int a str.

def encrypt(plaintext,key, mode): #Función para encriptar los datos donde recibimos los parámentros del constructor.
	encobj = AES.new(key,mode) #Una vez recibidos los parámentros por el costructor, se recoge el key, modo y se le asigna a la variable.
	return(encobj.encrypt(plaintext)) #Devolvemos el resultado del cifrado.

def decrypt(ciphertext,key, mode): #Función para encriptar los datos donde recibimos los parámentros del constructor.
	encobj = AES.new(key,mode) #Una vez recibidos los parámentros por el costructor, se recoge el key, modo y se le asigna a la variable.
	return(encobj.decrypt(ciphertext)) #Devolvemos el resultado del cifrado.


key = hashlib.sha256(password).digest() #Hasheamos la constraseña con sha-256, con la función digest en binario.

iv = hex(ival)[2:8].zfill(16) #Convierte el valor ival a hexadecimal, tomamos los caráracteres incluyendo el 2 caracter y excluyendo el 8 caracter,
							  #luego se rellena de 0 la cadena hasta completar 16 carácteres.



print("IV: "+iv)


plaintext = Padding.appendPadding(plaintext, blocksize = Padding.AES_blocksize, mode=0) #Rellenamos el texto a cifrar con el bloque de AES.
print("Input data (CMS): " + bytearray(plaintext)) #Nos devuelve una matriz de bytes.

ciphertext = encrypt(plaintext, key, AES.MODE_ECB) #Llamamos la función de encrypt y le pasamos por constructor, el texto a cifrar, la llave del cifrado y
												   #el modo de cifrado en AES (Hay varios tipos de cifrados para AES.)

print("Cipher (ECB): " + bytearray(b64encode(ciphertext))) #Volvemos a obtener la matriz de bytes del texto ya cifrado pero con formato base64.

plaintext = decrypt(ciphertext, key, AES.MODE_ECB) #Llamamos la función de descifrado y le pasamos por constructor, el texto cifrado, la llave del cifrado y
												   #el modo de cifrado en AES(Hay varios tipos de cifrados para AES.)
plaintext = Padding.removePadding(plaintext, mode = 0) #Se elimina el relleno de bloques de AES y se elimina el modo de cifrado.
print("  decrypt: " + plaintext)
