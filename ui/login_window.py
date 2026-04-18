from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QFrame, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ui.main_window import MainWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SCADA PRO - Connexion")
        self.resize(1200, 760)
        self.setMinimumSize(980, 620)

        self.colors = {
            "primary": "#0a0e27",
            "secondary": "#131b3c",
            "tertiary": "#1e2a5e",
            "card_bg": "#16213e",
            "accent": "#00d4ff",
            "accent2": "#ff6b6b",
            "text": "#ffffff",
            "text_muted": "#9aa7c7"
        }

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {self.colors["primary"]};
                color: {self.colors["text"]};
                font-family: Arial;
            }}

            QFrame#mainCard {{
                background-color: {self.colors["secondary"]};
                border: none;
                border-radius: 28px;
            }}

            QFrame#infoCard {{
                background-color: {self.colors["card_bg"]};
                border: none;
                border-radius: 24px;
            }}

            QLabel {{
                background: transparent;
                border: none;
            }}

            QLabel#titleLabel {{
                color: {self.colors["accent"]};
                font-size: 34px;
                font-weight: bold;
            }}

            QLabel#subtitleLabel {{
                color: {self.colors["text_muted"]};
                font-size: 17px;
            }}

            QLabel#sectionTitle {{
                color: {self.colors["text"]};
                font-size: 18px;
                font-weight: bold;
            }}

            QLabel#sideTitle {{
                color: {self.colors["accent"]};
                font-size: 30px;
                font-weight: bold;
            }}

            QLabel#sideText {{
                color: {self.colors["text_muted"]};
                font-size: 16px;
            }}

            QLabel#smallInfo {{
                color: {self.colors["text_muted"]};
                font-size: 14px;
            }}

            QLineEdit {{
                background-color: {self.colors["tertiary"]};
                color: {self.colors["text"]};
                border: 1px solid rgba(0,212,255,0.35);
                border-radius: 16px;
                padding: 16px 18px;
                font-size: 18px;
                min-height: 28px;
            }}

            QLineEdit:focus {{
                border: 1px solid {self.colors["accent"]};
            }}

            QPushButton#loginButton {{
                background-color: {self.colors["accent"]};
                color: black;
                border: none;
                border-radius: 16px;
                padding: 16px;
                font-size: 18px;
                font-weight: bold;
            }}

            QPushButton#loginButton:hover {{
                background-color: #4ce2ff;
            }}
        """)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(36, 36, 36, 36)
        main_layout.setSpacing(28)

        # Partie gauche
        left_card = QFrame()
        left_card.setObjectName("infoCard")

        left_layout = QVBoxLayout(left_card)
        left_layout.setContentsMargins(34, 34, 34, 34)
        left_layout.setSpacing(18)

        icon_label = QLabel("🏭")
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setFont(QFont("Arial", 56))

        side_title = QLabel("SCADA PRO")
        side_title.setObjectName("sideTitle")
        side_title.setAlignment(Qt.AlignCenter)

        side_subtitle = QLabel("Plateforme intelligente de supervision")
        side_subtitle.setObjectName("subtitleLabel")
        side_subtitle.setAlignment(Qt.AlignCenter)

        desc1 = QLabel("• Suivi des capteurs physiques")
        desc1.setObjectName("sideText")

        desc2 = QLabel("• Estimation des capteurs logiciels")
        desc2.setObjectName("sideText")

        desc3 = QLabel("• Tendances, alarmes et rapports")
        desc3.setObjectName("sideText")

        footer_info = QLabel("Interface claire, grande et bien structurée")
        footer_info.setObjectName("smallInfo")
        footer_info.setAlignment(Qt.AlignCenter)

        left_layout.addStretch()
        left_layout.addWidget(icon_label)
        left_layout.addWidget(side_title)
        left_layout.addWidget(side_subtitle)
        left_layout.addSpacing(10)
        left_layout.addWidget(desc1)
        left_layout.addWidget(desc2)
        left_layout.addWidget(desc3)
        left_layout.addStretch()
        left_layout.addWidget(footer_info)

        # Partie droite
        right_card = QFrame()
        right_card.setObjectName("mainCard")

        right_layout = QVBoxLayout(right_card)
        right_layout.setContentsMargins(40, 40, 40, 40)
        right_layout.setSpacing(18)

        title = QLabel("Connexion")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Accédez à votre espace de supervision")
        subtitle.setObjectName("subtitleLabel")
        subtitle.setAlignment(Qt.AlignCenter)

        user_label = QLabel("Utilisateur")
        user_label.setObjectName("sectionTitle")

        self.username = QLineEdit()
        self.username.setPlaceholderText("Entrer le nom d'utilisateur")
        self.username.setText("admin")

        password_label = QLabel("Mot de passe")
        password_label.setObjectName("sectionTitle")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Entrer le mot de passe")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setText("admin123")

        btn = QPushButton("CONNEXION")
        btn.setObjectName("loginButton")
        btn.clicked.connect(self.authenticate)

        info = QLabel("Identifiants par défaut : admin / admin123")
        info.setObjectName("smallInfo")
        info.setAlignment(Qt.AlignCenter)

        right_layout.addStretch()
        right_layout.addWidget(title)
        right_layout.addWidget(subtitle)
        right_layout.addSpacing(10)
        right_layout.addWidget(user_label)
        right_layout.addWidget(self.username)
        right_layout.addWidget(password_label)
        right_layout.addWidget(self.password)
        right_layout.addSpacing(10)
        right_layout.addWidget(btn)
        right_layout.addWidget(info)
        right_layout.addStretch()

        main_layout.addWidget(left_card, 1)
        main_layout.addWidget(right_card, 1)

        self.main_window = None

    def authenticate(self):
        if self.username.text() == "admin" and self.password.text() == "admin123":
            self.main_window = MainWindow(current_user=self.username.text())
            self.main_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "Erreur", "Identifiants incorrects")