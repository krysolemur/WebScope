# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SourcePage.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QHBoxLayout,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_sourcePage(object):
    def setupUi(self, sourcePage):
        if not sourcePage.objectName():
            sourcePage.setObjectName(u"sourcePage")
        sourcePage.resize(978, 793)
        self.mainLayout = QVBoxLayout(sourcePage)
        self.mainLayout.setSpacing(3)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(3, 3, 3, 3)
        self.sourceCodeScrollArea = QScrollArea(sourcePage)
        self.sourceCodeScrollArea.setObjectName(u"sourceCodeScrollArea")
        self.sourceCodeScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sourceCodeScrollArea.setWidgetResizable(True)
        self.sourceCodeScrollArea.setAlignment(Qt.AlignCenter)
        self.sourceCodeScrollContent = QWidget()
        self.sourceCodeScrollContent.setObjectName(u"sourceCodeScrollContent")
        self.sourceCodeScrollContent.setGeometry(QRect(0, 0, 970, 785))
        self.sourceCodeScrollLayout = QVBoxLayout(self.sourceCodeScrollContent)
        self.sourceCodeScrollLayout.setObjectName(u"sourceCodeScrollLayout")
        self.sourceCodeScrollLayout.setContentsMargins(0, 0, 0, 0)
        self.htmlElementsLayout = QHBoxLayout()
        self.htmlElementsLayout.setObjectName(u"htmlElementsLayout")
        self.htmlElementsLayout.setContentsMargins(6, 6, 6, 6)
        self.htmlElementsCheckBox = QCheckBox(self.sourceCodeScrollContent)
        self.htmlElementsCheckBox.setObjectName(u"htmlElementsCheckBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.htmlElementsCheckBox.sizePolicy().hasHeightForWidth())
        self.htmlElementsCheckBox.setSizePolicy(sizePolicy)

        self.htmlElementsLayout.addWidget(self.htmlElementsCheckBox)

        self.htmlElementsButton = QPushButton(self.sourceCodeScrollContent)
        self.htmlElementsButton.setObjectName(u"htmlElementsButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.htmlElementsButton.sizePolicy().hasHeightForWidth())
        self.htmlElementsButton.setSizePolicy(sizePolicy1)

        self.htmlElementsLayout.addWidget(self.htmlElementsButton)

        self.htmlElementsLayout.setStretch(0, 1)

        self.sourceCodeScrollLayout.addLayout(self.htmlElementsLayout)

        self.htmlAtributsLayout = QHBoxLayout()
        self.htmlAtributsLayout.setObjectName(u"htmlAtributsLayout")
        self.htmlAtributsLayout.setContentsMargins(6, 6, 6, 6)
        self.htmlAtributsCheckBox = QCheckBox(self.sourceCodeScrollContent)
        self.htmlAtributsCheckBox.setObjectName(u"htmlAtributsCheckBox")
        sizePolicy.setHeightForWidth(self.htmlAtributsCheckBox.sizePolicy().hasHeightForWidth())
        self.htmlAtributsCheckBox.setSizePolicy(sizePolicy)

        self.htmlAtributsLayout.addWidget(self.htmlAtributsCheckBox)

        self.htmlAtributsButton = QPushButton(self.sourceCodeScrollContent)
        self.htmlAtributsButton.setObjectName(u"htmlAtributsButton")
        sizePolicy1.setHeightForWidth(self.htmlAtributsButton.sizePolicy().hasHeightForWidth())
        self.htmlAtributsButton.setSizePolicy(sizePolicy1)

        self.htmlAtributsLayout.addWidget(self.htmlAtributsButton)

        self.htmlAtributsLayout.setStretch(0, 1)

        self.sourceCodeScrollLayout.addLayout(self.htmlAtributsLayout)

        self.atributsValuesLayout = QHBoxLayout()
        self.atributsValuesLayout.setObjectName(u"atributsValuesLayout")
        self.atributsValuesLayout.setContentsMargins(6, 6, 6, 6)
        self.atributsValuesCheckBox = QCheckBox(self.sourceCodeScrollContent)
        self.atributsValuesCheckBox.setObjectName(u"atributsValuesCheckBox")
        sizePolicy.setHeightForWidth(self.atributsValuesCheckBox.sizePolicy().hasHeightForWidth())
        self.atributsValuesCheckBox.setSizePolicy(sizePolicy)
        self.atributsValuesCheckBox.setTristate(False)

        self.atributsValuesLayout.addWidget(self.atributsValuesCheckBox)

        self.atributsValuesButton = QPushButton(self.sourceCodeScrollContent)
        self.atributsValuesButton.setObjectName(u"atributsValuesButton")
        sizePolicy1.setHeightForWidth(self.atributsValuesButton.sizePolicy().hasHeightForWidth())
        self.atributsValuesButton.setSizePolicy(sizePolicy1)

        self.atributsValuesLayout.addWidget(self.atributsValuesButton)

        self.atributsValuesLayout.setStretch(0, 1)

        self.sourceCodeScrollLayout.addLayout(self.atributsValuesLayout)

        self.sourceCodeLayoutSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sourceCodeScrollLayout.addItem(self.sourceCodeLayoutSpacer)

        self.sourceCodeScrollArea.setWidget(self.sourceCodeScrollContent)

        self.mainLayout.addWidget(self.sourceCodeScrollArea)


        self.retranslateUi(sourcePage)

        QMetaObject.connectSlotsByName(sourcePage)
    # setupUi

    def retranslateUi(self, sourcePage):
        sourcePage.setWindowTitle(QCoreApplication.translate("sourcePage", u"Form", None))
        self.htmlElementsCheckBox.setText(QCoreApplication.translate("sourcePage", u"Mark html elements", None))
        self.htmlElementsButton.setText(QCoreApplication.translate("sourcePage", u"Style", None))
        self.htmlAtributsCheckBox.setText(QCoreApplication.translate("sourcePage", u"Mark html atributs", None))
        self.htmlAtributsButton.setText(QCoreApplication.translate("sourcePage", u"Style", None))
        self.atributsValuesCheckBox.setText(QCoreApplication.translate("sourcePage", u"Mark atributs values", None))
        self.atributsValuesButton.setText(QCoreApplication.translate("sourcePage", u"Style", None))
    # retranslateUi

