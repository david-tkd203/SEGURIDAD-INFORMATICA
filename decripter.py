import hashlib

def descifrar_vigenere(texto_cifrado, clave):
    texto_descifrado = ""
    longitud_clave = len(clave)
    
    for i in range(len(texto_cifrado)):
        caracter = texto_cifrado[i]
        if caracter.isalpha():
            caracter_clave = clave[i % longitud_clave]
            desplazamiento = ord(caracter_clave) - ord('A')
            if caracter.islower():  #Comprobar si es minuscula
                caracter_descifrado = chr(((ord(caracter) - ord('a') - desplazamiento) % 26) + ord('a'))    #se hace un ord() en bas e a 26 como las letras del abecedario
            else:
                caracter_descifrado = chr(((ord(caracter) - ord('A') - desplazamiento) % 26) + ord('A'))
            texto_descifrado += caracter_descifrado #se suma la letra cifrada al texto vacio en primera instancia
        else:
            texto_descifrado += caracter
    return texto_descifrado #retornamos la variable texto cifrado

# Leer el mensaje cifrado y el hash SHA-256 del archivo "mensajeseguro.txt"
with open("mensajeseguro.txt", "r") as archivo_entrada:  #apertura de txt en forma de lectura(read)
    lineas = archivo_entrada.readlines()    #lectura de lineas dentro del txt
    mensaje_cifrado = lineas[0].split(":")[1].strip()    #cortamos el str que esta dentro del txt
    hash_original = lineas[1].split(":")[1].strip()

# Solicitar al usuario que ingrese la clave utilizada para cifrar el mensaje
clave = "mama"

# Descifrar el mensaje cifrado
mensaje_descifrado = descifrar_vigenere(mensaje_cifrado, clave)

# Calcular el hash SHA-256 del mensaje descifrado
hash_obj = hashlib.sha256(mensaje_descifrado.encode())
hash_calculado = hash_obj.hexdigest()

# Verificar si el hash calculado coincide con el hash original
if hash_calculado == hash_original:
    print("El mensaje no ha sido alterado.")
    print("Mensaje descifrado:", mensaje_descifrado)
else:
    print("El mensaje ha sido alterado o la clave es incorrecta.")
