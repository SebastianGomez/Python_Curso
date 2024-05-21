"""Sondeo: Utilice el código de favorite_languages.py. 
• Haz una lista de las personas que deberían participar en la encuesta de 
idiomas favoritos. Incluya algunos nombres que ya están en el diccionario y 
otros que no. 
• Recorra la lista de personas que deben realizar la encuesta. Si ya han 
respondido a la encuesta, imprime un mensaje agradeciéndoles por responder. Si 
aún no han respondido a la encuesta, imprima un mensaje invitándolos a realizar 
la encuesta."""

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 'scoth': 'java',
 'willow': 'c++',
 'spyke': 'cobol',

 }


encuestados = ["jen","pedro","edward","pablo","phil","jose","willow"]

for personas in encuestados:
    if personas in favorite_languages.keys():
        print(f"gracias {personas} por contestar la encuesta")
    else:
        print(f"{personas} aun no ha completado la encuesta")

