from sqlite3 import PARSE_COLNAMES


frase = input("Introduce una frase: ")
frase_invertida = []
for palabra in frase.split():
    frase_invertida.append(palabra)

string_final = ""

for i in range(len(frase_invertida)-1, -1, -1):
    string_final += frase_invertida[i]

print(string_final)