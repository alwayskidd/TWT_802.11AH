import virtualStation
class virtualStationTable():
	"""docstring for virtualStationTable"""
	def __init__(self,duty_table):
		self.table=[]
		self.size=0
		for each in duty_table:
			for i in range(0,each.amount):
				self.size+=1
        		table.append(virtualStation.virtualSation(each.duty_cycle,self.size))

	
	def find_best_solution(self,virtual_ID):
		