# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createRecipe.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(557, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nimiLabel = QtWidgets.QLabel(Dialog)
        self.nimiLabel.setObjectName("nimiLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nimiLabel)
        self.dialogName = QtWidgets.QLineEdit(Dialog)
        self.dialogName.setObjectName("dialogName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dialogName)
        self.aikaLabel = QtWidgets.QLabel(Dialog)
        self.aikaLabel.setObjectName("aikaLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.aikaLabel)
        self.dialogTime = QtWidgets.QLineEdit(Dialog)
        self.dialogTime.setObjectName("dialogTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dialogTime)
        self.lopputulosLabel = QtWidgets.QLabel(Dialog)
        self.lopputulosLabel.setObjectName("lopputulosLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lopputulosLabel)
        self.dialogOutcomeSize = QtWidgets.QLineEdit(Dialog)
        self.dialogOutcomeSize.setObjectName("dialogOutcomeSize")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dialogOutcomeSize)
        self.yksikkLabel = QtWidgets.QLabel(Dialog)
        self.yksikkLabel.setObjectName("yksikkLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.yksikkLabel)
        self.dialogOutcomeUnit = QtWidgets.QLineEdit(Dialog)
        self.dialogOutcomeUnit.setObjectName("dialogOutcomeUnit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dialogOutcomeUnit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.ensimmInenRaakaAineLabel = QtWidgets.QLabel(Dialog)
        self.ensimmInenRaakaAineLabel.setObjectName("ensimmInenRaakaAineLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ensimmInenRaakaAineLabel)
        self.dialogIngredient = QtWidgets.QLineEdit(Dialog)
        self.dialogIngredient.setObjectName("dialogIngredient")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dialogIngredient)
        self.mRLabel = QtWidgets.QLabel(Dialog)
        self.mRLabel.setObjectName("mRLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mRLabel)
        self.DialogQuantity = QtWidgets.QLineEdit(Dialog)
        self.DialogQuantity.setObjectName("DialogQuantity")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DialogQuantity)
        self.yksikkLabel_2 = QtWidgets.QLabel(Dialog)
        self.yksikkLabel_2.setObjectName("yksikkLabel_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.yksikkLabel_2)
        self.dialogUnit = QtWidgets.QLineEdit(Dialog)
        self.dialogUnit.setObjectName("dialogUnit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dialogUnit)
        self.gridLayout.addLayout(self.formLayout_2, 0, 1, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.ekaOhjeLabel = QtWidgets.QLabel(Dialog)
        self.ekaOhjeLabel.setObjectName("ekaOhjeLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ekaOhjeLabel)
        self.dialogInstruction = QtWidgets.QLineEdit(Dialog)
        self.dialogInstruction.setObjectName("dialogInstruction")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dialogInstruction)
        self.gridLayout.addLayout(self.formLayout_3, 0, 2, 1, 1)
        self.createRecipe = QtWidgets.QDialogButtonBox(Dialog)
        self.createRecipe.setOrientation(QtCore.Qt.Horizontal)
        self.createRecipe.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.createRecipe.setObjectName("createRecipe")
        self.gridLayout.addWidget(self.createRecipe, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.createRecipe.accepted.connect(Dialog.accept)
        self.createRecipe.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nimiLabel.setText(_translate("Dialog", "Nimi"))
        self.aikaLabel.setText(_translate("Dialog", "Aika"))
        self.lopputulosLabel.setText(_translate("Dialog", "Lopputulos"))
        self.yksikkLabel.setText(_translate("Dialog", "Yksikkö"))
        self.ensimmInenRaakaAineLabel.setText(_translate("Dialog", "1. raaka-aine"))
        self.mRLabel.setText(_translate("Dialog", "Määrä"))
        self.yksikkLabel_2.setText(_translate("Dialog", "Yksikkö"))
        self.ekaOhjeLabel.setText(_translate("Dialog", "1. Ohje"))

