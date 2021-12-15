# -*- coding: utf-8 -*-
#test city: (United States, New York), (United Kingdom, London), (Spain, Madrid), (France, Paris), (Austria, Vienna), (Italy, Rome), (Germany, Berlin)
import sys
import folium
import pyowm
import webbrowser
import numpy as np
import pandas as pd
import os
from folium.plugins import MarkerCluster
from folium import FeatureGroup, LayerControl, Map, Marker
from collections import namedtuple
from math import radians, cos, sin, asin, sqrt
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pygame


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 900)


        QToolTip.setFont(QFont('Times', 14))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label.setToolTip("Here you can view the weather at your destination")
        self.label.setStyleSheet("QLabel{\n"
                                 "font: 20pt \"Times\";\n"
                                 "color:#00FFFF ;\n"
                                 "border: none;\n"
                                 "}")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 60, 231, 41))
        self.label2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label2.setObjectName("label")
        self.label2.setToolTip("Here you can view the distance at your destination")
        self.label2.setStyleSheet("QLabel{\n"
                                 "font: 20pt \"Times\";\n"
                                 "color:#00FFFF ;\n"
                                 "border: none;\n"
                                 "}")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(10, 110, 171, 41))
        self.label3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label3.setObjectName("label")
        self.label3.setToolTip("Here you can view the price at your destination")
        self.label3.setStyleSheet("QLabel{\n"
                                 "font: 20pt \"Times\";\n"
                                 "color:#00FFFF ;\n"
                                 "border: none;\n"
                                 "}")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 350, 331, 41))
        self.pushButton.setToolTip("Click here to build path")
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 22pt \"Times\";\n"
"color:#00FFFF ;\n"
"background-color: rgba(0, 50, 50, 0.6);\n"
"border: none ;\n"
"}\n"
"QPushButton:hover{\n"
"color:#7CFC00 ;\n"
"background-color: rgba(0, 50, 50, 0.5);\n"
"}\n"
"QPushButton:pressed{\n"
"color: #CD853F ;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(430, 450, 131, 41))
        self.showButton.setStyleSheet("QPushButton{\n"
                                       "font: 22pt \"Times\";\n"
                                       "color:#00FFFF ;\n"
                                       "min-width: 90px; \n"
                                       "max-width: 90px; \n"
                                       "min-height: 90px; \n"
                                       "max-height: 90px; \n"
                                       "border-radius: 45px; \n"
                                       "background-color: rgba(0, 50, 50, 0.7);\n"
                                       "border: none ;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "color:#7CFC00 ;\n"
                                       "background-color: rgba(0, 50, 50, 0.6);\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "color: #CD853F ;\n"
                                       "}")
        self.showButton.setObjectName("showButton")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(300, 400, 331, 41))
        self.pushButton2.setToolTip("Click here to build path")
        self.pushButton2.setStyleSheet("QPushButton{\n"
                                      "font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 50, 50, 0.6);\n"
                                      "border: none ;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "color:#7CFC00 ;\n"
                                      "background-color: rgba(0, 50, 50, 0.5);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "color: #CD853F ;\n"
                                      "}")
        self.pushButton2.setObjectName("pushButton2")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(780, 10, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setToolTip("Do you want to listen the radio?")
        self.radioButton.setStyleSheet("QRadioButton{\n"
                                 "font: 15pt \"Times\";\n"
                                 "}")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " "))
        self.pushButton.setText(_translate("MainWindow", "Path"))
        self.pushButton2.setText(_translate("MainWindow", "Tour"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.showButton.setText(_translate("MainWindow", "Show"))
        self.label2.setText(_translate("MainWindow", " "))
        self.label3.setText(_translate("MainWindow", " "))

class Ui_ResultWindow(object):

    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(900, 900)

        QToolTip.setFont(QFont('Times', 14))
        self.centralwidget = QtWidgets.QWidget(ResultWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(585, 10, 101, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 20pt \"Times\";")
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{\n"
                                   "font: 22pt \"Times\";\n"
                                   "color:#00FFFF ;\n"
                                   "border: none;\n"
                                   "}")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(680, 10, 201, 41))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 0, 128, 0.2) ;\n"
                                      "border: 4px inset blue;\n"
                                      "")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setToolTip("Here you can input city from: Country, City")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(680, 60, 201, 41))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 0, 128, 0.2) ;\n"
                                      "border: 4px inset blue;\n"
                                      "")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setToolTip("Here you can input city to: Country, City")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(595, 60, 101, 41))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 20pt \"Times\";")
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font: 22pt \"Times\";\n"
                                   "color:#00FFFF ;\n"
                                   "border: none;\n"
                                   "}")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(680, 110, 201, 41))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 0, 128, 0.2) ;\n"
                                      "border: 4px inset blue;\n"
                                      "")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setToolTip("Here you can input priority")
        priority = ["time", "money"]
        pr = QCompleter(priority, self.lineEdit_3)
        self.lineEdit_3.setCompleter(pr)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 110, 101, 41))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("font: 20pt \"Times\";")
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font: 22pt \"Times\";\n"
                                   "color:#00FFFF ;\n"
                                   "border: none;\n"
                                   "}")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 160, 131, 41))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("font: 20pt \"Times\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font: 22pt \"Times\";\n"
                                   "color:#00FFFF ;\n"
                                   "border: none;\n"
                                   "}")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 210, 101, 41))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("font: 20pt \"Times\";")
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font: 22pt \"Times\";\n"
                                   "color:#00FFFF ;\n"
                                   "border: none;\n"
                                   "}")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(680, 160, 201, 41))
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 0, 128, 0.2) ;\n"
                                      "border: 4px inset blue;\n"
                                      "")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setToolTip("Here you can input the marker's color")
        color_list = ["red", "blue", "black", "green", "purple",
                      "yellow", "orange", "white",
                      "brown", "gray", "pink", "Red", "Blue", 'Black', 'Green', 'Purple',
                      "Yellow", "Orange", "White", "Brown", "Gray", "Pink"]
        colors = QCompleter(color_list, self.lineEdit_4)
        self.lineEdit_4.setCompleter(colors)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(680, 210, 201, 41))
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 0, 128, 0.2) ;\n"
                                      "border: 4px inset blue;\n"
                                      "")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setToolTip("Here you can input the type of map: "
                                   "Open street map,MapQuest Open Aerial, Mapbox Bright,Stamen Terrain, "
                                   "Stamen Toner, Stamen Watercolor,CartoDB Positron, CartoDB Dark Matter")

        strList = ["Open street map", "MapQuest Open Aerial", "Mapbox Bright",
                   "Stamen Terrain", "Stamen Toner", "Stamen Watercolor",
                   "CartoDB Positron", "CartoDB dark_matter"]
        completer = QCompleter(strList, self.lineEdit_5)
        self.lineEdit_5.setCompleter(completer)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.statusbar = QtWidgets.QStatusBar(ResultWindow)
        self.statusbar.setObjectName("statusbar")
        ResultWindow.setStatusBar(self.statusbar)

        ResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi2(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi2(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "ResultWindow"))
        self.label.setText(_translate("ResultWindow", "City from: "))
        self.label_2.setText(_translate("ResultWindow", "City to: "))
        self.label_3.setText(_translate("ResultWindow", "Priority: "))
        self.label_4.setText(_translate("ResultWindow", "Marker's color: "))
        self.label_5.setText(_translate("ResultWindow", "Map's type: "))


