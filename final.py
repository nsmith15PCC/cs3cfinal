import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
from testsuite import *
from tabulate import *
from checkcomments import *

from gui import Ui_MainWindow
from io_gui import Ui_Form

import testsuite

class SubForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #buttons
        self.ui.clearButton.clicked.connect(self.clear_list)
        self.ui.finishButton.clicked.connect(self.finished)
        self.ui.AddButton.clicked.connect(self.add_pairs)
        self.pairlist = list()
        
    def clear_list(self):
        self.ui.ListofIOPairs.clear()
        self.pairlist.clear()
        
    def add_pairs(self):
        user_in = self.ui.NewInput.text()
        user_out = self.ui.NewOutput.text()
        user_in = str(user_in)
        user_out = str(user_out)
        if not user_in == '' and not user_out == '':
            temp_pair = (user_in, user_out)
            self.ui.ListofIOPairs.append(str(temp_pair))
            self.pairlist.append(temp_pair)
    
    def finished(self):
        myapp.ui.StatusBox.append('Pairs of inputs and outputs: ')
        myapp.ui.StatusBox.append(str(self.pairlist))
        myapp.reset(self.pairlist)
        self.close()

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.popup = SubForm()
        self._files = None

        #buttons
        self.ui.browsebutton.clicked.connect(self.set_directory)
        self.ui.clearbutton.clicked.connect(self.clear_directory)
        self.ui.define_inout.clicked.connect(self.get_inout)
        self.ui.scriptlist.itemClicked.connect(self.doFile)
        self.ui.exportbutton.clicked.connect(self.writetoFile)

    def writetoFile(self):
        path = QFileDialog.getSaveFileName()
        f = open(path, 'w')
        f.write(str(self))
        f.close()


    def reset(self, listoftuples):
        if (self._files != None):
            print(listoftuples)
            self._files.createAlltests(listoftuples)
            self._files.runTests()

    def doFile(self):
        index = self.ui.scriptlist.currentRow()
        b = self._files._files[index]
        self.ui.StatusBox.setText(str(b))
        count = check_comments(b._filename)
        self.ui.linenumbers.setText(str(count._linecount))
        self.ui.commentnumbers.setText(str(count._commentcount))
        self.ui.functionnumbers.setText(str(count._functioncount))
        t = tabulate(b.getResults(), linecount=count._linecount, commentcount=count._commentcount, functioncount=count._functioncount, correctweight= int(self.ui.correctweight.text()), wrongweight = int(self.ui.incorrectweight.text()), errorweight = int(self.ui.errorweight.text()), commentfreq= int(self.ui.comment_freq.text()), functionfreq= int(self.ui.avg_func_len.text()), includeComments= self.ui.commentcheck.checkState(), includeFunctions= self.ui.functioncheck.checkState())
        self.ui.Total_score.setText(str(t.getScore()))
        self.ui.IO_score.setText(str(t.getIOScore()))
        self.ui.correctnum.setText(str(t._correctraw))
        self.ui.errornum.setText(str(t._errorraw))
        self.ui.incorrectnum.setText(str(t._incorrectraw))
        if (self.ui.commentcheck.checkState()):
            self.ui.comment_score.setText(str(t.getCommentScore()))
        else:
            self.ui.comment_score.setText("N/A")
        if (self.ui.functioncheck.checkState()):
            self.ui.Function_score.setText(str(t.getFunctionScore()))
        else:
            self.ui.Function_score.setText("N/A")


    def set_directory(self):
        self.ui.directorybox.clear()
        self.ui.directorybox.setText(QFileDialog.getExistingDirectory())
        path = self.ui.directorybox.text()
        self._files = allFiles(path,timeout = int(self.ui.timeout_box.text()), testcases= self.popup.pairlist)
        self._files.runTests()
        self.display_scripts()
	
    def clear_directory(self):
        self.ui.scriptlist.clear()
        self.ui.directorybox.clear()
        
    def display_scripts(self):
        self.ui.scriptlist.clear()
        path = self.ui.directorybox.text()
        os.chdir(path)
        filelist = os.listdir(path)
        
        for i in self._files._files:
            # if(i.endswith('.py')):
            self.ui.scriptlist.addItem(i._filename)
                

        if self.ui.scriptlist.size() != 0:
            self.startsession(path)
            
    def startsession(self, path):
        timelimit = self.ui.timeout_box.text()

        # print('file path: ' + path)
        # print('timeout: ' + timelimit)
        
    def get_inout(self):
        self.popup.show()

    def __str__(self):
        outs = str()
        for b in self._files._files:
            outs += str(b)
            count = check_comments(b._filename)
            outs +="\n\n    Lines: "+str(count._linecount)
            outs +="\n    Comments: "+str(count._commentcount)
            outs +="\n    Functions: "+str(count._functioncount)
            t = tabulate(b.getResults(), linecount=count._linecount, commentcount=count._commentcount, functioncount=count._functioncount, correctweight= int(self.ui.correctweight.text()), wrongweight = int(self.ui.incorrectweight.text()), errorweight = int(self.ui.errorweight.text()), commentfreq= int(self.ui.comment_freq.text()), functionfreq= int(self.ui.avg_func_len.text()), includeComments= self.ui.commentcheck.checkState(), includeFunctions= self.ui.functioncheck.checkState())
            outs+= "\n    Correct: "+str(t._correctraw)
            outs+= "\n    Errors: "+str(t._errorraw)
            outs+= "\n    Incorrect: "+str(t._incorrectraw)

            outs+= "\n    Total Score: "+str(t.getScore())
            outs +="\n    IO Score: " +str(t.getIOScore())
            outs += "\n    Comment Score: "
            if (self.ui.commentcheck.checkState()):
                outs+= str(t.getCommentScore())
            else:
              outs+= "N/A"
            outs+= "\n    Function Score: "
            if (self.ui.functioncheck.checkState()):
                outs+= str(t.getFunctionScore())
            else:
                outs+= "N/A"
            outs+= "\n\n"
        return outs

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
