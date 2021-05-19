from limpa_arquivo.func_limpar import limpar_arquivos_antigos
from logs_manager.logs_manager import get_logs

# @get_logs.logger
def executar_limpeza():
    print("\nLimpando arquivos antigos dos diretórios...\n")
    limpar_arquivos_antigos()
    print("Limpeza finalizada!\n")



if __name__ == '__main__':
    executar_limpeza()