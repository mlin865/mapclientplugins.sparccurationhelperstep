# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewswidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ViewsWidget(object):
    def setupUi(self, ViewsWidget):
        if not ViewsWidget.objectName():
            ViewsWidget.setObjectName(u"ViewsWidget")
        ViewsWidget.resize(374, 227)
        self.gridLayout = QGridLayout(ViewsWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEditThumbnail = QLineEdit(ViewsWidget)
        self.lineEditThumbnail.setObjectName(u"lineEditThumbnail")

        self.gridLayout.addWidget(self.lineEditThumbnail, 1, 3, 1, 1)

        self.labelThumbnail = QLabel(ViewsWidget)
        self.labelThumbnail.setObjectName(u"labelThumbnail")

        self.gridLayout.addWidget(self.labelThumbnail, 1, 1, 1, 1)

        self.labelPath = QLabel(ViewsWidget)
        self.labelPath.setObjectName(u"labelPath")

        self.gridLayout.addWidget(self.labelPath, 0, 1, 1, 1)

        self.labelAnnotation = QLabel(ViewsWidget)
        self.labelAnnotation.setObjectName(u"labelAnnotation")

        self.gridLayout.addWidget(self.labelAnnotation, 2, 1, 1, 1)

        self.lineEditPath = QLineEdit(ViewsWidget)
        self.lineEditPath.setObjectName(u"lineEditPath")

        self.gridLayout.addWidget(self.lineEditPath, 0, 3, 1, 1)

        self.labelSample = QLabel(ViewsWidget)
        self.labelSample.setObjectName(u"labelSample")

        self.gridLayout.addWidget(self.labelSample, 4, 1, 1, 1)

        self.comboBoxSample = QComboBox(ViewsWidget)
        self.comboBoxSample.addItem("")
        self.comboBoxSample.setObjectName(u"comboBoxSample")

        self.gridLayout.addWidget(self.comboBoxSample, 4, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 3, 1, 1)

        self.comboBoxAnnotation = QComboBox(ViewsWidget)
        self.comboBoxAnnotation.addItem("")
        self.comboBoxAnnotation.setObjectName(u"comboBoxAnnotation")
        self.comboBoxAnnotation.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxAnnotation, 2, 3, 1, 1)


        self.retranslateUi(ViewsWidget)

        QMetaObject.connectSlotsByName(ViewsWidget)
    # setupUi

    def retranslateUi(self, ViewsWidget):
        ViewsWidget.setWindowTitle(QCoreApplication.translate("ViewsWidget", u"ViewsWidget", None))
#if QT_CONFIG(tooltip)
        self.lineEditThumbnail.setToolTip(QCoreApplication.translate("ViewsWidget", u"Relative path from dataset root directory", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelThumbnail.setToolTip(QCoreApplication.translate("ViewsWidget", u"Relative path from dataset root directory", None))
#endif // QT_CONFIG(tooltip)
        self.labelThumbnail.setText(QCoreApplication.translate("ViewsWidget", u"Thumbnail:", None))
#if QT_CONFIG(tooltip)
        self.labelPath.setToolTip(QCoreApplication.translate("ViewsWidget", u"Relative path from dataset root directory", None))
#endif // QT_CONFIG(tooltip)
        self.labelPath.setText(QCoreApplication.translate("ViewsWidget", u"Path:", None))
        self.labelAnnotation.setText(QCoreApplication.translate("ViewsWidget", u"Annotation:", None))
#if QT_CONFIG(tooltip)
        self.lineEditPath.setToolTip(QCoreApplication.translate("ViewsWidget", u"Relative path from dataset root directory", None))
#endif // QT_CONFIG(tooltip)
        self.labelSample.setText(QCoreApplication.translate("ViewsWidget", u"Sample:", None))
        self.comboBoxSample.setItemText(0, QCoreApplication.translate("ViewsWidget", u"--", None))

        self.comboBoxAnnotation.setItemText(0, QCoreApplication.translate("ViewsWidget", u"--", None))

    # retranslateUi

