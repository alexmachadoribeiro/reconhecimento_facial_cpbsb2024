# importa as bibliotecas
import cv2
import os
import numpy as np

# função captura
def captura(largura, altura):
    # classificadores
    classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    classificador_olho = cv2.CascadeClassifier('haarcascade_eye.xml')

    # camera
    camera = cv2.VideoCapture(0)

    # número de amostras por usuário
    amostra = 1
    numero_amostras = 25

    # recebe o id e o nome do usuário
    id = input('Digite o ID do usuário: ')
    nome = input('Informe o nome do usuário: ')

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
            regiao_cinza_olho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
            olhos_detectados = classificador_olho.detectMultiScale(regiao_cinza_olho)

            # identifica a geometria dos olhos das faces
            for (ox, oy, ol, oa) in olhos_detectados:
                cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

                # salva as imagens em um arquivo do sistema ao apertar a letra c
                if cv2.waitKey(1) & 0xFF == ord('c'):
                    if np.average(imagem_cinza) > 110:
                        while amostra <= numero_amostras:
                            imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + l], (largura, altura))
                            cv2.imwrite(f'fotos/pessoa.{str(id)}.{str(amostra)}.{nome}.jpg', imagem_face)
                            print(f'[foto] {str(amostra)} de {nome} capturada com sucesso]')
                            amostra += 1

        cv2.imshow('Detectar faces', imagem)
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
    # fim de função

# função que lê as fotos salvas no diretório durante a captura e guarda os dados em lista
def get_imagem_com_id():
    caminhos =[os.path.join('fotos', f) for f in os.listdir('fotos')]
    faces = []
    ids = []

    for caminho_imagem in caminhos:
        imagem_face = cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminho_imagem)[-1].split('.')[1])
        ids.append(id)
        faces.append(imagem_face)

    # retorno da função
    return np.array(ids), faces

# função de treinamento
def treinamento():
    # cria os elementos de reconhecimento necessários
    eigenface = cv2.face.EigenFaceRecognizer_create()
    fisherface = cv2.face.FisherFaceRecognizer_create()
    lbph = cv2.face.LBPHFaceRecognizer_create()

    # executa a função e recebe as listas com os dados
    ids, faces = get_imagem_com_id()

    # treina o programa
    print('Treinando...')
    eigenface.train(faces, ids)
    eigenface.write('classificadorEigen.yml')

    fisherface.train(faces, ids)
    fisherface.write('classificadorFisher.yml')

    lbph.train(faces, ids)
    lbph.write('classificadorLBPH.yml')

    # finaliza o treinamento
    print('Treinamento realizado.')
    # fim de função

# função de reconhecimento facial
def reconhecedor_eigenfaces(largura, altura):
    # detecta as faces
    detector_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    reconhecedor = cv2.face.EigenFaceRecognizer_create()
    reconhecedor.read('classificadorEigen.yml')
    fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL

    # lê a camera
    camera = cv2.VideoCapture(0)

    # loop do reconhecimento facial
    while True:
        conectado, imagem = camera.read()
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        faces_detectadas = detector_face.detectMultiScale(imagem_cinza, scaleFactor=1.5, minSize=(30,30))

        # identifica as faces
        for (x, y, l, a) in faces_detectadas:
            imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + l], (largura, altura))
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
            id, confianca = reconhecedor.predict(imagem_face)
            cv2.putText(imagem, str(id),(x,y + (a + 30)), fonte, 2, (0, 0, 255))

        # para o reconhecimento ao apertar q
        cv2.imshow('Reconhecer faces', imagem)
        if cv2.waitKey(1) == ord('q'):
            break

    # encerra o programa
    camera.release()
    cv2.destroyAllWindows()
    # fim de função

if __name__ == '__main__':
    # define o tamanho da camera
    largura = 220
    altura = 220

    while True:
        # opções
        print(f'\n{'-'*20} RECONHECIMENTO FACIAL {'-'*20}\n')
        print('Escolha uma opção:\n')
        print('1 - Capturar imagem.')
        print('2 - Fazer reconhecimento facial.')
        print('3 - Encerrar programa.\n')

        # opção do usuário
        opcao = input('Opção escolhida: ')

        if opcao == '1':
            captura(largura, altura)
            continue
        elif opcao == '2':
            treinamento()
            reconhecedor_eigenfaces(largura, altura)
            continue
        elif opcao == '3':
            print('Programa encerrado.')
            break
        else:
            print('Opção inválida.')
            continue