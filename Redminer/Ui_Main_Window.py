# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WorkSpace\Redmine_Issue_Tracker\Redminer\Main_Window.ui'
#
# Created: Mon Feb 09 14:25:28 2015
#      by: PyQt4 UI code generator 4.10.1
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

class Ui_Redminer(object):
    def setupUi(self, Redminer):
        Redminer.setObjectName(_fromUtf8("Redminer"))
        Redminer.resize(915, 540)
        self.centralWidget = QtGui.QWidget(Redminer)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setContentsMargins(6, -1, 6, -1)
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.checkBox_source = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_source.setMinimumSize(QtCore.QSize(0, 25))
        self.checkBox_source.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.checkBox_source.setFont(font)
        self.checkBox_source.setObjectName(_fromUtf8("checkBox_source"))
        self.gridLayout_5.addWidget(self.checkBox_source, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setMinimumSize(QtCore.QSize(95, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboBox_project = MyComboBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_project.sizePolicy().hasHeightForWidth())
        self.comboBox_project.setSizePolicy(sizePolicy)
        self.comboBox_project.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_project.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.comboBox_project.setFont(font)
        self.comboBox_project.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_project.setMinimumContentsLength(23)
        self.comboBox_project.setObjectName(_fromUtf8("comboBox_project"))
        self.comboBox_project.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_project, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setMinimumSize(QtCore.QSize(95, 0))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)
        self.pushButton_project_load = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_project_load.sizePolicy().hasHeightForWidth())
        self.pushButton_project_load.setSizePolicy(sizePolicy)
        self.pushButton_project_load.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_project_load.setMaximumSize(QtCore.QSize(80, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.pushButton_project_load.setFont(font)
        self.pushButton_project_load.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_project_load.setObjectName(_fromUtf8("pushButton_project_load"))
        self.gridLayout_5.addWidget(self.pushButton_project_load, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 2, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralWidget)
        self.label_9.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 1, 2, 1, 1)
        self.textEdit_lastCopyTime = QtGui.QTextEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_lastCopyTime.sizePolicy().hasHeightForWidth())
        self.textEdit_lastCopyTime.setSizePolicy(sizePolicy)
        self.textEdit_lastCopyTime.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.textEdit_lastCopyTime.setFont(font)
        self.textEdit_lastCopyTime.setReadOnly(True)
        self.textEdit_lastCopyTime.setObjectName(_fromUtf8("textEdit_lastCopyTime"))
        self.gridLayout_5.addWidget(self.textEdit_lastCopyTime, 1, 1, 1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 3)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridGroupBox = QtGui.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.gridGroupBox.setFont(font)
        self.gridGroupBox.setObjectName(_fromUtf8("gridGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.gridGroupBox)
        self.gridLayout.setContentsMargins(8, -1, 12, -1)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dateEdit_end = QtGui.QDateEdit(self.gridGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_end.sizePolicy().hasHeightForWidth())
        self.dateEdit_end.setSizePolicy(sizePolicy)
        self.dateEdit_end.setMinimumSize(QtCore.QSize(160, 25))
        self.dateEdit_end.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.dateEdit_end.setFont(font)
        self.dateEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2014, 12, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setObjectName(_fromUtf8("dateEdit_end"))
        self.gridLayout.addWidget(self.dateEdit_end, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.dateEdit_start = QtGui.QDateEdit(self.gridGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_start.sizePolicy().hasHeightForWidth())
        self.dateEdit_start.setSizePolicy(sizePolicy)
        self.dateEdit_start.setMinimumSize(QtCore.QSize(160, 25))
        self.dateEdit_start.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.dateEdit_start.setFont(font)
        self.dateEdit_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2014, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setObjectName(_fromUtf8("dateEdit_start"))
        self.gridLayout.addWidget(self.dateEdit_start, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalSlider_accuracy = QtGui.QSlider(self.gridGroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.horizontalSlider_accuracy.setFont(font)
        self.horizontalSlider_accuracy.setMaximum(30)
        self.horizontalSlider_accuracy.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_accuracy.setObjectName(_fromUtf8("horizontalSlider_accuracy"))
        self.horizontalLayout_4.addWidget(self.horizontalSlider_accuracy)
        self.label_accuracy = QtGui.QLabel(self.gridGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_accuracy.sizePolicy().hasHeightForWidth())
        self.label_accuracy.setSizePolicy(sizePolicy)
        self.label_accuracy.setMinimumSize(QtCore.QSize(15, 0))
        self.label_accuracy.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(8)
        self.label_accuracy.setFont(font)
        self.label_accuracy.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_accuracy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_accuracy.setObjectName(_fromUtf8("label_accuracy"))
        self.horizontalLayout_4.addWidget(self.label_accuracy)
        self.label_unit = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(8)
        self.label_unit.setFont(font)
        self.label_unit.setObjectName(_fromUtf8("label_unit"))
        self.horizontalLayout_4.addWidget(self.label_unit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setRowStretch(0, 1)
        self.verticalLayout.addWidget(self.gridGroupBox)
        self.gridGroupBox1 = QtGui.QGroupBox(self.centralWidget)
        self.gridGroupBox1.setMinimumSize(QtCore.QSize(0, 0))
        self.gridGroupBox1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        self.gridGroupBox1.setFont(font)
        self.gridGroupBox1.setObjectName(_fromUtf8("gridGroupBox1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroupBox1)
        self.gridLayout_2.setMargin(10)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_priority = QtGui.QLabel(self.gridGroupBox1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(False)
        font.setWeight(50)
        self.label_priority.setFont(font)
        self.label_priority.setAlignment(QtCore.Qt.AlignCenter)
        self.label_priority.setObjectName(_fromUtf8("label_priority"))
        self.gridLayout_2.addWidget(self.label_priority, 0, 2, 1, 1)
        self.pushButton_status_switch = QtGui.QPushButton(self.gridGroupBox1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_status_switch.sizePolicy().hasHeightForWidth())
        self.pushButton_status_switch.setSizePolicy(sizePolicy)
        self.pushButton_status_switch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_status_switch.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_status_switch.setText(_fromUtf8(""))
        self.pushButton_status_switch.setObjectName(_fromUtf8("pushButton_status_switch"))
        self.gridLayout_2.addWidget(self.pushButton_status_switch, 2, 0, 1, 1)
        self.pushButton_status_select = QtGui.QPushButton(self.gridGroupBox1)
        self.pushButton_status_select.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_status_select.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.pushButton_status_select.setFont(font)
        self.pushButton_status_select.setObjectName(_fromUtf8("pushButton_status_select"))
        self.gridLayout_2.addWidget(self.pushButton_status_select, 1, 0, 1, 1)
        self.pushButton_category_select = QtGui.QPushButton(self.gridGroupBox1)
        self.pushButton_category_select.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_category_select.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.pushButton_category_select.setFont(font)
        self.pushButton_category_select.setObjectName(_fromUtf8("pushButton_category_select"))
        self.gridLayout_2.addWidget(self.pushButton_category_select, 1, 2, 1, 1)
        self.pushButton_category_switch = QtGui.QPushButton(self.gridGroupBox1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_category_switch.sizePolicy().hasHeightForWidth())
        self.pushButton_category_switch.setSizePolicy(sizePolicy)
        self.pushButton_category_switch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_category_switch.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_category_switch.setText(_fromUtf8(""))
        self.pushButton_category_switch.setObjectName(_fromUtf8("pushButton_category_switch"))
        self.gridLayout_2.addWidget(self.pushButton_category_switch, 2, 2, 1, 1)
        self.label_status = QtGui.QLabel(self.gridGroupBox1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(False)
        font.setWeight(50)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout_2.addWidget(self.label_status, 0, 0, 1, 1)
        self.label_severity = QtGui.QLabel(self.gridGroupBox1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(False)
        font.setWeight(50)
        self.label_severity.setFont(font)
        self.label_severity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_severity.setObjectName(_fromUtf8("label_severity"))
        self.gridLayout_2.addWidget(self.label_severity, 0, 1, 1, 1)
        self.pushButton_severity_select = QtGui.QPushButton(self.gridGroupBox1)
        self.pushButton_severity_select.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_severity_select.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.pushButton_severity_select.setFont(font)
        self.pushButton_severity_select.setObjectName(_fromUtf8("pushButton_severity_select"))
        self.gridLayout_2.addWidget(self.pushButton_severity_select, 1, 1, 1, 1)
        self.pushButton_severity_switch = QtGui.QPushButton(self.gridGroupBox1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_severity_switch.sizePolicy().hasHeightForWidth())
        self.pushButton_severity_switch.setSizePolicy(sizePolicy)
        self.pushButton_severity_switch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_severity_switch.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_severity_switch.setText(_fromUtf8(""))
        self.pushButton_severity_switch.setObjectName(_fromUtf8("pushButton_severity_switch"))
        self.gridLayout_2.addWidget(self.pushButton_severity_switch, 2, 1, 1, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.verticalLayout.addWidget(self.gridGroupBox1)
        self.horizontalGroupBox = QtGui.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        self.horizontalGroupBox.setFont(font)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.horizontalGroupBox)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 16)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(8)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_run = QtGui.QPushButton(self.horizontalGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_run.sizePolicy().hasHeightForWidth())
        self.pushButton_run.setSizePolicy(sizePolicy)
        self.pushButton_run.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_run.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.gridLayout_3.addWidget(self.pushButton_run, 0, 0, 1, 1)
        self.pushButton_stop = QtGui.QPushButton(self.horizontalGroupBox)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.gridLayout_3.addWidget(self.pushButton_stop, 0, 1, 1, 1)
        self.pushButton_result = QtGui.QPushButton(self.horizontalGroupBox)
        self.pushButton_result.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_result.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.pushButton_result.setFont(font)
        self.pushButton_result.setObjectName(_fromUtf8("pushButton_result"))
        self.gridLayout_3.addWidget(self.pushButton_result, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 10000, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.textBrowser_console = QtGui.QTextBrowser(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(9)
        self.textBrowser_console.setFont(font)
        self.textBrowser_console.setObjectName(_fromUtf8("textBrowser_console"))
        self.horizontalLayout.addWidget(self.textBrowser_console)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 8)
        Redminer.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Redminer)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 915, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuMenu = QtGui.QMenu(self.menuBar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuCredential = QtGui.QMenu(self.menuBar)
        self.menuCredential.setObjectName(_fromUtf8("menuCredential"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        Redminer.setMenuBar(self.menuBar)
        self.actionSave = QtGui.QAction(Redminer)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionRestart = QtGui.QAction(Redminer)
        self.actionRestart.setObjectName(_fromUtf8("actionRestart"))
        self.actionClear = QtGui.QAction(Redminer)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionSet = QtGui.QAction(Redminer)
        self.actionSet.setObjectName(_fromUtf8("actionSet"))
        self.actionReset = QtGui.QAction(Redminer)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionManual = QtGui.QAction(Redminer)
        self.actionManual.setObjectName(_fromUtf8("actionManual"))
        self.actionAbout = QtGui.QAction(Redminer)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionRestart)
        self.menuMenu.addAction(self.actionClear)
        self.menuCredential.addAction(self.actionSet)
        self.menuCredential.addAction(self.actionReset)
        self.menuAbout.addAction(self.actionManual)
        self.menuAbout.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.menuCredential.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Redminer)
        QtCore.QMetaObject.connectSlotsByName(Redminer)

    def retranslateUi(self, Redminer):
        Redminer.setWindowTitle(_translate("Redminer", "RedMiner", None))
        self.checkBox_source.setText(_translate("Redminer", "Use Local Data Copy (Speedup)", None))
        self.label_7.setText(_translate("Redminer", "Project Name  ", None))
        self.comboBox_project.setItemText(0, _translate("Redminer", " Click To Load Project List", None))
        self.label_8.setText(_translate("Redminer", "Data Source     ", None))
        self.pushButton_project_load.setText(_translate("Redminer", "Load", None))
        self.label_9.setText(_translate("Redminer", "Local Copy Time", None))
        self.textEdit_lastCopyTime.setHtml(_translate("Redminer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">N/A</span></p></body></html>", None))
        self.gridGroupBox.setTitle(_translate("Redminer", "Time Panel", None))
        self.label_2.setText(_translate("Redminer", "  End Date", None))
        self.label_3.setText(_translate("Redminer", "  Start Date", None))
        self.label_4.setText(_translate("Redminer", "  Date Interval ", None))
        self.label_accuracy.setText(_translate("Redminer", "1", None))
        self.label_unit.setText(_translate("Redminer", "( Day )", None))
        self.gridGroupBox1.setTitle(_translate("Redminer", "Filter Panel", None))
        self.label_priority.setText(_translate("Redminer", "Category", None))
        self.pushButton_status_select.setText(_translate("Redminer", "Select", None))
        self.pushButton_category_select.setText(_translate("Redminer", "Select", None))
        self.label_status.setText(_translate("Redminer", "Status", None))
        self.label_severity.setText(_translate("Redminer", "Severity", None))
        self.pushButton_severity_select.setText(_translate("Redminer", "Select", None))
        self.horizontalGroupBox.setTitle(_translate("Redminer", "Task Control", None))
        self.pushButton_run.setText(_translate("Redminer", "Run", None))
        self.pushButton_stop.setText(_translate("Redminer", "Stop", None))
        self.pushButton_result.setText(_translate("Redminer", "Result", None))
        self.menuMenu.setTitle(_translate("Redminer", "Environment", None))
        self.menuCredential.setTitle(_translate("Redminer", "Credential", None))
        self.menuAbout.setTitle(_translate("Redminer", "Help", None))
        self.actionSave.setText(_translate("Redminer", "Save", None))
        self.actionRestart.setText(_translate("Redminer", "Restart", None))
        self.actionClear.setText(_translate("Redminer", "Clear", None))
        self.actionSet.setText(_translate("Redminer", "Set", None))
        self.actionReset.setText(_translate("Redminer", "Reset", None))
        self.actionManual.setText(_translate("Redminer", "Manual", None))
        self.actionAbout.setText(_translate("Redminer", "About", None))

from Utility import MyComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Redminer = QtGui.QMainWindow()
    ui = Ui_Redminer()
    ui.setupUi(Redminer)
    Redminer.show()
    sys.exit(app.exec_())

