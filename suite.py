#!/usr/bin/env python3

try:
    #Try imports
    from src.login.loginActivity import loginActivity
    from PySide6.QtWidgets import QApplication
    import sys
except:
    #In case of exception install dependencies
    from libs.funcs import installDependencies
    installDependencies("requirements.txt")
finally:
    #Retry import
    from src.login.loginActivity import loginActivity
    from PySide6.QtWidgets import QApplication
    import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loginActivity()
    window.show()
    sys.exit(app.exec())