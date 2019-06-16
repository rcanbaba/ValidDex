# -*- coding: utf-8 -*-
import sys


from PyQt5.QtCore import QByteArray
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QPushButton, QPlainTextEdit, QFileDialog, QLineEdit, QVBoxLayout, QFileSystemModel, QTreeView, QMessageBox, \
    QTextEdit,QFormLayout
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import jsontopascalxml as jxml
import stats as st
import findXmlName as findXml
import validation as vt


class Validator(QtGui.QValidator):
    def validate(self,string,pos):
        return QtGui.QValidator.Acceptable, string.upper(), pos

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'ValidDex'
        self.left = 10
        self.top = 10
        self.width = 738
        self.height = 563
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Dex")
        # Download URL Plain Text
        self.downloadURLPT = QPlainTextEdit(self)
        self.downloadURLPT.setGeometry(QtCore.QRect(320, 190, 300, 40))
        self.downloadURLPT.setObjectName("downloadURLPT")

        #Download URL Push Btn
        self.downloadUrlPath = QPushButton('Download Url Image Path',self)
        self.downloadUrlPath.setGeometry(QtCore.QRect(40, 190, 211, 51))
        self.downloadUrlPath.setObjectName("downloadUrlPath")
        self.downloadUrlPath.clicked.connect(self.downloadBtn)

        # Validation Push Btn (Bottom)
        self.valid = QPushButton("Validation",self)
        self.valid.setGeometry(QtCore.QRect(340, 430, 300, 61))
        self.valid.setObjectName("valid")
        self.valid.clicked.connect(self.validation)

        # Xml find Push Btn
        self.xmlfind = QPushButton("Find Xml Files",self)
        self.xmlfind.setGeometry(QtCore.QRect(40, 40, 211, 51))
        self.xmlfind.setFlat(False)
        self.xmlfind.setObjectName("xmlfind")
        self.xmlfind.clicked.connect(self.on_click)

        # find Xml Plain Text
        self.findxmlPT = QPlainTextEdit(self)
        self.findxmlPT.setGeometry(QtCore.QRect(320, 40, 300, 40))
        self.findxmlPT.setObjectName("findxmlPT")

        # Product File Push Btn(BaseClass)
        self.prodfind = QPushButton("Find Product File",self)
        self.prodfind.setGeometry(QtCore.QRect(40, 120, 211, 51))
        self.prodfind.setObjectName("prodfind")
        self.prodfind.clicked.connect(self.prodFile)


        # Product File Plain Text (BaseClass)
        self.findprodfilePT = QPlainTextEdit(self)
        self.findprodfilePT.setGeometry(QtCore.QRect(320, 120, 300, 40))
        self.findprodfilePT.setObjectName("findprodfilePT")

        # Labeling Prod Push Btn
        self.labelingProdName = QLabel("Find Labeling Prod",self)
        self.labelingProdName.setGeometry(QtCore.QRect(50, 260, 211, 51))
        self.labelingProdName.setObjectName("labelingProdName")
        # self.labelingProdName.clicked.connect(self.findProdName)


        # Create Xml File Push Btn
        self.createXml = QPushButton("Create Xml Files",self)
        self.createXml.setGeometry(QtCore.QRect(340, 360, 300, 61))
        self.createXml.setObjectName("createXml")
        self.createXml.clicked.connect(self.createXmlBtn)

        # Find Product Push Btn
        self.find = QPushButton("Find Product", self)
        self.find.setGeometry(QtCore.QRect(20, 430, 300, 61))
        self.find.setObjectName("find")
        self.find.clicked.connect(self.find_Prod)


        # find labeking Plain Text

        self.findLabelingPT = QLineEdit(self)
        self.findLabelingPT.setGeometry(QtCore.QRect(320, 260, 300, 40))
        self.findLabelingPT.setPlaceholderText("Enter Product Name... ")
        self.findLabelingPT.installEventFilter(self)
        self.validator = Validator(self)
        self.findLabelingPT.setValidator(self.validator)


        # Stat Push Btn
        self.stats = QPushButton("Stats",self)
        self.stats.setGeometry(QtCore.QRect(20, 360, 300, 61))
        self.stats.setObjectName("stats")
        self.stats.clicked.connect(self.statsBtn)



    @QtCore.pyqtSlot()
    def find_Prod(self):
        aa = self.findLabelingPT.text()
        cc = self.findxmlPT.toPlainText()

        if aa == '' or cc == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please select Xml Files and Find Product Name')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            findXml.findAll(cc, aa)


    @QtCore.pyqtSlot()
    def findProdName(self):

        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)

        if dlg.exec_():
            file_name = dlg.selectedFiles()[0]
            self.findLabelingPT.setPlainText(file_name)


    @QtCore.pyqtSlot()
    def statsBtn(self):

        xmlFileName = self.findxmlPT.toPlainText()

        if xmlFileName == '' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please select Xml Files and Product Base File')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            st.main(xmlFileName)

    @QtCore.pyqtSlot()
    def createXmlBtn(self):
        mytext = self.downloadURLPT.toPlainText()
        jxml.writeDir(mytext)

    @QtCore.pyqtSlot()
    def downloadBtn(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)

        if dlg.exec_():
            file_name = dlg.selectedFiles()[0]
            self.downloadURLPT.setPlainText(file_name)


    @QtCore.pyqtSlot()
    def validation(self):
        xmlFileName = self.findxmlPT.toPlainText()
        baseFileName = self.findprodfilePT.toPlainText()

        if xmlFileName == '' or baseFileName == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please select Xml Files and Product Base File')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            vt.runValid(xmlFileName,baseFileName)

    @QtCore.pyqtSlot()
    def prodFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)

        if dlg.exec_():
            file_name = dlg.selectedFiles()[0]
            self.findprodfilePT.setPlainText(file_name)

    @QtCore.pyqtSlot()
    def setTextEdit(self):
        textValue = self.set_findProdTE.text()


    @QtCore.pyqtSlot()
    def on_click(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)

        filenames = QByteArray()
        if dlg.exec_():
            self.findxmlPT.setPlainText(dlg.selectedFiles()[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
