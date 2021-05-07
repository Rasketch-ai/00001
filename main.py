from PyQt5 import QtCore, QtGui, QtWidgets
from ring_of_integers_modulo_n import Integers_Modulo_N, gcd, num_pairs, extended_euclide_alg

class Ui_window_1 (object):
    def setupUi(self, window_1):
        window_1.setObjectName("window_1")
        window_1.resize(611, 140)
        self.centralwidget = QtWidgets.QWidget(window_1)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(100, 10, 420, 30))
        self.title_label.setStyleSheet("\n"
"font: 14pt \"Trebuchet MS\";")
        self.title_label.setObjectName("title_label")
        self.dif_1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dif_1_btn.setGeometry(QtCore.QRect(97, 65, 200, 23))
        self.dif_1_btn.setStyleSheet("background-color: rgb(255, 131, 43);\n"
"font: 75 8pt \"Trebuchet MS\"")
        self.dif_1_btn.setObjectName("dif_1_btn")
        self.dif_3_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dif_3_btn.setGeometry(QtCore.QRect(97, 95, 413, 30))
        self.dif_3_btn.setStyleSheet("background-color: rgb(187, 14, 255);\n"
"font: 75 8pt \"Trebuchet MS\"")
        self.dif_3_btn.setObjectName("dif_3_btn")
        self.dif_2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dif_2_btn.setGeometry(QtCore.QRect(320, 65, 190, 23))
        self.dif_2_btn.setStyleSheet("background-color: rgb(255, 36, 8);\n"
"font: 75 8pt \"Trebuchet MS\"")
        self.dif_2_btn.setObjectName("dif_2_btn")
        self.start_label = QtWidgets.QLabel(self.centralwidget)
        self.start_label.setGeometry(QtCore.QRect(100, 40, 410, 20))
        self.start_label.setStyleSheet("")
        self.start_label.setObjectName("start_label")
        window_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(window_1)
        QtCore.QMetaObject.connectSlotsByName(window_1)
        self.add_functions()

        

    def retranslateUi(self, window_1):
        _translate = QtCore.QCoreApplication.translate
        window_1.setWindowTitle(_translate("window_1", "MainWindow"))
        self.title_label.setText(_translate("window_1", "Добро пожаловать в мир остатков по модулю!"))
        self.dif_1_btn.setText(_translate("window_1", "Я новенький"))
        self.dif_3_btn.setText(_translate("window_1", "Я преисполненный алгоритмами Евклида первородный алгебраический дух"))
        self.dif_2_btn.setText(_translate("window_1", "Я уже смешарик"))
        self.start_label.setText(_translate("window_1", "Автор предлагает вам выбрать, насколько вы желаете усложнить свою жизнь"))
    
    def show_window_2(self):
        self.window_2 = QtWidgets.QMainWindow()
        ui = Ui_window_2()
        ui.setupUi(self.window_2)
        self.window_2.show()

    def show_window_3(self):
        self.window_3 = QtWidgets.QMainWindow()
        ui = Ui_window_3()
        ui.setupUi(self.window_3)
        self.window_3.show()

    def show_window_4(self):
        self.window_4 = QtWidgets.QMainWindow()
        ui = Ui_window_4()
        ui.setupUi(self.window_4)
        self.window_4.show()
    
    def add_functions(self):
        self.dif_1_btn.clicked.connect(self.show_window_2)
        self.dif_2_btn.clicked.connect(self.show_window_3)
        self.dif_3_btn.clicked.connect(self.show_window_4)
        



