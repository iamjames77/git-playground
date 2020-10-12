import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        NameLabel = QLabel('Name:',self)
        NameLine = QLineEdit(self)
        AgeLabel = QLabel('Age:', self)
        AgeLine = QLineEdit(self)
        ScoreLabel = QLabel('Score:', self)
        ScoreLine = QLineEdit(self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(NameLabel)
        hbox1.addWidget(NameLine)
        hbox1.addWidget(AgeLabel)
        hbox1.addWidget(AgeLine)
        hbox1.addWidget(ScoreLabel)
        hbox1.addWidget(ScoreLine)

        AmountLabel = QLabel('Amount:',self)
        AmountLine = QLineEdit(self)
        KeyLabel = QLabel('Key:',self)
        KeyComboBox = QComboBox(self)
        KeyComboBox.addItem('Name')
        KeyComboBox.addItem('Age')
        KeyComboBox.addItem('Score')

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(AmountLabel)
        hbox2.addWidget(AmountLine)
        hbox2.addWidget(KeyLabel)
        hbox2.addWidget(KeyComboBox)

        AddButton = QPushButton('Add',self)
        DelButton = QPushButton('Del', self)
        FindButton = QPushButton('Find', self)
        IncButton = QPushButton('Inc', self)
        showButton = QPushButton('show', self)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(AddButton)
        hbox3.addWidget(DelButton)
        hbox3.addWidget(FindButton)
        hbox3.addWidget(IncButton)
        hbox3.addWidget(showButton)

        ResultLabel = QLabel('Result:',self)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(ResultLabel)

        Result = QTextEdit()

        hbox5 = QHBoxLayout()
        hbox5.addWidget(Result)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

