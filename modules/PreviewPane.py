from PyQt5 import QtCore
from PyQt5.Qt import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QGridLayout, QFileDialog, QErrorMessage

from resource.previewpane import Ui_Form


class PreviewPane(QWidget, Ui_Form):
	def __init__(self, file, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.preview()
		url = QtCore.QUrl(QtCore.QFileInfo(file).absoluteFilePath())
		self.web.load(url)

	def print(self):
		path = QFileDialog.getSaveFileName(parent=self, caption="选择导出位置", filter='*.pdf')[0]
		if path:
			try:
				self.web.page().printToPdf(path)
				mes = QErrorMessage(self)
				mes.setWindowTitle("提示")
				mes.showMessage("导出成功！")
				mes.show()
				return
			except Exception as ret:
				print(ret)
		mes = QErrorMessage(self)
		mes.setWindowTitle("提示")
		mes.showMessage("导出失败！")
		mes.show()

	def preview(self):
		self.gl = QGridLayout(self.widget)
		self.web = QWebEngineView(self.widget)
		self.gl.addWidget(self.web)
