import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Hiding the window title
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # Will not be displayed
        self.setWindowTitle('-- Light_Manager_v0.01 --')

        # Changing the color to Black
        self.setStyleSheet('background-color: rgb(10,10,10)')

        
        '''
        WIDGETS
        '''

        # Setting up the Title Label
        self.title = QtWidgets.QLabel('Title', self)
        self.title.setStyleSheet('color: white')
        
        # Setting up the close button
        self.close = QtWidgets.QPushButton('close', self)
        self.close.setStyleSheet('color: white')


        # Setting up the Icon
        self.icon = QtWidgets.QLabel('ICON', self)
        self.icon.setStyleSheet('color: white')

        # Setting up the loading bar
        self.loadBar = QtWidgets.QLabel('LOADING BAR', self)
        self.loadBar.setStyleSheet('color: white')

        # Setting up the loading infos
        self.infoTop = QtWidgets.QLabel('Info top', self)
        self.infoTop.setStyleSheet('color: white')

        self.infoBot = QtWidgets.QLabel('Info bottom', self)
        self.infoBot.setStyleSheet('color: white')


        '''
        LAYOUT
        '''

        self.mainLayout = QtWidgets.QVBoxLayout(self)

        # Title and close button
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.addWidget(self.title)
        self.horizontalLayout.addWidget(self.close)

        # Adding the horizontal layout to the top of the the main layout
        self.mainLayout.addLayout(self.horizontalLayout)

        # Adding the other widgets to the vertical layout
        self.mainLayout.addWidget(self.icon)
        self.mainLayout.addWidget(self.loadBar)
        self.mainLayout.addWidget(self.infoTop)
        self.mainLayout.addWidget(self.infoBot)
        
        



if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800,500)
    widget.show()

    sys.exit(app.exec())
