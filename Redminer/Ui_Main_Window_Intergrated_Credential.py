# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WorkSpace\Redmine_Issue_Tracker\Redminer\Main_Window_Intergrated_Credential.ui'
#
# Created: Mon Jan 05 17:10:19 2015
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
        Redminer.resize(845, 534)
        self.centralWidget = QtGui.QWidget(Redminer)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridGroupBox = QtGui.QGroupBox(self.centralWidget)
        self.gridGroupBox.setObjectName(_fromUtf8("gridGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.gridGroupBox)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.dateEdit_start = QtGui.QDateEdit(self.gridGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_start.sizePolicy().hasHeightForWidth())
        self.dateEdit_start.setSizePolicy(sizePolicy)
        self.dateEdit_start.setMinimumSize(QtCore.QSize(160, 25))
        self.dateEdit_start.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dateEdit_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2014, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setObjectName(_fromUtf8("dateEdit_start"))
        self.gridLayout.addWidget(self.dateEdit_start, 2, 1, 1, 1)
        self.dateEdit_end = QtGui.QDateEdit(self.gridGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_end.sizePolicy().hasHeightForWidth())
        self.dateEdit_end.setSizePolicy(sizePolicy)
        self.dateEdit_end.setMinimumSize(QtCore.QSize(160, 25))
        self.dateEdit_end.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dateEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2014, 12, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setObjectName(_fromUtf8("dateEdit_end"))
        self.gridLayout.addWidget(self.dateEdit_end, 3, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBox_project = QtGui.QComboBox(self.gridGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_project.sizePolicy().hasHeightForWidth())
        self.comboBox_project.setSizePolicy(sizePolicy)
        self.comboBox_project.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_project.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_project.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_project.setMinimumContentsLength(23)
        self.comboBox_project.setObjectName(_fromUtf8("comboBox_project"))
        self.horizontalLayout_3.addWidget(self.comboBox_project)
        self.pushButton_project_load = QtGui.QPushButton(self.gridGroupBox)
        self.pushButton_project_load.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_project_load.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_project_load.setObjectName(_fromUtf8("pushButton_project_load"))
        self.horizontalLayout_3.addWidget(self.pushButton_project_load)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalSlider_accuracy = QtGui.QSlider(self.gridGroupBox)
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
        font.setPointSize(9)
        self.label_accuracy.setFont(font)
        self.label_accuracy.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_accuracy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_accuracy.setObjectName(_fromUtf8("label_accuracy"))
        self.horizontalLayout_4.addWidget(self.label_accuracy)
        self.label_unit = QtGui.QLabel(self.gridGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_unit.setFont(font)
        self.label_unit.setObjectName(_fromUtf8("label_unit"))
        self.horizontalLayout_4.addWidget(self.label_unit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)
        self.checkBox_source = QtGui.QCheckBox(self.gridGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.checkBox_source.setFont(font)
        self.checkBox_source.setObjectName(_fromUtf8("checkBox_source"))
        self.gridLayout.addWidget(self.checkBox_source, 5, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridGroupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridGroupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textEdit_key = QtGui.QTextEdit(self.gridGroupBox)
        self.textEdit_key.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit_key.setObjectName(_fromUtf8("textEdit_key"))
        self.horizontalLayout_2.addWidget(self.textEdit_key)
        self.pushButton_key_set = QtGui.QPushButton(self.gridGroupBox)
        self.pushButton_key_set.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_key_set.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_key_set.setObjectName(_fromUtf8("pushButton_key_set"))
        self.horizontalLayout_2.addWidget(self.pushButton_key_set)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.verticalLayout.addWidget(self.gridGroupBox)
        self.gridGroupBox1 = QtGui.QGroupBox(self.centralWidget)
        self.gridGroupBox1.setMinimumSize(QtCore.QSize(0, 0))
        self.gridGroupBox1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridGroupBox1.setObjectName(_fromUtf8("gridGroupBox1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroupBox1)
        self.gridLayout_2.setContentsMargins(9, 0, 9, 5)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_priority = QtGui.QLabel(self.gridGroupBox1)
        font = QtGui.QFont()
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
        self.pushButton_status_select.setObjectName(_fromUtf8("pushButton_status_select"))
        self.gridLayout_2.addWidget(self.pushButton_status_select, 1, 0, 1, 1)
        self.pushButton_category_select = QtGui.QPushButton(self.gridGroupBox1)
        self.pushButton_category_select.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_category_select.setMaximumSize(QtCore.QSize(16777215, 40))
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
        font.setBold(False)
        font.setWeight(50)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout_2.addWidget(self.label_status, 0, 0, 1, 1)
        self.label_severity = QtGui.QLabel(self.gridGroupBox1)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_severity.setFont(font)
        self.label_severity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_severity.setObjectName(_fromUtf8("label_severity"))
        self.gridLayout_2.addWidget(self.label_severity, 0, 1, 1, 1)
        self.pushButton_severity_select = QtGui.QPushButton(self.gridGroupBox1)
        self.pushButton_severity_select.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_severity_select.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.horizontalGroupBox)
        self.gridLayout_3.setMargin(10)
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
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.gridLayout_3.addWidget(self.pushButton_run, 0, 0, 1, 1)
        self.pushButton_stop = QtGui.QPushButton(self.horizontalGroupBox)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.gridLayout_3.addWidget(self.pushButton_stop, 0, 1, 1, 1)
        self.pushButton_result = QtGui.QPushButton(self.horizontalGroupBox)
        self.pushButton_result.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_result.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_result.setObjectName(_fromUtf8("pushButton_result"))
        self.gridLayout_3.addWidget(self.pushButton_result, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        self.horizontalGroupBox1 = QtGui.QGroupBox(self.centralWidget)
        self.horizontalGroupBox1.setObjectName(_fromUtf8("horizontalGroupBox1"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalGroupBox1)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setMargin(10)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_save = QtGui.QPushButton(self.horizontalGroupBox1)
        self.pushButton_save.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_save.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.horizontalLayout_5.addWidget(self.pushButton_save)
        self.pushButton_restart = QtGui.QPushButton(self.horizontalGroupBox1)
        self.pushButton_restart.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_restart.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_restart.setObjectName(_fromUtf8("pushButton_restart"))
        self.horizontalLayout_5.addWidget(self.pushButton_restart)
        self.pushButton_clear = QtGui.QPushButton(self.horizontalGroupBox1)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_clear.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.horizontalLayout_5.addWidget(self.pushButton_clear)
        self.verticalLayout.addWidget(self.horizontalGroupBox1)
        spacerItem = QtGui.QSpacerItem(20, 1000, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.textBrowser_console = QtGui.QTextBrowser(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        self.textBrowser_console.setFont(font)
        self.textBrowser_console.setObjectName(_fromUtf8("textBrowser_console"))
        self.horizontalLayout.addWidget(self.textBrowser_console)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 8)
        Redminer.setCentralWidget(self.centralWidget)

        self.retranslateUi(Redminer)
        QtCore.QMetaObject.connectSlotsByName(Redminer)

    def retranslateUi(self, Redminer):
        Redminer.setWindowTitle(_translate("Redminer", "Redminer", None))
        self.gridGroupBox.setTitle(_translate("Redminer", "Preference Panel", None))
        self.label.setText(_translate("Redminer", "Project Name", None))
        self.label_3.setText(_translate("Redminer", "Start Date", None))
        self.label_2.setText(_translate("Redminer", "End Date", None))
        self.pushButton_project_load.setText(_translate("Redminer", "< Load", None))
        self.label_4.setText(_translate("Redminer", "Accuracy", None))
        self.label_accuracy.setText(_translate("Redminer", "1", None))
        self.label_unit.setText(_translate("Redminer", "( Day )", None))
        self.checkBox_source.setText(_translate("Redminer", "Use local data Cache - Speedup", None))
        self.label_6.setText(_translate("Redminer", "Data Source", None))
        self.label_5.setText(_translate("Redminer", "Credential", None))
        self.pushButton_key_set.setText(_translate("Redminer", "Set", None))
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
        self.horizontalGroupBox1.setTitle(_translate("Redminer", "Environment Control", None))
        self.pushButton_save.setText(_translate("Redminer", "Save", None))
        self.pushButton_restart.setText(_translate("Redminer", "Restart", None))
        self.pushButton_clear.setText(_translate("Redminer", "Clear", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Redminer = QtGui.QMainWindow()
    ui = Ui_Redminer()
    ui.setupUi(Redminer)
    Redminer.show()
    sys.exit(app.exec_())

