# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IOcreate.ui'
#
# Created: Sun May  1 17:28:06 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(358, 347)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 331))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.NewInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.NewInput.setObjectName(_fromUtf8("NewInput"))
        self.horizontalLayout.addWidget(self.NewInput)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.NewOutput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.NewOutput.setObjectName(_fromUtf8("NewOutput"))
        self.horizontalLayout.addWidget(self.NewOutput)
        self.AddButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.horizontalLayout.addWidget(self.AddButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.ListofIOPairs = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.ListofIOPairs.setObjectName(_fromUtf8("ListofIOPairs"))
        self.verticalLayout.addWidget(self.ListofIOPairs)
        self.clearButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.verticalLayout.addWidget(self.clearButton)
        self.finishButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.finishButton.setObjectName(_fromUtf8("finishButton"))
        self.verticalLayout.addWidget(self.finishButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Input", None))
        self.label_2.setText(_translate("Form", "Output", None))
        self.AddButton.setText(_translate("Form", "Add", None))
        self.label_3.setText(_translate("Form", "Input, Output Pairs", None))
        self.clearButton.setText(_translate("Form", "Clear", None))
        self.finishButton.setText(_translate("Form", "Finished", None))