class ResultWindow(QMainWindow, Ui_ResultWindow):

    def __init__(self, parent=None):
        super(ResultWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("ResultWindow")

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.closebutton = QtWidgets.QPushButton(self)
        self.closebutton.setObjectName("closebutton")
        self.closebutton.clicked.connect(self.btnClosed)
        self.closebutton.setText("Close")
        self.closebutton.setToolTip("Has the choice been made?")
        self.closebutton.setStyleSheet("QPushButton{\n"
"font: 20pt \"Times\";\n"
"color:#000000 ;\n"
"min-width: 94px; \n"
"max-width: 94px; \n"
"min-height: 94px; \n"
"max-height: 94px; \n"
"border-radius: 47px; \n"                                        
"background-color: rgba(200, 14, 14, 1);\n"
"border: none ;\n"
"}\n"
"QPushButton:hover{\n"
"color:#ff0000 ;\n"
"background-color: rgba(255, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed{\n"
"color: #a20707 ;\n"
"}")

        self.verticalLayout.addWidget(self.closebutton)
        self.setWindowTitle("Result")

        self.closebutton.clicked.connect(self.get_result)
        self.closebutton.clicked.connect(self.get_weather_city)

    def init_priority(self):
        priority = self.lineEdit_3.text()
        return priority

    def init_type_of_map(self):
        type_of_map = self.lineEdit_5.text()
        return type_of_map

    def init_color_of_markers(self):
        color_of_markers = self.lineEdit_4.text()
        return color_of_markers

    def get_result(self):
        self.color = self.init_color_of_markers()
        self.type_of_map = self.init_type_of_map()
        self.priority = self.init_priority()
        all_dates = do_graph(self.color, self.type_of_map, self.priority)
        city_from = self.lineEdit.text()
        city_to = self.lineEdit_2.text()
        l = "(" + city_from + ")," + " " + "(" + city_to + ")"
        line = list(map(str, l.split('), ')))
        if len(line) == 2:
            s = line[0][1:]
            city_from = list(map(str, s.split(', ')))
            s = line[1][1:-1]
            city_to = list(map(str, s.split(', ')))
        m = all_dates.dijkstra(city_from, city_to)
        webbrowser.open("file:///Users/admin/Desktop/Project/FeatureGroup.html", new = 2)

    def btnClosed(self):
        self.close()

    def init_city(self):
        city_to = self.lineEdit_2.text()
        filename = 'lines.txt'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        file = open(fullpath, "w")
        file.write(city_to + "\n")
        file.close()

    def get_weather_city(self):
        super(Ui_ResultWindow, self).__init__()

        filename = 'lines.txt'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        file = open(fullpath, "w")
        owm = pyowm.OWM("e4e1efbc1a7afebbbc33ed068b32512c")
        s = self.lineEdit_2.text()
        city_to = s.split(",")[1]
        observation = owm.weather_at_place(city_to)
        w = observation.get_weather()
        temperature = w.get_temperature("celsius")['temp']
        file.write(str(temperature) + "\n")
        file.close()


class Ui_InputingWindow(object):

    def setupUi(self, InputingWindow):
        InputingWindow.setObjectName("InputingWindow")
        InputingWindow.resize(900, 900)

        QToolTip.setFont(QFont('Times', 14))
        self.centralwidget = QtWidgets.QWidget(InputingWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 370, 570, 41))
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 0, 128, 0.2) ;\n"
                                      "border: 4px inset blue;\n"
                                      "")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setToolTip("Input the number of countries: (Country1, City1), (...)")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 420, 281, 41))
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setStyleSheet("font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 0, 128, 0.2) ;\n"
                                      "border: 4px inset blue;\n"
                                      "")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setToolTip("Here you can input the marker's color")

        color_list = ["red", "blue", "black", "green", "purple",
                      "yellow", "orange", "white",
                      "brown", "gray", "pink", "Red", "Blue", 'Black', 'Green', 'Purple',
                      "Yellow", "Orange", "White", "Brown", "Gray", "Pink"]
        colors = QCompleter(color_list, self.lineEdit_6)
        self.lineEdit_6.setCompleter(colors)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(430, 470, 281, 41))
        self.lineEdit_7.setAutoFillBackground(False)
        self.lineEdit_7.setStyleSheet("font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "background-color: rgba(0, 0, 128, 0.2) ;\n"
                                      "border: 4px outset blue;\n"
                                      "")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setToolTip("Here you can input the type of map: "
                                   "Open street map,MapQuest Open Aerial, Mapbox Bright,Stamen Terrain, "
                                   "Stamen Toner, Stamen Watercolor,CartoDB Positron, CartoDB Dark Matter")

        strList = ["Open street map", "MapQuest Open Aerial", "Mapbox Bright",
                   "Stamen Terrain", "Stamen Toner", "Stamen Watercolor",
                   "CartoDB Positron", "CartoDB dark_matter"]
        completer = QCompleter(strList, self.lineEdit_7)
        self.lineEdit_7.setCompleter(completer)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 420, 181, 41))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{\n"
                                 "font: 22pt \"Times\";\n"
                                 "color:#00FFFF ;\n"
                                 "border: none;\n"
                                 "}")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 470, 181, 41))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font: 22pt \"Times\";\n"
                                   "color:#00FFFF ;\n"
                                   "border: none;\n"
                                   "}")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.statusbar = QtWidgets.QStatusBar(InputingWindow)
        self.statusbar.setObjectName("statusbar")
        InputingWindow.setStatusBar(self.statusbar)

        InputingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi3(InputingWindow)
        QtCore.QMetaObject.connectSlotsByName(InputingWindow)

    def retranslateUi3(self, InputingWindow):
        _translate = QtCore.QCoreApplication.translate
        InputingWindow.setWindowTitle(_translate("InputingWindow", "InputingWindow"))
        self.label_2.setText(_translate("InputingWindow", "Marker's color is: "))
        self.label_3.setText(_translate("InputingWindow", "Map's type is: "))

