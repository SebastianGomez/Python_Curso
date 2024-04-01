# Etapas de la vida: 
# Escribe una cadena if-elif-else que determine la etapa de la vida de una persona. 
# Establezca un valor para la variable edad y, a continuación: 
# • Si la persona tiene menos de 2 años, imprima un mensaje que indique que la persona es un bebé. 
# • Si la persona tiene al menos 2 años de edad pero menos de 4, imprima un mensaje que indique que la persona 
# es un niño pequeño. 
# • Si la persona tiene al menos 4 años de edad pero menos de 13, imprima un mensaje que indique que la persona
# es un niño. 
# • Si la persona tiene al menos 13 años de edad pero menos de 20, imprima un mensaje de que la persona
# es un adolescente. 
# • Si la persona tiene al menos 20 años de edad pero menos de 65, imprima un mensaje de que la persona
# es un adulto. 
# • Si la persona tiene 65 años o más, escriba un mensaje que indique que la persona es un anciano

edad = 65

if edad<2:
    print("La persona es un bebé")
elif edad<4:
    print("La persona es un niño pequeño")
elif edad<13:
    print("La persona es un niño")
elif edad<20:
    print("La persona es un adolescente")
elif edad<65:
    print("La persona es un adulto")
else:
    print("La persona es un anciano")
