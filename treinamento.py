# importa as bibliotecas
import cv2
import os
import numpy as np

# cria os elementos de reconhecimento necessários
eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

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

    return np.array(ids), faces

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