class InputingWindow(QMainWindow, Ui_InputingWindow):

    def __init__(self, parent=None):
        super(InputingWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("InputingWindow")

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.closebutton = QtWidgets.QPushButton(self)
        self.closebutton.setObjectName("closebutton")
        self.closebutton.setText("Close")
        self.closebutton.setToolTip("Has the choice been made?")
        self.closebutton.setStyleSheet("QPushButton{\n"
                                       "font: 20pt \"Times\";\n"
                                       "color:#000000 ;\n"
                                       "min-width: 94px; \n"
                                       "max-width: 94px; \n"
                                       "min-height: 94px; \n"
                                       "max-height: 94px; \n"
                                       "border-radius: 47px; \n"
                                       "background-color: rgba(200, 14, 14, 1);\n"
                                       "border: none ;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "color:#ff0000 ;\n"
                                       "background-color: rgba(255, 0, 0, 0.9);\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "color: #a20707 ;\n"
                                       "}")

        self.verticalLayout.addWidget(self.closebutton)
        self.setWindowTitle("Input points")

        self.closebutton.clicked.connect(self.btnClosed)
        self.closebutton.clicked.connect(self.build_tsp)

    def btnClosed(self):
        self.close()

    def build_tsp(self):
        color_of_markers = self.lineEdit_6.text()
        type_of_map = self.lineEdit_7.text()
        all_dates = do_graph(color_of_markers, type_of_map, "")
        self.points = self.lineEdit_5.text()
        line = list(map(str, self.points.split('), ')))
        countries = []
        for i in range(len(line)):
            s = str(line[i][1:])
            if i == len(line) - 1:
                s = s[:-1]
            countries.append(list(map(str, s.split(', '))))
        m = all_dates.tsp(countries)
        webbrowser.open("file:///Users/admin/Desktop/Project/FeatureGroup.html", new=2)

    def init_points(self):
        self.points = self.lineEdit_5.text()
        return self.points


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Main menu")

        self.pushButton.clicked.connect(self.openDialog)
        self.showButton.clicked.connect(self.print_weather_city)
        #self.pushButton.clicked.connect(self.open_site)
        self.pushButton2.clicked.connect(self.openDialog2)
        self.radioButton.clicked.connect(self.music)
        self.radioButton.setChecked(True)
        self.showButton.clicked.connect(self.print_cost)
        self.showButton.clicked.connect(self.print_distance)

    def openDialog(self):
        self.dialog = ResultWindow(self)
        self.dialog.show()

    def openDialog2(self):
        self.dialog2 = InputingWindow(self)
        self.dialog2.show()

    def print_weather_city(self):
        super(Ui_MainWindow, self).__init__()

        filename = 'lines.txt'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        file = open(fullpath, "r")
        c = 0
        for line in file:
            if c == 0:
                temperature = float(line)
                self.label.setText(f"Weather at your destination is: {temperature}")
            c += 1

    def open_site(self):
        self.loader.show()
        self.loader.loadFinished.connect(self.open_site)

    def music(self):
        radioButton = self.sender()
        filename = 'menu.mp3'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        pygame.mixer.init()
        pygame.mixer.music.load(fullpath)
        pygame.mixer.music.play(-1)
        if radioButton.isChecked():
            pygame.mixer.music.pause()

    def print_cost(self):
        filename = 'lines2.txt'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        file = open(fullpath, "r")
        for line in file:
            cost = float(line)
            self.label3.setText(f"Cost : {cost}" + " $")

    def print_distance(self):
        filename = 'lines3.txt'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        file = open(fullpath, "r")
        for line in file:
            distance = float(line)
            self.label2.setText(f"Total distance: : {distance}" + " km")

class Node:

    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc


class BinaryTree:

    def __init__(self, nodes=[]):
        self.nodes = nodes

    def root(self):
        return self.nodes[0]

    def iparent(self, i):
        return (i - 1) // 2

    def ileft(self, i):
        return 2 * i + 1

    def iright(self, i):
        return 2 * i + 2

    def left(self, i):
        return self.node_at_index(self.ileft(i))

    def right(self, i):
        return self.node_at_index(self.iright(i))

    def parent(self, i):
        return self.node_at_index(self.iparent(i))

    def node_at_index(self, i):
        return self.nodes[i]

    def size(self):
        return len(self.nodes)


class DijkstraNodeDecorator:

    def __init__(self, node):
        self.node = node
        self.prov_dist = float('inf')
        self.hops = []

    def index(self):
        return self.node.index

    def data(self):
        return self.node.data

    def update_data(self, data):
        self.prov_dist = data['prov_dist']
        self.hops = data['hops']
        return self


class MinHeap(BinaryTree):

    def __init__(self, nodes, is_less_than=lambda a, b: a < b, get_index=None, update_node=lambda node, newval: newval):
        BinaryTree.__init__(self, nodes)
        self.order_mapping = list(range(len(nodes)))
        self.is_less_than, self.get_index, self.update_node = is_less_than, get_index, update_node
        self.min_heapify()

    # Изменение в кучу узлов, предполагается, что все поддеревья уже кучи
    def min_heapify_subtree(self, i):

        size = self.size()
        ileft = self.ileft(i)
        iright = self.iright(i)
        imin = i
        if (ileft < size and self.is_less_than(self.nodes[ileft], self.nodes[imin])):
            imin = ileft
        if (iright < size and self.is_less_than(self.nodes[iright], self.nodes[imin])):
            imin = iright
        if (imin != i):
            self.nodes[i], self.nodes[imin] = self.nodes[imin], self.nodes[i]
            # Если есть лямбда для получения абсолютного индекса узла
            # обновляет массив order_mapping для указания, где находится индекс
            # в массиве узлов (осмотр для этого индекса будет 0(1))
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[imin])] = imin
                self.order_mapping[self.get_index(self.nodes[i])] = i
            self.min_heapify_subtree(imin)

    # Превращает в кучу массив, который еще ей не является
    def min_heapify(self):
        for i in range(len(self.nodes), -1, -1):
            self.min_heapify_subtree(i)

    def min(self):
        return self.nodes[0]

    def pop(self):
        min = self.nodes[0]
        if self.size() > 1:
            self.nodes[0] = self.nodes[-1]
            self.nodes.pop()
            # Обновляет order_mapping, если можно
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[0])] = 0
            self.min_heapify_subtree(0)
        elif self.size() == 1:
            self.nodes.pop()
        else:
            return None
        # Если self.get_index существует, обновляет self.order_mapping для указания, что
        # узел индекса больше не в куче
        if self.get_index is not None:
            # Устанавливает значение None для self.order_mapping для обозначения непринадлежности к куче
            self.order_mapping[self.get_index(min)] = None
        return min

    # Обновляет значение узла и подстраивает его, если нужно, чтобы сохранить свойства кучи
    def decrease_key(self, i, val):
        self.nodes[i] = self.update_node(self.nodes[i], val)
        iparent = self.iparent(i)
        while (i != 0 and not self.is_less_than(self.nodes[iparent], self.nodes[i])):
            self.nodes[iparent], self.nodes[i] = self.nodes[i], self.nodes[iparent]
            # Если есть лямбда для получения индекса узла
            # обновляет массив order_mapping для указания, где именно находится индекс
            # в массиве узлов (осмотр этого индекса O(1))
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[iparent])] = iparent
                self.order_mapping[self.get_index(self.nodes[i])] = i
            i = iparent
            iparent = self.iparent(i) if i > 0 else None

    def index_of_node_at(self, i):
        return self.get_index(self.nodes[i])


