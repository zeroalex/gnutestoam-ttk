from sys import platform
from cx_Freeze import setup, Executable


base = None
if platform == 'win32':
    base = 'Win32Gui'

setup(
    name='Abil Azul - Gerenciar Termos de Notificação de Penalidade',
    version='1.3',
    description='Ferramenta de uso exclusivo Ceagesp - para Gerenciar Termos de Notificação de Penalidade',
    options={
        'build_exe': {
            'includes': ['tkinter' ]
        }
    },
    executables=[
        Executable('main.py', base=base)
    ],
)

