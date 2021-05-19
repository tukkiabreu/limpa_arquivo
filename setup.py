from setuptools import setup, find_packages
import limpa_arquivo

setup(
    name='limpa_arquivo',
    version=limpa_arquivo.__version__,

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'limpar_arquivos_antigos=limpa_arquivo.main:executar_limpeza'
        ]
    }
)