# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReseptiGUI1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(985, 731)
        MainWindow.setMouseTracking(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.nimiLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.nimiLabel.setObjectName("nimiLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nimiLabel)
        self.storageName = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.storageName.setReadOnly(True)
        self.storageName.setClearButtonEnabled(False)
        self.storageName.setObjectName("storageName")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.storageName)
        self.mRLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.mRLabel.setObjectName("mRLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mRLabel)
        self.storageQuantity = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.storageQuantity.setObjectName("storageQuantity")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.storageQuantity)
        self.yksikkLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.yksikkLabel.setObjectName("yksikkLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.yksikkLabel)
        self.storageUnit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.storageUnit.setObjectName("storageUnit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.storageUnit)
        self.buttonSaveStorageInfo = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.buttonSaveStorageInfo.setDefault(False)
        self.buttonSaveStorageInfo.setObjectName("buttonSaveStorageInfo")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buttonSaveStorageInfo)
        self.buttonPopulateStorage = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.buttonPopulateStorage.setObjectName("buttonPopulateStorage")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonPopulateStorage)
        self.storageTable = QtWidgets.QTableWidget(self.splitter)
        self.storageTable.setStatusTip("")
        self.storageTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.storageTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.storageTable.setObjectName("storageTable")
        self.storageTable.setColumnCount(0)
        self.storageTable.setRowCount(0)
        self.storageTable.horizontalHeader().setCascadingSectionResizes(False)
        self.storageTable.horizontalHeader().setMinimumSectionSize(35)
        self.storageTable.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.nimiLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.nimiLabel_2.setObjectName("nimiLabel_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nimiLabel_2)
        self.ingredientName = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ingredientName.setReadOnly(False)
        self.ingredientName.setObjectName("ingredientName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ingredientName)
        self.tiheysLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tiheysLabel.setObjectName("tiheysLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tiheysLabel)
        self.ingredientDensity = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ingredientDensity.setObjectName("ingredientDensity")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ingredientDensity)
        self.allergeenitLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.allergeenitLabel.setObjectName("allergeenitLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.allergeenitLabel)
        self.ingredientAllergens = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ingredientAllergens.setObjectName("ingredientAllergens")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ingredientAllergens)
        self.reseptiLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.reseptiLabel.setObjectName("reseptiLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.reseptiLabel)
        self.ingredientRecipe = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ingredientRecipe.setObjectName("ingredientRecipe")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ingredientRecipe)
        self.buttonSaveIngredientInfo = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.buttonSaveIngredientInfo.setObjectName("buttonSaveIngredientInfo")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonSaveIngredientInfo)
        self.buttonPopulateIngredients = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.buttonPopulateIngredients.setObjectName("buttonPopulateIngredients")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonPopulateIngredients)
        self.ingredientsTable = QtWidgets.QTableWidget(self.splitter_2)
        self.ingredientsTable.setLineWidth(1)
        self.ingredientsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ingredientsTable.setObjectName("ingredientsTable")
        self.ingredientsTable.setColumnCount(0)
        self.ingredientsTable.setRowCount(0)
        self.ingredientsTable.horizontalHeader().setMinimumSectionSize(35)
        self.ingredientsTable.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_3.addWidget(self.splitter_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.nimiLabel_3 = QtWidgets.QLabel(self.tab_3)
        self.nimiLabel_3.setObjectName("nimiLabel_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nimiLabel_3)
        self.recipeName = QtWidgets.QLineEdit(self.tab_3)
        self.recipeName.setObjectName("recipeName")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.recipeName)
        self.lopputulosLabel = QtWidgets.QLabel(self.tab_3)
        self.lopputulosLabel.setObjectName("lopputulosLabel")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lopputulosLabel)
        self.recipeOutcomeSize = QtWidgets.QLineEdit(self.tab_3)
        self.recipeOutcomeSize.setObjectName("recipeOutcomeSize")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.recipeOutcomeSize)
        self.yksikkLabel_2 = QtWidgets.QLabel(self.tab_3)
        self.yksikkLabel_2.setObjectName("yksikkLabel_2")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.yksikkLabel_2)
        self.recipeOutcomeUnit = QtWidgets.QLineEdit(self.tab_3)
        self.recipeOutcomeUnit.setObjectName("recipeOutcomeUnit")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.recipeOutcomeUnit)
        self.aikaLabel = QtWidgets.QLabel(self.tab_3)
        self.aikaLabel.setObjectName("aikaLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.aikaLabel)
        self.recipeTime = QtWidgets.QLineEdit(self.tab_3)
        self.recipeTime.setObjectName("recipeTime")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.recipeTime)
        self.buttonSaveRecipesInfo = QtWidgets.QPushButton(self.tab_3)
        self.buttonSaveRecipesInfo.setObjectName("buttonSaveRecipesInfo")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonSaveRecipesInfo)
        self.buttonPopulateRecipes = QtWidgets.QPushButton(self.tab_3)
        self.buttonPopulateRecipes.setObjectName("buttonPopulateRecipes")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonPopulateRecipes)
        self.gridLayout.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.recipeIngredientsList = QtWidgets.QListWidget(self.tab_3)
        self.recipeIngredientsList.setObjectName("recipeIngredientsList")
        self.gridLayout.addWidget(self.recipeIngredientsList, 0, 1, 1, 1)
        self.recipeInstructionsList = QtWidgets.QListWidget(self.tab_3)
        self.recipeInstructionsList.setObjectName("recipeInstructionsList")
        self.gridLayout.addWidget(self.recipeInstructionsList, 0, 2, 1, 1)
        self.recipesTable = QtWidgets.QTableWidget(self.tab_3)
        self.recipesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.recipesTable.setObjectName("recipesTable")
        self.recipesTable.setColumnCount(0)
        self.recipesTable.setRowCount(0)
        self.recipesTable.horizontalHeader().setMinimumSectionSize(35)
        self.recipesTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.recipesTable, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.searchName = QtWidgets.QLineEdit(self.tab_4)
        self.searchName.setObjectName("searchName")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.searchName)
        self.buttonSearchName = QtWidgets.QPushButton(self.tab_4)
        self.buttonSearchName.setObjectName("buttonSearchName")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.buttonSearchName)
        self.nimiLabel_4 = QtWidgets.QLabel(self.tab_4)
        self.nimiLabel_4.setObjectName("nimiLabel_4")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nimiLabel_4)
        self.gridLayout_2.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.raakaAineLabel = QtWidgets.QLabel(self.tab_4)
        self.raakaAineLabel.setObjectName("raakaAineLabel")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.raakaAineLabel)
        self.searchIngredient = QtWidgets.QLineEdit(self.tab_4)
        self.searchIngredient.setObjectName("searchIngredient")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.searchIngredient)
        self.buttonSearchIngredient = QtWidgets.QPushButton(self.tab_4)
        self.buttonSearchIngredient.setObjectName("buttonSearchIngredient")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.buttonSearchIngredient)
        self.gridLayout_2.addLayout(self.formLayout_6, 0, 1, 1, 1)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.vHintNLabel = QtWidgets.QLabel(self.tab_4)
        self.vHintNLabel.setObjectName("vHintNLabel")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vHintNLabel)
        self.searchMinN = QtWidgets.QLineEdit(self.tab_4)
        self.searchMinN.setObjectName("searchMinN")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.searchMinN)
        self.buttonSearchMinN = QtWidgets.QPushButton(self.tab_4)
        self.buttonSearchMinN.setObjectName("buttonSearchMinN")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.buttonSearchMinN)
        self.gridLayout_2.addLayout(self.formLayout_8, 0, 2, 1, 1)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.maksimissaanPuuttuuLabel = QtWidgets.QLabel(self.tab_4)
        self.maksimissaanPuuttuuLabel.setObjectName("maksimissaanPuuttuuLabel")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.maksimissaanPuuttuuLabel)
        self.searchNMissing = QtWidgets.QLineEdit(self.tab_4)
        self.searchNMissing.setObjectName("searchNMissing")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.searchNMissing)
        self.buttonSearchNMissing = QtWidgets.QPushButton(self.tab_4)
        self.buttonSearchNMissing.setObjectName("buttonSearchNMissing")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.buttonSearchNMissing)
        self.gridLayout_2.addLayout(self.formLayout_7, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget, 2, 0, 1, 4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.buttonLoadAll = QtWidgets.QPushButton(self.tab_5)
        self.buttonLoadAll.setObjectName("buttonLoadAll")
        self.verticalLayout_2.addWidget(self.buttonLoadAll)
        self.buttonLoadIngredients = QtWidgets.QPushButton(self.tab_5)
        self.buttonLoadIngredients.setObjectName("buttonLoadIngredients")
        self.verticalLayout_2.addWidget(self.buttonLoadIngredients)
        self.buttonLoadRecipes = QtWidgets.QPushButton(self.tab_5)
        self.buttonLoadRecipes.setObjectName("buttonLoadRecipes")
        self.verticalLayout_2.addWidget(self.buttonLoadRecipes)
        self.buttonLoadStorage = QtWidgets.QPushButton(self.tab_5)
        self.buttonLoadStorage.setObjectName("buttonLoadStorage")
        self.verticalLayout_2.addWidget(self.buttonLoadStorage)
        self.buttonLoadSettings = QtWidgets.QPushButton(self.tab_5)
        self.buttonLoadSettings.setObjectName("buttonLoadSettings")
        self.verticalLayout_2.addWidget(self.buttonLoadSettings)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonSaveAll = QtWidgets.QPushButton(self.tab_5)
        self.buttonSaveAll.setObjectName("buttonSaveAll")
        self.verticalLayout.addWidget(self.buttonSaveAll)
        self.buttonSaveIngredients = QtWidgets.QPushButton(self.tab_5)
        self.buttonSaveIngredients.setObjectName("buttonSaveIngredients")
        self.verticalLayout.addWidget(self.buttonSaveIngredients)
        self.buttonSaveRecipes = QtWidgets.QPushButton(self.tab_5)
        self.buttonSaveRecipes.setObjectName("buttonSaveRecipes")
        self.verticalLayout.addWidget(self.buttonSaveRecipes)
        self.buttonSaveStorage = QtWidgets.QPushButton(self.tab_5)
        self.buttonSaveStorage.setObjectName("buttonSaveStorage")
        self.verticalLayout.addWidget(self.buttonSaveStorage)
        self.buttonSaveSettings = QtWidgets.QPushButton(self.tab_5)
        self.buttonSaveSettings.setObjectName("buttonSaveSettings")
        self.verticalLayout.addWidget(self.buttonSaveSettings)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.raakaAineetLabel = QtWidgets.QLabel(self.tab_5)
        self.raakaAineetLabel.setObjectName("raakaAineetLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.raakaAineetLabel)
        self.ingredientsFileLineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.ingredientsFileLineEdit.setText("")
        self.ingredientsFileLineEdit.setObjectName("ingredientsFileLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ingredientsFileLineEdit)
        self.reseptitLabel = QtWidgets.QLabel(self.tab_5)
        self.reseptitLabel.setObjectName("reseptitLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.reseptitLabel)
        self.recipesFileLineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.recipesFileLineEdit.setObjectName("recipesFileLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.recipesFileLineEdit)
        self.varastotilanneLabel = QtWidgets.QLabel(self.tab_5)
        self.varastotilanneLabel.setObjectName("varastotilanneLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.varastotilanneLabel)
        self.storageFileLineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.storageFileLineEdit.setObjectName("storageFileLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.storageFileLineEdit)
        self.asetuksetLabel = QtWidgets.QLabel(self.tab_5)
        self.asetuksetLabel.setObjectName("asetuksetLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.asetuksetLabel)
        self.settingsFileLineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.settingsFileLineEdit.setObjectName("settingsFileLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.settingsFileLineEdit)
        self.buttonSaveFiles = QtWidgets.QPushButton(self.tab_5)
        self.buttonSaveFiles.setObjectName("buttonSaveFiles")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonSaveFiles)
        self.label = QtWidgets.QLabel(self.tab_5)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Älykäs reseptikirja"))
        self.nimiLabel.setText(_translate("MainWindow", "Nimi"))
        self.mRLabel.setText(_translate("MainWindow", "Määrä"))
        self.yksikkLabel.setText(_translate("MainWindow", "Yksikkö"))
        self.buttonSaveStorageInfo.setText(_translate("MainWindow", "Tallenna"))
        self.buttonPopulateStorage.setText(_translate("MainWindow", "Päivitä lista"))
        self.storageTable.setToolTip(_translate("MainWindow", "<html><head/><body><p>Varastossa olevat tuotteet</p></body></html>"))
        self.storageTable.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Varastossa olevat tuotteet</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Varasto"))
        self.nimiLabel_2.setText(_translate("MainWindow", "Nimi"))
        self.tiheysLabel.setText(_translate("MainWindow", "Tiheys"))
        self.allergeenitLabel.setText(_translate("MainWindow", "Allergeenit"))
        self.reseptiLabel.setText(_translate("MainWindow", "Resepti"))
        self.buttonSaveIngredientInfo.setText(_translate("MainWindow", "Tallenna"))
        self.buttonPopulateIngredients.setText(_translate("MainWindow", "Päivitä lista"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Raaka-aineet"))
        self.nimiLabel_3.setText(_translate("MainWindow", "Nimi"))
        self.lopputulosLabel.setText(_translate("MainWindow", "Lopputulos"))
        self.yksikkLabel_2.setText(_translate("MainWindow", "Yksikkö"))
        self.aikaLabel.setText(_translate("MainWindow", "Aika"))
        self.buttonSaveRecipesInfo.setText(_translate("MainWindow", "Tallenna"))
        self.buttonPopulateRecipes.setText(_translate("MainWindow", "Päivitä lista"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Reseptit"))
        self.buttonSearchName.setText(_translate("MainWindow", "Hae"))
        self.nimiLabel_4.setText(_translate("MainWindow", "Nimi"))
        self.raakaAineLabel.setText(_translate("MainWindow", "Raaka-aine"))
        self.buttonSearchIngredient.setText(_translate("MainWindow", "Hae"))
        self.vHintNLabel.setText(_translate("MainWindow", "Vähintään"))
        self.buttonSearchMinN.setText(_translate("MainWindow", "Hae"))
        self.maksimissaanPuuttuuLabel.setText(_translate("MainWindow", "Maksimissaan puuttuu"))
        self.buttonSearchNMissing.setText(_translate("MainWindow", "Hae"))
        self.pushButton.setText(_translate("MainWindow", "Hae kaikki"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Haku"))
        self.label_2.setText(_translate("MainWindow", "Lataa uudelleen"))
        self.buttonLoadAll.setText(_translate("MainWindow", "Kaikki"))
        self.buttonLoadIngredients.setText(_translate("MainWindow", "Raaka-aineet"))
        self.buttonLoadRecipes.setText(_translate("MainWindow", "Reseptit"))
        self.buttonLoadStorage.setText(_translate("MainWindow", "Varastotilanne"))
        self.buttonLoadSettings.setText(_translate("MainWindow", "Asetukset"))
        self.label_3.setText(_translate("MainWindow", "Tallenna"))
        self.buttonSaveAll.setText(_translate("MainWindow", "Kaikki"))
        self.buttonSaveIngredients.setText(_translate("MainWindow", "Raaka-aineet"))
        self.buttonSaveRecipes.setText(_translate("MainWindow", "Reseptit"))
        self.buttonSaveStorage.setText(_translate("MainWindow", "Varastotilanne"))
        self.buttonSaveSettings.setText(_translate("MainWindow", "Asetukset"))
        self.raakaAineetLabel.setText(_translate("MainWindow", "Raaka-aineet"))
        self.reseptitLabel.setText(_translate("MainWindow", "Reseptit"))
        self.varastotilanneLabel.setText(_translate("MainWindow", "Varastotilanne"))
        self.asetuksetLabel.setText(_translate("MainWindow", "Asetukset"))
        self.buttonSaveFiles.setText(_translate("MainWindow", "Tallenna"))
        self.label.setText(_translate("MainWindow", "Tiedostot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Asetukset"))