class Ui_window_2(object):
    def setupUi(self, window_2):
        window_2.setObjectName("window_2")
        window_2.resize(611, 190)
        self.centralwidget = QtWidgets.QWidget(window_2)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_1 = QtWidgets.QLabel(self.centralwidget)
        self.lb_1.setGeometry(QtCore.QRect(30, 20, 600, 13))
        self.lb_1.setObjectName("lb_1")
        self.lb_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_2.setGeometry(QtCore.QRect(30, 35, 550, 13))
        self.lb_2.setObjectName("lb_2")
        self.le_value = QtWidgets.QLineEdit(self.centralwidget)
        self.le_value.setGeometry(QtCore.QRect(150, 70, 40, 30))
        self.le_value.setObjectName("le_value")
        self.le_module = QtWidgets.QLineEdit(self.centralwidget)
        self.le_module.setGeometry(QtCore.QRect(250, 70, 40, 30))
        self.le_module.setObjectName("le_module")
        self.lb_value = QtWidgets.QLabel(self.centralwidget)
        self.lb_value.setGeometry(QtCore.QRect(110, 80, 40, 10))
        self.lb_value.setObjectName("lb_value")
        self.lb_module = QtWidgets.QLabel(self.centralwidget)
        self.lb_module.setGeometry(QtCore.QRect(200, 80, 50, 12))
        self.lb_module.setObjectName("lb_module")
        self.lb_magic = QtWidgets.QLabel(self.centralwidget)
        self.lb_magic.setGeometry(QtCore.QRect(300, 80, 90, 13))
        self.lb_magic.setObjectName("lb_magic")
        self.lb_result = QtWidgets.QLabel(self.centralwidget)
        self.lb_result.setGeometry(QtCore.QRect(390, 80, 60, 13))
        self.lb_result.setObjectName("lb_result")
        self.le_res_numb = QtWidgets.QLineEdit(self.centralwidget)
        self.le_res_numb.setGeometry(QtCore.QRect(450, 70, 40, 30))
        self.le_res_numb.setObjectName("le_res_numb")
        self.lb_note = QtWidgets.QLabel(self.centralwidget)
        self.lb_note.setGeometry(QtCore.QRect(135, 110, 500, 13))
        self.lb_note.setObjectName("lb_note")
        self.go_btn = QtWidgets.QPushButton(self.centralwidget)
        self.go_btn.setGeometry(QtCore.QRect(270, 135, 80, 35))
        self.go_btn.setStyleSheet("\n"
"font: 75 12pt \"Trebuchet MS\";\n"
"background-color: rgb(255, 255, 127)")
        self.go_btn.setObjectName("go_btn")
        window_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(window_2)
        QtCore.QMetaObject.connectSlotsByName(window_2)
        self.go_btn_function()
        

    def retranslateUi(self, window_2):
        _translate = QtCore.QCoreApplication.translate
        window_2.setWindowTitle(_translate("window_2", "MainWindow"))
        self.lb_1.setText(_translate("window_2", "Итак, вы здесь впервые. Давайте разберемся как устроен этот мир и проникнемся сравнением по модулю"))
        self.lb_2.setText(_translate("window_2", "Введите число и модуль, а я вам скажу, что введенное число из себя представляет по заданному модулю"))
        self.lb_value.setText(_translate("window_2", "Число:"))
        self.lb_module.setText(_translate("window_2", "Модуль:"))
        self.lb_magic.setText(_translate("window_2", "*  колдунство *"))
        self.lb_result.setText(_translate("window_2", "Результат:"))
        self.lb_note.setText(_translate("window_2", "Примечание: Число должно быть целым, а модуль натуральным"))
        self.go_btn.setText(_translate("window_2", "Поехали!"))
    
    
    def go_btn_function(self):
        self.go_btn.clicked.connect(lambda: self.write_result(int(self.le_value.text()),int(self.le_module.text())))
        
    def write_result(self, value, module):
        vle = Integers_Modulo_N(value, module)
        self.le_res_numb.setText(vle.__str__())
        

