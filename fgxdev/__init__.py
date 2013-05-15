
from PyQt4 import QtGui, QtCore

def show_splash():

    splashImage = QtGui.QPixmap( "../images/corp/splash.png" )
    splashScreen = QtGui.QSplashScreen( splashImage )
    #splashScreen.showMessage( "Loading. . ." )
    splashScreen.show()
    return splashScreen
