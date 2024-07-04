# PyScriptRunner - Python Script Runner

Execute Python scripts without installing Python.
Usefull for machines that have no internet connection (air gap environment) to install Python and dependency libraries.
The single file executable can be created for Windows, Linux, Unix, and MacOS.

## Detail
1. The single file tool utilizes PyInstaller to create a single executable package.
2. The exectuable tool will then utilize the Python library "importlib.import_module" to run external Python script.
3. This tool demonstrates how easy to create a package that executes Python scripts without an installed Python.

## Sample How to Create the Tool For Windows
1. Download and install Python 3.X
2. Install Python's Virtual Environment module
```sh
       pip install virtualenv
```
3. Create a python virtual environment
```sh
       python -m venv c:\virtualpython\PYTHON3
```
4. Activate the python virtual environment
```sh
       c:\virtualpython\PYTHON3\Scripts\activate.bat
```
5. Change folder to PyScriptRunner source code path
```sh
       cd C:\PyScriptRunner
```
6. Install the required modules
```sh
       pip install -r PyInstaller
```
7. Build the single executable app. The executable file will be placed at dist subfolder.
```sh
       Pyinstaller main.spec
```
## Sample usage on Windows
```sh
       PyScriptRunner.exe yourscript.py
```

## Adding your script's needed Python libraries
If your script needs other Python libraries:
1. You need to install the Python library in your build environment
2. Declare the library import in Main.py
3. Build the single executable app again.

Example if your script needs psutil:
1. pip install -r psutil
2. Add "import psutil" in pyscriptrunner.py
3. Pyinstaller main.spec

## Contributing:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Safety:

Always ensure that the Python scripts are safe to run, as they will be executed as-is.

## License:

[MIT](https://choosealicense.com/licenses/mit/)
