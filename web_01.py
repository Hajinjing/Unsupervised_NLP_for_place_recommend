import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from PyQt5.QtWebEngineWidgets import QWebEngineView

form_window = uic.loadUiType('./webWidget.ui')[0]
class WebView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def release(self):
        self.deleteLater()
        self.close()
class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._webview = WebView()
        self.web.addWidget(self._webview)
        self._webview.load(QUrl('http://www.naver.com'))


app = QApplication(sys.argv)
mainWindow = Exam()
mainWindow.show()
sys.exit(app.exec_())