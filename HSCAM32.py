import cv2

url='http://192.168.0.28/240x240.jpg'
cap = cv2.VideoCapture(url, cv2.CAP_DSHOW) # Criar objeto video de captura de video

winName = 'HSCAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

while(1):

    cap.open(url) # Antes de capturar o frame abrimos a url
    
    ret,frame = cap.read() # Carptura de frame
    
    
    #frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    #gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow(winName,frame)
    
    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break
     
cv2.destroyAllWindows()