class Graph:

    def __init__(self, nodes):

        self.adj_list = [[node, []] for node in nodes]
        for i in range(len(nodes)):
            nodes[i].index = i

    def connect_dir(self, node1, node2, weight):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        # Отмечает, что нижеуказанное не предотвращает от добавления связи дважды
        self.adj_list[node1][1].append((node2, weight))

    def connect(self, node1, node2, weight):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    def connections(self, node):
        node = self.get_index_from_node(node)
        return self.adj_list[node][1]

    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index

    def dijkstra(self, src):

        src_index = self.get_index_from_node(src)
        # Указывает узлы к DijkstraNodeDecorators
        # Это инициализирует все предварительные расстояния до бесконечности
        dnodes = [DijkstraNodeDecorator(node_edges[0]) for node_edges in self.adj_list]
        # Устанавливает предварительное расстояние исходного узла до 0 и его массив перескоков к его узлу
        dnodes[src_index].prov_dist = 0
        dnodes[src_index].hops.append(dnodes[src_index].node)
        # Устанавливает все методы настройки кучи
        is_less_than = lambda a, b: a.prov_dist < b.prov_dist
        get_index = lambda node: node.index()
        update_node = lambda node, data: node.update_data(data)

        # Подтверждает работу кучи с DijkstraNodeDecorators с узлами
        heap = MinHeap(dnodes, is_less_than, get_index, update_node)

        min_dist_list = []

        while heap.size() > 0:
            # Получает узел кучи, что еще не просматривался ('seen')
            # и находится на минимальном расстоянии от исходного узла
            min_decorated_node = heap.pop()
            min_dist = min_decorated_node.prov_dist
            hops = min_decorated_node.hops
            min_dist_list.append([min_dist, hops])

            # Получает все следующие перескоки. Это больше не O(n^2) операция
            connections = self.connections(min_decorated_node.node)
            # Для каждой связи обновляет ее путь и полное расстояние от
            # исходного узла, если общее расстояние меньше, чем текущее расстояние
            # в массиве dist
            for (inode, weight) in connections:
                node = self.adj_list[inode][0]
                heap_location = heap.order_mapping[inode]
                if (heap_location is not None):
                    tot_dist = weight + min_dist
                    if tot_dist < heap.nodes[heap_location].prov_dist:
                        hops_cpy = list(hops)
                        hops_cpy.append(node)
                        data = {'prov_dist': tot_dist, 'hops': hops_cpy}
                        heap.decrease_key(heap_location, data)

        return min_dist_list

    def path_from_to(self, from_nod, to_ind):

        l = ([(weight, [n.data for n in node]) for (weight, node) in self.dijkstra(from_nod)])
        path = []
        w = []
        for ob in l:
            if len(ob[1]) > 0:
                if ob[1][len(ob[1]) - 1] == to_ind:
                    # print(l)
                    path = ob[1]
                    w = ob[0]
        ans = [w, path]
        return ans


