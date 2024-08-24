first: ui

ui: UI/patientUI.ui UI/exploitUI.ui UI/launcherUI.ui UI/credentialsUI.ui UI/loginUI.ui
	pyside6-uic UI/patientUI.ui -o src/patient/patientUI.py
	pyside6-uic UI/loginUI.ui -o src/login/loginUI.py
	pyside6-uic UI/launcherUI.ui -o src/launcher/launcherUI.py
	pyside6-uic UI/exploitUI.ui -o src/exploit/exploitUI.py
	pyside6-uic UI/credentialsUI.ui -o src/credentials/credentialsUI.py

clean:
	rm -rfv dist/
	rm -rfv build/

executables: clean ui
	pyinstaller --onefile --windowed main.py
	pyinstaller --onefile scripts/importExcel.py