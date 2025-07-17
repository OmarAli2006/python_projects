import speech_recognition as sr
import keyboard
import os

def listar_dispositivos():
    dispositivos = sr.Microphone.list_microphone_names()
    for index, name in enumerate(dispositivos):
        print(f"{index}: {name}")

def SpeechToText(device_index=None):
    Ai = sr.Recognizer()
    with sr.Microphone(device_index=device_index) as source:
        print("Hablando... Presiona 'q' para detener.")
        listening = Ai.listen(source, phrase_time_limit=10)

        try:
            command = Ai.recognize_google(listening, language='es-ES')
            print(f"Haz dicho: {command}")

            with open("transcripcion.txt", "a", encoding="utf-8") as file:
                file.write(command + "\n")
            
        except sr.UnknownValueError:
            print("No se pudo entender el audio, intentalo de nuevo.")

print("Lista de dispositivos de audio disponibles:")
listar_dispositivos()

# Clear the transcription file at the beginning
with open("transcripcion.txt", "w", encoding="utf-8") as file:
    file.write("")

while True:
    try:
        indice_microfono = int(input("Selecciona el índice del micrófono que deseas usar: "))
        if indice_microfono < 0 or indice_microfono >= len(sr.Microphone.list_microphone_names()):
            print("Índice de micrófono inválido. Por favor, selecciona un índice de la lista.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")

print("Presiona 'q' para detener la grabación.")
while True:
    if keyboard.is_pressed('q'):
        print("Grabación detenida.")
        break
    else:
        SpeechToText(device_index=indice_microfono)