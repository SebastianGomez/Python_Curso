""" Envío de mensajes: Comience con una copia del programa dado 

mensajes = ["Hola","como","estan","todos","ustedes?"]

def show_messages(mensajes):
    for mensaje in mensajes:
        print(mensaje)

show_messages(mensajes)


Escriba una función llamada send_messages() que imprima cada mensaje de texto y 
mueva cada mensaje a una nueva lista llamada sent_messages a medida que se imprime. 
Después de llamar a la función, imprima ambas listas para asegurarse de que los 
mensajes se hayan movido correctamente."""

mensajes = ["Hola","como","estan","todos","ustedes?"]
sent_messages = []

def send_messages(mensajes):
    while mensajes:
        mensaje = mensajes.pop()
        print(mensaje)
        sent_messages.append(mensaje)


send_messages(mensajes[:]) # no modifica la lista original
#send_messages(mensajes) # modifica la lista original
print(mensajes)
print(sent_messages)
sent_messages.reverse()
print(sent_messages)


