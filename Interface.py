from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QScrollArea
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette

class ShopInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tienda de Componentes")
        self.setGeometry(100, 100, 1200, 700)

        # Main layout
        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)

        # Sidebar for categories
        sidebar = QVBoxLayout()
        sidebar.setSpacing(10)
        main_layout.addLayout(sidebar, 1)

        category_label = QLabel("CATEGORIA")
        category_label.setAlignment(Qt.AlignCenter)
        category_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        sidebar.addWidget(category_label)

        categories = ["COMPUTADORAS", "IMPRESORAS", "COMPONENTES", "AUDIO Y VIDEO", "ENERGIA"]
        for category in categories:
            btn = self.create_rounded_button(category)
            sidebar.addWidget(btn)

        subcategory_label = QLabel("COMPONENTES")
        subcategory_label.setAlignment(Qt.AlignCenter)
        subcategory_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        sidebar.addWidget(subcategory_label)

        subcategories = ["PROCESADOR", "RAM", "ALMACENAMIENTO", "GABINETE", "FUENTE DE PODER", "ENFRIAMIENTO", "TARJETA DE RED", "GRAFICA"]
        for subcategory in subcategories:
            btn = self.create_rounded_button(subcategory)
            sidebar.addWidget(btn)

        # Product grid
        product_frame = QVBoxLayout()
        main_layout.addLayout(product_frame, 3)

        nav_label = QLabel("CATEGORIA / COMPONENTES / ALMACENAMIENTO")
        nav_label.setStyleSheet("font-size: 14px; color: white;")
        product_frame.addWidget(nav_label)

        products = [
            {"name": "SSD ACER SA100", "capacity": "512GB", "price": "$949.00", "interface": "SATA III"},
            {"name": "SSD Samsung 870 EVO", "capacity": "1TB", "price": "$1024.00", "interface": "SATA III"},
            {"name": "SSD ADATA Ultimate SU630", "capacity": "1.9TB", "price": "$2045.00", "interface": "SATA III"}
        ]

        for product in products:
            product_card = QFrame()
            product_card.setFrameShape(QFrame.StyledPanel)
            product_card.setStyleSheet("background-color: white; border-radius: 10px;")

            card_layout = QHBoxLayout(product_card)

            details = QLabel(f"<b>Modelo:</b> {product['name']}<br><b>Capacidad:</b> {product['capacity']}<br><b>Interface:</b> {product['interface']}")
            details.setStyleSheet("font-size: 12px;")
            card_layout.addWidget(details, 3)

            price_label = QLabel(product['price'])
            price_label.setStyleSheet("font-size: 14px; font-weight: bold;")
            card_layout.addWidget(price_label, 1, alignment=Qt.AlignCenter)

            add_to_cart = self.create_rounded_button("Agregar al Carrito")
            card_layout.addWidget(add_to_cart, 1, alignment=Qt.AlignCenter)

            product_frame.addWidget(product_card)

        # Background color
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor("black"))
        self.setPalette(palette)

    def create_rounded_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet(
            """
            QPushButton {
                background-color: rgb(26, 185, 203);
                color: black;
                border: 5px solid rgb(20, 67, 103);
                border-radius: 30px;
                font-size: 12px;
                padding: 20px;
            }
            QPushButton:hover {
                background-color:rgb(204, 255, 0);
            }
            QPushButton:pressed {
                background-color: #1E90FF;
                color: white;
  
            }
            """
        )
        return button

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ShopInterface()
    window.show()
    sys.exit(app.exec_())
