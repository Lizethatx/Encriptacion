from cryptography.fernet import Fernet
import os, sys, time

menu = True

while menu:
    print('-----MENU-----\n1.- Cifrar\n2.- Descifrar\n0.- Salir\n')
    val = int(input('Elija una opcion: '))

    if val == 1:
        os.system('cls')
        print('\t\t\t *Cifrar* \n\n')

        # inicia cifrado cesar
        archivo = open('texto.txt', 'w')
        texto = input('Texto a cifrar: ')

        if texto == texto.upper():
            abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        else:
            abc = 'abcdefghijklmnñopqrstuvwxyz'

        d = 1
        cif = ''

        for i in texto:
            if i in abc:
                cif += abc[(abc.index(i) + d) % (len(abc))]
            else:
                cif += i
        # lo escribe en el archivo
        archivo.write(cif)
        archivo.close()


        # inicia cifrado AES en el archivo
        def genera_clave():
            clave = Fernet.generate_key()
            with open("clave.key", "wb") as archivo_clave:
                archivo_clave.write(clave)


        def cargar_clave():
            return open("clave.key", "rb").read()


        def encriptar(nom_archivo, clave):
            f = Fernet(clave)
            with open(nom_archivo, "rb") as file:
                archivo_info = file.read()
            encrypted_data = f.encrypt(archivo_info)
            with open(nom_archivo, "wb") as file:
                file.write(encrypted_data)


        genera_clave()
        clave = cargar_clave()
        nom_archivo = "texto.txt"
        f = Fernet(clave)

        # encripta el texto en cifrado cesar
        encriptar(nom_archivo, clave)

        print('Texto cifrado con éxito!')

        os.system('pause')
        os.system('cls')

    elif val == 2:
        os.system('cls')
        print('\t\t\t *Descifrar*\n\n\n\n')


        # se desencripta el archivo con cifrado AES y escribe el resultado del cifrado cesar
        def desencriptar(nom_archivo, clave):
            f = Fernet(clave)
            with open(nom_archivo, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(nom_archivo, "wb") as file:
                file.write(decrypted_data)


        nom_archivo = "texto.txt"
        desencriptar(nom_archivo, clave)

        # se abre el archivo que ya fue desencriptado en cesar
        archivo = open('texto.txt', 'r')
        originalText = archivo.read()

        if originalText == originalText.upper():
            abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        else:
            abc = 'abcdefghijklmnñopqrstuvwxyz'

        d = 1
        dec = ''

        for i in originalText:
            if i in abc:
                dec += abc[(abc.index(i) - d % (len(abc)))]
            else:
                dec += i

        archivo.close()
        archivo = open('textodescifrado.txt', 'w')
        archivo.write(dec)
        archivo.close()
        print('Has descifrado el texto!')
        os.system('pause')
        os.system('cls')

    elif val == 0:
        menu == False
        break
