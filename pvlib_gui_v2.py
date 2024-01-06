
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import matplotlib.pyplot as plt
import pvlib
from pvlib.pvsystem import PVSystem, FixedMount, Array, pvwatts_losses
from pvlib.location import Location
from pvlib.modelchain import ModelChain
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

class Ui_Form(object):

    # defining the global variables
    dataframe = None
    input_latitude = None
    input_longitude = None
    input_timezone = None
    input_plant = None
    input_ghi = None
    input_dhi = None
    input_dni = None
    input_temp = None
    input_windspeed = None
    input_date = None
    input_capacity = None
    input_model_parameters = None
    input_tilt = None
    input_azimuth = None
    input_albedo = None
    input_losses_model = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(912, 527)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(460, 70, 20, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 70, 431, 161))
        self.frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_location = QtWidgets.QLabel(self.frame)
        self.label_location.setGeometry(QtCore.QRect(10, 0, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_location.setFont(font)
        self.label_location.setObjectName("label_location")
        self.lineEdit_latitude = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_latitude.setGeometry(QtCore.QRect(240, 30, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_latitude.setFont(font)
        self.lineEdit_latitude.setObjectName("lineEdit_latitude")
        self.lineEdit_longitude = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_longitude.setGeometry(QtCore.QRect(240, 60, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_longitude.setFont(font)
        self.lineEdit_longitude.setObjectName("lineEdit_longitude")
        self.lineEdit_timezone = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_timezone.setGeometry(QtCore.QRect(240, 90, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_timezone.setFont(font)
        self.lineEdit_timezone.setObjectName("lineEdit_timezone")
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_name.setGeometry(QtCore.QRect(240, 120, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_plant = QtWidgets.QLabel(self.frame)
        self.label_plant.setGeometry(QtCore.QRect(20, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_plant.setFont(font)
        self.label_plant.setObjectName("label_plant")
        self.label_timezone = QtWidgets.QLabel(self.frame)
        self.label_timezone.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_timezone.setFont(font)
        self.label_timezone.setObjectName("label_timezone")
        self.label_latitude = QtWidgets.QLabel(self.frame)
        self.label_latitude.setGeometry(QtCore.QRect(20, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_latitude.setFont(font)
        self.label_latitude.setObjectName("label_latitude")
        self.label_longitude = QtWidgets.QLabel(self.frame)
        self.label_longitude.setGeometry(QtCore.QRect(20, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_longitude.setFont(font)
        self.label_longitude.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_longitude.setObjectName("label_longitude")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(480, 70, 411, 251))
        self.frame_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_weather = QtWidgets.QLabel(self.frame_5)
        self.label_weather.setGeometry(QtCore.QRect(10, 0, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_weather.setFont(font)
        self.label_weather.setObjectName("label_weather")
        self.pushButton_upload = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_upload.setGeometry(QtCore.QRect(260, 30, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setObjectName("pushButton_upload")

        # connection to dataframe button
        self.pushButton_upload.clicked.connect(self.upload_dataframe)

        self.lineEdit_ghi = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_ghi.setGeometry(QtCore.QRect(240, 60, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_ghi.setFont(font)
        self.lineEdit_ghi.setObjectName("lineEdit_ghi")
        self.lineEdit_dhi = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_dhi.setGeometry(QtCore.QRect(240, 90, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dhi.setFont(font)
        self.lineEdit_dhi.setObjectName("lineEdit_dhi")
        self.lineEdit_dni = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_dni.setGeometry(QtCore.QRect(240, 120, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dni.setFont(font)
        self.lineEdit_dni.setObjectName("lineEdit_dni")
        self.lineEdit_temp = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_temp.setGeometry(QtCore.QRect(240, 150, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_temp.setFont(font)
        self.lineEdit_temp.setObjectName("lineEdit_temp")
        self.lineEdit_windspeed = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_windspeed.setGeometry(QtCore.QRect(240, 180, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_windspeed.setFont(font)
        self.lineEdit_windspeed.setObjectName("lineEdit_windspeed")
        self.lineEdit_date = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_date.setGeometry(QtCore.QRect(240, 210, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_date.setFont(font)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.label_date = QtWidgets.QLabel(self.frame_5)
        self.label_date.setGeometry(QtCore.QRect(20, 210, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.label_windspeed = QtWidgets.QLabel(self.frame_5)
        self.label_windspeed.setGeometry(QtCore.QRect(20, 176, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_windspeed.setFont(font)
        self.label_windspeed.setObjectName("label_windspeed")
        self.label_ghi = QtWidgets.QLabel(self.frame_5)
        self.label_ghi.setGeometry(QtCore.QRect(20, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_ghi.setFont(font)
        self.label_ghi.setObjectName("label_ghi")
        self.label_dhi = QtWidgets.QLabel(self.frame_5)
        self.label_dhi.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_dhi.setFont(font)
        self.label_dhi.setObjectName("label_dhi")
        self.label_temp = QtWidgets.QLabel(self.frame_5)
        self.label_temp.setGeometry(QtCore.QRect(20, 150, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_temp.setFont(font)
        self.label_temp.setObjectName("label_temp")
        self.label_dni = QtWidgets.QLabel(self.frame_5)
        self.label_dni.setGeometry(QtCore.QRect(20, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_dni.setFont(font)
        self.label_dni.setObjectName("label_dni")
        self.label_weather_file = QtWidgets.QLabel(self.frame_5)
        self.label_weather_file.setGeometry(QtCore.QRect(20, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_weather_file.setFont(font)
        self.label_weather_file.setObjectName("label_weather_file")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(20, 250, 431, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_system = QtWidgets.QLabel(self.frame_2)
        self.label_system.setGeometry(QtCore.QRect(10, 0, 91, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
        font.setUnderline(True)
        self.label_system.setFont(font)
        self.label_system.setObjectName("label_system")
        self.lineEdit_capacity = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_capacity.setGeometry(QtCore.QRect(240, 30, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_capacity.setFont(font)
        self.lineEdit_capacity.setObjectName("lineEdit_capacity")
        self.comboBox_mounting = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_mounting.setGeometry(QtCore.QRect(240, 60, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_mounting.setFont(font)
        self.comboBox_mounting.setObjectName("comboBox_mounting")
        self.comboBox_mounting.addItem("")
        self.comboBox_mounting.addItem("")
        self.comboBox_mounting.addItem("")
        self.comboBox_mounting.addItem("")
        self.lineEdit_tilt = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_tilt.setGeometry(QtCore.QRect(240, 90, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_tilt.setFont(font)
        self.lineEdit_tilt.setObjectName("lineEdit_tilt")
        self.lineEdit_azimuth = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_azimuth.setGeometry(QtCore.QRect(240, 120, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_azimuth.setFont(font)
        self.lineEdit_azimuth.setObjectName("lineEdit_azimuth")
        self.lineEdit_albedo = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_albedo.setGeometry(QtCore.QRect(240, 150, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_albedo.setFont(font)
        self.lineEdit_albedo.setObjectName("lineEdit_albedo")
        self.label_losses = QtWidgets.QLabel(self.frame_2)
        self.label_losses.setGeometry(QtCore.QRect(20, 180, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_losses.setFont(font)
        self.label_losses.setObjectName("label_losses")
        self.label_mount = QtWidgets.QLabel(self.frame_2)
        self.label_mount.setGeometry(QtCore.QRect(20, 61, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_mount.setFont(font)
        self.label_mount.setObjectName("label_mount")
        self.label_tilt = QtWidgets.QLabel(self.frame_2)
        self.label_tilt.setGeometry(QtCore.QRect(20, 91, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_tilt.setFont(font)
        self.label_tilt.setObjectName("label_tilt")
        self.label_azimuth = QtWidgets.QLabel(self.frame_2)
        self.label_azimuth.setGeometry(QtCore.QRect(20, 121, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_azimuth.setFont(font)
        self.label_azimuth.setObjectName("label_azimuth")
        self.label_albedo = QtWidgets.QLabel(self.frame_2)
        self.label_albedo.setGeometry(QtCore.QRect(20, 151, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_albedo.setFont(font)
        self.label_albedo.setObjectName("label_albedo")
        self.label_capacity = QtWidgets.QLabel(self.frame_2)
        self.label_capacity.setGeometry(QtCore.QRect(20, 31, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_capacity.setFont(font)
        self.label_capacity.setObjectName("label_capacity")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(240, 181, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_simulate = QtWidgets.QPushButton(Form)
        self.pushButton_simulate.setGeometry(QtCore.QRect(680, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_simulate.setFont(font)
        self.pushButton_simulate.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_simulate.setAutoFillBackground(True)
        self.pushButton_simulate.setObjectName("pushButton_simulate")

        # connection to switch
        self.pushButton_simulate.clicked.connect(self.solve_mc)

        self.label_pvlib = QtWidgets.QLabel(Form)
        self.label_pvlib.setGeometry(QtCore.QRect(200, 20, 483, 25))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_pvlib.setFont(font)
        self.label_pvlib.setObjectName("label_pvlib")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(480, 330, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_upload_2 = QtWidgets.QPushButton(Form)
        self.pushButton_upload_2.setGeometry(QtCore.QRect(510, 460, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_upload_2.setFont(font)
        self.pushButton_upload_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_upload_2.setAutoFillBackground(True)
        self.pushButton_upload_2.setObjectName("pushButton_upload_2")

        # connection to switch
        self.pushButton_upload_2.clicked.connect(self.latitude)
        self.pushButton_upload_2.clicked.connect(self.longitude)
        self.pushButton_upload_2.clicked.connect(self.timezone)
        self.pushButton_upload_2.clicked.connect(self.plant)
        self.pushButton_upload_2.clicked.connect(self.ghi)
        self.pushButton_upload_2.clicked.connect(self.dhi)
        self.pushButton_upload_2.clicked.connect(self.dni)
        self.pushButton_upload_2.clicked.connect(self.temp)
        self.pushButton_upload_2.clicked.connect(self.windspeed)
        self.pushButton_upload_2.clicked.connect(self.date)
        self.pushButton_upload_2.clicked.connect(self.capacity)
        self.pushButton_upload_2.clicked.connect(self.model_parameters)
        self.pushButton_upload_2.clicked.connect(self.tilt)
        self.pushButton_upload_2.clicked.connect(self.azimuth)
        self.pushButton_upload_2.clicked.connect(self.albedo)
        self.pushButton_upload_2.clicked.connect(self.losses)

        self.frame_2.raise_()
        self.frame_5.raise_()
        self.frame.raise_()
        self.line.raise_()
        self.pushButton_simulate.raise_()
        self.label_pvlib.raise_()
        self.plainTextEdit.raise_()
        self.pushButton_upload_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_location.setText(_translate("Form", "Location:"))
        self.lineEdit_latitude.setPlaceholderText(_translate("Form", "Ex: 51.49"))
        self.lineEdit_longitude.setPlaceholderText(_translate("Form", "Ex: 10.81"))
        self.lineEdit_timezone.setPlaceholderText(_translate("Form", "Ex: Europe/Berlin"))
        self.lineEdit_name.setPlaceholderText(_translate("Form", "name of your plant"))
        self.label_plant.setText(_translate("Form", "Plant name:"))
        self.label_timezone.setText(_translate("Form", "Time Zone:"))
        self.label_latitude.setText(_translate("Form", "Latitude:"))
        self.label_longitude.setText(_translate("Form", "Latitude:"))
        self.label_weather.setText(_translate("Form", "Weather Data:"))
        self.pushButton_upload.setText(_translate("Form", "upload"))
        self.lineEdit_ghi.setPlaceholderText(_translate("Form", "Ex: ghi"))
        self.lineEdit_dhi.setPlaceholderText(_translate("Form", "Ex: dhi"))
        self.lineEdit_dni.setPlaceholderText(_translate("Form", "Ex: dni"))
        self.lineEdit_temp.setPlaceholderText(_translate("Form", "Ex: Temperature"))
        self.lineEdit_windspeed.setPlaceholderText(_translate("Form", "Ex: wind speed"))
        self.lineEdit_date.setPlaceholderText(_translate("Form", "Ex: 2023-01-01"))
        self.label_date.setText(_translate("Form", "Start date: "))
        self.label_windspeed.setText(_translate("Form", "Wind speed column:"))
        self.label_ghi.setText(_translate("Form", "GHI column:"))
        self.label_dhi.setText(_translate("Form", "DHI column:"))
        self.label_temp.setText(_translate("Form", "Temperature column:"))
        self.label_dni.setText(_translate("Form", "DNI column:"))
        self.label_weather_file.setText(_translate("Form", "Weather data File:"))
        self.label_system.setText(_translate("Form", "system:"))
        self.lineEdit_capacity.setPlaceholderText(_translate("Form", "in KW"))
        self.comboBox_mounting.setItemText(0, _translate("Form", "open rack glass glass"))
        self.comboBox_mounting.setItemText(1, _translate("Form", "close mount glass glass"))
        self.comboBox_mounting.setItemText(2, _translate("Form", "open rack glass polymer"))
        self.comboBox_mounting.setItemText(3, _translate("Form", "insulated back glass polymer"))
        self.lineEdit_tilt.setPlaceholderText(_translate("Form", "Ex: 30"))
        self.lineEdit_azimuth.setPlaceholderText(_translate("Form", "Ex: 180"))
        self.lineEdit_albedo.setPlaceholderText(_translate("Form", "Ex: 0.25"))
        self.label_losses.setText(_translate("Form", "Losses:"))
        self.label_mount.setText(_translate("Form", "Module\'s mounting parameters:"))
        self.label_tilt.setText(_translate("Form", "Surface Tilt:"))
        self.label_azimuth.setText(_translate("Form", "surface Azimuth:"))
        self.label_albedo.setText(_translate("Form", "Albedo:"))
        self.label_capacity.setText(_translate("Form", "Plant capacity:"))
        self.comboBox.setItemText(0, _translate("Form", "PV watts model"))
        self.comboBox.setItemText(1, _translate("Form", "None"))
        self.pushButton_simulate.setText(_translate("Form", "Simulate"))
        self.label_pvlib.setText(_translate("Form", "                                       P V L i b                                               "))
        self.pushButton_upload_2.setText(_translate("Form", "Upload Inputs"))


    # function for weather data
    def upload_dataframe(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)
        if file_name:
            # Read the CSV file into a DataFrame
            try:
                dataframe = pd.read_csv(file_name)
                self.dataframe = dataframe
                #print("weather data uploaded")
                self.plainTextEdit.appendPlainText("weather data uploaded")
                return dataframe
            except Exception as e:
                #print("error uploading the selected file")
                self.plainTextEdit.appendPlainText("Error uploading the selected file")

    # function for latitude
    def latitude(self):
        input_latitude = self.lineEdit_latitude.text()
        try:
           self.input_latitude = float(input_latitude)
           #print(input_latitude)
           self.plainTextEdit.appendPlainText(f"Latitude :{input_latitude}")
           return input_latitude
        except ValueError:
            #print("invalid value for latitude")
            self.plainTextEdit.appendPlainText("invalid value for latitude")

    # function for longiude
    def longitude(self):
        input_longitude = self.lineEdit_longitude.text()
        try:
           self.input_longitude = float(input_longitude)
           #print(input_longitude)
           self.plainTextEdit.appendPlainText(f"Longitude :{input_longitude}")
           return input_longitude
        except ValueError:
            print("invalid value for longitude")
            self.plainTextEdit.appendPlainText("invalid value for longitude")

    # function for timezone
    def timezone(self):
        input_timezone = self.lineEdit_timezone.text()
        self.input_timezone = input_timezone
        self.plainTextEdit.appendPlainText(f"Timezone :{input_timezone}")
        #print(input_timezone)
        return input_timezone

    # function for plant name
    def plant(self):
        input_plant = self.lineEdit_name.text()
        self.input_plant = input_plant
        #print(input_plant)
        self.plainTextEdit.appendPlainText(f"Plant name :{input_plant}")
        return input_plant

    # function for ghi column
    def ghi(self):
        input_ghi = self.lineEdit_ghi.text()
        self.input_ghi = input_ghi
        #print(input_ghi)
        self.plainTextEdit.appendPlainText(f"ghi column :{input_ghi}")
        return input_ghi

    # function for dhi column
    def dhi(self):
        input_dhi = self.lineEdit_dhi.text()
        self.input_dhi = input_dhi
        #print(input_dhi)
        self.plainTextEdit.appendPlainText(f"dhi column :{input_dhi}")
        return input_dhi

    # function for dni column
    def dni(self):
        input_dni = self.lineEdit_dni.text()
        self.input_dni = input_dni
        #print(input_dni)
        self.plainTextEdit.appendPlainText(f"dni column :{input_dni}")
        return input_dni

    # function for temperature column
    def temp(self):
        input_temp = self.lineEdit_temp.text()
        self.input_temp = input_temp
        self.plainTextEdit.appendPlainText(f"Temp column :{input_temp}")
        #print(input_temp)
        return input_temp

    # function for windspeed column
    def windspeed(self):
        input_windspeed = self.lineEdit_windspeed.text()
        self.input_windspeed = input_windspeed
        #print(input_windspeed)
        self.plainTextEdit.appendPlainText(f"Wind speed column :{input_windspeed}")
        return input_windspeed

    # function for date
    def date(self):
        input_date = self.lineEdit_date.text()
        self.input_date = input_date
        #print(input_date)
        self.plainTextEdit.appendPlainText(f"Start date :{input_date}")
        return input_date

    # function for capacity
    def capacity(self):
        input_capacity = self.lineEdit_capacity.text()
        try:
            self.input_capacity = float(input_capacity)
            #print(input_capacity)
            self.plainTextEdit.appendPlainText(f"Plant capacity :{input_capacity}")
            return input_capacity
        except ValueError:
            #print("invalid value for plant capacity")
            self.plainTextEdit.appendPlainText("invalid value for plant capacity")

    # function for tilt
    def tilt(self):
        input_tilt = self.lineEdit_tilt.text()
        try:
           self.input_tilt = float(input_tilt)
           #print(input_tilt)
           self.plainTextEdit.appendPlainText(f"Tilt :{input_tilt}")
           return input_tilt
        except ValueError:
            #print("invalid value for surface tilt")
            self.plainTextEdit.appendPlainText("invalid value for surface tilt")

    # function for azimuth
    def azimuth(self):
        input_azimuth = self.lineEdit_azimuth.text()
        try:
           self.input_azimuth = float(input_azimuth)
           #print(input_azimuth)
           self.plainTextEdit.appendPlainText(f"Azimuth :{input_azimuth}")
           return input_azimuth
        except ValueError:
            #print("invalid value for surface azimuth")
            self.plainTextEdit.appendPlainText("invalid value for surface azimuth")

    # function for albedo
    def albedo(self):
        input_albedo = self.lineEdit_albedo.text()
        try:
           self.input_albedo = float(input_albedo)
           #print(input_albedo)
           self.plainTextEdit.appendPlainText(f"Albedo :{input_albedo}")
           return input_albedo
        except ValueError:
            print("invalid value for albedo")
            self.plainTextEdit.appendPlainText("invalid value for albedo")

    # function for losses model
    def losses(self):
        input_losses_model = self.comboBox.currentText()

        if input_losses_model == 'PV watts model':
            input_losses_model = 'pvwatts_losses'
        if input_losses_model == 'None':
            input_losses_model = None

        self.input_losses_model = input_losses_model
        self.plainTextEdit.appendPlainText(f"Losses model :{input_losses_model}")
        return input_losses_model

    # function for temp model parameters
    def model_parameters(self):
        input_model_parameters = self.comboBox_mounting.currentText()

        if input_model_parameters == 'open rack glass glass':
            input_model_parameters = 'open_rack_glass_glass'
        if input_model_parameters == 'close mount glass glass':
            input_model_parameters = 'close_mount_glass_glass'
        if input_model_parameters == 'open rack glass polymer':
            input_model_parameters = 'open_rack_glass_polymer'
        if input_model_parameters == 'insulated back glass polymer':
            input_model_parameters = 'insulated_back_glass_polymer'
        self.input_model_parameters = input_model_parameters
        self.plainTextEdit.appendPlainText(f"Model parameters :{input_model_parameters}")
        return input_model_parameters

    def solve_mc(self):

        weather_data = self.dataframe
        latitude = self.input_latitude
        longitude = self.input_longitude
        timezone = self.input_timezone
        plant_name = self.input_plant
        ghi_column = self.input_ghi
        dhi_column = self.input_dhi
        dni_column = self.input_dni
        temp_column = self.input_temp
        windspeed_column = self.input_windspeed
        start_date = self.input_date
        capacity = self.input_capacity
        model_parameters = self.input_model_parameters
        tilt = self.input_tilt
        azimuth = self.input_azimuth
        albedo = self.input_albedo
        losses_model = self.input_losses_model

        location = Location(latitude=latitude,
                            longitude=longitude,
                            tz=timezone,
                            name=plant_name)

        # weather_data = pd.read_csv('weather_data_nordhausen.csv')
        data = weather_data[[ghi_column, dhi_column, dni_column, temp_column, windspeed_column]]

        dti = pd.date_range(start_date, periods=8760, freq='H')
        data.index = dti
        data = data.copy()
        data.rename(columns={ghi_column: 'ghi',
                             dhi_column: 'dhi',
                             dni_column: 'dni',
                             temp_column: 'Temperature',
                             windspeed_column: 'Wind Speed'}, inplace=True)

        CEC_module = pvlib.pvsystem.retrieve_sam('CECMod')
        cec_inverters = pvlib.pvsystem.retrieve_sam('CECInverter')

        module = CEC_module[
            'Canadian_Solar_Inc__CS6X_300M']  # 300W mono-si module   # choose module from pvlib CEC modules
        inverter = cec_inverters['ABB__PVI_6000_OUTD_S_US_A__277V_']  # choose inverter from pvlib CEC inverters

        temperature_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm'][model_parameters]

        surface_tilt = tilt
        surface_azimuth = azimuth

        mount = FixedMount(surface_tilt, surface_azimuth)

        plant_capacity = capacity * 1000  # in watts
        no_of_modules = int(plant_capacity / module.STC)
        #print("Number of modules:", no_of_modules)
        self.plainTextEdit.setPlainText(f"Number of modules :{no_of_modules}")

        array = Array(mount=mount,
                      albedo=albedo,
                      module=module,
                      module_parameters=module,
                      temperature_model_parameters=temperature_parameters,
                      modules_per_string=no_of_modules,
                      strings=1,
                      array_losses_parameters=None)

        system = PVSystem(arrays=[array],
                          surface_tilt=surface_tilt,
                          surface_azimuth=surface_azimuth,
                          module_parameters=module,
                          inverter_parameters=inverter,
                          temperature_model_parameters=temperature_parameters,
                          losses_parameters=losses_model)

        mc = ModelChain(system, location, aoi_model="no_loss", spectral_model="no_loss")
        mc.run_model(data)

        # results block
        DC_annual = mc.results.dc.p_mp  # p_mp is scaled by voltage*current
        DC_annual_energy = pd.DataFrame(DC_annual)
        DC_annual_energy_KW = DC_annual_energy / 1000
        DC_annual_energy_KW.columns = ['DC_Power']

        Ac_annual = mc.results.ac
        Ac_annual_energy = pd.DataFrame(Ac_annual)
        AC_annual_energy_KW = Ac_annual_energy / 1000
        AC_annual_energy_KW.columns = ['AC_power']


        DC_annual_value = DC_annual_energy_KW.sum()
        #print(DC_annual_value)
        self.plainTextEdit.appendPlainText(f"DC annual : {DC_annual_value}")
        AC_annual_value =  AC_annual_energy_KW.sum()
        #print(AC_annual_value)
        self.plainTextEdit.appendPlainText(f"AC annual : {AC_annual_value}")

        scaled_data1 = DC_annual_energy_KW / DC_annual_energy_KW.max()
        scaled_data = AC_annual_energy_KW / AC_annual_energy_KW.max()

        self.plainTextEdit.appendPlainText(f"DC annual peak : {DC_annual_energy_KW.max()}")
        self.plainTextEdit.appendPlainText(f"AC annual peak: {AC_annual_energy_KW.max()}")

        df1 = scaled_data1
        df1.index = dti
        df2 = scaled_data

        df = pd.concat([df1, df2], axis=1)
        df.to_csv("normalised_output.csv")
        #print("DC and AC output is saved to the current directory")


        # plotting
        plt.plot(scaled_data, label='AC Power')
        #plt.plot(scaled_data1, label='DC Power')
        plt.ylabel("Normalised Production")
        plt.legend()
        plt.show()

        self.plainTextEdit.appendPlainText("DC and AC output is saved to the current directory")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
