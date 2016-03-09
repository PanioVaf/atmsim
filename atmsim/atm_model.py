class Model(object):
	"""This class represents the ATM's current balance.

    Attributes:
  
    """
	def __init__(self):
		self.twenty_notes = 0
		self.fifty_notes = 0

	def set_balance(self, balance_twenty=0, balance_fifty=0):
		self.twenty_notes = balance_twenty
		self.fifty_notes = balance_fifty
        
	def withdaw(self, amount):
		""" 
		20x + 50y = amount
		x \in [0,amount/20]
		"""
		for y in range(1 + amount / 50):
			x = (amount - y * 50) / 20
			if 20 * x + 50 * y == 180:
				self.twenty_notes -= x
				self.fifty_notes -= y
				return (x,y)
		return (0,0)

	def show(self):
		print self.twenty_notes
		print self.fifty_notes