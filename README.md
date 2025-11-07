Ejemplo simplificado del cifrado AES

Este programa muestra de forma sencilla cómo funciona el proceso básico de cifrado AES (Advanced Encryption Standard).

El texto se convierte en una matriz de 4x4 bytes (estado) y pasa por las siguientes transformaciones:

1. SubBytes: sustituye cada byte usando una tabla fija llamada S-Box, que introduce confusión en los datos.


2. ShiftRows: desplaza las filas de la matriz hacia la izquierda según su posición, mezclando los bytes.


3. MixColumns: combina los valores de cada columna mediante operaciones matemáticas en el campo GF(2⁸), aumentando la difusión.


4. AddRoundKey: aplica una operación XOR entre el bloque resultante y una clave de igual tamaño.
