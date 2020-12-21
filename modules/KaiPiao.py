from PyQt5.Qt import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QErrorMessage

from modules.DBTool import CreditAbout, PiaoJu
from resource.kaipiao import Ui_Form
from modules.KaipiaoDialog import KaipaioDialog
from modules.PreviewPane import PreviewPane


class KaiPiao(QWidget, Ui_Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.model = QStandardItemModel()
		self.title = ['合同id', '合同公司', '合同金额', '签定日期', '交货日期', '付款日期']
		self.data = list()
		self.showAll()

	def showTable(self):
		# 设置表格表头
		self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.model.clear()
		self.model.setHorizontalHeaderLabels(self.title)
		self.tableView.setModel(self.model)
		if self.data:
			for b in self.data:
				for col in range(6):
					item = QStandardItem("{}".format(b[col]))
					self.model.setItem(self.data.index(b), col, item)
			self.tableView.setModel(self.model)

	def showAll(self):
		"""显示所有合同"""
		self.model.clear()
		c = CreditAbout()
		self.data = c.getFilter(key=1)
		if self.data:
			self.showTable()

	def onPay(self):
		print("开票")
		try:
			index = self.tableView.currentIndex().row()
			self.cid = self.data[index][0]
			zid = self.cid.replace('H', 'P')
			self.kaipiaodialog = KaipaioDialog([zid, self.data[index][6], self.data[index][7], self.data[index][8]])
			self.kaipiaodialog.show()
			self.kaipiaodialog.finish_signal.connect(self.pay)
		except Exception as ret:
			print(ret)
			mes = QErrorMessage(self)
			mes.setWindowTitle("提示")
			mes.showMessage("支付失败")
			mes.show()

	def pay(self, data):
		c = PiaoJu()
		c.addPiaoju(data)
		self.showAll()
		f = open("resource/static/piaojumodel.html", 'r', encoding="utf-8")
		m = f.read()
		f.close()
		mat = data[-1].split('x')[0]
		num = data[-1].split('x')[1]
		data[-1] = mat
		data.append(num)
		temp = ""
		n = 0
		for i in m:
			if i == "{":
				temp += "{}".format(data[n])
				n += 1
			else:
				temp += i
		with open('resource/static/piaojures.html', 'w', encoding='utf-8') as f:
			f.write(temp)
			print("制作完成")
		self.preview = PreviewPane("resource/static/piaojures.html")
		self.preview.show()
