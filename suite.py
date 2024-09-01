from src.login.loginActivity import loginActivity
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = loginActivity()
    window.show()
    sys.exit(app.exec())