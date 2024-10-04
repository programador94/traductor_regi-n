traduccion = {
    "JUICIOSO":"es una persona respunsable ",
    "AGUACATE":"es una fruta que en alguno paises se la conoce como palta",
    "ESFERO":"también conocido como boligrafo",
    "EH AVE MARIA PUES":"se le utiliza para expresar sorpresa"
}

word = input("escribe una palabra que no entiendas (¡con mayusculas!): ")

if word in traduccion.keys():
    print("El significado de la palabra ingresado es:",traduccion[word])
             
else:
    print("Esa palabra no se encuentra en el diccionario")
