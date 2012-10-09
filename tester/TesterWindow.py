# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('tester')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('tester')

from tester_lib import Window
from tester.AboutTesterDialog import AboutTesterDialog
from tester.PreferencesTesterDialog import PreferencesTesterDialog

from tester import window_steering as windows
from gi.repository import Gtk

# See tester_lib.Window.py for more details about how this class works
class TesterWindow(Window):
    __gtype_name__ = "TesterWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(TesterWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutTesterDialog
        self.PreferencesDialog = PreferencesTesterDialog

        self.toolbar = windows.showManualWindow("Manual Window")
        self.toolbar_open = False
        self.openWindow()
        #self.toolbar2 = windows.show2ndWindow("Testapplication","window8", "./data/ui/test-window.glade")
        

        # Code for other initialization actions should be added here.

    def on_mnu_save_activate(self, widget, data=None):
        print "save"

    def on_button1_clicked(self, widget, data=None):
        windows.showManualWindow("Hahahaaaa")

    def on_button2_clicked(self, widget, data=None):
        self.toolbar.changeLabel("Changed from outside!!!")        

    def on_button3_clicked(self, widget, data=None):
        self.toolbar.closeWindow()

    def on_button4_clicked(self, widget, data=None):
    
        self.windowClass.changeLabelFromOutside("Changed from outside")

    def on_button5_clicked(self, widget, data=None):
        self.openWindow()

    def on_button6_clicked(self, widget, data=None):
        if self.toolbar_open == True:
            self.win.destroy()
            self.toolbar_open = False

    def openWindow(self):
        if self.toolbar_open == False:
            self.windowClass = windows.MyAutomaticWindow("Automatic Window", "./data/ui/test-window.glade", "window8")
            self.win = self.windowClass.getWindow()
	        self.win.show_all()
            self.toolbar_open = True
            
