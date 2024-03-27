# importa a OpenCV
import cv2

# detecta as faces
detector_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read('classificadorEigen.yml')
fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL

# define o tamanho da camera
largura = 220
altura = 220

# lê a camera
camera = cv2.VideoCapture(0)

# loop do reconhecimento facial
while True:
    conectado, imagem =camera.read()
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces_detectadas = detector_face.detectMultiScale(imagem_cinza, scaleFactor=1.5, minSize=(30,30))

    # identifica as faces
    for (x, y, l, a) in faces_detectadas:
        imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + l], (largura, altura))
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        id, confianca = reconhecedor.predict(imagem_face)
        cv2.putText(imagem, str(id), (x,y + (a + 30)), fonte, 2, (0, 0, 255))

    # para o reconhecimento ao apertar q
    cv2.imshow('Face', imagem)
    if cv2.waitKey(1) == ord('q'):
        break

# encerra o programa
camera.release()
cv2.destroyAllWindows()