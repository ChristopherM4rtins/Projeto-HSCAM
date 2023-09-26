import cv2
import mediapipe as mp
import RPi.GPIO as GPIO
import time

url = "http://192.168.0.26/400x296.jpg"
cap = cv2.VideoCapture(url, cv2.CAP_DSHOW)

winName = 'HSCAM'
#cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

detecion_face = mp.solutions.face_detection
reconhecedor_faces = detecion_face.FaceDetection()
desenho = mp.solutions.drawing_utils


channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def led_on(pin):
    GPIO.output(pin, GPIO.HIGH) #Liga o Led

def led_off(pin):
    GPIO.output(pin, GPIO.LOW)  #Desliga o Led

while True:
    cap.open(url)
    verificador, frame = cap.read()

    if not verificador:
        break

    lista_rotos =  reconhecedor_faces.process(frame)

    if lista_rotos.detections:
        for rosto in lista_rotos.detections:
            desenho.draw_detection(frame, rosto)
            print("Face Detectada")
            led_on(channel)
            time.sleep(30)  #tempo em que o led ficara ligado.
            led_off(channel)

    #cv2.imshow(winName, frame)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break

GPIO.cleanup()
cv2.destroyAllWindows()

