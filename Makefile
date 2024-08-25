first: ui

ui: UI/patientUI.ui UI/exploitUI.ui UI/launcherUI.ui UI/credentialsUI.ui UI/loginUI.ui
	pyside6-uic UI/patientUI.ui -o src/patient/patientUI.py
	pyside6-uic UI/loginUI.ui -o src/login/loginUI.py
	pyside6-uic UI/launcherUI.ui -o src/launcher/launcherUI.py
	pyside6-uic UI/exploitUI.ui -o src/exploit/exploitUI.py
	pyside6-uic UI/credentialsUI.ui -o src/credentials/credentialsUI.py
	pyside6-uic UI/dialogUI.ui -o src/dialog/dialogUI.py

clean:
	rm -rfv dist/
	rm -rfv build/

executables: clean ui
	pyinstaller --onefile --windowed main.py
	pyinstaller --onefile scripts/importExcel.py
	wine ./Scripts/pyinstaller.exe --windowed --onefile main.py
	wine ./Scripts/pyinstaller.exe --onefile scripts/importExcel.py

dependencies:
	pip3 install -r requirements.txt --break-system-packages
win:
	wine ./Scripts/pyinstaller.exe --windowed --onefile main.py
	wine ./Scripts/pyinstaller.exe --onefile scripts/importExcel.py
