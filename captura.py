# importa as bibliotecas OpenCV e NumPy
import cv2
import numpy as np

# classificadores
classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classificador_olho = cv2.CascadeClassifier('haarcascade_eye.xml')

# camera
camera = cv2.VideoCapture(0)

# número de amostras por usuário
amostra = 1
numero_amostras = 25

# recebe o id do usuário
id = input('Digite o ID do usuário: ')

# define o tamanho das imagens
largura = 220
altura = 220

# mensagem indicando as capturas
print('Capturando as faces...')

# loop das capturas
while True:
    conectado, imagem = camera.read() # inicializa a camera
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # gera uma imagem em escala cinza
    print(np.average(imagem_cinza)) # exibe em números as escalas de cinzas da imagem
    faces_detectadas = classificador.detectMultiScale(imagem_cinza, scaleFactor=1.5, minSize=(150,150)) # detecta as faces

    # identifica a geometria das faces
    for (x, y, l, a) in faces_detectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        regiao = imagem[y:y + a, x:x + l]
        regiao_cinza_olho =cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhos_detectados = classificador_olho.detectMultiScale(regiao_cinza_olho)

        # identifica a geometria dos olhos das faces
        for (ox, oy, ol, oa) in olhos_detectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

            # salva as imagens em um arquivo do sistema ao apertar a letra c
            if cv2.waitKey(1) & 0xFF == ord('c'):
                if np.average(imagem_cinza) > 110:
                    imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + l], (largura, altura))
                    cv2.imwrite('fotos/pessoa.' + str(id) + '.' + str(amostra) + '.jpg', imagem_face)
                    print('[foto] ' + str(amostra) + 'capturada com sucesso]')
                    amostra += 1

    cv2.imshow('Face', imagem)
    cv2.waitKey(1)

    # encerra o loop caso o número de fotos do usuário tenha chegado a 25
    if (amostra >= numero_amostras + 1):
        print('Faces capturadas com sucesso.')
        break
    elif cv2.waitKey(1) == ord('q'):
        print('Programa encerrado.')
        break

# encerra a captura
camera.release()
cv2.destroyAllWindows()