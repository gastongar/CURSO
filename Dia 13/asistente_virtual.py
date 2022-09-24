import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Opciones de voz / Idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


# Escuchar nuestro Mic y Devolver audio como texto
def transformar_audio_en_texto():

    # Almacenar recognizer en variable
    r= sr.Recognizer()

    #configurar el mic
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        #Informar start grabacion
        print("ya puedes hablar")

        #Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que pudo ingresa
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso que no comprenda
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print(" Ups, no entendí")
            #devolver error
            return "sigo esperando"

        # en caso que pueda resolver el pedido
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print(" Ups, no hay servicio")
            # devolver error
            return "sigo esperando"

        # Error inesperado
        except:
            # prueba de que no comprendio el audio
            print(" Ups, algo ha salido mal")
            # devolver error
            return "sigo esperando"

# Funcion para que el asistente hable
def hablar(mensaje):
    #encender el motor de  pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#Informa dia de la semana
def pedir_dia():
    #crear variable dia
    dia = datetime.date.today()
    print(dia)

    #dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)
    #diccionario dias de la semana
    calendario = { 0: 'Lunes',
                   1: 'Martes',
                   2: 'Miércoles',
                   3: 'Jueves',
                   4: 'Viernes',
                   5: 'Sábado',
                   6: 'Domingo'}
    # Decir dia de la semana
    hablar(f'hoy es {calendario[dia_semana]}')

# informar la Hora
def pedir_hora():

    # Crear variable hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)
    #decir hora
    hablar(hora)

#saludo Inicial
def saludo_inical():
    # crea variable con datos hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buneas Noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas Tardes'




    #decir saludo
    hablar (f' {momento}, soy Lucía, tu asistente personal, Por favor, dime en que te puedo ayudar')



# Funcion Central del Asistente

def pedir_cosas():
    #activar saludo inicial
    saludo_inical()

    #variable de corte
    comenzar = True
    #lopp Central
    while comenzar:
        #acticar el micro y guardar pedido
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abrien Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar(' Claro, estoy en eso')
            webbrowser.open('https://www.google.com.ar')
            continue
        elif 'qué día es' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en Wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy buscando eso en Internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado:')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya empiezo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL',}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break


pedir_cosas()




























