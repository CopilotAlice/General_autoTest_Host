# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Automated_testing2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QTabWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1268, 1045)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 11, -1)
        self.widget1 = QWidget(self.groupBox_2)
        self.widget1.setObjectName(u"widget1")
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(self.widget1)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy2)
        self.radioButton.setCheckable(False)
        self.radioButton.setChecked(False)

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.comboBox_com_select = QComboBox(self.widget1)
        self.comboBox_com_select.addItem("")
        self.comboBox_com_select.addItem("")
        self.comboBox_com_select.setObjectName(u"comboBox_com_select")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_com_select.sizePolicy().hasHeightForWidth())
        self.comboBox_com_select.setSizePolicy(sizePolicy3)
        self.comboBox_com_select.setMinimumSize(QSize(0, 25))
        self.comboBox_com_select.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_com_select)

        self.comboBox_baund_select = QComboBox(self.widget1)
        self.comboBox_baund_select.addItem("")
        self.comboBox_baund_select.addItem("")
        self.comboBox_baund_select.addItem("")
        self.comboBox_baund_select.addItem("")
        self.comboBox_baund_select.setObjectName(u"comboBox_baund_select")
        self.comboBox_baund_select.setMinimumSize(QSize(0, 25))
        self.comboBox_baund_select.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_baund_select)

        self.comboBox_check_select = QComboBox(self.widget1)
        self.comboBox_check_select.addItem("")
        self.comboBox_check_select.addItem("")
        self.comboBox_check_select.addItem("")
        self.comboBox_check_select.setObjectName(u"comboBox_check_select")
        self.comboBox_check_select.setMinimumSize(QSize(0, 25))
        self.comboBox_check_select.setEditable(False)

        self.horizontalLayout_2.addWidget(self.comboBox_check_select)


        self.verticalLayout_2.addWidget(self.widget1)

        self.widget2 = QWidget(self.groupBox_2)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.comboBox_rulename = QComboBox(self.widget2)
        self.comboBox_rulename.addItem("")
        self.comboBox_rulename.setObjectName(u"comboBox_rulename")
        self.comboBox_rulename.setEditable(True)

        self.horizontalLayout_3.addWidget(self.comboBox_rulename)


        self.verticalLayout_2.addWidget(self.widget2)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, -1, 11, 11)
        self.widget3 = QWidget(self.groupBox)
        self.widget3.setObjectName(u"widget3")
        sizePolicy1.setHeightForWidth(self.widget3.sizePolicy().hasHeightForWidth())
        self.widget3.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_turntable_check = QRadioButton(self.widget3)
        self.radioButton_turntable_check.setObjectName(u"radioButton_turntable_check")
        self.radioButton_turntable_check.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.radioButton_turntable_check.sizePolicy().hasHeightForWidth())
        self.radioButton_turntable_check.setSizePolicy(sizePolicy4)
        self.radioButton_turntable_check.setMouseTracking(True)
        self.radioButton_turntable_check.setAcceptDrops(False)
        self.radioButton_turntable_check.setCheckable(True)
        self.radioButton_turntable_check.setChecked(False)
        self.radioButton_turntable_check.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.radioButton_turntable_check)

        self.combox_turntable_com = QComboBox(self.widget3)
        self.combox_turntable_com.addItem("")
        self.combox_turntable_com.addItem("")
        self.combox_turntable_com.addItem("")
        self.combox_turntable_com.addItem("")
        self.combox_turntable_com.addItem("")
        self.combox_turntable_com.setObjectName(u"combox_turntable_com")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.combox_turntable_com.sizePolicy().hasHeightForWidth())
        self.combox_turntable_com.setSizePolicy(sizePolicy5)
        self.combox_turntable_com.setEditable(True)

        self.horizontalLayout.addWidget(self.combox_turntable_com)

        self.pushButton_com_open = QPushButton(self.widget3)
        self.pushButton_com_open.setObjectName(u"pushButton_com_open")
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_com_open.sizePolicy().hasHeightForWidth())
        self.pushButton_com_open.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.pushButton_com_open)

        self.pushButton_com_close = QPushButton(self.widget3)
        self.pushButton_com_close.setObjectName(u"pushButton_com_close")
        sizePolicy6.setHeightForWidth(self.pushButton_com_close.sizePolicy().hasHeightForWidth())
        self.pushButton_com_close.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.pushButton_com_close)


        self.verticalLayout.addWidget(self.widget3)

        self.widget4 = QWidget(self.groupBox)
        self.widget4.setObjectName(u"widget4")
        self.gridLayout = QGridLayout(self.widget4)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_outside_location = QLineEdit(self.widget4)
        self.lineEdit_outside_location.setObjectName(u"lineEdit_outside_location")
        sizePolicy6.setHeightForWidth(self.lineEdit_outside_location.sizePolicy().hasHeightForWidth())
        self.lineEdit_outside_location.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.lineEdit_outside_location, 3, 3, 1, 1)

        self.lineEdit_outside_acceleration = QLineEdit(self.widget4)
        self.lineEdit_outside_acceleration.setObjectName(u"lineEdit_outside_acceleration")
        sizePolicy6.setHeightForWidth(self.lineEdit_outside_acceleration.sizePolicy().hasHeightForWidth())
        self.lineEdit_outside_acceleration.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.lineEdit_outside_acceleration, 5, 3, 1, 1)

        self.lineEdit_outside_speed = QLineEdit(self.widget4)
        self.lineEdit_outside_speed.setObjectName(u"lineEdit_outside_speed")
        sizePolicy6.setHeightForWidth(self.lineEdit_outside_speed.sizePolicy().hasHeightForWidth())
        self.lineEdit_outside_speed.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.lineEdit_outside_speed, 4, 3, 1, 1)

        self.pushButton_inside_reset = QPushButton(self.widget4)
        self.pushButton_inside_reset.setObjectName(u"pushButton_inside_reset")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_inside_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_inside_reset.setSizePolicy(sizePolicy7)
        self.pushButton_inside_reset.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.pushButton_inside_reset, 6, 0, 1, 1)

        self.label_2 = QLabel(self.widget4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.label_6 = QLabel(self.widget4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)

        self.label_3 = QLabel(self.widget4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.widget4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.lcdNumber_inside_location = QLCDNumber(self.widget4)
        self.lcdNumber_inside_location.setObjectName(u"lcdNumber_inside_location")
        sizePolicy8 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.lcdNumber_inside_location.sizePolicy().hasHeightForWidth())
        self.lcdNumber_inside_location.setSizePolicy(sizePolicy8)
        self.lcdNumber_inside_location.setMinimumSize(QSize(0, 25))
        self.lcdNumber_inside_location.setSmallDecimalPoint(True)
        self.lcdNumber_inside_location.setDigitCount(6)
        self.lcdNumber_inside_location.setMode(QLCDNumber.Dec)
        self.lcdNumber_inside_location.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_inside_location.setProperty("value", 0.001000000000000)

        self.gridLayout.addWidget(self.lcdNumber_inside_location, 1, 1, 1, 1)

        self.pushButton_outside_reset = QPushButton(self.widget4)
        self.pushButton_outside_reset.setObjectName(u"pushButton_outside_reset")
        sizePolicy1.setHeightForWidth(self.pushButton_outside_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_outside_reset.setSizePolicy(sizePolicy1)
        self.pushButton_outside_reset.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.pushButton_outside_reset, 6, 2, 1, 1)

        self.lcdNumber_outside_location = QLCDNumber(self.widget4)
        self.lcdNumber_outside_location.setObjectName(u"lcdNumber_outside_location")
        sizePolicy8.setHeightForWidth(self.lcdNumber_outside_location.sizePolicy().hasHeightForWidth())
        self.lcdNumber_outside_location.setSizePolicy(sizePolicy8)
        self.lcdNumber_outside_location.setMinimumSize(QSize(0, 0))
        self.lcdNumber_outside_location.setSmallDecimalPoint(True)
        self.lcdNumber_outside_location.setDigitCount(6)
        self.lcdNumber_outside_location.setMode(QLCDNumber.Dec)
        self.lcdNumber_outside_location.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_outside_location.setProperty("value", 360.011000000000024)

        self.gridLayout.addWidget(self.lcdNumber_outside_location, 1, 3, 1, 1)

        self.lcdNumber_inside_speed = QLCDNumber(self.widget4)
        self.lcdNumber_inside_speed.setObjectName(u"lcdNumber_inside_speed")
        sizePolicy8.setHeightForWidth(self.lcdNumber_inside_speed.sizePolicy().hasHeightForWidth())
        self.lcdNumber_inside_speed.setSizePolicy(sizePolicy8)
        self.lcdNumber_inside_speed.setMinimumSize(QSize(0, 25))
        self.lcdNumber_inside_speed.setSmallDecimalPoint(True)
        self.lcdNumber_inside_speed.setDigitCount(5)
        self.lcdNumber_inside_speed.setMode(QLCDNumber.Dec)
        self.lcdNumber_inside_speed.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_inside_speed.setProperty("value", 0.000000000000000)

        self.gridLayout.addWidget(self.lcdNumber_inside_speed, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.lineEdit_inside_location = QLineEdit(self.widget4)
        self.lineEdit_inside_location.setObjectName(u"lineEdit_inside_location")
        sizePolicy6.setHeightForWidth(self.lineEdit_inside_location.sizePolicy().hasHeightForWidth())
        self.lineEdit_inside_location.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.lineEdit_inside_location, 3, 1, 1, 1)

        self.pushButton_start_location = QPushButton(self.widget4)
        self.pushButton_start_location.setObjectName(u"pushButton_start_location")

        self.gridLayout.addWidget(self.pushButton_start_location, 6, 1, 1, 1)

        self.label_7 = QLabel(self.widget4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)

        self.pushButton_start_speed = QPushButton(self.widget4)
        self.pushButton_start_speed.setObjectName(u"pushButton_start_speed")

        self.gridLayout.addWidget(self.pushButton_start_speed, 6, 3, 1, 1)

        self.label_10 = QLabel(self.widget4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 0, 3, 1, 1)

        self.label_12 = QLabel(self.widget4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)

        self.lineEdit_inside_speed = QLineEdit(self.widget4)
        self.lineEdit_inside_speed.setObjectName(u"lineEdit_inside_speed")
        sizePolicy6.setHeightForWidth(self.lineEdit_inside_speed.sizePolicy().hasHeightForWidth())
        self.lineEdit_inside_speed.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.lineEdit_inside_speed, 4, 1, 1, 1)

        self.lcdNumber_outside_speed = QLCDNumber(self.widget4)
        self.lcdNumber_outside_speed.setObjectName(u"lcdNumber_outside_speed")
        sizePolicy8.setHeightForWidth(self.lcdNumber_outside_speed.sizePolicy().hasHeightForWidth())
        self.lcdNumber_outside_speed.setSizePolicy(sizePolicy8)
        self.lcdNumber_outside_speed.setMinimumSize(QSize(0, 0))
        self.lcdNumber_outside_speed.setSmallDecimalPoint(True)
        self.lcdNumber_outside_speed.setDigitCount(5)
        self.lcdNumber_outside_speed.setMode(QLCDNumber.Dec)
        self.lcdNumber_outside_speed.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_outside_speed.setProperty("value", 0.000000000000000)
        self.lcdNumber_outside_speed.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber_outside_speed, 2, 3, 1, 1)

        self.label_5 = QLabel(self.widget4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_inside_acceleration = QLineEdit(self.widget4)
        self.lineEdit_inside_acceleration.setObjectName(u"lineEdit_inside_acceleration")
        sizePolicy6.setHeightForWidth(self.lineEdit_inside_acceleration.sizePolicy().hasHeightForWidth())
        self.lineEdit_inside_acceleration.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.lineEdit_inside_acceleration, 5, 1, 1, 1)

        self.label_4 = QLabel(self.widget4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_13 = QLabel(self.widget4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 5, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget4)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_turntable_check_2 = QRadioButton(self.groupBox_3)
        self.radioButton_turntable_check_2.setObjectName(u"radioButton_turntable_check_2")
        self.radioButton_turntable_check_2.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.radioButton_turntable_check_2.sizePolicy().hasHeightForWidth())
        self.radioButton_turntable_check_2.setSizePolicy(sizePolicy4)
        self.radioButton_turntable_check_2.setMouseTracking(True)
        self.radioButton_turntable_check_2.setAcceptDrops(False)
        self.radioButton_turntable_check_2.setCheckable(True)
        self.radioButton_turntable_check_2.setChecked(False)
        self.radioButton_turntable_check_2.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.radioButton_turntable_check_2)

        self.combox_turntable_com_2 = QComboBox(self.groupBox_3)
        self.combox_turntable_com_2.addItem("")
        self.combox_turntable_com_2.addItem("")
        self.combox_turntable_com_2.addItem("")
        self.combox_turntable_com_2.addItem("")
        self.combox_turntable_com_2.addItem("")
        self.combox_turntable_com_2.setObjectName(u"combox_turntable_com_2")
        sizePolicy5.setHeightForWidth(self.combox_turntable_com_2.sizePolicy().hasHeightForWidth())
        self.combox_turntable_com_2.setSizePolicy(sizePolicy5)
        self.combox_turntable_com_2.setEditable(True)

        self.horizontalLayout_4.addWidget(self.combox_turntable_com_2)

        self.pushButton_com_open_2 = QPushButton(self.groupBox_3)
        self.pushButton_com_open_2.setObjectName(u"pushButton_com_open_2")
        sizePolicy6.setHeightForWidth(self.pushButton_com_open_2.sizePolicy().hasHeightForWidth())
        self.pushButton_com_open_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.pushButton_com_open_2)

        self.pushButton_com_close_2 = QPushButton(self.groupBox_3)
        self.pushButton_com_close_2.setObjectName(u"pushButton_com_close_2")
        sizePolicy6.setHeightForWidth(self.pushButton_com_close_2.sizePolicy().hasHeightForWidth())
        self.pushButton_com_close_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.pushButton_com_close_2)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.combox_turntable_com_3 = QComboBox(self.groupBox_4)
        self.combox_turntable_com_3.addItem("")
        self.combox_turntable_com_3.addItem("")
        self.combox_turntable_com_3.addItem("")
        self.combox_turntable_com_3.addItem("")
        self.combox_turntable_com_3.addItem("")
        self.combox_turntable_com_3.setObjectName(u"combox_turntable_com_3")
        sizePolicy5.setHeightForWidth(self.combox_turntable_com_3.sizePolicy().hasHeightForWidth())
        self.combox_turntable_com_3.setSizePolicy(sizePolicy5)
        self.combox_turntable_com_3.setMinimumSize(QSize(0, 0))
        self.combox_turntable_com_3.setEditable(True)

        self.gridLayout_3.addWidget(self.combox_turntable_com_3, 0, 1, 1, 1)

        self.pushButton_com_close_3 = QPushButton(self.groupBox_4)
        self.pushButton_com_close_3.setObjectName(u"pushButton_com_close_3")
        sizePolicy6.setHeightForWidth(self.pushButton_com_close_3.sizePolicy().hasHeightForWidth())
        self.pushButton_com_close_3.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.pushButton_com_close_3, 0, 3, 1, 1)

        self.pushButton_com_open_3 = QPushButton(self.groupBox_4)
        self.pushButton_com_open_3.setObjectName(u"pushButton_com_open_3")
        sizePolicy6.setHeightForWidth(self.pushButton_com_open_3.sizePolicy().hasHeightForWidth())
        self.pushButton_com_open_3.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.pushButton_com_open_3, 0, 2, 1, 1)

        self.lcdNumber_inside_speed_4 = QLCDNumber(self.groupBox_4)
        self.lcdNumber_inside_speed_4.setObjectName(u"lcdNumber_inside_speed_4")
        self.lcdNumber_inside_speed_4.setMinimumSize(QSize(0, 25))
        self.lcdNumber_inside_speed_4.setSmallDecimalPoint(True)
        self.lcdNumber_inside_speed_4.setDigitCount(5)
        self.lcdNumber_inside_speed_4.setMode(QLCDNumber.Dec)
        self.lcdNumber_inside_speed_4.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_inside_speed_4.setProperty("value", 0.000000000000000)

        self.gridLayout_3.addWidget(self.lcdNumber_inside_speed_4, 1, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        sizePolicy7.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy7)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)

        self.lcdNumber_outside_speed_2 = QLCDNumber(self.groupBox_4)
        self.lcdNumber_outside_speed_2.setObjectName(u"lcdNumber_outside_speed_2")
        self.lcdNumber_outside_speed_2.setMinimumSize(QSize(0, 25))
        self.lcdNumber_outside_speed_2.setSmallDecimalPoint(True)
        self.lcdNumber_outside_speed_2.setDigitCount(5)
        self.lcdNumber_outside_speed_2.setMode(QLCDNumber.Dec)
        self.lcdNumber_outside_speed_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_outside_speed_2.setProperty("value", 0.000000000000000)
        self.lcdNumber_outside_speed_2.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.lcdNumber_outside_speed_2, 1, 3, 1, 1)

        self.radioButton_turntable_check_3 = QRadioButton(self.groupBox_4)
        self.radioButton_turntable_check_3.setObjectName(u"radioButton_turntable_check_3")
        self.radioButton_turntable_check_3.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.radioButton_turntable_check_3.sizePolicy().hasHeightForWidth())
        self.radioButton_turntable_check_3.setSizePolicy(sizePolicy4)
        self.radioButton_turntable_check_3.setMouseTracking(True)
        self.radioButton_turntable_check_3.setAcceptDrops(False)
        self.radioButton_turntable_check_3.setCheckable(True)
        self.radioButton_turntable_check_3.setChecked(False)
        self.radioButton_turntable_check_3.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radioButton_turntable_check_3, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalWidget_2 = QWidget(self.groupBox_5)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy9)
        self.horizontalWidget_2.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_inside_speed_2 = QLCDNumber(self.horizontalWidget_2)
        self.lcdNumber_inside_speed_2.setObjectName(u"lcdNumber_inside_speed_2")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.lcdNumber_inside_speed_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_inside_speed_2.setSizePolicy(sizePolicy10)
        self.lcdNumber_inside_speed_2.setMinimumSize(QSize(0, 25))
        self.lcdNumber_inside_speed_2.setSmallDecimalPoint(True)
        self.lcdNumber_inside_speed_2.setDigitCount(4)
        self.lcdNumber_inside_speed_2.setMode(QLCDNumber.Dec)
        self.lcdNumber_inside_speed_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_inside_speed_2.setProperty("value", 0.000000000000000)

        self.horizontalLayout_6.addWidget(self.lcdNumber_inside_speed_2)

        self.pushButton_openFile = QPushButton(self.horizontalWidget_2)
        self.pushButton_openFile.setObjectName(u"pushButton_openFile")
        sizePolicy10.setHeightForWidth(self.pushButton_openFile.sizePolicy().hasHeightForWidth())
        self.pushButton_openFile.setSizePolicy(sizePolicy10)

        self.horizontalLayout_6.addWidget(self.pushButton_openFile)

        self.pushButton_reloadFile = QPushButton(self.horizontalWidget_2)
        self.pushButton_reloadFile.setObjectName(u"pushButton_reloadFile")
        sizePolicy10.setHeightForWidth(self.pushButton_reloadFile.sizePolicy().hasHeightForWidth())
        self.pushButton_reloadFile.setSizePolicy(sizePolicy10)

        self.horizontalLayout_6.addWidget(self.pushButton_reloadFile)


        self.verticalLayout_5.addWidget(self.horizontalWidget_2)

        self.textBrowser_filePath = QTextBrowser(self.groupBox_5)
        self.textBrowser_filePath.setObjectName(u"textBrowser_filePath")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.textBrowser_filePath.sizePolicy().hasHeightForWidth())
        self.textBrowser_filePath.setSizePolicy(sizePolicy11)
        self.textBrowser_filePath.setMinimumSize(QSize(0, 0))
        self.textBrowser_filePath.setMaximumSize(QSize(16777215, 16777215))
        self.textBrowser_filePath.setSizeIncrement(QSize(0, 0))
        self.textBrowser_filePath.setLineWrapMode(QTextEdit.NoWrap)
        self.textBrowser_filePath.setReadOnly(False)
        self.textBrowser_filePath.setOverwriteMode(False)
        self.textBrowser_filePath.setAcceptRichText(True)

        self.verticalLayout_5.addWidget(self.textBrowser_filePath)


        self.verticalLayout_4.addWidget(self.groupBox_5)


        self.horizontalLayout_5.addWidget(self.widget)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy12)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 831, 481))
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(0, 25))
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 1)
        self.combox_set_baund_12 = QComboBox(self.frame_2)
        self.combox_set_baund_12.addItem("")
        self.combox_set_baund_12.addItem("")
        self.combox_set_baund_12.addItem("")
        self.combox_set_baund_12.addItem("")
        self.combox_set_baund_12.addItem("")
        self.combox_set_baund_12.setObjectName(u"combox_set_baund_12")
        self.combox_set_baund_12.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_12.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_12, 11, 2, 1, 1)

        self.lineEdit_file_names_11 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_11.setObjectName(u"lineEdit_file_names_11")
        self.lineEdit_file_names_11.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_11, 10, 6, 1, 1)

        self.comboBox_stopbit_6 = QComboBox(self.frame_2)
        self.comboBox_stopbit_6.addItem("")
        self.comboBox_stopbit_6.addItem("")
        self.comboBox_stopbit_6.setObjectName(u"comboBox_stopbit_6")
        self.comboBox_stopbit_6.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_6, 5, 4, 1, 1)

        self.pushButton_com_open_6 = QPushButton(self.frame_2)
        self.pushButton_com_open_6.setObjectName(u"pushButton_com_open_6")
        self.pushButton_com_open_6.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_6.setAutoDefault(False)
        self.pushButton_com_open_6.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_6, 5, 5, 1, 1)

        self.comboBox_set_check_4 = QComboBox(self.frame_2)
        self.comboBox_set_check_4.addItem("")
        self.comboBox_set_check_4.addItem("")
        self.comboBox_set_check_4.addItem("")
        self.comboBox_set_check_4.setObjectName(u"comboBox_set_check_4")
        self.comboBox_set_check_4.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_4, 3, 3, 1, 1)

        self.label_51 = QLabel(self.frame_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_51, 6, 0, 1, 1)

        self.combox_set_com_11 = QComboBox(self.frame_2)
        self.combox_set_com_11.addItem("")
        self.combox_set_com_11.addItem("")
        self.combox_set_com_11.addItem("")
        self.combox_set_com_11.addItem("")
        self.combox_set_com_11.addItem("")
        self.combox_set_com_11.setObjectName(u"combox_set_com_11")
        self.combox_set_com_11.setMinimumSize(QSize(0, 30))
        self.combox_set_com_11.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_11, 10, 1, 1, 1)

        self.combox_set_baund_7 = QComboBox(self.frame_2)
        self.combox_set_baund_7.addItem("")
        self.combox_set_baund_7.addItem("")
        self.combox_set_baund_7.addItem("")
        self.combox_set_baund_7.addItem("")
        self.combox_set_baund_7.addItem("")
        self.combox_set_baund_7.setObjectName(u"combox_set_baund_7")
        self.combox_set_baund_7.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_7.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_7, 6, 2, 1, 1)

        self.comboBox_stopbit_12 = QComboBox(self.frame_2)
        self.comboBox_stopbit_12.addItem("")
        self.comboBox_stopbit_12.addItem("")
        self.comboBox_stopbit_12.setObjectName(u"comboBox_stopbit_12")
        self.comboBox_stopbit_12.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_12, 11, 4, 1, 1)

        self.pushButton_com_open_8 = QPushButton(self.frame_2)
        self.pushButton_com_open_8.setObjectName(u"pushButton_com_open_8")
        self.pushButton_com_open_8.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_8.setCheckable(False)
        self.pushButton_com_open_8.setAutoDefault(False)
        self.pushButton_com_open_8.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_8, 1, 5, 1, 1)

        self.combox_set_baund_1 = QComboBox(self.frame_2)
        self.combox_set_baund_1.addItem("")
        self.combox_set_baund_1.addItem("")
        self.combox_set_baund_1.addItem("")
        self.combox_set_baund_1.addItem("")
        self.combox_set_baund_1.addItem("")
        self.combox_set_baund_1.setObjectName(u"combox_set_baund_1")
        self.combox_set_baund_1.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_1.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_1, 0, 2, 1, 1)

        self.comboBox_set_check_8 = QComboBox(self.frame_2)
        self.comboBox_set_check_8.addItem("")
        self.comboBox_set_check_8.addItem("")
        self.comboBox_set_check_8.addItem("")
        self.comboBox_set_check_8.setObjectName(u"comboBox_set_check_8")
        self.comboBox_set_check_8.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_8, 7, 3, 1, 1)

        self.combox_set_com_5 = QComboBox(self.frame_2)
        self.combox_set_com_5.addItem("")
        self.combox_set_com_5.addItem("")
        self.combox_set_com_5.addItem("")
        self.combox_set_com_5.addItem("")
        self.combox_set_com_5.addItem("")
        self.combox_set_com_5.setObjectName(u"combox_set_com_5")
        self.combox_set_com_5.setMinimumSize(QSize(0, 30))
        self.combox_set_com_5.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_5, 4, 1, 1, 1)

        self.comboBox_stopbit_10 = QComboBox(self.frame_2)
        self.comboBox_stopbit_10.addItem("")
        self.comboBox_stopbit_10.addItem("")
        self.comboBox_stopbit_10.setObjectName(u"comboBox_stopbit_10")
        self.comboBox_stopbit_10.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_10, 9, 4, 1, 1)

        self.comboBox_stopbit_3 = QComboBox(self.frame_2)
        self.comboBox_stopbit_3.addItem("")
        self.comboBox_stopbit_3.addItem("")
        self.comboBox_stopbit_3.setObjectName(u"comboBox_stopbit_3")
        self.comboBox_stopbit_3.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_3, 2, 4, 1, 1)

        self.comboBox_set_check_3 = QComboBox(self.frame_2)
        self.comboBox_set_check_3.addItem("")
        self.comboBox_set_check_3.addItem("")
        self.comboBox_set_check_3.addItem("")
        self.comboBox_set_check_3.setObjectName(u"comboBox_set_check_3")
        self.comboBox_set_check_3.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_3, 2, 3, 1, 1)

        self.combox_set_com_2 = QComboBox(self.frame_2)
        self.combox_set_com_2.addItem("")
        self.combox_set_com_2.addItem("")
        self.combox_set_com_2.addItem("")
        self.combox_set_com_2.addItem("")
        self.combox_set_com_2.addItem("")
        self.combox_set_com_2.setObjectName(u"combox_set_com_2")
        self.combox_set_com_2.setMinimumSize(QSize(0, 30))
        self.combox_set_com_2.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_2, 1, 1, 1, 1)

        self.comboBox_stopbit_5 = QComboBox(self.frame_2)
        self.comboBox_stopbit_5.addItem("")
        self.comboBox_stopbit_5.addItem("")
        self.comboBox_stopbit_5.setObjectName(u"comboBox_stopbit_5")
        self.comboBox_stopbit_5.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_5, 4, 4, 1, 1)

        self.pushButton_com_open_10 = QPushButton(self.frame_2)
        self.pushButton_com_open_10.setObjectName(u"pushButton_com_open_10")
        self.pushButton_com_open_10.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_10.setAutoDefault(False)
        self.pushButton_com_open_10.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_10, 9, 5, 1, 1)

        self.pushButton_com_open_14 = QPushButton(self.frame_2)
        self.pushButton_com_open_14.setObjectName(u"pushButton_com_open_14")
        self.pushButton_com_open_14.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_14.setAutoDefault(False)
        self.pushButton_com_open_14.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_14, 7, 5, 1, 1)

        self.comboBox_set_check_9 = QComboBox(self.frame_2)
        self.comboBox_set_check_9.addItem("")
        self.comboBox_set_check_9.addItem("")
        self.comboBox_set_check_9.addItem("")
        self.comboBox_set_check_9.setObjectName(u"comboBox_set_check_9")
        self.comboBox_set_check_9.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_9, 8, 3, 1, 1)

        self.combox_set_com_8 = QComboBox(self.frame_2)
        self.combox_set_com_8.addItem("")
        self.combox_set_com_8.addItem("")
        self.combox_set_com_8.addItem("")
        self.combox_set_com_8.addItem("")
        self.combox_set_com_8.addItem("")
        self.combox_set_com_8.setObjectName(u"combox_set_com_8")
        self.combox_set_com_8.setMinimumSize(QSize(0, 30))
        self.combox_set_com_8.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_8, 7, 1, 1, 1)

        self.lineEdit_file_names_6 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_6.setObjectName(u"lineEdit_file_names_6")
        self.lineEdit_file_names_6.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_6, 5, 6, 1, 1)

        self.combox_set_baund_9 = QComboBox(self.frame_2)
        self.combox_set_baund_9.addItem("")
        self.combox_set_baund_9.addItem("")
        self.combox_set_baund_9.addItem("")
        self.combox_set_baund_9.addItem("")
        self.combox_set_baund_9.addItem("")
        self.combox_set_baund_9.setObjectName(u"combox_set_baund_9")
        self.combox_set_baund_9.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_9.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_9, 8, 2, 1, 1)

        self.combox_set_com_12 = QComboBox(self.frame_2)
        self.combox_set_com_12.addItem("")
        self.combox_set_com_12.addItem("")
        self.combox_set_com_12.addItem("")
        self.combox_set_com_12.addItem("")
        self.combox_set_com_12.addItem("")
        self.combox_set_com_12.setObjectName(u"combox_set_com_12")
        self.combox_set_com_12.setMinimumSize(QSize(0, 30))
        self.combox_set_com_12.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_12, 11, 1, 1, 1)

        self.combox_set_com_6 = QComboBox(self.frame_2)
        self.combox_set_com_6.addItem("")
        self.combox_set_com_6.addItem("")
        self.combox_set_com_6.addItem("")
        self.combox_set_com_6.addItem("")
        self.combox_set_com_6.addItem("")
        self.combox_set_com_6.setObjectName(u"combox_set_com_6")
        self.combox_set_com_6.setMinimumSize(QSize(0, 30))
        self.combox_set_com_6.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_6, 5, 1, 1, 1)

        self.combox_set_baund_10 = QComboBox(self.frame_2)
        self.combox_set_baund_10.addItem("")
        self.combox_set_baund_10.addItem("")
        self.combox_set_baund_10.addItem("")
        self.combox_set_baund_10.addItem("")
        self.combox_set_baund_10.addItem("")
        self.combox_set_baund_10.setObjectName(u"combox_set_baund_10")
        self.combox_set_baund_10.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_10.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_10, 9, 2, 1, 1)

        self.label_84 = QLabel(self.frame_2)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_84, 10, 0, 1, 1)

        self.comboBox_stopbit_7 = QComboBox(self.frame_2)
        self.comboBox_stopbit_7.addItem("")
        self.comboBox_stopbit_7.addItem("")
        self.comboBox_stopbit_7.setObjectName(u"comboBox_stopbit_7")
        self.comboBox_stopbit_7.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_7, 6, 4, 1, 1)

        self.label_46 = QLabel(self.frame_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_46, 4, 0, 1, 1)

        self.lineEdit_file_names_25 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_25.setObjectName(u"lineEdit_file_names_25")
        self.lineEdit_file_names_25.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_25, 0, 6, 1, 1)

        self.comboBox_set_check_7 = QComboBox(self.frame_2)
        self.comboBox_set_check_7.addItem("")
        self.comboBox_set_check_7.addItem("")
        self.comboBox_set_check_7.addItem("")
        self.comboBox_set_check_7.setObjectName(u"comboBox_set_check_7")
        self.comboBox_set_check_7.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_7, 6, 3, 1, 1)

        self.combox_set_com_10 = QComboBox(self.frame_2)
        self.combox_set_com_10.addItem("")
        self.combox_set_com_10.addItem("")
        self.combox_set_com_10.addItem("")
        self.combox_set_com_10.addItem("")
        self.combox_set_com_10.addItem("")
        self.combox_set_com_10.setObjectName(u"combox_set_com_10")
        self.combox_set_com_10.setMinimumSize(QSize(0, 30))
        self.combox_set_com_10.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_10, 9, 1, 1, 1)

        self.combox_set_baund_11 = QComboBox(self.frame_2)
        self.combox_set_baund_11.addItem("")
        self.combox_set_baund_11.addItem("")
        self.combox_set_baund_11.addItem("")
        self.combox_set_baund_11.addItem("")
        self.combox_set_baund_11.addItem("")
        self.combox_set_baund_11.setObjectName(u"combox_set_baund_11")
        self.combox_set_baund_11.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_11.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_11, 10, 2, 1, 1)

        self.lineEdit_file_names_3 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_3.setObjectName(u"lineEdit_file_names_3")
        self.lineEdit_file_names_3.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_3, 2, 6, 1, 1)

        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_39, 1, 0, 1, 1)

        self.comboBox_set_check_10 = QComboBox(self.frame_2)
        self.comboBox_set_check_10.addItem("")
        self.comboBox_set_check_10.addItem("")
        self.comboBox_set_check_10.addItem("")
        self.comboBox_set_check_10.setObjectName(u"comboBox_set_check_10")
        self.comboBox_set_check_10.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_10, 9, 3, 1, 1)

        self.pushButton_com_open_4 = QPushButton(self.frame_2)
        self.pushButton_com_open_4.setObjectName(u"pushButton_com_open_4")
        self.pushButton_com_open_4.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_4.setAutoDefault(False)
        self.pushButton_com_open_4.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_4, 3, 5, 1, 1)

        self.combox_set_baund_2 = QComboBox(self.frame_2)
        self.combox_set_baund_2.addItem("")
        self.combox_set_baund_2.addItem("")
        self.combox_set_baund_2.addItem("")
        self.combox_set_baund_2.addItem("")
        self.combox_set_baund_2.addItem("")
        self.combox_set_baund_2.setObjectName(u"combox_set_baund_2")
        self.combox_set_baund_2.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_2.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_2, 1, 2, 1, 1)

        self.pushButton_com_open_12 = QPushButton(self.frame_2)
        self.pushButton_com_open_12.setObjectName(u"pushButton_com_open_12")
        self.pushButton_com_open_12.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_12.setAutoDefault(False)
        self.pushButton_com_open_12.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_12, 11, 5, 1, 1)

        self.label_53 = QLabel(self.frame_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_53, 7, 0, 1, 1)

        self.comboBox_stopbit_9 = QComboBox(self.frame_2)
        self.comboBox_stopbit_9.addItem("")
        self.comboBox_stopbit_9.addItem("")
        self.comboBox_stopbit_9.setObjectName(u"comboBox_stopbit_9")
        self.comboBox_stopbit_9.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_9, 8, 4, 1, 1)

        self.combox_set_baund_5 = QComboBox(self.frame_2)
        self.combox_set_baund_5.addItem("")
        self.combox_set_baund_5.addItem("")
        self.combox_set_baund_5.addItem("")
        self.combox_set_baund_5.addItem("")
        self.combox_set_baund_5.addItem("")
        self.combox_set_baund_5.setObjectName(u"combox_set_baund_5")
        self.combox_set_baund_5.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_5.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_5, 4, 2, 1, 1)

        self.lineEdit_file_names_12 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_12.setObjectName(u"lineEdit_file_names_12")
        self.lineEdit_file_names_12.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_12, 11, 6, 1, 1)

        self.comboBox_stopbit_1 = QComboBox(self.frame_2)
        self.comboBox_stopbit_1.addItem("")
        self.comboBox_stopbit_1.addItem("")
        self.comboBox_stopbit_1.setObjectName(u"comboBox_stopbit_1")
        self.comboBox_stopbit_1.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_1, 0, 4, 1, 1)

        self.combox_set_com_1 = QComboBox(self.frame_2)
        self.combox_set_com_1.addItem("")
        self.combox_set_com_1.addItem("")
        self.combox_set_com_1.addItem("")
        self.combox_set_com_1.addItem("")
        self.combox_set_com_1.addItem("")
        self.combox_set_com_1.setObjectName(u"combox_set_com_1")
        self.combox_set_com_1.setMinimumSize(QSize(90, 30))
        self.combox_set_com_1.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_1, 0, 1, 1, 1)

        self.combox_set_com_3 = QComboBox(self.frame_2)
        self.combox_set_com_3.addItem("")
        self.combox_set_com_3.addItem("")
        self.combox_set_com_3.addItem("")
        self.combox_set_com_3.addItem("")
        self.combox_set_com_3.addItem("")
        self.combox_set_com_3.setObjectName(u"combox_set_com_3")
        self.combox_set_com_3.setMinimumSize(QSize(0, 30))
        self.combox_set_com_3.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_3, 2, 1, 1, 1)

        self.comboBox_set_check_12 = QComboBox(self.frame_2)
        self.comboBox_set_check_12.addItem("")
        self.comboBox_set_check_12.addItem("")
        self.comboBox_set_check_12.addItem("")
        self.comboBox_set_check_12.setObjectName(u"comboBox_set_check_12")
        self.comboBox_set_check_12.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_12, 11, 3, 1, 1)

        self.label_82 = QLabel(self.frame_2)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_82, 9, 0, 1, 1)

        self.pushButton_com_open_13 = QPushButton(self.frame_2)
        self.pushButton_com_open_13.setObjectName(u"pushButton_com_open_13")
        self.pushButton_com_open_13.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_13.setAutoDefault(False)
        self.pushButton_com_open_13.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_13, 8, 5, 1, 1)

        self.comboBox_stopbit_8 = QComboBox(self.frame_2)
        self.comboBox_stopbit_8.addItem("")
        self.comboBox_stopbit_8.addItem("")
        self.comboBox_stopbit_8.setObjectName(u"comboBox_stopbit_8")
        self.comboBox_stopbit_8.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_8, 7, 4, 1, 1)

        self.comboBox_stopbit_4 = QComboBox(self.frame_2)
        self.comboBox_stopbit_4.addItem("")
        self.comboBox_stopbit_4.addItem("")
        self.comboBox_stopbit_4.setObjectName(u"comboBox_stopbit_4")
        self.comboBox_stopbit_4.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_4, 3, 4, 1, 1)

        self.combox_set_baund_4 = QComboBox(self.frame_2)
        self.combox_set_baund_4.addItem("")
        self.combox_set_baund_4.addItem("")
        self.combox_set_baund_4.addItem("")
        self.combox_set_baund_4.addItem("")
        self.combox_set_baund_4.addItem("")
        self.combox_set_baund_4.setObjectName(u"combox_set_baund_4")
        self.combox_set_baund_4.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_4.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_4, 3, 2, 1, 1)

        self.combox_set_com_9 = QComboBox(self.frame_2)
        self.combox_set_com_9.addItem("")
        self.combox_set_com_9.addItem("")
        self.combox_set_com_9.addItem("")
        self.combox_set_com_9.addItem("")
        self.combox_set_com_9.addItem("")
        self.combox_set_com_9.setObjectName(u"combox_set_com_9")
        self.combox_set_com_9.setMinimumSize(QSize(0, 30))
        self.combox_set_com_9.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_9, 8, 1, 1, 1)

        self.lineEdit_file_names_9 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_9.setObjectName(u"lineEdit_file_names_9")
        self.lineEdit_file_names_9.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_9, 8, 6, 1, 1)

        self.lineEdit_file_names_2 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_2.setObjectName(u"lineEdit_file_names_2")
        self.lineEdit_file_names_2.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_2, 1, 6, 1, 1)

        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_38, 0, 0, 1, 1)

        self.combox_set_baund_8 = QComboBox(self.frame_2)
        self.combox_set_baund_8.addItem("")
        self.combox_set_baund_8.addItem("")
        self.combox_set_baund_8.addItem("")
        self.combox_set_baund_8.addItem("")
        self.combox_set_baund_8.addItem("")
        self.combox_set_baund_8.setObjectName(u"combox_set_baund_8")
        self.combox_set_baund_8.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_8.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_8, 7, 2, 1, 1)

        self.label_80 = QLabel(self.frame_2)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_80, 8, 0, 1, 1)

        self.combox_set_baund_6 = QComboBox(self.frame_2)
        self.combox_set_baund_6.addItem("")
        self.combox_set_baund_6.addItem("")
        self.combox_set_baund_6.addItem("")
        self.combox_set_baund_6.addItem("")
        self.combox_set_baund_6.addItem("")
        self.combox_set_baund_6.setObjectName(u"combox_set_baund_6")
        self.combox_set_baund_6.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_6.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_6, 5, 2, 1, 1)

        self.comboBox_set_check_5 = QComboBox(self.frame_2)
        self.comboBox_set_check_5.addItem("")
        self.comboBox_set_check_5.addItem("")
        self.comboBox_set_check_5.addItem("")
        self.comboBox_set_check_5.setObjectName(u"comboBox_set_check_5")
        self.comboBox_set_check_5.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_5, 4, 3, 1, 1)

        self.pushButton_com_open_1 = QPushButton(self.frame_2)
        self.pushButton_com_open_1.setObjectName(u"pushButton_com_open_1")
        self.pushButton_com_open_1.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_1.setAutoDefault(False)
        self.pushButton_com_open_1.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_1, 0, 5, 1, 1)

        self.combox_set_baund_3 = QComboBox(self.frame_2)
        self.combox_set_baund_3.addItem("")
        self.combox_set_baund_3.addItem("")
        self.combox_set_baund_3.addItem("")
        self.combox_set_baund_3.addItem("")
        self.combox_set_baund_3.addItem("")
        self.combox_set_baund_3.setObjectName(u"combox_set_baund_3")
        self.combox_set_baund_3.setMinimumSize(QSize(0, 30))
        self.combox_set_baund_3.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_3, 2, 2, 1, 1)

        self.combox_set_com_7 = QComboBox(self.frame_2)
        self.combox_set_com_7.addItem("")
        self.combox_set_com_7.addItem("")
        self.combox_set_com_7.addItem("")
        self.combox_set_com_7.addItem("")
        self.combox_set_com_7.addItem("")
        self.combox_set_com_7.setObjectName(u"combox_set_com_7")
        self.combox_set_com_7.setMinimumSize(QSize(0, 30))
        self.combox_set_com_7.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_7, 6, 1, 1, 1)

        self.comboBox_set_check_2 = QComboBox(self.frame_2)
        self.comboBox_set_check_2.addItem("")
        self.comboBox_set_check_2.addItem("")
        self.comboBox_set_check_2.addItem("")
        self.comboBox_set_check_2.setObjectName(u"comboBox_set_check_2")
        self.comboBox_set_check_2.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_2, 1, 3, 1, 1)

        self.combox_set_com_4 = QComboBox(self.frame_2)
        self.combox_set_com_4.addItem("")
        self.combox_set_com_4.addItem("")
        self.combox_set_com_4.addItem("")
        self.combox_set_com_4.addItem("")
        self.combox_set_com_4.addItem("")
        self.combox_set_com_4.setObjectName(u"combox_set_com_4")
        self.combox_set_com_4.setMinimumSize(QSize(0, 30))
        self.combox_set_com_4.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_com_4, 3, 1, 1, 1)

        self.pushButton_com_open_9 = QPushButton(self.frame_2)
        self.pushButton_com_open_9.setObjectName(u"pushButton_com_open_9")
        self.pushButton_com_open_9.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_9.setAutoDefault(False)
        self.pushButton_com_open_9.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_9, 2, 5, 1, 1)

        self.comboBox_stopbit_11 = QComboBox(self.frame_2)
        self.comboBox_stopbit_11.addItem("")
        self.comboBox_stopbit_11.addItem("")
        self.comboBox_stopbit_11.setObjectName(u"comboBox_stopbit_11")
        self.comboBox_stopbit_11.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_11, 10, 4, 1, 1)

        self.lineEdit_file_names_10 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_10.setObjectName(u"lineEdit_file_names_10")
        self.lineEdit_file_names_10.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_10, 9, 6, 1, 1)

        self.comboBox_set_check_6 = QComboBox(self.frame_2)
        self.comboBox_set_check_6.addItem("")
        self.comboBox_set_check_6.addItem("")
        self.comboBox_set_check_6.addItem("")
        self.comboBox_set_check_6.setObjectName(u"comboBox_set_check_6")
        self.comboBox_set_check_6.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_6, 5, 3, 1, 1)

        self.pushButton_com_open_11 = QPushButton(self.frame_2)
        self.pushButton_com_open_11.setObjectName(u"pushButton_com_open_11")
        self.pushButton_com_open_11.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_11.setAutoDefault(False)
        self.pushButton_com_open_11.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_11, 10, 5, 1, 1)

        self.lineEdit_file_names_8 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_8.setObjectName(u"lineEdit_file_names_8")
        self.lineEdit_file_names_8.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_8, 7, 6, 1, 1)

        self.comboBox_set_check_1 = QComboBox(self.frame_2)
        self.comboBox_set_check_1.addItem("")
        self.comboBox_set_check_1.addItem("")
        self.comboBox_set_check_1.addItem("")
        self.comboBox_set_check_1.setObjectName(u"comboBox_set_check_1")
        self.comboBox_set_check_1.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_1, 0, 3, 1, 1)

        self.label_86 = QLabel(self.frame_2)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_86, 11, 0, 1, 1)

        self.pushButton_com_open_5 = QPushButton(self.frame_2)
        self.pushButton_com_open_5.setObjectName(u"pushButton_com_open_5")
        self.pushButton_com_open_5.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_5.setAutoDefault(False)
        self.pushButton_com_open_5.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_5, 4, 5, 1, 1)

        self.pushButton_com_open_7 = QPushButton(self.frame_2)
        self.pushButton_com_open_7.setObjectName(u"pushButton_com_open_7")
        self.pushButton_com_open_7.setMinimumSize(QSize(0, 30))
        self.pushButton_com_open_7.setAutoDefault(False)
        self.pushButton_com_open_7.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_7, 6, 5, 1, 1)

        self.lineEdit_file_names_4 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_4.setObjectName(u"lineEdit_file_names_4")
        self.lineEdit_file_names_4.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_4, 3, 6, 1, 1)

        self.lineEdit_file_names_5 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_5.setObjectName(u"lineEdit_file_names_5")
        self.lineEdit_file_names_5.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_5, 4, 6, 1, 1)

        self.label_49 = QLabel(self.frame_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_49, 5, 0, 1, 1)

        self.lineEdit_file_names_7 = QLineEdit(self.frame_2)
        self.lineEdit_file_names_7.setObjectName(u"lineEdit_file_names_7")
        self.lineEdit_file_names_7.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_7, 6, 6, 1, 1)

        self.comboBox_stopbit_2 = QComboBox(self.frame_2)
        self.comboBox_stopbit_2.addItem("")
        self.comboBox_stopbit_2.addItem("")
        self.comboBox_stopbit_2.setObjectName(u"comboBox_stopbit_2")
        self.comboBox_stopbit_2.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_2, 1, 4, 1, 1)

        self.comboBox_set_check_11 = QComboBox(self.frame_2)
        self.comboBox_set_check_11.addItem("")
        self.comboBox_set_check_11.addItem("")
        self.comboBox_set_check_11.addItem("")
        self.comboBox_set_check_11.setObjectName(u"comboBox_set_check_11")
        self.comboBox_set_check_11.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_set_check_11, 10, 3, 1, 1)

        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_44, 3, 0, 1, 1)

        self.label_42 = QLabel(self.frame_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_42, 2, 0, 1, 1)

        self.label_78 = QLabel(self.frame_2)
        self.label_78.setObjectName(u"label_78")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy13)
        self.label_78.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.label_78, 12, 0, 1, 1)

        self.combox_set_com_all = QComboBox(self.frame_2)
        self.combox_set_com_all.addItem("")
        self.combox_set_com_all.addItem("")
        self.combox_set_com_all.addItem("")
        self.combox_set_com_all.addItem("")
        self.combox_set_com_all.addItem("")
        self.combox_set_com_all.setObjectName(u"combox_set_com_all")
        sizePolicy13.setHeightForWidth(self.combox_set_com_all.sizePolicy().hasHeightForWidth())
        self.combox_set_com_all.setSizePolicy(sizePolicy13)
        self.combox_set_com_all.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.combox_set_com_all, 12, 1, 1, 1)

        self.comboBox_set_check_all = QComboBox(self.frame_2)
        self.comboBox_set_check_all.addItem("")
        self.comboBox_set_check_all.addItem("")
        self.comboBox_set_check_all.addItem("")
        self.comboBox_set_check_all.setObjectName(u"comboBox_set_check_all")
        sizePolicy13.setHeightForWidth(self.comboBox_set_check_all.sizePolicy().hasHeightForWidth())
        self.comboBox_set_check_all.setSizePolicy(sizePolicy13)
        self.comboBox_set_check_all.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.comboBox_set_check_all, 12, 3, 1, 1)

        self.combox_set_baund_all = QComboBox(self.frame_2)
        self.combox_set_baund_all.addItem("")
        self.combox_set_baund_all.addItem("")
        self.combox_set_baund_all.addItem("")
        self.combox_set_baund_all.addItem("")
        self.combox_set_baund_all.addItem("")
        self.combox_set_baund_all.setObjectName(u"combox_set_baund_all")
        sizePolicy13.setHeightForWidth(self.combox_set_baund_all.sizePolicy().hasHeightForWidth())
        self.combox_set_baund_all.setSizePolicy(sizePolicy13)
        self.combox_set_baund_all.setMinimumSize(QSize(0, 28))
        self.combox_set_baund_all.setEditable(True)

        self.gridLayout_4.addWidget(self.combox_set_baund_all, 12, 2, 1, 1)

        self.comboBox_stopbit_all = QComboBox(self.frame_2)
        self.comboBox_stopbit_all.addItem("")
        self.comboBox_stopbit_all.addItem("")
        self.comboBox_stopbit_all.setObjectName(u"comboBox_stopbit_all")
        sizePolicy13.setHeightForWidth(self.comboBox_stopbit_all.sizePolicy().hasHeightForWidth())
        self.comboBox_stopbit_all.setSizePolicy(sizePolicy13)
        self.comboBox_stopbit_all.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.comboBox_stopbit_all, 12, 4, 1, 1)

        self.pushButton_com_open_all = QPushButton(self.frame_2)
        self.pushButton_com_open_all.setObjectName(u"pushButton_com_open_all")
        sizePolicy9.setHeightForWidth(self.pushButton_com_open_all.sizePolicy().hasHeightForWidth())
        self.pushButton_com_open_all.setSizePolicy(sizePolicy9)
        self.pushButton_com_open_all.setMinimumSize(QSize(0, 28))
        self.pushButton_com_open_all.setAutoDefault(False)
        self.pushButton_com_open_all.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_com_open_all, 12, 5, 1, 1)

        self.lineEdit_file_names_all = QLineEdit(self.frame_2)
        self.lineEdit_file_names_all.setObjectName(u"lineEdit_file_names_all")
        sizePolicy14 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.lineEdit_file_names_all.sizePolicy().hasHeightForWidth())
        self.lineEdit_file_names_all.setSizePolicy(sizePolicy14)
        self.lineEdit_file_names_all.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.lineEdit_file_names_all, 12, 6, 1, 1)

        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(200, 500, 301, 91))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_begin_test = QPushButton(self.layoutWidget)
        self.pushButton_begin_test.setObjectName(u"pushButton_begin_test")
        self.pushButton_begin_test.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_7.addWidget(self.pushButton_begin_test)

        self.pushButton_stop_test = QPushButton(self.layoutWidget)
        self.pushButton_stop_test.setObjectName(u"pushButton_stop_test")
        self.pushButton_stop_test.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_7.addWidget(self.pushButton_stop_test)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_5 = QTextBrowser(self.tab)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.gridLayout_2.addWidget(self.textBrowser_5, 3, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.textBrowser_3 = QTextBrowser(self.tab)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.gridLayout_2.addWidget(self.textBrowser_3, 1, 0, 1, 1)

        self.textBrowser_6 = QTextBrowser(self.tab)
        self.textBrowser_6.setObjectName(u"textBrowser_6")

        self.gridLayout_2.addWidget(self.textBrowser_6, 1, 1, 1, 1)

        self.textBrowser_9 = QTextBrowser(self.tab)
        self.textBrowser_9.setObjectName(u"textBrowser_9")

        self.gridLayout_2.addWidget(self.textBrowser_9, 4, 0, 1, 1)

        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 1, 1, 1)

        self.textBrowser_4 = QTextBrowser(self.tab)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.gridLayout_2.addWidget(self.textBrowser_4, 2, 0, 1, 1)

        self.textBrowser_7 = QTextBrowser(self.tab)
        self.textBrowser_7.setObjectName(u"textBrowser_7")

        self.gridLayout_2.addWidget(self.textBrowser_7, 2, 1, 1, 1)

        self.textBrowser_8 = QTextBrowser(self.tab)
        self.textBrowser_8.setObjectName(u"textBrowser_8")

        self.gridLayout_2.addWidget(self.textBrowser_8, 3, 1, 1, 1)

        self.textBrowser_10 = QTextBrowser(self.tab)
        self.textBrowser_10.setObjectName(u"textBrowser_10")

        self.gridLayout_2.addWidget(self.textBrowser_10, 5, 0, 1, 1)

        self.textBrowser_11 = QTextBrowser(self.tab)
        self.textBrowser_11.setObjectName(u"textBrowser_11")

        self.gridLayout_2.addWidget(self.textBrowser_11, 4, 1, 1, 1)

        self.textBrowser_12 = QTextBrowser(self.tab)
        self.textBrowser_12.setObjectName(u"textBrowser_12")

        self.gridLayout_2.addWidget(self.textBrowser_12, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_9 = QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(7)
        self.gridLayout_9.setVerticalSpacing(0)
        self.graphicsView_gyr_Z_2 = GraphicsLayoutWidget(self.tab_6)
        self.graphicsView_gyr_Z_2.setObjectName(u"graphicsView_gyr_Z_2")
        self.graphicsView_gyr_Z_2.setAcceptDrops(False)
        self.graphicsView_gyr_Z_2.setAutoFillBackground(False)

        self.gridLayout_9.addWidget(self.graphicsView_gyr_Z_2, 2, 0, 1, 1)

        self.graphicsView_gyr_Y_2 = GraphicsLayoutWidget(self.tab_6)
        self.graphicsView_gyr_Y_2.setObjectName(u"graphicsView_gyr_Y_2")

        self.gridLayout_9.addWidget(self.graphicsView_gyr_Y_2, 1, 0, 1, 1)

        self.graphicsView_gyr_X_2 = GraphicsLayoutWidget(self.tab_6)
        self.graphicsView_gyr_X_2.setObjectName(u"graphicsView_gyr_X_2")

        self.gridLayout_9.addWidget(self.graphicsView_gyr_X_2, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_inside_location_2 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_2.setObjectName(u"lineEdit_inside_location_2")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_2, 0, 1, 1, 1)

        self.label_15 = QLabel(self.tab_6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 2, 1, 1)

        self.label_16 = QLabel(self.tab_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_17 = QLabel(self.tab_6)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 1, 4, 1, 1)

        self.lineEdit_inside_location_3 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_3.setObjectName(u"lineEdit_inside_location_3")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_3, 1, 3, 1, 1)

        self.label_18 = QLabel(self.tab_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 2, 8, 1, 1)

        self.lineEdit_inside_location_14 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_14.setObjectName(u"lineEdit_inside_location_14")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_14, 2, 9, 1, 1)

        self.label_19 = QLabel(self.tab_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 0, 6, 1, 1)

        self.lineEdit_inside_location_4 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_4.setObjectName(u"lineEdit_inside_location_4")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_4, 0, 7, 1, 1)

        self.lineEdit_inside_location_5 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_5.setObjectName(u"lineEdit_inside_location_5")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_5, 0, 3, 1, 1)

        self.lineEdit_inside_location_7 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_7.setObjectName(u"lineEdit_inside_location_7")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_7, 2, 7, 1, 1)

        self.lineEdit_inside_location_12 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_12.setObjectName(u"lineEdit_inside_location_12")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_12, 2, 1, 1, 1)

        self.lineEdit_inside_location_13 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_13.setObjectName(u"lineEdit_inside_location_13")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_13, 1, 9, 1, 1)

        self.label_20 = QLabel(self.tab_6)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_5.addWidget(self.label_20, 0, 4, 1, 1)

        self.label_21 = QLabel(self.tab_6)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.tab_6)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_5.addWidget(self.label_22, 1, 2, 1, 1)

        self.label_23 = QLabel(self.tab_6)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_5.addWidget(self.label_23, 1, 8, 1, 1)

        self.lineEdit_inside_location_6 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_6.setObjectName(u"lineEdit_inside_location_6")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_6, 1, 7, 1, 1)

        self.lineEdit_inside_location_9 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_9.setObjectName(u"lineEdit_inside_location_9")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_9, 0, 9, 1, 1)

        self.lineEdit_inside_location_8 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_8.setObjectName(u"lineEdit_inside_location_8")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_8, 2, 3, 1, 1)

        self.label_24 = QLabel(self.tab_6)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_5.addWidget(self.label_24, 2, 6, 1, 1)

        self.label_25 = QLabel(self.tab_6)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 2, 2, 1, 1)

        self.lineEdit_inside_location_11 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_11.setObjectName(u"lineEdit_inside_location_11")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_11, 1, 1, 1, 1)

        self.label_26 = QLabel(self.tab_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_27 = QLabel(self.tab_6)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 2, 4, 1, 1)

        self.label_28 = QLabel(self.tab_6)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 1, 6, 1, 1)

        self.label_29 = QLabel(self.tab_6)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 0, 8, 1, 1)

        self.lineEdit_inside_location_15 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_15.setObjectName(u"lineEdit_inside_location_15")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_15, 0, 5, 1, 1)

        self.lineEdit_inside_location_10 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_10.setObjectName(u"lineEdit_inside_location_10")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_10, 1, 5, 1, 1)

        self.lineEdit_inside_location_16 = QLineEdit(self.tab_6)
        self.lineEdit_inside_location_16.setObjectName(u"lineEdit_inside_location_16")

        self.gridLayout_5.addWidget(self.lineEdit_inside_location_16, 2, 5, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_5, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1268, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_com_open_6.setDefault(False)
        self.pushButton_com_open_8.setDefault(False)
        self.pushButton_com_open_10.setDefault(False)
        self.pushButton_com_open_14.setDefault(False)
        self.pushButton_com_open_4.setDefault(False)
        self.pushButton_com_open_12.setDefault(False)
        self.pushButton_com_open_13.setDefault(False)
        self.pushButton_com_open_1.setDefault(False)
        self.pushButton_com_open_9.setDefault(False)
        self.pushButton_com_open_11.setDefault(False)
        self.pushButton_com_open_5.setDefault(False)
        self.pushButton_com_open_7.setDefault(False)
        self.pushButton_com_open_all.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u901a\u8baf\u534f\u8bae\u6a21\u5757", None))
        self.radioButton.setText("")
        self.comboBox_com_select.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.comboBox_com_select.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))

        self.comboBox_baund_select.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.comboBox_baund_select.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.comboBox_baund_select.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.comboBox_baund_select.setItemText(3, QCoreApplication.translate("MainWindow", u"921600", None))

        self.comboBox_check_select.setItemText(0, QCoreApplication.translate("MainWindow", u"none", None))
        self.comboBox_check_select.setItemText(1, QCoreApplication.translate("MainWindow", u"odd", None))
        self.comboBox_check_select.setItemText(2, QCoreApplication.translate("MainWindow", u"even", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u534f\u8bae:", None))
        self.comboBox_rulename.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8f6c\u53f0\u63a7\u5236\u6a21\u5757", None))
        self.radioButton_turntable_check.setText("")
        self.combox_turntable_com.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_turntable_com.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_turntable_com.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_turntable_com.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_turntable_com.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_turntable_com.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_com_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.pushButton_com_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.lineEdit_outside_location.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_outside_acceleration.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.lineEdit_outside_speed.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_inside_reset.setText(QCoreApplication.translate("MainWindow", u"\u5f52\u96f6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u901f\u7387", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u901f\u7387", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None))
        self.pushButton_outside_reset.setText(QCoreApplication.translate("MainWindow", u"\u5f52\u96f6", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5185\u6846", None))
        self.lineEdit_inside_location.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_start_location.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e\u8f6c\u52a8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None))
        self.pushButton_start_speed.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6\u8f6c\u52a8", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5916\u6846", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u901f", None))
        self.lineEdit_inside_speed.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u901f\u7387", None))
        self.lineEdit_inside_acceleration.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u901f\u7387", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u901f", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7535\u6e90\u63a7\u5236\u6a21\u5757", None))
        self.radioButton_turntable_check_2.setText("")
        self.combox_turntable_com_2.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_turntable_com_2.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_turntable_com_2.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_turntable_com_2.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_turntable_com_2.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_turntable_com_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_com_open_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.pushButton_com_close_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6e29\u7bb1\u63a7\u5236\u6a21\u5757", None))
        self.combox_turntable_com_3.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_turntable_com_3.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_turntable_com_3.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_turntable_com_3.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_turntable_com_3.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_turntable_com_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_com_close_3.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.pushButton_com_open_3.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6  \u8bbe\u5b9a", None))
        self.radioButton_turntable_check_3.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6d4b\u8bd5\u6a21\u5757", None))
#if QT_CONFIG(tooltip)
        self.pushButton_openFile.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8f7d\u5165\u5341\u516d\u8fdb\u5236\u6587\u4ef6\u81ea\u52a8\u89e3\u7b97</p><p>\u8f7d\u5165\u6570\u636e\u6587\u4ef6\u81ea\u52a8\u7ed8\u56fe</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_openFile.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u5165\u6587\u4ef6", None))
        self.pushButton_reloadFile.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u8f7d\u6587\u4ef6", None))
        self.textBrowser_filePath.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.combox_set_baund_12.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_12.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_12.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_12.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_12.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_12.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_file_names_11.setText(QCoreApplication.translate("MainWindow", u"autosave11", None))
        self.comboBox_stopbit_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.pushButton_com_open_6.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.comboBox_set_check_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_4.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Tab_7", None))
        self.combox_set_com_11.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_11.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_11.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_11.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_11.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.combox_set_baund_7.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_7.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_7.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_7.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_7.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_stopbit_12.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_12.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.pushButton_com_open_8.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.combox_set_baund_1.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_1.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_1.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_1.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_1.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_set_check_8.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_8.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_8.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.combox_set_com_5.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_5.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_5.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_5.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_5.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_stopbit_10.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_10.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.comboBox_stopbit_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.comboBox_set_check_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_3.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.combox_set_com_2.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_2.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_2.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_2.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_2.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_stopbit_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.pushButton_com_open_10.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.pushButton_com_open_14.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.comboBox_set_check_9.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_9.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_9.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.combox_set_com_8.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_8.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_8.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_8.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_8.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_8.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_file_names_6.setText(QCoreApplication.translate("MainWindow", u"autosave6", None))
        self.combox_set_baund_9.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_9.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_9.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_9.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_9.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_9.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.combox_set_com_12.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_12.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_12.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_12.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_12.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_12.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.combox_set_com_6.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_6.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_6.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_6.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_6.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.combox_set_baund_10.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_10.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_10.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_10.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_10.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Tab_11", None))
        self.comboBox_stopbit_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Tab_5", None))
        self.lineEdit_file_names_25.setText(QCoreApplication.translate("MainWindow", u"autosave1", None))
        self.comboBox_set_check_7.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_7.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_7.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.combox_set_com_10.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_10.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_10.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_10.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_10.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.combox_set_baund_11.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_11.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_11.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_11.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_11.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_file_names_3.setText(QCoreApplication.translate("MainWindow", u"autosave3", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Tab_2", None))
        self.comboBox_set_check_10.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_10.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_10.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.pushButton_com_open_4.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.combox_set_baund_2.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_2.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_2.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_2.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_2.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_com_open_12.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Tab_8", None))
        self.comboBox_stopbit_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_9.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.combox_set_baund_5.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_5.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_5.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_5.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_5.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_file_names_12.setText(QCoreApplication.translate("MainWindow", u"autosave12", None))
        self.comboBox_stopbit_1.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.combox_set_com_1.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_1.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_1.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_1.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_1.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.combox_set_com_3.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_3.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_3.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_3.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_3.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_set_check_12.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_12.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_12.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Tab_10", None))
        self.pushButton_com_open_13.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.comboBox_stopbit_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.comboBox_stopbit_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.combox_set_baund_4.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_4.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_4.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_4.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_4.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.combox_set_com_9.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_9.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_9.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_9.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_9.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_9.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_file_names_9.setText(QCoreApplication.translate("MainWindow", u"autosave9", None))
        self.lineEdit_file_names_2.setText(QCoreApplication.translate("MainWindow", u"autosave2", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Tab_1", None))
        self.combox_set_baund_8.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_8.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_8.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_8.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_8.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_8.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Tab_9", None))
        self.combox_set_baund_6.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_6.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_6.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_6.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_6.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_set_check_5.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_5.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_5.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.pushButton_com_open_1.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.combox_set_baund_3.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_3.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_3.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_3.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_3.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.combox_set_com_7.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_7.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_7.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_7.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_7.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_set_check_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.combox_set_com_4.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_4.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_4.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_4.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_4.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_com_open_9.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.comboBox_stopbit_11.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_11.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.lineEdit_file_names_10.setText(QCoreApplication.translate("MainWindow", u"autosave10", None))
        self.comboBox_set_check_6.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_6.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_6.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.pushButton_com_open_11.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.lineEdit_file_names_8.setText(QCoreApplication.translate("MainWindow", u"autosave8", None))
        self.comboBox_set_check_1.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_1.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Tab_12", None))
        self.pushButton_com_open_5.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.pushButton_com_open_7.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.lineEdit_file_names_4.setText(QCoreApplication.translate("MainWindow", u"autosave4", None))
        self.lineEdit_file_names_5.setText(QCoreApplication.translate("MainWindow", u"autosave5", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Tab_6", None))
        self.lineEdit_file_names_7.setText(QCoreApplication.translate("MainWindow", u"autosave7", None))
        self.comboBox_stopbit_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.comboBox_set_check_11.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_11.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_11.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Tab_4", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Tab_3", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u603b\u63a7</span></p></body></html>", None))
        self.combox_set_com_all.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combox_set_com_all.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combox_set_com_all.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combox_set_com_all.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combox_set_com_all.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

#if QT_CONFIG(tooltip)
        self.combox_set_com_all.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_set_check_all.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0\u6821\u9a8c", None))
        self.comboBox_set_check_all.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5076\u6821\u9a8c", None))
        self.comboBox_set_check_all.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5947\u6821\u9a8c", None))

        self.combox_set_baund_all.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_set_baund_all.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.combox_set_baund_all.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_set_baund_all.setItemText(3, QCoreApplication.translate("MainWindow", u"614400", None))
        self.combox_set_baund_all.setItemText(4, QCoreApplication.translate("MainWindow", u"921600", None))

#if QT_CONFIG(tooltip)
        self.combox_set_baund_all.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u7279\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_stopbit_all.setItemText(0, QCoreApplication.translate("MainWindow", u"Stop1", None))
        self.comboBox_stopbit_all.setItemText(1, QCoreApplication.translate("MainWindow", u"Stop2", None))

        self.pushButton_com_open_all.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.lineEdit_file_names_all.setText(QCoreApplication.translate("MainWindow", u"autosave", None))
        self.pushButton_begin_test.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\n"
"\u6d4b\u8bd5", None))
        self.pushButton_stop_test.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\n"
"\u6d4b\u8bd5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u63a5\u6536", None))
        self.lineEdit_inside_location_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"X\u8f74", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc7", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u6570", None))
        self.lineEdit_inside_location_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u6807\u51c6\u5dee", None))
        self.lineEdit_inside_location_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5747\u503c", None))
        self.lineEdit_inside_location_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_inside_location_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_inside_location_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_inside_location_12.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_inside_location_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u6570", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u6ed1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Y\u8f74", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u6807\u51c6\u5dee", None))
        self.lineEdit_inside_location_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_inside_location_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_inside_location_8.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u5747\u503c", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Z\u8f74", None))
        self.lineEdit_inside_location_11.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u9640\u87ba", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u6570", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u5747\u503c", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u6807\u51c6\u5dee", None))
        self.lineEdit_inside_location_15.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_inside_location_10.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_inside_location_16.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
    # retranslateUi

