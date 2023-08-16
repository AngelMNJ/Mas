# Este fragmento nos permite leer la totalidad de un archivo de texto

f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()
# Y así es como podemos reescribir la totalidad de un archivo de texto
f = open('text.txt', 'w+', encoding='utf-8')
text = input('¿Que deseas añadir?: ')
f.write(text)
f.close()
# Y he aquí una versión más corta
with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.read())
