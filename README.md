# Sistema de Reconhecimento Facial da CPBSB6

Este é um sistema de Reconhecimento Facial por IA desenvolvido exclusivamente para apresentação no stand do SENAI DF na Campus Party Brasília, ocorrida no ano de 2024.

O objetivo da apresentação do sistema é exibir uma amostra do que será produzido no Curso de Desenvolvedor de IA. O curso, que possui um total de 400 horas de duração, fará sua estréia no SENAI DF no ano de 2024, e este será um dos vários sistemas que serão desenvolvidos pelos alunos neste curso.

## Como funciona o sistema?

Inicialmente composto por 3 algoritmos feitos na linguagem Python, o sistema foi unificado para apenas um único algoritmo Python, para facilitar a execução da demonstração do sistema.

O programa principal é executado pelo arquivo "main.py", que exibe 3 opções para o usuário:

- Capturar imagem.
- Fazer reconhecimento facial.
- Encerrar o programa.

A primeira opção é obrigatória para o usuário que ainda não possui cadastro no sistema. Ao selecioná-la, o usuário deverá informar um número de ID desejado e o seu nome. Em seguida, o algoritmo abre uma janela para a câmera do dispositivo, que irá detectar o rosto do usuário e fazer uma leitura em 3 dimensões do rosto.

Ao pressionar a letra "c", o programa irá realizar imediatamente a captura de 25 quadros de imagem do rosto do usuário, e guardá-las em um diretório do dispositivo de armazenamento da máquina, e o programa irá encerrar a câmera, retornando ao menu inicial.

Obs: para que a opção de reconhecimento facial funcione, é necessário a captura de imagens de pelo menos 2 pessoas ou mais, para o treinamento da IA do sowftware.

Caso o usuário escolha a opção de Fazer reconhecimento facial, o programa irá abrir novamente a tela da câmera, mas desta vez, ele irá fazer um breve treinamento do software, o que pode demorar alguns segundos, e em seguida, ele irá reconhecer a face do usuário e realizar a leitura dos dados que ficaram gravados durante a primeira etapa da execução de software.

## Outras observações

O sistema se encontra atualmente incompleto. Porém, realizou com sucesso sua tarefa: detectar faces e ser apresentável na Campus Party, sendo um sucesso absoluto.

A intenção é desenvolvê-lo em sua totalidade no Curso de Desenvolvedor de IA, cuja primeira turma está prevista para o segundo semestre de 2024.