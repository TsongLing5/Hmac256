# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QPushButton,QTextEdit,QApplication,QWidget,QLabel
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
# import difflib
import os
import hashlib
import hmac
# key='00000000000000000000000000000000'
# d = difflib.HtmlDiff()
app = QApplication(sys.argv)
mywindows=QWidget()
button=QPushButton(mywindows)
text1=QTextEdit(mywindows)
text2=QTextEdit(mywindows)
testResult=QTextEdit(mywindows)
labelKey=QLabel(mywindows)
labelResult=QLabel(mywindows)
labelData=QLabel(mywindows)
def p():
#     print(text1.toPlainText())
    
    s1=text1.toPlainText()  
    s2=text2.toPlainText() 
    print(type(s2))
    print("Data:"+s1)
    print("Key:"+s2)
    msg=bytes.fromhex(s1.replace(" ",""))
    key=bytes.fromhex(s2.replace(" ","")[0:32])
    text2.setText(s2.replace(" ","")[0:32])
    print(type(key))
    print(key)
    m = hmac.new(key,msg, hashlib.sha256)
    result=m.hexdigest()[0:32]
    str=""
    for i in range(0,32):
        str=str+result[i]
        if(i%2):
            str=str+" "
    print(str)
    testResult.setText(str.upper())
#     html=d.make_file(s1,s2)
#     web.setHtml("\'\'\'"+html+"\'\'\'")
if __name__=="__main__":
#     mywindows.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    mywindows.setWindowTitle("HmacSHA256")
    mywindows.setFixedSize(1050,250)
    mywindows.showMaximized()
    button.setGeometry(950,50,50,30)
    button.setText("生成")
    text2.setText("00000000000000000000000000000000")
    text1.setText("22 F1 98 ")
    button.clicked.connect(p)
    text1.setGeometry(20,50,400,50)    
    text2.setGeometry(500,50,400,50) 
    testResult.setGeometry(20,150,400,50)    
    labelData.setText("Data:")
    labelData.setGeometry(20,10,400,50)  
    labelKey.setText("Key(16Byte is necessary):")
    labelKey.setGeometry(500,10,400,50)
    labelResult.setText("Result:")
    labelResult.setGeometry(20,110,400,50)    
    mywindows.show()
    # app.exec_()
    sys.exit(app.exec_())
