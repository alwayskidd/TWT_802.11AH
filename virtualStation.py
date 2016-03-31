class virtualSation():
	def __init__(self,duty_cycle,ID):
		self.duty_cycle=duty_cycle
		self.offset=-1
		self.ID=ID
	def set_offset(self,offset):
		if offset>=0 and offset<self.duty_cycle:
			self.offset=offset
			return True
		else:
			return False
