import subprocess
cmd = "python launch.py --precision full --no-half"
p=subprocess.Popen(cmd, shell=True)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys
import time
 
# creating main window class
class MainWindow(QMainWindow):
 
    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # creating a QWebEngineView
        self.browser = QWebEngineView()
        self.setWindowIcon(QIcon('favicon.ico'))
        # setting default browser url as google
        self.browser.setUrl(QUrl("http://localhost:5080/index.html"))
        # adding action when loading is finished
        self.browser.loadFinished.connect(self.update_title)
        # set this browser as central widget or main window
        self.setCentralWidget(self.browser)
        # creating QToolBar for navigation
        navtb = QToolBar("Navigation")
        # adding this tool bar tot he main window
        self.addToolBar(navtb)
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        self.settings = QWebEngineSettings.defaultSettings()
        self.settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.QWebEnginePage=QWebEnginePage().setFeaturePermission(QUrl("http://127.0.0.1:7861/"), QWebEnginePage.MediaVideoCapture, QWebEnginePage.PermissionGrantedByUser)
        self.showMaximized()
    def ready(self, returnValue):
        print(returnValue)
 
    # method for updating the title of the window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Clown Idea" % title)
 
 
    # method called by the home action
    def navigate_home(self):
 
        # open the google
        self.browser.setUrl(QUrl("http://127.0.0.1:7861/"))
 
 
# creating a pyQt5 application
app = QApplication(sys.argv)
# setting name to the application
app.setApplicationName("Clown Idea")
# creating a main window object
window = MainWindow()
# loop
time.sleep(75)
app.exec_()
p.terminate()
p.kill()