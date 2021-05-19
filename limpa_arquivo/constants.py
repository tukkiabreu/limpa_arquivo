import os

DIRETORIOS_LIMPAR = {1: r'{0}:\schedule_server\modelos\outputs'.format("D" if os.path.isdir("D:/") else "C"),
                     2: r'{0}:\schedule_server\Arquivos'.format("D" if os.path.isdir("D:/") else "C")
                     }
