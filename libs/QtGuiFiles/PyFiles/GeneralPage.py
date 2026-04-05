# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GeneralPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QHBoxLayout,
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_generalPage(object):
    def setupUi(self, generalPage):
        if not generalPage.objectName():
            generalPage.setObjectName(u"generalPage")
        generalPage.resize(893, 820)
        self.mainLayout = QVBoxLayout(generalPage)
        self.mainLayout.setSpacing(3)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(3, 3, 3, 3)
        self.generalScrollArea = QScrollArea(generalPage)
        self.generalScrollArea.setObjectName(u"generalScrollArea")
        self.generalScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.generalScrollArea.setWidgetResizable(True)
        self.generalScrollContent = QWidget()
        self.generalScrollContent.setObjectName(u"generalScrollContent")
        self.generalScrollContent.setGeometry(QRect(0, 0, 885, 812))
        self.verticalLayout_2 = QVBoxLayout(self.generalScrollContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fontSizeLayout = QHBoxLayout()
        self.fontSizeLayout.setObjectName(u"fontSizeLayout")
        self.fontSizeLayout.setContentsMargins(6, 6, 6, 6)
        self.fontSizeLabel = QLabel(self.generalScrollContent)
        self.fontSizeLabel.setObjectName(u"fontSizeLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontSizeLabel.sizePolicy().hasHeightForWidth())
        self.fontSizeLabel.setSizePolicy(sizePolicy)

        self.fontSizeLayout.addWidget(self.fontSizeLabel)

        self.fontSizeSlider = QSlider(self.generalScrollContent)
        self.fontSizeSlider.setObjectName(u"fontSizeSlider")
        sizePolicy.setHeightForWidth(self.fontSizeSlider.sizePolicy().hasHeightForWidth())
        self.fontSizeSlider.setSizePolicy(sizePolicy)
        self.fontSizeSlider.setMinimum(10)
        self.fontSizeSlider.setMaximum(13)
        self.fontSizeSlider.setOrientation(Qt.Horizontal)

        self.fontSizeLayout.addWidget(self.fontSizeSlider)

        self.fontSizeLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.fontSizeLayout)

        self.fontLayout = QHBoxLayout()
        self.fontLayout.setObjectName(u"fontLayout")
        self.fontLayout.setContentsMargins(6, 6, 6, 6)
        self.fontLabel = QLabel(self.generalScrollContent)
        self.fontLabel.setObjectName(u"fontLabel")
        sizePolicy.setHeightForWidth(self.fontLabel.sizePolicy().hasHeightForWidth())
        self.fontLabel.setSizePolicy(sizePolicy)

        self.fontLayout.addWidget(self.fontLabel)

        self.fontComboBox = QFontComboBox(self.generalScrollContent)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setEditable(False)
        self.fontComboBox.setFrame(True)

        self.fontLayout.addWidget(self.fontComboBox)

        self.fontAddButton = QPushButton(self.generalScrollContent)
        self.fontAddButton.setObjectName(u"fontAddButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fontAddButton.sizePolicy().hasHeightForWidth())
        self.fontAddButton.setSizePolicy(sizePolicy1)

        self.fontLayout.addWidget(self.fontAddButton)

        self.fontLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.fontLayout)

        self.stylesheetLayout = QHBoxLayout()
        self.stylesheetLayout.setObjectName(u"stylesheetLayout")
        self.stylesheetLayout.setContentsMargins(6, 6, 6, 6)
        self.stylesheetLabel = QLabel(self.generalScrollContent)
        self.stylesheetLabel.setObjectName(u"stylesheetLabel")
        sizePolicy.setHeightForWidth(self.stylesheetLabel.sizePolicy().hasHeightForWidth())
        self.stylesheetLabel.setSizePolicy(sizePolicy)

        self.stylesheetLayout.addWidget(self.stylesheetLabel)

        self.stylesheetComboBox = QComboBox(self.generalScrollContent)
        self.stylesheetComboBox.setObjectName(u"stylesheetComboBox")
        sizePolicy.setHeightForWidth(self.stylesheetComboBox.sizePolicy().hasHeightForWidth())
        self.stylesheetComboBox.setSizePolicy(sizePolicy)

        self.stylesheetLayout.addWidget(self.stylesheetComboBox)

        self.stylesheetButton = QPushButton(self.generalScrollContent)
        self.stylesheetButton.setObjectName(u"stylesheetButton")
        sizePolicy1.setHeightForWidth(self.stylesheetButton.sizePolicy().hasHeightForWidth())
        self.stylesheetButton.setSizePolicy(sizePolicy1)

        self.stylesheetLayout.addWidget(self.stylesheetButton)

        self.stylesheetLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.stylesheetLayout)

        self.themeLayout = QHBoxLayout()
        self.themeLayout.setObjectName(u"themeLayout")
        self.themeLayout.setContentsMargins(6, 6, 6, 6)
        self.themeLabel = QLabel(self.generalScrollContent)
        self.themeLabel.setObjectName(u"themeLabel")
        sizePolicy.setHeightForWidth(self.themeLabel.sizePolicy().hasHeightForWidth())
        self.themeLabel.setSizePolicy(sizePolicy)

        self.themeLayout.addWidget(self.themeLabel)

        self.themeComboBox = QComboBox(self.generalScrollContent)
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.themeComboBox.setObjectName(u"themeComboBox")
        sizePolicy.setHeightForWidth(self.themeComboBox.sizePolicy().hasHeightForWidth())
        self.themeComboBox.setSizePolicy(sizePolicy)

        self.themeLayout.addWidget(self.themeComboBox)

        self.themeAddButton = QPushButton(self.generalScrollContent)
        self.themeAddButton.setObjectName(u"themeAddButton")
        sizePolicy1.setHeightForWidth(self.themeAddButton.sizePolicy().hasHeightForWidth())
        self.themeAddButton.setSizePolicy(sizePolicy1)

        self.themeLayout.addWidget(self.themeAddButton)

        self.themeLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.themeLayout)

        self.askOnCloseLayout = QHBoxLayout()
        self.askOnCloseLayout.setObjectName(u"askOnCloseLayout")
        self.askOnCloseLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.askOnCloseLayout.setContentsMargins(6, 6, 6, 6)
        self.askOnCloseLabel = QLabel(self.generalScrollContent)
        self.askOnCloseLabel.setObjectName(u"askOnCloseLabel")
        sizePolicy.setHeightForWidth(self.askOnCloseLabel.sizePolicy().hasHeightForWidth())
        self.askOnCloseLabel.setSizePolicy(sizePolicy)

        self.askOnCloseLayout.addWidget(self.askOnCloseLabel)

        self.askOnCloseComboBox = QComboBox(self.generalScrollContent)
        self.askOnCloseComboBox.addItem("")
        self.askOnCloseComboBox.addItem("")
        self.askOnCloseComboBox.setObjectName(u"askOnCloseComboBox")
        sizePolicy.setHeightForWidth(self.askOnCloseComboBox.sizePolicy().hasHeightForWidth())
        self.askOnCloseComboBox.setSizePolicy(sizePolicy)
        self.askOnCloseComboBox.setMaxCount(2)
        self.askOnCloseComboBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.askOnCloseComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.askOnCloseLayout.addWidget(self.askOnCloseComboBox)

        self.askOnCloseLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.askOnCloseLayout)

        self.checkUpdatesLayout = QHBoxLayout()
        self.checkUpdatesLayout.setObjectName(u"checkUpdatesLayout")
        self.checkUpdatesLayout.setContentsMargins(6, 6, 6, 6)
        self.checkUpdatesLabel = QLabel(self.generalScrollContent)
        self.checkUpdatesLabel.setObjectName(u"checkUpdatesLabel")
        sizePolicy.setHeightForWidth(self.checkUpdatesLabel.sizePolicy().hasHeightForWidth())
        self.checkUpdatesLabel.setSizePolicy(sizePolicy)

        self.checkUpdatesLayout.addWidget(self.checkUpdatesLabel)

        self.checkUpdatesComboBox = QComboBox(self.generalScrollContent)
        self.checkUpdatesComboBox.addItem("")
        self.checkUpdatesComboBox.addItem("")
        self.checkUpdatesComboBox.setObjectName(u"checkUpdatesComboBox")
        self.checkUpdatesComboBox.setMaxVisibleItems(2)
        self.checkUpdatesComboBox.setMaxCount(2)

        self.checkUpdatesLayout.addWidget(self.checkUpdatesComboBox)

        self.checkUpdatesLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.checkUpdatesLayout)

        self.layoutSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.layoutSpacer)

        self.generalScrollArea.setWidget(self.generalScrollContent)

        self.mainLayout.addWidget(self.generalScrollArea)


        self.retranslateUi(generalPage)

        QMetaObject.connectSlotsByName(generalPage)
    # setupUi

    def retranslateUi(self, generalPage):
        generalPage.setWindowTitle(QCoreApplication.translate("generalPage", u"Form", None))
        self.fontSizeLabel.setText(QCoreApplication.translate("generalPage", u"Font size: ", None))
        self.fontLabel.setText(QCoreApplication.translate("generalPage", u"Font: ", None))
        self.fontAddButton.setText(QCoreApplication.translate("generalPage", u"Add font", None))
        self.stylesheetLabel.setText(QCoreApplication.translate("generalPage", u"Stylesheet: ", None))
        self.stylesheetButton.setText(QCoreApplication.translate("generalPage", u"Add stylesheet", None))
        self.themeLabel.setText(QCoreApplication.translate("generalPage", u"Theme: ", None))
        self.themeComboBox.setItemText(0, QCoreApplication.translate("generalPage", u"Default", None))
        self.themeComboBox.setItemText(1, QCoreApplication.translate("generalPage", u"Dark", None))
        self.themeComboBox.setItemText(2, QCoreApplication.translate("generalPage", u"Light", None))

        self.themeAddButton.setText(QCoreApplication.translate("generalPage", u"Add Theme", None))
        self.askOnCloseLabel.setText(QCoreApplication.translate("generalPage", u"Ask on close: ", None))
        self.askOnCloseComboBox.setItemText(0, QCoreApplication.translate("generalPage", u"Yes", None))
        self.askOnCloseComboBox.setItemText(1, QCoreApplication.translate("generalPage", u"No", None))

        self.checkUpdatesLabel.setText(QCoreApplication.translate("generalPage", u"Checking updates automaticly:", None))
        self.checkUpdatesComboBox.setItemText(0, QCoreApplication.translate("generalPage", u"Yes", None))
        self.checkUpdatesComboBox.setItemText(1, QCoreApplication.translate("generalPage", u"No", None))

    # retranslateUi

