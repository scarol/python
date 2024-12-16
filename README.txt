venv module in python:

D:\PycharmProjects\PythonProjects>py -m venv myvenv, this creates a new virtual env named myvenv in
the given directory

To activate the virtual env:
D:\PycharmProjects\PythonProjects>myvenv\Scripts\activate

(myvenv) D:\PycharmProjects\PythonProjects>

To deactivate the virtual env
(myvenv) D:\PycharmProjects\PythonProjects>deactivate
D:\PycharmProjects\PythonProjects>

To install the QR Code package from PyPi: pypi.org/project/qrcode - used this package for the QR Code generator
(myvenv) D:\PycharmProjects\PythonProjects>pip install qrcode
Collecting qrcode
  Downloading qrcode-8.0-py3-none-any.whl.metadata (17 kB)
Collecting colorama (from qrcode)
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Downloading qrcode-8.0-py3-none-any.whl (45 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: colorama, qrcode
Successfully installed colorama-0.4.6 qrcode-8.0

Also use pip install image

Python Virtual Environments work like separate workspace within your computer and isolate it from
 the rest of the computer tp provide a separate isolated work area for your Python applications. This
  is especially helpful when working on multiple Python projects at the same time that need different
  versions of libraries that might otherwise conflict if run on the same system. So with Virtual
  Environments multiple applications having dependency on different versions of the same libraries can
  run easily.

Python “Virtual Environments” allow Python packages to be installed in an isolated location for a
particular application, rather than being installed globally.

A virtual environment is created on top of an existing Python installation, known as the virtual
environment’s “base” Python, and may optionally be isolated from the packages in the base environment,
so only those explicitly installed in the virtual environment are available.

pip module in python:
The most popular tool for installing Python packages, and the one included with modern versions of
Python. It provides the essential core features for finding, downloading, and installing packages
from PyPI and other Python package indexes, and can be incorporated into a wide range of development
workflows via its command-line interface (CLI).

