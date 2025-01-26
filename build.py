import PyInstaller.__main__
import os

# Get the directory containing build.py
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'password_generator.py',
    '--name=Password_Generator',
    '--onefile',
    '--windowed',
    '--add-data=README.md;.',
    '--clean',
    '--noconfirm',
    '--noconsole',
]) 