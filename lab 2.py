import hashlib

def cifrado_vigenere(texto, clave):  #Funcion Vigenere
    texto_cifrado = ""
    longitud_clave = len(clave)
    for i in range(len(texto)):
        letra = texto[i]
        if letra.isalpha():
            letra_clave = clave[i % longitud_clave]
            desplazamiento = ord(letra_clave) - ord('A')
            if letra.islower():  #Comprobar si es minuscula
                letra_cifrado = chr(((ord(letra) - ord('a') + desplazamiento) % 26) + ord('a'))  #se hace un ord() en bas e a 26 como las letras del abecedario
            else:
                letra_cifrado = chr(((ord(letra) - ord('A') + desplazamiento) % 26) + ord('A'))
            texto_cifrado += letra_cifrado  #se suma la letra cifrada al texto vacio en primera instancia
        else:
            texto_cifrado += letra
    
    return texto_cifrado     #retornamos la variable texto cifrado

# Solicitar al usuario que ingrese una clave
clave = "papa"

with open("mensajeentrada.txt", "r") as mensaje:  #apertura de txt en forma de lectura(read)
    mensaje_original = mensaje.read().strip()     #cortamos el str que esta dentro del txt

# Cifrar el mensaje con la clave ingresada
cifrado = cifrado_vigenere(mensaje_original, clave)   #llamada a la funcion vigenere

# Calcular el hash SHA-256 del mensaje cifrado
hash_obj = hashlib.sha256(mensaje_original.encode())   #transforma el texto en un hash
hash_result = hash_obj.hexdigest()    #transforma el hash en un texto legile

# Guardar el mensaje cifrado y el hash en un archivo
with open("decripter/mensajeseguro.txt", "w") as output_file:
    output_file.write(f"Mensaje cifrado: {cifrado}\n")    #escritura del contenido de cifrado
    output_file.write(f"Hash SHA-256: {hash_result}\n")

# Salida de datos
print("Mensaje cifrado:", cifrado)
print("Hash SHA-256:", hash_result)