class Ui_window_3(object):
    def setupUi(self, window_3):
        window_3.setObjectName("window_3")
        window_3.resize(700, 150)
        self.centralwidget = QtWidgets.QWidget(window_3)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_intro = QtWidgets.QLabel(self.centralwidget)
        self.lb_intro.setGeometry(QtCore.QRect(35, 20, 641, 16))
        self.lb_intro.setObjectName("lb_intro")
        self.lb_inp_offer = QtWidgets.QLabel(self.centralwidget)
        self.lb_inp_offer.setGeometry(QtCore.QRect(150, 40, 340, 13))
        self.lb_inp_offer.setObjectName("lb_inp_offer")
        self.le_op_numb_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_op_numb_1.setGeometry(QtCore.QRect(150, 60, 40, 30))
        self.le_op_numb_1.setObjectName("le_op_numb_1")
        self.le_op_numb_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_op_numb_2.setGeometry(QtCore.QRect(250, 60, 40, 30))
        self.le_op_numb_2.setObjectName("le_op_numb_2")
        self.le_op_result = QtWidgets.QLineEdit(self.centralwidget)
        self.le_op_result.setGeometry(QtCore.QRect(536, 60, 40, 30))
        self.le_op_result.setObjectName("le_op_result")
        self.lb_op_number_1 = QtWidgets.QLabel(self.centralwidget)
        self.lb_op_number_1.setGeometry(QtCore.QRect(100, 70, 47, 13))
        self.lb_op_number_1.setObjectName("lb_op_number_1")
        self.lb_op_number_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_op_number_2.setGeometry(QtCore.QRect(200, 70, 47, 13))
        self.lb_op_number_2.setObjectName("lb_op_number_2")
        self.lb_op_result = QtWidgets.QLabel(self.centralwidget)
        self.lb_op_result.setGeometry(QtCore.QRect(475, 70, 55, 13))
        self.lb_op_result.setObjectName("lb_op_result")
        self.lb_op_module = QtWidgets.QLabel(self.centralwidget)
        self.lb_op_module.setGeometry(QtCore.QRect(300, 70, 47, 13))
        self.lb_op_module.setObjectName("lb_op_module")
        self.le_op_module = QtWidgets.QLineEdit(self.centralwidget)
        self.le_op_module.setGeometry(QtCore.QRect(350, 60, 40, 30))
        self.le_op_module.setObjectName("le_op_module")
        self.lb_op_magic = QtWidgets.QLabel(self.centralwidget)
        self.lb_op_magic.setGeometry(QtCore.QRect(396, 70, 72, 13))
        self.lb_op_magic.setObjectName("lb_op_magic")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 80, 30))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 12pt \"Trebuchet MS\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 100, 130, 30))
        self.pushButton_2.setStyleSheet("font: 75 12pt \"Trebuchet MS\";\n"
"background-color: rgb(255, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 100, 230, 30))
        self.pushButton_3.setStyleSheet("font: 75 12pt \"Trebuchet MS\";\n"
"background-color: rgb(255, 170, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        window_3.setCentralWidget(self.centralwidget)

        self.retranslateUi(window_3)
        QtCore.QMetaObject.connectSlotsByName(window_3)
        self.add_functions_s()

    def retranslateUi(self, window_3):
        _translate = QtCore.QCoreApplication.translate
        window_3.setWindowTitle(_translate("window_3", "MainWindow"))
        self.lb_intro.setText(_translate("window_3", "Вы уже бывали здесь, стало быть можно повеселиться с операциями. Пока что доступны: сумма, разность и произведение."))
        self.lb_inp_offer.setText(_translate("window_3", "Введите два целых числа, которые станут нашими подопытными"))
        self.lb_op_number_1.setText(_translate("window_3", "Число 1:"))
        self.lb_op_number_2.setText(_translate("window_3", "Число 2:"))
        self.lb_op_result.setText(_translate("window_3", "Результат:"))
        self.lb_op_module.setText(_translate("window_3", "Модуль:"))
        self.lb_op_magic.setText(_translate("window_3", "*колдунство*l"))
        self.pushButton.setText(_translate("window_3", "Cумма"))
        self.pushButton_2.setText(_translate("window_3", "Произведение"))
        self.pushButton_3.setText(_translate("window_3", "Вычитание (Из 1-ого 2-ое)"))

    def add_functions_s(self):
        self.pushButton.clicked.connect(lambda: self.write_sum(int(self.le_op_numb_1.text()), int(self.le_op_numb_2.text()), int(self.le_op_module.text())))
        self.pushButton_2.clicked.connect(lambda: self.write_multp(int(self.le_op_numb_1.text()), int(self.le_op_numb_2.text()), int(self.le_op_module.text())))
        self.pushButton_3.clicked.connect(lambda: self.write_subtr(int(self.le_op_numb_1.text()), int(self.le_op_numb_2.text()), int(self.le_op_module.text())))

    def write_sum(self, number_1, number_2, module):
        term_1 = Integers_Modulo_N(number_1, module)
        term_2 = Integers_Modulo_N(number_2, module)
        sum = term_1 + term_2
        self.le_op_result.setText(sum.__str__())
    
    def write_multp(self, number_1, number_2, module):
        multiplier_1 = Integers_Modulo_N(number_1, module)
        multiplier_2 = Integers_Modulo_N(number_2, module)
        multp = multiplier_1 * multiplier_2
        self.le_op_result.setText(multp.__str__())
    
    def write_subtr(self, number_1, number_2, module):
        minuend = Integers_Modulo_N(number_1, module)
        subtracted = Integers_Modulo_N(number_2, module)
        subtr = minuend + subtracted.__neg__()
        self.le_op_result.setText(subtr.__str__())

    
class Ui_window_4(object):
    def setupUi(self, window_4):
        window_4.setObjectName("window_4")
        window_4.resize(750, 235)
        self.centralwidget = QtWidgets.QWidget(window_4)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_1.setGeometry(QtCore.QRect(30, 10, 700, 13))
        self.lbl_1.setObjectName("lbl_1")
        self.lbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(100, 30, 550, 13))
        self.lbl_2.setObjectName("lbl_2")
        self.lb_value = QtWidgets.QLabel(self.centralwidget)
        self.lb_value.setGeometry(QtCore.QRect(120, 60, 40, 10))
        self.lb_value.setObjectName("lb_value")
        self.led_value = QtWidgets.QLineEdit(self.centralwidget)
        self.led_value.setGeometry(QtCore.QRect(160, 50, 40, 30))
        self.led_value.setObjectName("led_value")
        self.lbl_module_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_module_1.setGeometry(QtCore.QRect(210, 60, 50, 12))
        self.lbl_module_1.setObjectName("lbl_module_1")
        self.lbl_magic_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_magic_1.setGeometry(QtCore.QRect(407, 60, 90, 13))
        self.lbl_magic_1.setObjectName("lbl_magic_1")
        self.lbl_result_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_1.setGeometry(QtCore.QRect(515, 60, 60, 13))
        self.lbl_result_1.setObjectName("lbl_result_1")
        self.led_module = QtWidgets.QLineEdit(self.centralwidget)
        self.led_module.setGeometry(QtCore.QRect(260, 50, 40, 30))
        self.led_module.setObjectName("led_module")
        self.led_result_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.led_result_1.setGeometry(QtCore.QRect(580, 50, 40, 30))
        self.led_result_1.setObjectName("led_result_1")
        self.vzuh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.vzuh_btn.setGeometry(QtCore.QRect(325, 55, 60, 20))
        self.vzuh_btn.setStyleSheet("font: 75 italic 12pt \"Times New Roman\";\n"
"\n"
"background-color: rgb(170, 85, 255)")
        self.vzuh_btn.setObjectName("vzuh_btn")
        self.lbl_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_3.setGeometry(QtCore.QRect(60, 90, 650, 13))
        self.lbl_3.setObjectName("lbl_3")
        self.lbl_note = QtWidgets.QLabel(self.centralwidget)
        self.lbl_note.setGeometry(QtCore.QRect(340, 75, 60, 13))
        self.lbl_note.setStyleSheet("font: italic 7pt \"Times New Roman\";")
        self.lbl_note.setObjectName("lbl_note")
        self.lbl_dividend = QtWidgets.QLabel(self.centralwidget)
        self.lbl_dividend.setGeometry(QtCore.QRect(120, 120, 50, 13))
        self.lbl_dividend.setObjectName("lbl_dividend")
        self.lbl_divider = QtWidgets.QLabel(self.centralwidget)
        self.lbl_divider.setGeometry(QtCore.QRect(220, 120, 60, 13))
        self.lbl_divider.setObjectName("lbl_divider")
        self.division_btn = QtWidgets.QPushButton(self.centralwidget)
        self.division_btn.setGeometry(QtCore.QRect(300, 150, 150, 30))
        self.division_btn.setStyleSheet("background-color: rgb(170, 85, 127);\n"
"font: 75 12pt \"Trebuchet MS\";")
        self.division_btn.setObjectName("division_btn")
        self.led_value_dnd = QtWidgets.QLineEdit(self.centralwidget)
        self.led_value_dnd.setGeometry(QtCore.QRect(170, 110, 40, 30))
        self.led_value_dnd.setObjectName("led_value_dnd")
        self.led_value_dder = QtWidgets.QLineEdit(self.centralwidget)
        self.led_value_dder.setGeometry(QtCore.QRect(280, 110, 40, 30))
        self.led_value_dder.setObjectName("led_value_dder")
        self.lbl_module_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_module_2.setGeometry(QtCore.QRect(330, 120, 50, 12))
        self.lbl_module_2.setObjectName("lbl_module_2")
        self.led_module_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.led_module_2.setGeometry(QtCore.QRect(380, 110, 40, 30))
        self.led_module_2.setObjectName("led_module_2")
        self.lbl_magic_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_magic_2.setGeometry(QtCore.QRect(430, 120, 90, 13))
        self.lbl_magic_2.setObjectName("lbl_magic_2")
        self.led_result_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.led_result_2.setGeometry(QtCore.QRect(580, 110, 40, 30))
        self.led_result_2.setObjectName("led_result_2")
        self.lbl_result_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_2.setGeometry(QtCore.QRect(520, 120, 60, 13))
        self.lbl_result_2.setObjectName("lbl_result_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 190, 500, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(65, 205, 620, 20))
        self.label_2.setObjectName("label_2")
        window_4.setCentralWidget(self.centralwidget)

        self.retranslateUi(window_4)
        QtCore.QMetaObject.connectSlotsByName(window_4)
        self.add_functions_ss()
        self.add_functions_sss()

    def retranslateUi(self, window_4):
        _translate = QtCore.QCoreApplication.translate
        window_4.setWindowTitle(_translate("window_4", "MainWindow"))
        self.lbl_1.setText(_translate("window_4", "Вы уже знакомы с обычными операциями. Самое время научиться делению! Однако делить тут можно только на обратимые элементы"))
        self.lbl_2.setText(_translate("window_4", "Введите целое число и модуль, а я вам скажу, является ли ваше число обратимым по заданному модулю"))
        self.lb_value.setText(_translate("window_4", "Число:"))
        self.lbl_module_1.setText(_translate("window_4", "Модуль:"))
        self.lbl_magic_1.setText(_translate("window_4", "*  колдунство *"))
        self.lbl_result_1.setText(_translate("window_4", "Результат:"))
        self.vzuh_btn.setText(_translate("window_4", "Вжухх"))
        self.lbl_3.setText(_translate("window_4", "Теперь можно делить чиселки со спокойной душой. Введите делимое, модуль и делитель (сперва проверьте обратимость)"))
        self.lbl_note.setText(_translate("window_4", "кнопка"))
        self.lbl_dividend.setText(_translate("window_4", "Делимое:"))
        self.lbl_divider.setText(_translate("window_4", "Делитель:"))
        self.division_btn.setText(_translate("window_4", "Поделить"))
        self.lbl_module_2.setText(_translate("window_4", "Модуль:"))
        self.lbl_magic_2.setText(_translate("window_4", "*  колдунство *"))
        self.lbl_result_2.setText(_translate("window_4", "Результат:"))
        self.label.setText(_translate("window_4", "Я бы мог и сам по себе обратный элемент вам сообщать, однако делать я это не буду, хыхы."))
        self.label_2.setText(_translate("window_4", "Однако прежде чем злиться на меня, подумайте, как этот обратный элемент получить при поиощи того, что на экране"))



    def add_functions_ss(self):
        self.vzuh_btn.clicked.connect(lambda: self.write_reverse(int(self.led_value.text()),int(self.led_module.text())))
        
    def add_functions_sss(self):
        self.division_btn.clicked.connect(lambda: self.write_div(int(self.led_value_dnd.text()), int(self.led_value_dder.text()), int(self.led_module_2.text())))

    def write_reverse(self, number, module):
        element = Integers_Modulo_N(number, module)
        self.led_result_1.setText(str(element.__reversibility__()))
    
    def write_div(self, number_1, number_2, module):
        dividend = Integers_Modulo_N(number_1, module)
        divider = Integers_Modulo_N(number_2, module)
        div_value = dividend / divider
        self.led_result_2.setText(div_value.__str__())












if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_1 = QtWidgets.QMainWindow()
    ui = Ui_window_1()
    ui.setupUi(window_1)
    window_1.show()
    sys.exit(app.exec_())

