from PyQt5.Qt import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGridLayout

from modules.ClientManage import ClientManage
from modules.SystemManage import SystemManage
from resource.functionpane import Ui_MainWindow

from modules.AddContract import AddContract
from modules.DelContract import DelContract
from modules.PayManagePane import PayManagePane
from modules.KaiPiao import KaiPiao
from modules.FindPane import FindPane


class FP(QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.addWelcome()
		self.addcontract()
		self.adddelcontract()
		self.addpaymanagepane()
		self.addkaipiao()
		self.addClientManage()
		self.addsystemmanage()
		self.addsearch()

	def addWelcome(self):
		pix = QPixmap("resource/static/bg.jpg")
		self.label.setScaledContents(True)  # 图片自适应
		self.label.setPixmap(pix)

	def addcontract(self):
		self.gl2 = QGridLayout(self.widget_2)
		self.addcontractpane = AddContract(self.widget_2)
		self.gl2.addWidget(self.addcontractpane)

	def adddelcontract(self):
		self.gl8 = QGridLayout(self.widget_8)
		self.delcontractpane = DelContract(self.widget_8)
		self.gl8.addWidget(self.delcontractpane)

	def addpaymanagepane(self):
		self.gl3 = QGridLayout(self.widget_3)
		self.addpay = PayManagePane(self.widget_3)
		self.gl3.addWidget(self.addpay)

	def addkaipiao(self):
		self.gl5 = QGridLayout(self.widget_5)
		self.kaipiao = KaiPiao(self.widget_5)
		self.gl5.addWidget(self.kaipiao)

	def addsystemmanage(self):
		self.cmg6 = QGridLayout(self.widget_6)
		self.systemmanage = SystemManage(self.widget_6)
		self.cmg6.addWidget(self.systemmanage)

	def addsearch(self):
		self.gl7 = QGridLayout(self.widget_7)
		self.findpane = FindPane(self.widget_7)
		self.gl7.addWidget(self.findpane)

	def addClientManage(self):
		self.cmg4 = QGridLayout(self.widget_4)
		self.clientmanage = ClientManage(self.widget_4)
		self.cmg4.addWidget(self.clientmanage)

