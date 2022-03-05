from detectarIdioma import detectarIdioma, leerDiccionario

mensaje = "nochedeverano"
diccionario = "diccionario.txt"

resultado = detectarIdioma(mensaje,diccionario)
print(resultado)