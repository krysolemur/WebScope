# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDialog,
    QFontComboBox, QFrame, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.setWindowModality(Qt.WindowModal)
        SettingsDialog.resize(1022, 624)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        SettingsDialog.setMinimumSize(QSize(0, 0))
        SettingsDialog.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        SettingsDialog.setContextMenuPolicy(Qt.NoContextMenu)
        SettingsDialog.setSizeGripEnabled(False)
        SettingsDialog.setModal(True)
        self.mainLayout = QVBoxLayout(SettingsDialog)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsLayout = QHBoxLayout()
        self.settingsLayout.setSpacing(0)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.settingsView = QListWidget(SettingsDialog)
        QListWidgetItem(self.settingsView)
        QListWidgetItem(self.settingsView)
        self.settingsView.setObjectName(u"settingsView")
        sizePolicy.setHeightForWidth(self.settingsView.sizePolicy().hasHeightForWidth())
        self.settingsView.setSizePolicy(sizePolicy)

        self.settingsLayout.addWidget(self.settingsView)

        self.settingsWidget = QStackedWidget(SettingsDialog)
        self.settingsWidget.setObjectName(u"settingsWidget")
        sizePolicy.setHeightForWidth(self.settingsWidget.sizePolicy().hasHeightForWidth())
        self.settingsWidget.setSizePolicy(sizePolicy)
        self.generalPage = QWidget()
        self.generalPage.setObjectName(u"generalPage")
        sizePolicy.setHeightForWidth(self.generalPage.sizePolicy().hasHeightForWidth())
        self.generalPage.setSizePolicy(sizePolicy)
        self.generalPage.setMinimumSize(QSize(0, 0))
        self.generalPage.setMaximumSize(QSize(16777215, 16777215))
        self.generalPageLayout = QHBoxLayout(self.generalPage)
        self.generalPageLayout.setSpacing(3)
        self.generalPageLayout.setObjectName(u"generalPageLayout")
        self.generalPageLayout.setContentsMargins(3, 3, 3, 3)
        self.generalScrollArea = QScrollArea(self.generalPage)
        self.generalScrollArea.setObjectName(u"generalScrollArea")
        sizePolicy.setHeightForWidth(self.generalScrollArea.sizePolicy().hasHeightForWidth())
        self.generalScrollArea.setSizePolicy(sizePolicy)
        self.generalScrollArea.setMinimumSize(QSize(0, 0))
        self.generalScrollArea.setFrameShape(QFrame.NoFrame)
        self.generalScrollArea.setFrameShadow(QFrame.Plain)
        self.generalScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.generalScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.generalScrollArea.setWidgetResizable(True)
        self.generalScrollArea.setAlignment(Qt.AlignCenter)
        self.generalScrollAreaContents = QWidget()
        self.generalScrollAreaContents.setObjectName(u"generalScrollAreaContents")
        self.generalScrollAreaContents.setGeometry(QRect(0, 0, 758, 581))
        sizePolicy.setHeightForWidth(self.generalScrollAreaContents.sizePolicy().hasHeightForWidth())
        self.generalScrollAreaContents.setSizePolicy(sizePolicy)
        self.generalScrollAreaContents.setMinimumSize(QSize(0, 0))
        self.generalScrollAreaContents.setMaximumSize(QSize(16777215, 16777215))
        self.generalScrollAreaLayout = QVBoxLayout(self.generalScrollAreaContents)
        self.generalScrollAreaLayout.setObjectName(u"generalScrollAreaLayout")
        self.askOnCloseLayout = QHBoxLayout()
        self.askOnCloseLayout.setObjectName(u"askOnCloseLayout")
        self.askOnCloseLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.askOnCloseLayout.setContentsMargins(6, 6, 6, 6)
        self.askOnCloseLabel = QLabel(self.generalScrollAreaContents)
        self.askOnCloseLabel.setObjectName(u"askOnCloseLabel")
        sizePolicy.setHeightForWidth(self.askOnCloseLabel.sizePolicy().hasHeightForWidth())
        self.askOnCloseLabel.setSizePolicy(sizePolicy)

        self.askOnCloseLayout.addWidget(self.askOnCloseLabel)

        self.askOnCloseComboBox = QComboBox(self.generalScrollAreaContents)
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

        self.generalScrollAreaLayout.addLayout(self.askOnCloseLayout)

        self.themeLayout = QHBoxLayout()
        self.themeLayout.setObjectName(u"themeLayout")
        self.themeLayout.setContentsMargins(6, 6, 6, 6)
        self.themeLabel = QLabel(self.generalScrollAreaContents)
        self.themeLabel.setObjectName(u"themeLabel")
        sizePolicy.setHeightForWidth(self.themeLabel.sizePolicy().hasHeightForWidth())
        self.themeLabel.setSizePolicy(sizePolicy)

        self.themeLayout.addWidget(self.themeLabel)

        self.themeComboBox = QComboBox(self.generalScrollAreaContents)
        self.themeComboBox.setObjectName(u"themeComboBox")
        sizePolicy.setHeightForWidth(self.themeComboBox.sizePolicy().hasHeightForWidth())
        self.themeComboBox.setSizePolicy(sizePolicy)

        self.themeLayout.addWidget(self.themeComboBox)

        self.themeAddButton = QPushButton(self.generalScrollAreaContents)
        self.themeAddButton.setObjectName(u"themeAddButton")
        sizePolicy.setHeightForWidth(self.themeAddButton.sizePolicy().hasHeightForWidth())
        self.themeAddButton.setSizePolicy(sizePolicy)

        self.themeLayout.addWidget(self.themeAddButton)

        self.themeLayout.setStretch(1, 1)

        self.generalScrollAreaLayout.addLayout(self.themeLayout)

        self.fontLayout = QHBoxLayout()
        self.fontLayout.setObjectName(u"fontLayout")
        self.fontLayout.setContentsMargins(6, 6, 6, 6)
        self.fontLabel = QLabel(self.generalScrollAreaContents)
        self.fontLabel.setObjectName(u"fontLabel")
        sizePolicy.setHeightForWidth(self.fontLabel.sizePolicy().hasHeightForWidth())
        self.fontLabel.setSizePolicy(sizePolicy)

        self.fontLayout.addWidget(self.fontLabel)

        self.fontComboBox = QFontComboBox(self.generalScrollAreaContents)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)

        self.fontLayout.addWidget(self.fontComboBox)

        self.fontAddButton = QPushButton(self.generalScrollAreaContents)
        self.fontAddButton.setObjectName(u"fontAddButton")
        sizePolicy.setHeightForWidth(self.fontAddButton.sizePolicy().hasHeightForWidth())
        self.fontAddButton.setSizePolicy(sizePolicy)

        self.fontLayout.addWidget(self.fontAddButton)

        self.fontLayout.setStretch(1, 1)

        self.generalScrollAreaLayout.addLayout(self.fontLayout)

        self.fontSizeLayout = QHBoxLayout()
        self.fontSizeLayout.setObjectName(u"fontSizeLayout")
        self.fontSizeLayout.setContentsMargins(6, 6, 6, 6)
        self.fontSizeLabel = QLabel(self.generalScrollAreaContents)
        self.fontSizeLabel.setObjectName(u"fontSizeLabel")
        sizePolicy.setHeightForWidth(self.fontSizeLabel.sizePolicy().hasHeightForWidth())
        self.fontSizeLabel.setSizePolicy(sizePolicy)

        self.fontSizeLayout.addWidget(self.fontSizeLabel)

        self.fontSizeSlider = QSlider(self.generalScrollAreaContents)
        self.fontSizeSlider.setObjectName(u"fontSizeSlider")
        sizePolicy.setHeightForWidth(self.fontSizeSlider.sizePolicy().hasHeightForWidth())
        self.fontSizeSlider.setSizePolicy(sizePolicy)
        self.fontSizeSlider.setOrientation(Qt.Horizontal)

        self.fontSizeLayout.addWidget(self.fontSizeSlider)

        self.fontSizeLayout.setStretch(1, 1)

        self.generalScrollAreaLayout.addLayout(self.fontSizeLayout)

        self.generalLayoutSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.generalScrollAreaLayout.addItem(self.generalLayoutSpacer)

        self.generalScrollAreaLayout.setStretch(4, 1)
        self.generalScrollArea.setWidget(self.generalScrollAreaContents)

        self.generalPageLayout.addWidget(self.generalScrollArea)

        self.settingsWidget.addWidget(self.generalPage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.settingsWidget.addWidget(self.page)
        self.shortcustPage = QWidget()
        self.shortcustPage.setObjectName(u"shortcustPage")
        self.settingsWidget.addWidget(self.shortcustPage)

        self.settingsLayout.addWidget(self.settingsWidget)

        self.settingsLayout.setStretch(1, 1)

        self.mainLayout.addLayout(self.settingsLayout)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.buttonsLayout.setContentsMargins(6, 6, 6, 6)
        self.cancelButton = QPushButton(SettingsDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy1)

        self.buttonsLayout.addWidget(self.cancelButton)

        self.resetButton = QPushButton(SettingsDialog)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy1.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy1)

        self.buttonsLayout.addWidget(self.resetButton)

        self.applyButton = QPushButton(SettingsDialog)
        self.applyButton.setObjectName(u"applyButton")
        sizePolicy1.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy1)

        self.buttonsLayout.addWidget(self.applyButton)

        self.removeProfileButton = QPushButton(SettingsDialog)
        self.removeProfileButton.setObjectName(u"removeProfileButton")
        sizePolicy1.setHeightForWidth(self.removeProfileButton.sizePolicy().hasHeightForWidth())
        self.removeProfileButton.setSizePolicy(sizePolicy1)

        self.buttonsLayout.addWidget(self.removeProfileButton)

        self.addProfileButton = QPushButton(SettingsDialog)
        self.addProfileButton.setObjectName(u"addProfileButton")
        sizePolicy1.setHeightForWidth(self.addProfileButton.sizePolicy().hasHeightForWidth())
        self.addProfileButton.setSizePolicy(sizePolicy1)

        self.buttonsLayout.addWidget(self.addProfileButton)

        self.profilesComboBox = QComboBox(SettingsDialog)
        self.profilesComboBox.setObjectName(u"profilesComboBox")
        sizePolicy1.setHeightForWidth(self.profilesComboBox.sizePolicy().hasHeightForWidth())
        self.profilesComboBox.setSizePolicy(sizePolicy1)

        self.buttonsLayout.addWidget(self.profilesComboBox)


        self.mainLayout.addLayout(self.buttonsLayout)

        self.mainLayout.setStretch(0, 1)

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Dialog", None))

        __sortingEnabled = self.settingsView.isSortingEnabled()
        self.settingsView.setSortingEnabled(False)
        ___qlistwidgetitem = self.settingsView.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("SettingsDialog", u"General", None))
        ___qlistwidgetitem1 = self.settingsView.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("SettingsDialog", u"Shortcuts", None))
        self.settingsView.setSortingEnabled(__sortingEnabled)

        self.askOnCloseLabel.setText(QCoreApplication.translate("SettingsDialog", u"Ask on close: ", None))
        self.askOnCloseComboBox.setItemText(0, QCoreApplication.translate("SettingsDialog", u"Yes", None))
        self.askOnCloseComboBox.setItemText(1, QCoreApplication.translate("SettingsDialog", u"No", None))

        self.themeLabel.setText(QCoreApplication.translate("SettingsDialog", u"Theme: ", None))
        self.themeAddButton.setText(QCoreApplication.translate("SettingsDialog", u"Add Theme", None))
        self.fontLabel.setText(QCoreApplication.translate("SettingsDialog", u"Font: ", None))
        self.fontAddButton.setText(QCoreApplication.translate("SettingsDialog", u"Add font", None))
        self.fontSizeLabel.setText(QCoreApplication.translate("SettingsDialog", u"Font size: ", None))
        self.cancelButton.setText(QCoreApplication.translate("SettingsDialog", u"Cancel", None))
        self.resetButton.setText(QCoreApplication.translate("SettingsDialog", u"Reset", None))
        self.applyButton.setText(QCoreApplication.translate("SettingsDialog", u"Apply", None))
        self.removeProfileButton.setText(QCoreApplication.translate("SettingsDialog", u"Remove", None))
        self.addProfileButton.setText(QCoreApplication.translate("SettingsDialog", u"Add", None))
    # retranslateUi

