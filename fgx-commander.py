#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@authors: 
 - Pete Morgan <pete@daffodil.uk.com>
 - and other shoulders
"""

import sys
from PyQt4 import QtGui, QtCore


from fgx.gui import CommanderMainWindow, show_splash




if __name__ == '__main__':

    app = QtGui.QApplication( sys.argv )

    # splash something
    splashScreen = show_splash()
    app.processEvents()

    ## Main Window laod
    window = CommanderMainWindow.CommanderMainWindow()

    ## done 
    splashScreen.finish( window )
    window.show()

    sys.exit( app.exec_() )


