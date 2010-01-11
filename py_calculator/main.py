from PyQt4 import QtCore, QtGui
from ui_calculator import Ui_CalDialog
import sys

class CalDialog(QtGui.QDialog, Ui_CalDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
        
        
    @QtCore.pyqtSignature("QString")
    def on_txtInput_textChanged(self, input):
        (num, b) = input.toInt()
        if not b:
            ans='Error'
        else:
            if num>40 or num<=0:
                ans='Plz input correctly'
            elif num<23:
                ans='Small than 6'
            elif num<30:
                ans='6'
            elif num<35:
                ans='7'
            elif num<40:
                ans='8'
            else:
                ans='9'
        self.txtOutput.setText(ans)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    calculator = CalDialog()
    calculator.show()
    sys.exit(app.exec_())
