import sqlite3
import hashlib


class BaseDb:
	"""数据库基础类"""

	def __init__(self, dbpath="", *args, **kwargs):
		self.con = sqlite3.connect(dbpath)

	def __del__(self):
		self.con.close()


class CheckLogin(BaseDb):
	def __init__(self, account, password):
		super().__init__("resource/db/scmis.gzh")
		try:
			md = hashlib.md5()
			md.update(password.encode())
			pa = md.hexdigest().upper()
			self.sql = """select * from users where account='{}' and password='{}'""".format(account, pa)
		except Exception as ret:
			print(ret)
			self.con.close()

	def isHave(self):
		"""登录检查"""
		try:
			res = self.con.execute(self.sql).fetchall()
			print(res, "登录")
			if res:
				return True
		except Exception as ret:
			print(ret, "登录检查出错！")
		return False


class SaveContract(BaseDb):
	def __init__(self, data, *args, **kwargs):
		super().__init__("resource/db/scmis.gzh")
		self.sql = """insert into contracts (cid, materials, cost, paymethod, ccompany, cman, phone, caddres, 
		signdate, givedate, myname, myphone, myddress, paydate) values ('{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', 
		'{}', '{}', '{}', '{}', '{}', '{}')""".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6],
		                                              data[7], data[8], data[9], data[10], data[11], data[12], data[13])

	def saveContract(self):
		try:
			self.con.execute(self.sql)
			self.con.commit()
			return True
		except Exception as ret:
			print(ret)
			return False


def getToday(d):
	sql = """select * from contracts where signdate='{}'""".format(d)
	con = sqlite3.connect('resource/db/scmis.gzh')
	try:
		res = con.execute(sql).fetchall()
		con.close()
		return "{:02}".format(len(res)+1)
	except Exception as ret:
		print(ret)
		con.close()
		return "01"


class CreditAbout(BaseDb):
	def __init__(self, *args, **kwargs):
		super().__init__("resource/db/scmis.gzh")
		self.sql = "select * from contracts"

	def getAllContract(self):
		try:
			res = self.con.execute(self.sql).fetchall()
			if res:
				need = list()
				for c in res:
					need.append((c[0], c[4], c[2], c[8], c[9], c[13]))
				return need
		except Exception as ret:
			print(ret, "登录检查出错！")
		return []

	def getFilter(self, key=0):
		"""key=0未支付"""
		try:
			res = self.con.execute(self.sql).fetchall()
			if res:
				need = list()
				for c in res:
					if c[-1] == key:
						need.append((c[0], c[4], c[2], c[8], c[9], c[13], c[4], c[10], c[1]))
				return need
		except Exception as ret:
			print(ret, "登录检查出错！")
		return []

	def setPayed(self, c):
		self.sql = """update contracts set state=1  where cid='{}'""".format(c)
		try:
			self.con.execute(self.sql)
			self.con.commit()
			return True
		except Exception as ret:
			print(ret)
			return False

	def delcontract(self, c):
		sql = """delete from contracts where cid='{}'""".format(c)
		try:
			self.con.execute(sql)
			self.con.commit()
			return True
		except Exception as ret:
			print(ret)
			return False

	def getList(self, ty, d):
		sql = """select * from contracts where {} like '%{}%'""".format(ty, d)
		try:
			res = self.con.execute(sql).fetchall()
			if res:
				need = list()
				for c in res:
					need.append((c[0], c[4], c[2], c[8], c[9], c[13]))
				return need
		except Exception as ret:
			print(ret, "登录检查出错！")
		return []


class UserManage(BaseDb):
	def __init__(self, *args, **kwargs):
		super().__init__("resource/db/scmis.gzh")

	def getUsers(self):
		sql = "select * from users"
		try:
			res = self.con.execute(sql).fetchall()
			if res:
				need = list()
				for c in res:
					need.append((c[0], c[1], c[3]))
				return need
		except Exception as ret:
			print(ret, "登录检查出错！")
		return []

	def addUser(self, acc, paw):
		md = hashlib.md5()
		md.update(paw.encode())
		pa = md.hexdigest().upper()
		sql = """insert into users (account, password) values ('{}', '{}')""".format(acc, pa)
		try:
			self.con.execute(sql)
			self.con.commit()
			return True
		except Exception as ret:
			print(ret)
			return False

	def delUser(self, acc):
		sql = """delete from users where uid='{}'""".format(acc)
		try:
			self.con.execute(sql)
			self.con.commit()
			return True
		except Exception as ret:
			print(ret)
			return False


class ZhuanzhangNote(BaseDb):
	def __init__(self, *args, **kwargs):
		super().__init__("resource/db/scmis.gzh")

	def addNote(self, data):
		sql = """insert into zhuanzhangnote (zid, kkaihu, kcardid, mykaihu, mycardid, mtype, cost, zdate) values ('{}', '{}', '{}', '{}', '{}', '{}', {}, '{}')""".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
		try:
			self.con.execute(sql)
			self.con.commit()
			return True
		except Exception as ret:
			print(ret)
			return False


class PiaoJu(BaseDb):
	def __init__(self, *args, **kwargs):
		super().__init__("resource/db/scmis.gzh")

	def addPiaoju(self, data):
		sql = """insert into piaoju (pid, pdate, kname, myname, materials) values ('{}', '{}', '{}', '{}', '{}')""".format(data[0], data[1], data[2], data[3], data[4])
		try:
			self.con.execute(sql)
			self.con.commit()
			return True
		except Exception as ret:
			print(ret)
			return False


class ClientManager(BaseDb):
	def __init__(self, *args, **kwargs):
		super().__init__("resource/db/scmis.gzh")

	def getClients(self):
		need = list()
		sql1 = "select * from contracts"
		try:
			res = self.con.execute(sql1).fetchall()
			if res:
				for c in res:
					need.append([c[4], c[5], c[6], c[7]])
				if not need:
					return []
		except Exception as ret:
			print(ret, "登录检查出错！")
			return []
		sql2 = "select * from zhuanzhangnote"
		try:
			res = self.con.execute(sql2).fetchall()
			if res:
				for c in res:
					need[res.index(c)].append(c[1])
					need[res.index(c)].append(c[2])
				if not need:
					return []
		except Exception as ret:
			print(ret, "登录检查出错！")
			return []
		return need
