import speech_recognition as sr

#Cria reconhecedor
r = sr.Recognizer()

#Abri o microfone para captura de audio

with sr.Microphone() as source:
    audio = r.listen(source) # define o microfone como audio

    print(r.recognize_google(audio, language='pt'))