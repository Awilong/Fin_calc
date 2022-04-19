
import sys
import os
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from fin3 import Ui_MainWindow



class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Задачник')
        self.all_dates = {}
        self.pushButton_3.clicked.connect(self.dream)
        self.pushButton_2.clicked.connect(self.find_date)
        self.pushButton.clicked.connect(self.rezul)
    def dream(self):
        old_edit_1 = 0
        old_edit_2 = 0
        old_edit_3 = 0
        old_edit_4 = 0
                               
        line_edit_1 = self.lineEdit_12.text()
        line_edit_2 = self.lineEdit_13.text()
        line_edit_3 = self.lineEdit_14.text()
        line_edit_4 = self.lineEdit_15.text()
       
        # задаем словарю новое значение или переопределяем старое
        self.textBrowser_2.clear()
        # сортируем даты и выводим их
        self.textBrowser_2.append('Поездка во Владивосток  '+'Нужно 150000  ' + 'Осталось  '+ str(150000-int(line_edit_1)-old_edit_1))
        self.textBrowser_2.append('Покупка компьютерного кресла  '+'Нужно 15000  ' + 'Осталось  '+ str(15000-int(line_edit_2)-old_edit_2))
        self.textBrowser_2.append('Покупка трюкового самоката  '+'Нужно 15000  ' + 'Осталось  '+ str(15000-int(line_edit_3)-old_edit_3))
        self.textBrowser_2.append('Покупка аквариумных рыб'+' Нужно 1500  ' + 'Осталось  '+ str(1500-int(line_edit_4)-old_edit_4))
        

    def find_date(self):
        # получаем дату
        string_date = self.calendarWidget.selectedDate().getDate()
        # добавляем ноль, елси месяц <= 9
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        # добавляем ноль, елси день <= 9
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        # берем текст из line edit
                
        self.line_edit_5 = 'Зп_папа   +' + self.lineEdit_9.text()
        self.line_edit_6 = 'Зп_мама   +' + self.lineEdit_8.text()
        self.line_edit_7 = 'Депозит   +' + self.lineEdit_10.text()
        self.line_edit_8 = 'Стипендия   +' + self.lineEdit_11.text()

        self.line_edit_9 = 'Питание   -' + self.lineEdit_4.text()
        self.line_edit_10 = 'ЖКХ   -' + self.lineEdit_5.text()
        self.line_edit_11 = 'Здоровье   -' + self.lineEdit_6.text()
        self.line_edit_12 = 'Хобби   -' + self.lineEdit_7.text()
        # задаем словарю новое значение или переопределяем старое
                
        # изюавляемся от повторов
        self.textBrowser_3.clear()
        # сортируем даты и выводим их
        self.textBrowser_3.append(f'{string_date[0]}-{string_date[1]}-{string_date[2]}')
        self.textBrowser_3.append(str(self.line_edit_5))
        self.textBrowser_3.append(str(self.line_edit_6))
        self.textBrowser_3.append(str(self.line_edit_7))
        self.textBrowser_3.append(str(self.line_edit_8))

        self.textBrowser_3.append(str(self.line_edit_9))
        self.textBrowser_3.append(str(self.line_edit_10))
        self.textBrowser_3.append(str(self.line_edit_11))
        self.textBrowser_3.append(str(self.line_edit_12))

    def rezul(self):
        # получаем дату
        string_date = self.calendarWidget.selectedDate().getDate()
        # добавляем ноль, елси месяц <= 9
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        # добавляем ноль, елси день <= 9
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        # берем текст из line edit
                
        line_edit_max = int(self.lineEdit_9.text()) + int(self.lineEdit_8.text()) + int(self.lineEdit_10.text()) + int(self.lineEdit_11.text())
        line_edit_min = int(self.lineEdit_4.text()) + int(self.lineEdit_5.text()) + int(self.lineEdit_6.text()) + int(self.lineEdit_7.text())
        # задаем словарю новое значение или переопределяем старое
        
        # изюавляемся от повторов
        self.textBrowser.clear()
        # сортируем даты и выводим их
        self.textBrowser.append(f'{string_date[0]}-{string_date[1]}')
        self.textBrowser.append('Заработано  ' +  str(line_edit_max))
        self.textBrowser.append('Потрачено  ' +  str(line_edit_min))
        self.textBrowser.append('Сальдо  ' +  str(line_edit_max - line_edit_min))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())