pyside6-uic UI/patientUI.ui -o src/patient/patientUI.py
pyside6-uic UI/loginUI.ui -o src/login/loginUI.py
pyside6-uic UI/launcherUI.ui -o src/launcher/launcherUI.py
pyside6-uic UI/exploitUI.ui -o src/exploit/exploitUI.py
pyinstaller --onefile --windowed main.py
pyinstaller --onefile scripts/importExcel.py