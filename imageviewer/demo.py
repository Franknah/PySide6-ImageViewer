import sys
from PySide6.QtCore import QSize
from widget_ui import Ui_MainWindow
from PySide6.QtWidgets import QWidget,QMainWindow,QApplication,QFileDialog
from imageviewer import ImageViewer
class window(QMainWindow):
    '''主窗口'''
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.viewer=ImageViewer(self.ui.frame)
        self.ui.actionOpen.triggered.connect(self.Open)
    def resizeEvent(self, event):
        size=QSize()
        size.setWidth(int(event.size().width()*0.999))
        size.setHeight(int(event.size().height()*0.98))
        self.viewer.resize(size)
    def Open(self):
        file, _ = QFileDialog.getOpenFileName(
                caption='打开', filter='其他(*);;jpg格式(*.jpg);;png格式(*.png)')
        self.viewer.setImage(file)
app=QApplication()
w=window()
w.show()
sys.exit(app.exec())