import pickle
import sys
from typing import List, Any

from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QDialog)
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
        self.NameLine = QLineEdit(self)
        AgeLabel = QLabel('Age:', self)
        self.AgeLine = QLineEdit(self)
        ScoreLabel = QLabel('Score:', self)
        self.ScoreLine = QLineEdit(self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(NameLabel)
        hbox1.addWidget(self.NameLine)
        hbox1.addWidget(AgeLabel)
        hbox1.addWidget(self.AgeLine)
        hbox1.addWidget(ScoreLabel)
        hbox1.addWidget(self.ScoreLine)

        AmountLabel = QLabel('Amount:',self)
        self.AmountLine = QLineEdit(self)
        KeyLabel = QLabel('Key:',self)
        self.KeyComboBox = QComboBox(self)
        self.KeyComboBox.addItem('Name')
        self.KeyComboBox.addItem('Age')
        self.KeyComboBox.addItem('Score')

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(AmountLabel)
        hbox2.addWidget(self.AmountLine)
        hbox2.addWidget(KeyLabel)
        hbox2.addWidget(self.KeyComboBox)

        AddButton = QPushButton('Add',self)
        DelButton = QPushButton('Del', self)
        FindButton = QPushButton('Find', self)
        IncButton = QPushButton('Inc', self)
        showButton = QPushButton('show', self)

        AddButton.clicked.connect(self.AddClicked)
        DelButton.clicked.connect(self.DelClicked)
        IncButton.clicked.connect(self.IncClicked)
        FindButton.clicked.connect(self.FindClicked)
        showButton.clicked.connect(self.showClicked)

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

        self.Result = QTextEdit()

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.Result)

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

    def AddClicked(self):
        name = self.NameLine.text()
        age = int(self.AgeLine.text())
        score = int(self.ScoreLine.text())


        record = {'Name':name, 'Age':age, 'Score':score}
        self.scoredb +=[record]
        self.showScoreDB()

    def DelClicked(self):
        delname = self.NameLine.text()
        scdb = self.scoredb
        self.scoredb = []

        for p in sorted(scdb, key=lambda person: person['Name']):
            if p['Name'] != delname:
                self.scoredb += [p]

        self.showScoreDB()

    def FindClicked(self):
        findname = self.NameLine.text()
        msg = ""
        for p in self.scoredb:
            if p['Name'] != findname:
                continue
            for attr in sorted(p):
                msg += attr + "=" + str(p[attr]) + "    \t"
            msg += "\n"
        self.Result.setText(msg)
    
    def IncClicked(self):
        Incname = self.NameLine.text()
        Amount = int(self.AmountLine.text())
        scdb = self.scoredb
        self.scoredb = []

        for p in sorted(scdb, key=lambda person: person['Name']):
            if p['Name'] == Incname:
                x = int(p['Score'])
                x += Amount
                p['Score'] = x
                self.scoredb += [p]
            else:
                self.scoredb += [p]

        self.showScoreDB()

    def showClicked(self):
        self.showScoreDB()

    def showScoreDB(self):
        keyname = str(self.KeyComboBox.currentText())
        msg = ""
        keyname = "Name" if not keyname else keyname

        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                msg += attr + "=" +str(p[attr]) + "     \t"
            msg +="\n"
        self.Result.setText(msg)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

