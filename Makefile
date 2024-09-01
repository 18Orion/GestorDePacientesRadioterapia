first: ui

ui: UI/patientUI.ui UI/exploitUI.ui UI/launcherUI.ui UI/credentialsUI.ui UI/loginUI.ui
	pyside6-uic UI/patientUI.ui -o src/patient/patientUI.py
	pyside6-uic UI/loginUI.ui -o src/login/loginUI.py
	pyside6-uic UI/launcherUI.ui -o src/launcher/launcherUI.py
	pyside6-uic UI/exploitUI.ui -o src/exploit/exploitUI.py
	pyside6-uic UI/credentialsUI.ui -o src/credentials/credentialsUI.py
	pyside6-uic UI/dialogUI.ui -o src/dialog/dialogUI.py
	pyside6-uic UI/userCreatorUI.ui -o src/userCreator/userCreatorUI.py
	pyside6-uic UI/equipmentUI.ui -o src/equipment/equipmentUI.py
	pyside6-uic UI/equipmentRegistrationUI.ui -o src/equipmentRegistration/equipmentRegistrationUI.py

clean:
	rm -rfv dist/
	rm -rfv build/
	rm -rfv package/
	rm -rfv suite.spec
	rm -rfv importExcel.spec
	rm -rfv winRelease.zip
	rm -rfv linuxRelease.zip

linux:
	pyinstaller --onefile --windowed suite.py
	pyinstaller --onefile scripts/importExcel.py
	pyinstaller --onefile scripts/update.py
	pyinstaller --onefile scripts/createDummyDB.py

dependencies:
	pip3 install -r requirements.txt --break-system-packages

win:
	wine ./Scripts/pyinstaller.exe --windowed --onefile suite.py
	wine ./Scripts/pyinstaller.exe --onefile scripts/importExcel.py
	wine ./Scripts/pyinstaller.exe --onefile scripts/createDummyDB.py
	wine ./Scripts/pyinstaller.exe --onefile scripts/update.py

package: 
	mkdir package
	mkdir package/assets
	cp assets/* package/assets
	cp configuration.json package
	cp README.md package
	cp scripts/*.txt package -r
	cp package winPackage -r
	cp package linuxPackage -r
	cp dist/*.exe winPackage
	cp dist/suite linuxPackage -r
	cp dist/importExcel linuxPackage -r
	cp dist/update linuxPackage -r
	cp dist/createDummyDB linuxPackage -r
	zip linuxRelease.zip linuxPackage -r
	zip winRelease.zip winPackage -r
	rm -rfv package winPackage linuxPackage


all: ui linux win package