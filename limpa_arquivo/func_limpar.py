from limpa_arquivo import constants as c
import os
import shutil
import traceback


def limpar_arquivos_antigos():
    for dir in c.DIRETORIOS_LIMPAR.values():
        try:
            shutil.rmtree(dir)
            os.makedirs(dir)
            print(f"Limpo com suceso! {dir}\n")
        except:
            print(f"ERRO: {dir}\n", traceback.format_exc())


#se houver outras coisas para limpar as funçoes serão adicionadas aqui e chamadas no main