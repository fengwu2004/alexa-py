from cx_Freeze import setup, Executable
import sys

base = None

executables = [
    
    Executable('start.py')
]

options = {
        'build_exe': {
        'includes': [
            'main',
        ],
        'path': sys.path,
        'packages': ['encodings', 'asyncio']
    }
}

setup(
    name = 'alexa-py',
    version = '0.1',
    description = 'Sample cx_Freeze wxPython script',
    executables = executables,
    options = options
    )