# -*- coding: utf-8 -*-
"""
@authors: 
 - Pete Morgan <pete@daffodil.uk.com>
 - and other shoulders
@copyright: fgx
"""

import sys
from PyQt4 import QtGui, QtCore


    

class CommanderMainWindow( QtGui.QMainWindow ):

    def __init__( self, parent=None ):
        QtGui.QMainWindow.__init__( self, parent )
        
        
        
        self.menuApp = self.menuBar().addMenu( "App" )
    

        self.menuApp.addSeparator()

        

        

        self.actionQuit = self.menuApp.addAction( "Quit", self.on_quit )
        self.actionQuit.setIconVisibleInMenu( True )


        ## View Menu
        self.menuView = self.menuBar().addMenu( "Open" )
        
        
        
        

    def on_quit(self):
        sys.exit(0) # maybe we kill with qt ??
        
        