class do_graph:
    def __init__(self, color, type_of_map, priority):

        airports_from = "airports_from.txt"
        airports_to = "airports_to.txt"
        routes = "routes.txt"
        fullpath1 = QtCore.QDir.current().absoluteFilePath(airports_from)
        fullpath2 = QtCore.QDir.current().absoluteFilePath(airports_to)
        fullpath3 = QtCore.QDir.current().absoluteFilePath(routes)

        self.df_from = pd.read_csv(fullpath1)
        self.df_to = pd.read_csv(fullpath2)
        del self.df_from['Source_from']
        del self.df_from['Type_from']
        del self.df_from['DB_timezone_from']
        del self.df_from['DST_from']
        del self.df_from['ICAO_from']

        del self.df_to['Source_to']
        del self.df_to['Type_to']
        del self.df_to['DB_timezone_to']
        del self.df_to['DST_to']
        del self.df_to['ICAO_to']

        df1 = pd.read_csv(fullpath3)

        del df1['Codeshare']
        del df1['Stops']
        del df1['Equipment']

        self.color = color
        self.type_of_map = type_of_map
        self.priority = priority

        self.color.lower()
        self.type_of_map.lower()

        if self.color == "":
            self.color = "blue"

        if self.type_of_map == "":
            self.type_of_map = "Stamen Terrain"  # "CartoDB dark_matter"

        self.df = pd.merge(df1, self.df_from[['LAT_from', 'LON_from', 'Airport_from_ID', 'City_from', 'Country_from']],
                           how='inner', on='Airport_from_ID')
        self.df = pd.merge(self.df, self.df_to[['LAT_to', 'LON_to', 'Airport_to_ID', 'City_to', 'Country_to']],
                           how='inner', on='Airport_to_ID')
        self.unique_airports = np.unique(self.df_to[["Airport_to_ID"]])

        # Создаем вершины графа
        self.nodes_int = [i for i in range(max(self.unique_airports) + 1)]
        self.nodes = [Node(str(self.nodes_int[i])) for i in range(len(self.nodes_int))]

        self.list_dist = self.list_distance()

        # Создаем граф со списками сежности
        self.g_money = Graph(self.nodes)

        self.g_time = Graph(self.nodes)

        for i in self.list_dist:
            self.g_time.connect(self.nodes[i[0]], self.nodes[i[1]], i[2])
            self.g_money.connect(self.nodes[i[0]], self.nodes[i[1]], i[3])

    def list_distance(self):

        # Расстояние через широты

        def haversine(lat1, lon1, lat2, lon2):
            # Вычисляет расстояние в километрах между двумя точками, учитывая окружность Земли.
            # https://en.wikipedia.org/wiki/Haversine_formula

            # convert decimal degrees to radians
            lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            km = 6367 * c
            return km

        unique_airports = np.unique(self.df[["Airport_from_ID", "Airport_to_ID"]])
        list_dist = []

        for index, row in self.df.iterrows():
            dist = int(haversine(row['LAT_from'], row['LON_from'], row['LAT_to'], row['LON_to']))
            if dist != 0:
                cost = int(np.random.random() * dist)
            else:
                cost = 0
            list_dist.append((row['Airport_from_ID'], row['Airport_to_ID'], dist, cost))

        un_country_city = np.unique(self.df[['City_to']])

        for city in un_country_city:
            df_city = self.df_to[self.df_to['City_to'] == city]
            un_country = np.unique(df_city['Country_to'])
            for country in un_country:
                df_cc = df_city[df_city['Country_to'] == country]
                df_id = np.array(df_cc['Airport_to_ID'])
                for i in df_id:
                    for j in df_id:
                        if i < j:
                            list_dist.append([i, j, 0, 0])
                            list_dist.append([j, i, 0, 0])
        return list_dist

    #################################################
    ## dijkstra ##
    #################################################

    def dijkstra(self, city_from, city_to):
        ############################

        def get_bearing(p1, p2):

            '''
            Returns compass bearing from p1 to p2

            Parameters
            p1 : namedtuple with lat lon
            p2 : namedtuple with lat lon

            Return
            compass bearing of type float

            Notes
            Based on https://gist.github.com/jeromer/2005586
            '''

            long_diff = np.radians(p2.lon - p1.lon)

            lat1 = np.radians(p1.lat)
            lat2 = np.radians(p2.lat)

            x = np.sin(long_diff) * np.cos(lat2)
            y = (np.cos(lat1) * np.sin(lat2)
                 - (np.sin(lat1) * np.cos(lat2)
                    * np.cos(long_diff)))
            bearing = np.degrees(np.arctan2(x, y))

            # adjusting for compass bearing
            if bearing < 0:
                return bearing + 360
            return bearing

        def get_arrows(locations, color='blue', size=5, n_arrows=3):

            '''
            Get a list of correctly placed and rotated
            arrows/markers to be plotted

            Parameters
            locations : list of lists of lat lons that represent the
                        start and end of the line.
                        eg [[41.1132, -96.1993],[41.3810, -95.8021]]
            arrow_color : default is 'blue'
            size : default is 6
            n_arrows : number of arrows to create.  default is 3
            Return
            list of arrows/markers
            '''

            Point = namedtuple('Point', field_names=['lat', 'lon'])

            # creating point from our Point named tuple
            p1 = Point(locations[0][0], locations[0][1])
            p2 = Point(locations[1][0], locations[1][1])

            # getting the rotation needed for our marker.
            # Subtracting 90 to account for the marker's orientation
            # of due East(get_bearing returns North)
            rotation = get_bearing(p1, p2) - 90

            # get an evenly space list of lats and lons for our arrows
            # note that I'm discarding the first and last for aesthetics
            # as I'm using markers to denote the start and end
            arrow_lats = np.linspace(p1.lat, p2.lat, n_arrows + 2)[1:n_arrows + 1]
            arrow_lons = np.linspace(p1.lon, p2.lon, n_arrows + 2)[1:n_arrows + 1]

            arrows = []

            # creating each "arrow" and appending them to our arrows list
            for points in zip(arrow_lats, arrow_lons):
                arrows.append(folium.RegularPolygonMarker(location=points,
                                                     fill_color=color, number_of_sides=3,
                                                     radius=size + 2, rotation=rotation - 15))
            return arrows

        ##########################################################

        def amount_arrows(p1, p2):
            def haversine(lat1, lon1, lat2, lon2):
                # Вычисляет расстояние в километрах между двумя точками, учитывая окружность Земли.
                # https://en.wikipedia.org/wiki/Haversine_formula

                # convert decimal degrees to radians
                lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

                # haversine formula
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
                c = 2 * asin(sqrt(a))
                km = 6367 * c
                return km

            n = int(haversine(p1[0], p1[1], p2[0], p2[1]) / 1000)
            if n == 0:
                n = int(haversine(p1[0], p1[1], p2[0], p2[1]) / 500)
                if n == 0:
                    n = 1
            return n

        def total_cost_dist(path_int):
            cost = 0
            dist = 0
            for i in range(len(path_int) - 1):
                ld = pd.DataFrame(self.list_dist)
                l = ld[ld[0] == path_int[i]]
                l = l[l[1] == path_int[i + 1]]
                cost += l[3].min()
                dist += l[2].min()
            return cost, dist

        priority = self.priority
        bd_f = self.df_from[self.df_from['Country_from'] == city_from[0]]
        int_from = bd_f[bd_f['City_from'] == city_from[1]]['Airport_from_ID'].iloc[0]
        bd_t = self.df_from[self.df_from['Country_from'] == city_to[0]]
        int_to = bd_t[bd_t['City_from'] == city_to[1]]['Airport_from_ID'].iloc[0]

        ans1 = self.g_time.path_from_to(self.nodes[int_from], str(int_to))  # nodes[]- исходная вершина, str - конечная
        ans2 = self.g_money.path_from_to(self.nodes[int_from], str(int_to))

        if priority == 'time':
            path = ans1[1]
        else:
            path_int1 = [int(p) for p in ans1[1]]
            path_int2 = [int(p) for p in ans2[1]]
            if total_cost_dist(path_int1)[0] < total_cost_dist(path_int2)[0]:
                path = ans1[1]
            else:
                path = ans2[1]
        path_int = [int(p) for p in path]

        if len(path) > 0:

            df_airports_path = self.df_from[self.df_from['Airport_from_ID'].isin(path_int)]

            # Собираем точки в нужном порядке
            data = []
            path_city_str = []
            path_country_str = []
            for i in range(len(path)):
                data.append(
                    [float(df_airports_path[df_airports_path['Airport_from_ID'] == int(path[i])]['LAT_from'].iloc[0]),
                     float(df_airports_path[df_airports_path['Airport_from_ID'] == int(path[i])]['LON_from'].iloc[0])]
                )
                path_city_str.append(
                    df_airports_path[df_airports_path['Airport_from_ID'] == int(path[i])]['City_from'].iloc[0])
                path_country_str.append(
                    df_airports_path[df_airports_path['Airport_from_ID'] == int(path[i])]['Country_from'].iloc[0])
                subset = pd.DataFrame(data)

            ####################################################
            ## вывод пути ##
            ####################################################

            for i in range(len(path_city_str)):
                print(path_city_str[i], ',', path_country_str[i], end=' -------> ')
                if i == len(path_city_str) - 1:
                    print(path_city_str[i], ',', path_country_str[i])

            cost = total_cost_dist(path_int)
            distance = cost[1]
            cost = cost[0]
            filename = 'lines2.txt'
            fullpath = QtCore.QDir.current().absoluteFilePath(filename)
            file = open(fullpath, "w")
            file.write(str(cost))

            filename = 'lines3.txt'
            fullpath = QtCore.QDir.current().absoluteFilePath(filename)
            file = open(fullpath, "w")
            file.write(str(distance))

            print(*path_int)
            ################################################
            ## MAP ##
            ################################################

            feature_group = FeatureGroup(name='All airports')
            feature_group2 = FeatureGroup(name='My path')

            m1 = folium.Map(location=[50.296933, -101.9574983], zoom_start=5, tiles=self.type_of_map)
            feature_group.add_to(m1)
            feature_group2.add_to(m1)
            LayerControl().add_to(m1)
            marker_cluster = MarkerCluster().add_to(feature_group)

            for at, on, city, country in zip(self.df_from["LAT_from"],
                                             self.df_from["LON_from"],
                                             self.df_from["City_from"],
                                             self.df_from["Country_from"]):
                folium.CircleMarker(location=[at, on], radius=9, popup=str(city) + ", " + str(country),

                               color="gray", fill_opacity=0.9).add_to(marker_cluster)

            for at, on, city in zip(df_airports_path['LAT_from'], df_airports_path['LON_from'],
                                    df_airports_path['City_from']):
                folium.Marker(location=[at, on],
                         popup=city,
                         icon=folium.Icon(self.color), draggable=False).add_to(feature_group2)

            for i in range(len(subset) - 1):
                p1 = [float(subset.iloc[i][0]), float(subset.iloc[i][1])]
                p2 = [float(subset.iloc[i + 1][0]), float(subset.iloc[i + 1][1])]
                arrows = get_arrows(locations=[p1, p2], n_arrows=amount_arrows(p1, p2))
                for arrow in arrows:
                    arrow.add_to(feature_group2)

        m1.save(os.path.join('FeatureGroup.html'))
        if len(path) == 0:
            print('Вы не сможете добраться до этого города')
        return m1

    ######################################################################
    ##tsp##
    ########################################################################

    def tsp(self, countries):

        def haversine(lat1, lon1, lat2, lon2):
            # Вычисляет расстояние в километрах между двумя точками, учитывая окружность Земли.
            # https://en.wikipedia.org/wiki/Haversine_formula

            # convert decimal degrees to radians
            lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            km1 = 6367 * c
            return km1

        def find_cycle(matrix, n):
            # Функция нахождения минимального элемента, исключая текущий элемент
            def Min(lst, myindex):
                return min(x for idx, x in enumerate(lst) if idx != myindex)

            # функция удаления нужной строки и столбцах
            def Delete(matrix, index1, index2):
                del matrix[index1]
                for i in matrix:
                    del i[index2]
                return matrix

            vert = []
            H = 0
            PathLenght = 0
            Str = []
            Stb = []
            res = []
            result = []
            StartMatrix = []

            for i in range(n):
                Str.append(i)
                Stb.append(i)

            # Сохраняем изначальную матрицу
            for i in range(n): StartMatrix.append(matrix[i].copy())

            # Присваеваем главной диагонали float(inf)
            for i in range(n): matrix[i][i] = float('inf')

            while True:
                # Редуцируем
                # --------------------------------------
                # Вычитаем минимальный элемент в строках
                for i in range(len(matrix)):
                    temp = min(matrix[i])
                    H += temp
                    for j in range(len(matrix)):
                        matrix[i][j] -= temp

                # Вычитаем минимальный элемент в столбцах
                for i in range(len(matrix)):
                    temp = min(row[i] for row in matrix)
                    H += temp
                    for j in range(len(matrix)):
                        matrix[j][i] -= temp
                # --------------------------------------

                # Оцениваем нулевые клетки и ищем нулевую клетку с максимальной оценкой
                # --------------------------------------
                NullMax = 0
                index1 = 0
                index2 = 0
                tmp = 0
                for i in range(len(matrix)):
                    for j in range(len(matrix)):
                        if matrix[i][j] == 0:
                            tmp = Min(matrix[i], j) + Min((row[j] for row in matrix), i)
                            if tmp >= NullMax:
                                NullMax = tmp
                                index1 = i
                                index2 = j
                # --------------------------------------

                # Находим нужный нам путь, записываем его в res и удаляем все ненужное
                res.append(Str[index1])
                res.append(Stb[index2])

                oldIndex1 = Str[index1]
                oldIndex2 = Stb[index2]
                if oldIndex2 in Str and oldIndex1 in Stb:
                    NewIndex1 = Str.index(oldIndex2)
                    NewIndex2 = Stb.index(oldIndex1)
                    matrix[NewIndex1][NewIndex2] = float('inf')
                del Str[index1]
                del Stb[index2]
                matrix = Delete(matrix, index1, index2)
                if len(matrix) == 1:
                    break

            # Формируем порядок пути
            for i in range(0, len(res) - 1, 2):
                if res.count(res[i]) < 2:
                    result.append(res[i])
                    result.append(res[i + 1])
            for i in range(0, len(res) - 1, 2):
                for j in range(0, len(res) - 1, 2):
                    if result[len(result) - 1] == res[j]:
                        result.append(res[j + 1])
            result.append(result[0])

            result = np.array(result)

            return result

        ##################################
        # Осталось вывести их на карту()
        def print_cycle(path_id):
            lons = []
            lats = []
            city = []
            for i in range(len(path_id)):
                df_airports_path = self.df_from[self.df_from['Airport_from_ID'] == path_id[i]]
                df_airports_path = df_airports_path[df_airports_path['Country_from'] == country_path[i]]
                lons.append(df_airports_path['LON_from'].iloc[0])
                lats.append(df_airports_path['LAT_from'].iloc[0])
                city.append(df_airports_path['City_from'].iloc[0])

            feature_group2 = FeatureGroup(name='My path')

            m1 = folium.Map(location=[lons[1], lats[1]], zoom_start=3, tiles=self.type_of_map)

            feature_group2.add_to(m1)
            LayerControl().add_to(m1)

            for at, on, c, country in zip(lats, lons, city, country_path):
                folium.Marker(location=[at, on],
                         popup=c + ", " + country,
                         icon=folium.Icon(self.color)).add_to(feature_group2)

            subset = []
            for i in range(len(lats)):
                subset.append((lats[i], lons[i]))
            for at, on in zip(lats, lons):
                folium.PolyLine(locations=subset, opacity=0.1,
                           color='cadetblue',
                           dash_array='10').add_to(m1)
            return m1

        ############################################

        city_int = []
        n = len(countries)

        for i in range(n):

            db = self.df_from[self.df_from['City_from'] == countries[i][1]]
            db = db[db['Country_from'] == countries[i][0]]
            city_int.append(db['Airport_from_ID'].iloc[0])
        matrix_id = []
        for i in range(n):
            db = self.df_from[self.df_from['City_from'] == countries[i][1]]
            db = db[db['Country_from'] == countries[i][0]]
            id_ports = np.array(db['Airport_from_ID'])
            matrix_id.append(id_ports)

        id_airports = []
        for i in range(0, n):
            db = self.df[self.df['Airport_from_ID'].isin(matrix_id[i])]
            for j in range(n):
                if i == j:
                    continue
                db1 = db[db['Airport_to_ID'].isin(matrix_id[j])]
                #if db1.empty:
                    #break
            if (db1.empty):
                pass
                #print('SORRY')
                #return -1

            id_airports.append(db1['Airport_from_ID'].iloc[0])

        countries_lons = []
        countries_lats = []
        countries_routes = []
        matrix_dist = []

        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    d = 0
                if i != j:
                    db = self.df[self.df['Airport_from_ID'].isin(matrix_id[i])]
                    db1 = db[db['Airport_to_ID'].isin(matrix_id[j])]
                    if db1.empty:
                        d = 100000000000000 #float("inf")
                    else:
                        d = int(haversine(db1['LAT_from'].iloc[0], db1['LON_from'].iloc[0],
                                          db1['LAT_to'].iloc[0], db1['LON_to'].iloc[0]))

                row.append(d)
            matrix_dist.append(row)

        path = find_cycle(matrix_dist, n)
        country_path = []
        path_id = []
        for i in path:
            path_id.append(city_int[i])
            country_path.append(countries[i][0])
        m1 = print_cycle(path_id)
        m1.save(os.path.join('FeatureGroup.html'))
        return m1


