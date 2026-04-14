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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_sourcePage(object):
    def setupUi(self, sourcePage):
        if not sourcePage.objectName():
            sourcePage.setObjectName(u"sourcePage")
        sourcePage.resize(650, 900)
        self.mainLayout = QVBoxLayout(sourcePage)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.sa_source_code = QScrollArea(sourcePage)
        self.sa_source_code.setObjectName(u"sa_source_code")
        self.sa_source_code.setWidgetResizable(True)
        self.sa_source_code.setFrameShape(QFrame.NoFrame)
        self.sourceCodeScrollContent = QWidget()
        self.sourceCodeScrollContent.setObjectName(u"sourceCodeScrollContent")
        self.sourceCodeScrollLayout = QVBoxLayout(self.sourceCodeScrollContent)
        self.sourceCodeScrollLayout.setSpacing(20)
        self.sourceCodeScrollLayout.setObjectName(u"sourceCodeScrollLayout")
        self.sourceCodeScrollLayout.setContentsMargins(15, 15, 15, 15)
        self.te_preview = QTextEdit(self.sourceCodeScrollContent)
        self.te_preview.setObjectName(u"te_preview")
        self.te_preview.setMinimumSize(QSize(0, 250))
        self.te_preview.setReadOnly(True)

        self.sourceCodeScrollLayout.addWidget(self.te_preview)

        self.grid_styling = QGridLayout()
        self.grid_styling.setObjectName(u"grid_styling")
        self.btn_sel_tags = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_tags.setObjectName(u"btn_sel_tags")
        self.btn_sel_tags.setCheckable(True)

        self.grid_styling.addWidget(self.btn_sel_tags, 0, 0, 1, 1)

        self.btn_sel_attrs = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_attrs.setObjectName(u"btn_sel_attrs")
        self.btn_sel_attrs.setCheckable(True)

        self.grid_styling.addWidget(self.btn_sel_attrs, 0, 1, 1, 1)

        self.btn_sel_strings = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_strings.setObjectName(u"btn_sel_strings")
        self.btn_sel_strings.setCheckable(True)

        self.grid_styling.addWidget(self.btn_sel_strings, 1, 0, 1, 1)

        self.btn_sel_comments = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_comments.setObjectName(u"btn_sel_comments")
        self.btn_sel_comments.setCheckable(True)

        self.grid_styling.addWidget(self.btn_sel_comments, 1, 1, 1, 1)


        self.sourceCodeScrollLayout.addLayout(self.grid_styling)

        self.style_tools = QHBoxLayout()
        self.style_tools.setObjectName(u"style_tools")
        self.btn_style_color = QPushButton(self.sourceCodeScrollContent)
        self.btn_style_color.setObjectName(u"btn_style_color")

        self.style_tools.addWidget(self.btn_style_color)

        self.btn_style_bold = QPushButton(self.sourceCodeScrollContent)
        self.btn_style_bold.setObjectName(u"btn_style_bold")
        self.btn_style_bold.setCheckable(True)

        self.style_tools.addWidget(self.btn_style_bold)

        self.btn_style_italic = QPushButton(self.sourceCodeScrollContent)
        self.btn_style_italic.setObjectName(u"btn_style_italic")
        self.btn_style_italic.setCheckable(True)

        self.style_tools.addWidget(self.btn_style_italic)


        self.sourceCodeScrollLayout.addLayout(self.style_tools)

        self.layout_features = QVBoxLayout()
        self.layout_features.setSpacing(8)
        self.layout_features.setObjectName(u"layout_features")
        self.chk_auto_close = QCheckBox(self.sourceCodeScrollContent)
        self.chk_auto_close.setObjectName(u"chk_auto_close")

        self.layout_features.addWidget(self.chk_auto_close)

        self.chk_line_numbers = QCheckBox(self.sourceCodeScrollContent)
        self.chk_line_numbers.setObjectName(u"chk_line_numbers")

        self.layout_features.addWidget(self.chk_line_numbers)

        self.chk_word_wrap = QCheckBox(self.sourceCodeScrollContent)
        self.chk_word_wrap.setObjectName(u"chk_word_wrap")

        self.layout_features.addWidget(self.chk_word_wrap)

        self.chk_format_save = QCheckBox(self.sourceCodeScrollContent)
        self.chk_format_save.setObjectName(u"chk_format_save")

        self.layout_features.addWidget(self.chk_format_save)


        self.sourceCodeScrollLayout.addLayout(self.layout_features)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sourceCodeScrollLayout.addItem(self.verticalSpacer)

        self.sa_source_code.setWidget(self.sourceCodeScrollContent)

        self.mainLayout.addWidget(self.sa_source_code)


        self.retranslateUi(sourcePage)

        QMetaObject.connectSlotsByName(sourcePage)
    # setupUi

    def retranslateUi(self, sourcePage):
        self.te_preview.setHtml(QCoreApplication.translate("sourcePage", u"<pre style=\"background:#1e1e1e; color:#d4d4d4; padding:10px; border-radius:5px;\">\n"
"<span style=\"color:#808080;\">&lt;!-- HTML --&gt;</span>\n"
"<span style=\"color:#569cd6;\">&lt;div</span> <span style=\"color:#9cdcfe;\">class</span>=<span style=\"color:#ce9178;\">\"box\"</span><span style=\"color:#569cd6;\">&gt;</span>Xyra<span style=\"color:#569cd6;\">&lt;/div&gt;</span>\n"
"\n"
"<span style=\"color:#808080;\">/* CSS */</span>\n"
"<span style=\"color:#d7ba7d;\">.box</span> { <span style=\"color:#9cdcfe;\">display</span>: flex; }\n"
"\n"
"<span style=\"color:#808080;\">// JS</span>\n"
"<span style=\"color:#569cd6;\">const</span> <span style=\"color:#9cdcfe;\">init</span> = () =&gt; <span style=\"color:#b5cea8;\">true</span>;\n"
"</pre>", None))
        self.btn_sel_tags.setText(QCoreApplication.translate("sourcePage", u"HTML Tags", None))
        self.btn_sel_attrs.setText(QCoreApplication.translate("sourcePage", u"Attributes", None))
        self.btn_sel_strings.setText(QCoreApplication.translate("sourcePage", u"Strings", None))
        self.btn_sel_comments.setText(QCoreApplication.translate("sourcePage", u"Comments", None))
        self.btn_style_color.setText(QCoreApplication.translate("sourcePage", u"Color", None))
        self.btn_style_bold.setText(QCoreApplication.translate("sourcePage", u"B", None))
        self.btn_style_italic.setText(QCoreApplication.translate("sourcePage", u"I", None))
        self.chk_auto_close.setText(QCoreApplication.translate("sourcePage", u"Auto-close Tags & Brackets", None))
        self.chk_line_numbers.setText(QCoreApplication.translate("sourcePage", u"Show Line Numbers", None))
        self.chk_word_wrap.setText(QCoreApplication.translate("sourcePage", u"Enable Word Wrap", None))
        self.chk_format_save.setText(QCoreApplication.translate("sourcePage", u"Format on Save", None))
        pass
    # retranslateUi

