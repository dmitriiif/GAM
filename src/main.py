import time
import sys
import psutil
import GPUtil


from ui_interface import *
from Custom_Widgets.Widgets import *
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon, QRegion



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.setMask(QRegion(self.ui.startButton.x()+10,self.ui.startButton.y(),300,300, QRegion.Ellipse))
        
        loadJsonStyle(self, self.ui)

        self.setWindowIcon(QIcon(":/images/gamcoin.png"))
        
        self.ui.startButton.clicked.connect(lambda:self.start())

        self.running = QTimer()
        self.running.timeout.connect(self.update_progress_bars)
        self.running.start(1000)

        for w in self.ui.leftMenuContainer.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)

    def applyButtonStyle(self):
        for w in self.ui.leftMenuContainer.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName:
                defaultStyle = w.styleSheet().replace("border-left: 2px solid #C6A052;", "border-left: 2px solid transparent;")
                defaultStyle = defaultStyle.replace("border-bottom: 2px solid #C6A052;", "border-bottom: 2px solid transparent;")
                defaultStyle = defaultStyle.replace("border-top: 2px solid #C6A052;", "border-top: 2px solid transparent;")
                defaultStyle = defaultStyle.replace("background-color: #1f232a;", "background-color: #16191d;")

                w.setStyleSheet(defaultStyle)
        
        newStyle = self.sender().styleSheet().replace("border-left: 2px solid transparent;", "border-left: 2px solid #C6A052;")
        newStyle = newStyle.replace("border-bottom: 2px solid transparent;", "border-bottom: 2px solid #C6A052;")
        newStyle = newStyle.replace("border-top: 2px solid transparent;", "border-top: 2px solid #C6A052;")
        newStyle = newStyle.replace("background-color: #16191d;", "background-color: #1f232a;")
        self.sender().setStyleSheet(newStyle)

        return
    def moveWindow(self, event):  
            if self.isMaximized() == False: 
                if event.buttons() == Qt.LeftButton:  
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def closeEvent(self, event):
        # Confirmation before closing app
        '''
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to close the application?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        '''
    
    def update_progress_bars(self):
        cpu_value = psutil.cpu_percent()
        self.ui.CPUProgressBar.setValue(cpu_value)
        
        # only for people with nvidia drivers
        gpus = GPUtil.getGPUs()
        gpu_values, total_number = 0, 0
        for gpu in gpus:
            total_number += 1
            gpu_values += gpu.load * 100
        
        try:
            average_gpu_value = gpu_values/total_number
        except ZeroDivisionError:
            average_gpu_value = 0

        self.ui.GPUProgressBar.setValue(average_gpu_value)

    def start(self):
        print("test")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