stylesheet = """
    QMainWindow {
        background-image: url("/Users/admin/Desktop/Project/fon.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
    
"""

if __name__ == "__main__":


    """Create application"""
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)

    """init"""
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    wonder = MyWindow()
    wonder.show()

    """Hook logic"""

    df_from = pd.read_csv('/Users/admin/Desktop/Project/airports_from.txt')
    df_to = pd.read_csv('/Users/admin/Desktop/Project/airports_to.txt')
    del df_from['Source_from']
    del df_from['Type_from']
    del df_from['DB_timezone_from']
    del df_from['DST_from']
    del df_from['ICAO_from']

    del df_to['Source_to']
    del df_to['Type_to']
    del df_to['DB_timezone_to']
    del df_to['DST_to']
    del df_to['ICAO_to']

    df1 = pd.read_csv('/Users/admin/Desktop/Project/routes.txt')
    del df1['Codeshare']
    del df1['Stops']
    del df1['Equipment']

    df = pd.merge(df1, df_from[['LAT_from', 'LON_from', 'Airport_from_ID', 'City_from', 'Country_from']],
                  how='inner', on='Airport_from_ID')
    df = pd.merge(df, df_to[['LAT_to', 'LON_to', 'Airport_to_ID', 'City_to', 'Country_to']],
                  how='inner', on='Airport_to_ID')
    unique_airports = np.unique(df["Airport_from_ID"])

    """Main loop"""
    sys.exit(app.exec_())
