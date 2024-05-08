# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IMU_plot_withsate.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLCDNumber, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget
from pyqtgraph.opengl import GLViewWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 889)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolTipDuration(-1)
        self.action_hextoStr = QAction(MainWindow)
        self.action_hextoStr.setObjectName(u"action_hextoStr")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy1)
        self.verticalWidget.setMinimumSize(QSize(0, 0))
        self.verticalWidget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.radioButton = QRadioButton(self.verticalWidget)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy2)
        self.radioButton.setCheckable(False)
        self.radioButton.setChecked(False)

        self.horizontalLayout_5.addWidget(self.radioButton)

        self.comboBox_com_select = QComboBox(self.verticalWidget)
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

        self.horizontalLayout_5.addWidget(self.comboBox_com_select)

        self.comboBox_baund_select = QComboBox(self.verticalWidget)
        self.comboBox_baund_select.addItem("")
        self.comboBox_baund_select.addItem("")
        self.comboBox_baund_select.addItem("")
        self.comboBox_baund_select.addItem("")
        self.comboBox_baund_select.setObjectName(u"comboBox_baund_select")
        self.comboBox_baund_select.setMinimumSize(QSize(0, 25))
        self.comboBox_baund_select.setEditable(True)

        self.horizontalLayout_5.addWidget(self.comboBox_baund_select)

        self.comboBox_check_select = QComboBox(self.verticalWidget)
        self.comboBox_check_select.addItem("")
        self.comboBox_check_select.addItem("")
        self.comboBox_check_select.addItem("")
        self.comboBox_check_select.setObjectName(u"comboBox_check_select")
        self.comboBox_check_select.setMinimumSize(QSize(0, 25))
        self.comboBox_check_select.setEditable(False)

        self.horizontalLayout_5.addWidget(self.comboBox_check_select)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 7)
        self.pushButton_open_com = QPushButton(self.verticalWidget)
        self.pushButton_open_com.setObjectName(u"pushButton_open_com")

        self.horizontalLayout_6.addWidget(self.pushButton_open_com)

        self.pushButton_close_com = QPushButton(self.verticalWidget)
        self.pushButton_close_com.setObjectName(u"pushButton_close_com")

        self.horizontalLayout_6.addWidget(self.pushButton_close_com)

        self.pushButton_flush_com = QPushButton(self.verticalWidget)
        self.pushButton_flush_com.setObjectName(u"pushButton_flush_com")

        self.horizontalLayout_6.addWidget(self.pushButton_flush_com)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalWidget_2 = QWidget(self.verticalWidget)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy4)
        self.horizontalWidget_2.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_openFile = QPushButton(self.horizontalWidget_2)
        self.pushButton_openFile.setObjectName(u"pushButton_openFile")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_openFile.sizePolicy().hasHeightForWidth())
        self.pushButton_openFile.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.pushButton_openFile)

        self.pushButton_reloadFile = QPushButton(self.horizontalWidget_2)
        self.pushButton_reloadFile.setObjectName(u"pushButton_reloadFile")
        sizePolicy5.setHeightForWidth(self.pushButton_reloadFile.sizePolicy().hasHeightForWidth())
        self.pushButton_reloadFile.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.pushButton_reloadFile)


        self.verticalLayout.addWidget(self.horizontalWidget_2)

        self.gridWidget_2 = QWidget(self.verticalWidget)
        self.gridWidget_2.setObjectName(u"gridWidget_2")
        sizePolicy.setHeightForWidth(self.gridWidget_2.sizePolicy().hasHeightForWidth())
        self.gridWidget_2.setSizePolicy(sizePolicy)
        self.gridWidget_2.setAutoFillBackground(False)
        self.gridLayout_7 = QGridLayout(self.gridWidget_2)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_8 = QLabel(self.gridWidget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)
        self.label_8.setMinimumSize(QSize(40, 0))
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_8)

        self.lineEdit_bd_X = QLineEdit(self.gridWidget_2)
        self.lineEdit_bd_X.setObjectName(u"lineEdit_bd_X")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lineEdit_bd_X.sizePolicy().hasHeightForWidth())
        self.lineEdit_bd_X.setSizePolicy(sizePolicy7)

        self.horizontalLayout_21.addWidget(self.lineEdit_bd_X)


        self.gridLayout_7.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(self.gridWidget_2)
        self.label_20.setObjectName(u"label_20")
        sizePolicy6.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy6)
        self.label_20.setMinimumSize(QSize(40, 0))
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_20)

        self.lineEdit_std_Y = QLineEdit(self.gridWidget_2)
        self.lineEdit_std_Y.setObjectName(u"lineEdit_std_Y")
        sizePolicy7.setHeightForWidth(self.lineEdit_std_Y.sizePolicy().hasHeightForWidth())
        self.lineEdit_std_Y.setSizePolicy(sizePolicy7)

        self.horizontalLayout_8.addWidget(self.lineEdit_std_Y)


        self.gridLayout_7.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_9 = QLabel(self.gridWidget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy6.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy6)
        self.label_9.setMinimumSize(QSize(40, 0))
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_9)

        self.lineEdit_bd_Y = QLineEdit(self.gridWidget_2)
        self.lineEdit_bd_Y.setObjectName(u"lineEdit_bd_Y")
        sizePolicy7.setHeightForWidth(self.lineEdit_bd_Y.sizePolicy().hasHeightForWidth())
        self.lineEdit_bd_Y.setSizePolicy(sizePolicy7)

        self.horizontalLayout_23.addWidget(self.lineEdit_bd_Y)


        self.gridLayout_7.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_21 = QLabel(self.gridWidget_2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy6.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy6)
        self.label_21.setMinimumSize(QSize(40, 0))
        self.label_21.setLayoutDirection(Qt.LeftToRight)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_21)

        self.lineEdit_std_X = QLineEdit(self.gridWidget_2)
        self.lineEdit_std_X.setObjectName(u"lineEdit_std_X")
        sizePolicy7.setHeightForWidth(self.lineEdit_std_X.sizePolicy().hasHeightForWidth())
        self.lineEdit_std_X.setSizePolicy(sizePolicy7)

        self.horizontalLayout_9.addWidget(self.lineEdit_std_X)


        self.gridLayout_7.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_7 = QLabel(self.gridWidget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)
        self.label_7.setMinimumSize(QSize(40, 0))
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_7)

        self.lineEdit_bd_Z = QLineEdit(self.gridWidget_2)
        self.lineEdit_bd_Z.setObjectName(u"lineEdit_bd_Z")
        sizePolicy7.setHeightForWidth(self.lineEdit_bd_Z.sizePolicy().hasHeightForWidth())
        self.lineEdit_bd_Z.setSizePolicy(sizePolicy7)

        self.horizontalLayout_22.addWidget(self.lineEdit_bd_Z)


        self.gridLayout_7.addLayout(self.horizontalLayout_22, 2, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_22 = QLabel(self.gridWidget_2)
        self.label_22.setObjectName(u"label_22")
        sizePolicy6.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy6)
        self.label_22.setMinimumSize(QSize(40, 0))
        self.label_22.setLayoutDirection(Qt.LeftToRight)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_22)

        self.lineEdit_std_Z = QLineEdit(self.gridWidget_2)
        self.lineEdit_std_Z.setObjectName(u"lineEdit_std_Z")
        sizePolicy7.setHeightForWidth(self.lineEdit_std_Z.sizePolicy().hasHeightForWidth())
        self.lineEdit_std_Z.setSizePolicy(sizePolicy7)

        self.horizontalLayout_10.addWidget(self.lineEdit_std_Z)


        self.gridLayout_7.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.gridWidget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy6.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy6)
        self.label_10.setMinimumSize(QSize(40, 0))
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.lineEdit_rolls = QLineEdit(self.gridWidget_2)
        self.lineEdit_rolls.setObjectName(u"lineEdit_rolls")
        sizePolicy7.setHeightForWidth(self.lineEdit_rolls.sizePolicy().hasHeightForWidth())
        self.lineEdit_rolls.setSizePolicy(sizePolicy7)

        self.horizontalLayout_11.addWidget(self.lineEdit_rolls)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_11 = QLabel(self.gridWidget_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy6.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy6)
        self.label_11.setMinimumSize(QSize(40, 0))
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_11)

        self.lineEdit_others2 = QLineEdit(self.gridWidget_2)
        self.lineEdit_others2.setObjectName(u"lineEdit_others2")
        sizePolicy7.setHeightForWidth(self.lineEdit_others2.sizePolicy().hasHeightForWidth())
        self.lineEdit_others2.setSizePolicy(sizePolicy7)

        self.horizontalLayout_26.addWidget(self.lineEdit_others2)


        self.gridLayout_7.addLayout(self.horizontalLayout_26, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.gridWidget_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy8)

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBox_rulename = QComboBox(self.verticalWidget)
        self.comboBox_rulename.addItem("")
        self.comboBox_rulename.setObjectName(u"comboBox_rulename")
        self.comboBox_rulename.setEditable(True)

        self.horizontalLayout_3.addWidget(self.comboBox_rulename)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.radioButton_sate = QRadioButton(self.verticalWidget)
        self.radioButton_sate.setObjectName(u"radioButton_sate")
        sizePolicy2.setHeightForWidth(self.radioButton_sate.sizePolicy().hasHeightForWidth())
        self.radioButton_sate.setSizePolicy(sizePolicy2)
        self.radioButton_sate.setCheckable(False)
        self.radioButton_sate.setChecked(False)

        self.horizontalLayout_12.addWidget(self.radioButton_sate)

        self.comboBox_com_sate = QComboBox(self.verticalWidget)
        self.comboBox_com_sate.addItem("")
        self.comboBox_com_sate.addItem("")
        self.comboBox_com_sate.setObjectName(u"comboBox_com_sate")
        sizePolicy3.setHeightForWidth(self.comboBox_com_sate.sizePolicy().hasHeightForWidth())
        self.comboBox_com_sate.setSizePolicy(sizePolicy3)
        self.comboBox_com_sate.setMinimumSize(QSize(0, 25))
        self.comboBox_com_sate.setEditable(True)

        self.horizontalLayout_12.addWidget(self.comboBox_com_sate)

        self.comboBox_baund_sate = QComboBox(self.verticalWidget)
        self.comboBox_baund_sate.addItem("")
        self.comboBox_baund_sate.addItem("")
        self.comboBox_baund_sate.addItem("")
        self.comboBox_baund_sate.addItem("")
        self.comboBox_baund_sate.setObjectName(u"comboBox_baund_sate")
        self.comboBox_baund_sate.setMinimumSize(QSize(0, 25))
        self.comboBox_baund_sate.setEditable(True)

        self.horizontalLayout_12.addWidget(self.comboBox_baund_sate)

        self.checkBox_sate = QCheckBox(self.verticalWidget)
        self.checkBox_sate.setObjectName(u"checkBox_sate")
        sizePolicy2.setHeightForWidth(self.checkBox_sate.sizePolicy().hasHeightForWidth())
        self.checkBox_sate.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.checkBox_sate)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy8.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy8)

        self.horizontalLayout_13.addWidget(self.label_2)

        self.comboBox_rulename_sate = QComboBox(self.verticalWidget)
        self.comboBox_rulename_sate.addItem("")
        self.comboBox_rulename_sate.setObjectName(u"comboBox_rulename_sate")
        self.comboBox_rulename_sate.setEditable(True)

        self.horizontalLayout_13.addWidget(self.comboBox_rulename_sate)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.textBrowser_filePath = QTextBrowser(self.verticalWidget)
        self.textBrowser_filePath.setObjectName(u"textBrowser_filePath")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.textBrowser_filePath.sizePolicy().hasHeightForWidth())
        self.textBrowser_filePath.setSizePolicy(sizePolicy9)
        self.textBrowser_filePath.setMinimumSize(QSize(0, 60))
        self.textBrowser_filePath.setMaximumSize(QSize(16777215, 80))
        self.textBrowser_filePath.setSizeIncrement(QSize(0, 0))
        self.textBrowser_filePath.setLineWrapMode(QTextEdit.NoWrap)
        self.textBrowser_filePath.setReadOnly(False)
        self.textBrowser_filePath.setOverwriteMode(False)
        self.textBrowser_filePath.setAcceptRichText(True)

        self.verticalLayout.addWidget(self.textBrowser_filePath)

        self.textBrowser_fileCsv = QTextBrowser(self.verticalWidget)
        self.textBrowser_fileCsv.setObjectName(u"textBrowser_fileCsv")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.textBrowser_fileCsv.sizePolicy().hasHeightForWidth())
        self.textBrowser_fileCsv.setSizePolicy(sizePolicy10)
        self.textBrowser_fileCsv.setAutoFillBackground(False)
        self.textBrowser_fileCsv.setTabChangesFocus(False)
        self.textBrowser_fileCsv.setUndoRedoEnabled(False)
        self.textBrowser_fileCsv.setLineWrapMode(QTextEdit.NoWrap)
        self.textBrowser_fileCsv.setAcceptRichText(True)

        self.verticalLayout.addWidget(self.textBrowser_fileCsv)

        self.lineEdit_showPercent = QLineEdit(self.verticalWidget)
        self.lineEdit_showPercent.setObjectName(u"lineEdit_showPercent")

        self.verticalLayout.addWidget(self.lineEdit_showPercent)

        self.frame_2 = QFrame(self.verticalWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy7.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy7)
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.gridLayout_12 = QGridLayout(self.frame_2)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_alignment_time = QLineEdit(self.frame_2)
        self.lineEdit_alignment_time.setObjectName(u"lineEdit_alignment_time")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lineEdit_alignment_time.sizePolicy().hasHeightForWidth())
        self.lineEdit_alignment_time.setSizePolicy(sizePolicy11)

        self.gridLayout_12.addWidget(self.lineEdit_alignment_time, 5, 3, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy8.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_13, 1, 2, 1, 1)

        self.lineEdit_skip_count = QLineEdit(self.frame_2)
        self.lineEdit_skip_count.setObjectName(u"lineEdit_skip_count")
        sizePolicy5.setHeightForWidth(self.lineEdit_skip_count.sizePolicy().hasHeightForWidth())
        self.lineEdit_skip_count.setSizePolicy(sizePolicy5)

        self.gridLayout_12.addWidget(self.lineEdit_skip_count, 5, 1, 1, 1)

        self.lcdNumber_receive_count = QLCDNumber(self.frame_2)
        self.lcdNumber_receive_count.setObjectName(u"lcdNumber_receive_count")
        sizePolicy5.setHeightForWidth(self.lcdNumber_receive_count.sizePolicy().hasHeightForWidth())
        self.lcdNumber_receive_count.setSizePolicy(sizePolicy5)
        self.lcdNumber_receive_count.setMinimumSize(QSize(0, 25))

        self.gridLayout_12.addWidget(self.lcdNumber_receive_count, 0, 3, 1, 1)

        self.lineEdit_height = QLineEdit(self.frame_2)
        self.lineEdit_height.setObjectName(u"lineEdit_height")
        sizePolicy11.setHeightForWidth(self.lineEdit_height.sizePolicy().hasHeightForWidth())
        self.lineEdit_height.setSizePolicy(sizePolicy11)

        self.gridLayout_12.addWidget(self.lineEdit_height, 4, 3, 1, 1)

        self.lcdNumber_error_count = QLCDNumber(self.frame_2)
        self.lcdNumber_error_count.setObjectName(u"lcdNumber_error_count")
        sizePolicy5.setHeightForWidth(self.lcdNumber_error_count.sizePolicy().hasHeightForWidth())
        self.lcdNumber_error_count.setSizePolicy(sizePolicy5)
        self.lcdNumber_error_count.setMinimumSize(QSize(0, 25))

        self.gridLayout_12.addWidget(self.lcdNumber_error_count, 1, 3, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy8.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_14, 0, 2, 1, 1)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        sizePolicy8.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy8.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_24, 3, 2, 1, 1)

        self.lineEdit_plot_axis_2 = QLineEdit(self.frame_2)
        self.lineEdit_plot_axis_2.setObjectName(u"lineEdit_plot_axis_2")
        sizePolicy11.setHeightForWidth(self.lineEdit_plot_axis_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_plot_axis_2.setSizePolicy(sizePolicy11)

        self.gridLayout_12.addWidget(self.lineEdit_plot_axis_2, 3, 1, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy8.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_16, 3, 0, 1, 1)

        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy8.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_23, 2, 2, 1, 1)

        self.lineEdit_longitude = QLineEdit(self.frame_2)
        self.lineEdit_longitude.setObjectName(u"lineEdit_longitude")
        sizePolicy11.setHeightForWidth(self.lineEdit_longitude.sizePolicy().hasHeightForWidth())
        self.lineEdit_longitude.setSizePolicy(sizePolicy11)
        self.lineEdit_longitude.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_longitude.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_longitude.setAutoFillBackground(False)
        self.lineEdit_longitude.setEchoMode(QLineEdit.Normal)
        self.lineEdit_longitude.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.lineEdit_longitude, 2, 3, 1, 1)

        self.lineEdit_plot_axis_1 = QLineEdit(self.frame_2)
        self.lineEdit_plot_axis_1.setObjectName(u"lineEdit_plot_axis_1")
        sizePolicy11.setHeightForWidth(self.lineEdit_plot_axis_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_plot_axis_1.setSizePolicy(sizePolicy11)

        self.gridLayout_12.addWidget(self.lineEdit_plot_axis_1, 2, 1, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        sizePolicy8.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_18, 5, 0, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy8.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_15, 2, 0, 1, 1)

        self.lineEdit_plot_axis_3 = QLineEdit(self.frame_2)
        self.lineEdit_plot_axis_3.setObjectName(u"lineEdit_plot_axis_3")
        sizePolicy11.setHeightForWidth(self.lineEdit_plot_axis_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_plot_axis_3.setSizePolicy(sizePolicy11)

        self.gridLayout_12.addWidget(self.lineEdit_plot_axis_3, 4, 1, 1, 1)

        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy8.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_25, 4, 2, 1, 1)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        sizePolicy8.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy8.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_6, 1, 0, 1, 1)

        self.comboBox_begin_axis = QComboBox(self.frame_2)
        self.comboBox_begin_axis.addItem("")
        self.comboBox_begin_axis.addItem("")
        self.comboBox_begin_axis.setObjectName(u"comboBox_begin_axis")
        sizePolicy5.setHeightForWidth(self.comboBox_begin_axis.sizePolicy().hasHeightForWidth())
        self.comboBox_begin_axis.setSizePolicy(sizePolicy5)
        self.comboBox_begin_axis.setSizeIncrement(QSize(0, 0))
        self.comboBox_begin_axis.setBaseSize(QSize(0, 0))
        self.comboBox_begin_axis.setTabletTracking(False)
        self.comboBox_begin_axis.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_begin_axis.setAcceptDrops(False)
        self.comboBox_begin_axis.setAutoFillBackground(False)
        self.comboBox_begin_axis.setEditable(True)
        self.comboBox_begin_axis.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_begin_axis.setMinimumContentsLength(0)
        self.comboBox_begin_axis.setDuplicatesEnabled(False)

        self.gridLayout_12.addWidget(self.comboBox_begin_axis, 1, 1, 1, 1)

        self.lineEdit_dimensions = QLineEdit(self.frame_2)
        self.lineEdit_dimensions.setObjectName(u"lineEdit_dimensions")
        sizePolicy11.setHeightForWidth(self.lineEdit_dimensions.sizePolicy().hasHeightForWidth())
        self.lineEdit_dimensions.setSizePolicy(sizePolicy11)

        self.gridLayout_12.addWidget(self.lineEdit_dimensions, 3, 3, 1, 1)

        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy8.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.label_26, 5, 2, 1, 1)

        self.lineEdit_type = QLineEdit(self.frame_2)
        self.lineEdit_type.setObjectName(u"lineEdit_type")
        sizePolicy5.setHeightForWidth(self.lineEdit_type.sizePolicy().hasHeightForWidth())
        self.lineEdit_type.setSizePolicy(sizePolicy5)
        self.lineEdit_type.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_12.addWidget(self.lineEdit_type, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.verticalWidget)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy10.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy10)
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_9 = QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(7)
        self.gridLayout_9.setVerticalSpacing(0)
        self.graphicsView_gyr_Y_2 = GraphicsLayoutWidget(self.tab_6)
        self.graphicsView_gyr_Y_2.setObjectName(u"graphicsView_gyr_Y_2")

        self.gridLayout_9.addWidget(self.graphicsView_gyr_Y_2, 1, 0, 1, 1)

        self.graphicsView_gyr_Z_2 = GraphicsLayoutWidget(self.tab_6)
        self.graphicsView_gyr_Z_2.setObjectName(u"graphicsView_gyr_Z_2")
        self.graphicsView_gyr_Z_2.setAcceptDrops(False)
        self.graphicsView_gyr_Z_2.setAutoFillBackground(False)

        self.gridLayout_9.addWidget(self.graphicsView_gyr_Z_2, 2, 0, 1, 1)

        self.graphicsView_gyr_X_2 = GraphicsLayoutWidget(self.tab_6)
        self.graphicsView_gyr_X_2.setObjectName(u"graphicsView_gyr_X_2")

        self.gridLayout_9.addWidget(self.graphicsView_gyr_X_2, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self.tab_6)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.gridLayout_11 = QGridLayout(self.frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(7)
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_receive_data = QTextBrowser(self.frame)
        self.textBrowser_receive_data.setObjectName(u"textBrowser_receive_data")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.textBrowser_receive_data.sizePolicy().hasHeightForWidth())
        self.textBrowser_receive_data.setSizePolicy(sizePolicy12)
        self.textBrowser_receive_data.setLineWrapMode(QTextEdit.NoWrap)

        self.gridLayout_11.addWidget(self.textBrowser_receive_data, 0, 1, 1, 1)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_serial_send = QTextBrowser(self.widget)
        self.textBrowser_serial_send.setObjectName(u"textBrowser_serial_send")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.textBrowser_serial_send.sizePolicy().hasHeightForWidth())
        self.textBrowser_serial_send.setSizePolicy(sizePolicy13)
        self.textBrowser_serial_send.setMinimumSize(QSize(0, 30))
        self.textBrowser_serial_send.setReadOnly(False)

        self.horizontalLayout_7.addWidget(self.textBrowser_serial_send)

        self.pushButton_serial_send = QPushButton(self.widget)
        self.pushButton_serial_send.setObjectName(u"pushButton_serial_send")

        self.horizontalLayout_7.addWidget(self.pushButton_serial_send)


        self.gridLayout_11.addWidget(self.widget, 2, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame)


        self.gridLayout_9.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_10 = QGridLayout(self.tab_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.graphicsView_realtime_xyz = GraphicsLayoutWidget(self.tab_7)
        self.graphicsView_realtime_xyz.setObjectName(u"graphicsView_realtime_xyz")

        self.gridLayout_10.addWidget(self.graphicsView_realtime_xyz, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_0 = QWidget()
        self.tab_0.setObjectName(u"tab_0")
        self.gridLayout_5 = QGridLayout(self.tab_0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.graphicsView_all_plot = GLViewWidget(self.tab_0)
        self.graphicsView_all_plot.setObjectName(u"graphicsView_all_plot")

        self.gridLayout_5.addWidget(self.graphicsView_all_plot, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_0, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.graphicsView_gyr_X = GraphicsLayoutWidget(self.tab_1)
        self.graphicsView_gyr_X.setObjectName(u"graphicsView_gyr_X")

        self.gridLayout.addWidget(self.graphicsView_gyr_X, 0, 0, 1, 1)

        self.graphicsView_gyr_Y = GraphicsLayoutWidget(self.tab_1)
        self.graphicsView_gyr_Y.setObjectName(u"graphicsView_gyr_Y")

        self.gridLayout.addWidget(self.graphicsView_gyr_Y, 2, 0, 1, 1)

        self.graphicsView_gyr_Z = GraphicsLayoutWidget(self.tab_1)
        self.graphicsView_gyr_Z.setObjectName(u"graphicsView_gyr_Z")

        self.gridLayout.addWidget(self.graphicsView_gyr_Z, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.graphicsView_gyr = GraphicsLayoutWidget(self.tab_2)
        self.graphicsView_gyr.setObjectName(u"graphicsView_gyr")

        self.gridLayout_2.addWidget(self.graphicsView_gyr, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(0)
        self.graphicsView_acc_Y = GraphicsLayoutWidget(self.tab_3)
        self.graphicsView_acc_Y.setObjectName(u"graphicsView_acc_Y")

        self.gridLayout_3.addWidget(self.graphicsView_acc_Y, 1, 0, 1, 1)

        self.graphicsView_acc_X = GraphicsLayoutWidget(self.tab_3)
        self.graphicsView_acc_X.setObjectName(u"graphicsView_acc_X")

        self.gridLayout_3.addWidget(self.graphicsView_acc_X, 0, 0, 1, 1)

        self.graphicsView_acc_Z = GraphicsLayoutWidget(self.tab_3)
        self.graphicsView_acc_Z.setObjectName(u"graphicsView_acc_Z")

        self.gridLayout_3.addWidget(self.graphicsView_acc_Z, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_8 = QGridLayout(self.tab_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.graphicsView_acc_pos = GraphicsLayoutWidget(self.tab_5)
        self.graphicsView_acc_pos.setObjectName(u"graphicsView_acc_pos")

        self.gridLayout_8.addWidget(self.graphicsView_acc_pos, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.graphicsView_acc_sqrt = GraphicsLayoutWidget(self.tab_4)
        self.graphicsView_acc_sqrt.setObjectName(u"graphicsView_acc_sqrt")

        self.gridLayout_4.addWidget(self.graphicsView_acc_sqrt, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.graphicsView_time = GraphicsLayoutWidget(self.tab)
        self.graphicsView_time.setObjectName(u"graphicsView_time")

        self.gridLayout_6.addWidget(self.graphicsView_time, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_hextoStr.setText(QCoreApplication.translate("MainWindow", u"Hex\u8f6cStr", None))
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

#if QT_CONFIG(tooltip)
        self.pushButton_open_com.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6253\u5f00\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_open_com.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.pushButton_close_com.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5173\u95ed\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_close_com.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#if QT_CONFIG(tooltip)
        self.pushButton_flush_com.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5237\u65b0\u4e32\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_flush_com.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
#if QT_CONFIG(tooltip)
        self.pushButton_openFile.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8f7d\u5165\u5341\u516d\u8fdb\u5236\u6587\u4ef6\u81ea\u52a8\u89e3\u7b97</p><p>\u8f7d\u5165\u6570\u636e\u6587\u4ef6\u81ea\u52a8\u7ed8\u56fe</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_openFile.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u5165\u6587\u4ef6", None))
        self.pushButton_reloadFile.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u8f7d\u6587\u4ef6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X\u8f74 *", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_bd_X.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>X\u8f74\u7ed8\u5236\u7cfb\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_bd_X.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_bd_X.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Z_std", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_std_Y.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Z\u8f74\u6807\u51c6\u5dee</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_std_Y.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Z\u8f74\u6807\u51c6\u5dee</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_std_Y.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Y\u8f74 *", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_bd_Y.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Y\u8f74\u7ed8\u5236\u7cfb\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_bd_Y.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_bd_Y.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"X_std", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_std_X.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>X\u8f74\u6807\u51c6\u5dee</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_std_X.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_std_X.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Z\u8f74 *", None))
#if QT_CONFIG(whatsthis)
        self.lineEdit_bd_Z.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Z\u8f74\u7ed8\u5236\u7cfb\u6570</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_bd_Z.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Y_std", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_std_Z.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Y\u8f74\u6807\u51c6\u5dee</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_std_Z.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_std_Z.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u6ed1", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_rolls.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u540c\u4e00\u5e73\u6ed1\u7cfb\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_rolls.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_rolls.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u9891\u7387", None))
        self.lineEdit_others2.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u673a\uff1a", None))
        self.comboBox_rulename.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))

        self.radioButton_sate.setText("")
        self.comboBox_com_sate.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.comboBox_com_sate.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))

        self.comboBox_baund_sate.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.comboBox_baund_sate.setItemText(1, QCoreApplication.translate("MainWindow", u"230400", None))
        self.comboBox_baund_sate.setItemText(2, QCoreApplication.translate("MainWindow", u"460800", None))
        self.comboBox_baund_sate.setItemText(3, QCoreApplication.translate("MainWindow", u"921600", None))

        self.checkBox_sate.setText(QCoreApplication.translate("MainWindow", u"\u8f85\u673a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f85\u673a\uff1a", None))
        self.comboBox_rulename_sate.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))

        self.textBrowser_filePath.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_fileCsv.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_alignment_time.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5bf9\u51c6\u4f7f\u7528\u65f6\u95f4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_alignment_time.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_alignment_time.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u9519\u8bef", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_skip_count.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7ed8\u5236\u8df3\u8fc7\u65f6\u95f4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_skip_count.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_skip_count.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_height.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5bf9\u51c6\u53d1\u9001\u9ad8\u5ea6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_height.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_height.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Z\u8f74", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u7eac\u5ea6", None))
        self.lineEdit_plot_axis_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Y\u8f74", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_longitude.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5bf9\u51c6\u53d1\u9001\u7ecf\u5ea6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_longitude.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_longitude.setText("")
        self.lineEdit_plot_axis_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc7", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"X\u8f74", None))
        self.lineEdit_plot_axis_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u5ea6", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb", None))
        self.comboBox_begin_axis.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_begin_axis.setItemText(1, QCoreApplication.translate("MainWindow", u"test_long_combobox_11111111111111111", None))

#if QT_CONFIG(tooltip)
        self.comboBox_begin_axis.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u521d\u59cb\u7ed8\u5236\u8f74\u5411</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.comboBox_begin_axis.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.lineEdit_dimensions.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5bf9\u51c6\u53d1\u9001\u7eac\u5ea6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_dimensions.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_dimensions.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_type.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u60ef\u5bfc\u5f53\u524d\u72b6\u6001</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_type.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_type.setText("")
#if QT_CONFIG(tooltip)
        self.textBrowser_serial_send.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u53d1\u9001\u88c5\u8ba2\u6307\u4ee4\u5341\u516d\u8fdb\u5236\u539f\u59cb\u5185\u5bb9\uff0c\u66f4\u6539\u5de6\u4fa7\u7ecf\u7eac\u9ad8\u65f6\u95f4\uff0c\u81ea\u52a8\u66f4\u65b0</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_serial_send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u566a\u58f0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), QCoreApplication.translate("MainWindow", u"\u5904\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u89d2\u901f\u5ea6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u7d2f\u52a0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u52a0\u901f\u5ea6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u7d2f\u52a0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u5730\u901f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u6233", None))
    # retranslateUi

