# lightManager_gui.py

import sys
import random
from PyQt5 import QtWidgets, QtCore, QtGui 
from lightManager_main import readDictionnary, getDictBasedOnName

lightDictionnary = readDictionnary()

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Light Manager v0.1')

        self.hello =  ["Bonjour", "hi", "hei maailma", "hola mundo"]

        # Creating one button for every instance of light
        btnList = []
        current = 0
        for i in lightDictionnary:
            btnName = 'btn' + str(current)
            currentButton = (QtWidgets.QPushButton(i['name']))
            # Adding Icon to the button if the dict doesnt indicate its false
            if i['icon'] != False:
                currentButton.setIcon(QtGui.QIcon(i['icon']))
            btnList.append(currentButton)
            current += 1

        # Creating a QLabel displaying the fullpath
        self.text = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)

        # Creating an image displaying the light icon if it exists
        self.image = QtWidgets.QLabel(alignment = QtCore.Qt.AlignCenter)
        self.image.setText('IMAGE')
        self.pixmap = QtGui.QPixmap('LIB/LIGHT/iconPlaceHolder.jpeg')
        self.image.setPixmap(self.pixmap)
        
        # Creating the vertical Layout for the main splits of the application
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.image)

        # Defining the grid layout containing the other widgets
        self.gridLayout = QtWidgets.QGridLayout()
        # Loop for adding buttons to the QTWidgets
        col = 0
        row = 0
        for i in btnList:
            self.gridLayout.addWidget(i, col, row)
            i.clicked.connect(self.magic)
            # Changing the position of row x column depending on the previous one
            if row > 0:
                row = 0
                col += 1
            else:
                row +=1

        # Adding the gridLayout to the base one
        self.layout.addLayout(self.gridLayout)



    '''
    PYQT SLOT FUNCTIONS
    '''

    @QtCore.pyqtSlot()
    def magic(self):
        #self.text.setText(random.choice(self.hello))

        # Getting the pressed button
        sendingButton = self.sender()
        buttonName = sendingButton.text()
        currentLightDict = getDictBasedOnName(buttonName, lightDictionnary)
        # Getting the text on the pressed button
        self.text.setText(currentLightDict['fullPath'])
        # Setting the image to the current icon if it exists
        if currentLightDict['icon'] != None:
            self.icon = QtGui.QPixmap(currentLightDict['icon'])
            self.image.setPixmap(self.icon)






if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())
