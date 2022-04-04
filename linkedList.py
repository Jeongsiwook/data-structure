"""
구슬 넣기
입력의 첫 번째 줄에는 구슬의 개수 n이 주어짐
두 번째 줄부터는 토끼가 구슬을 넣는 행위가 주어짐
각 줄은 두 개의 정수 a, b로 이루어지며, 이 뜻은 구슬 a를 왼쪽 혹은 오른쪽으로 넣는다는 의미
b가 0이면 왼쪽, b가 1이면 오른쪽
"""

class LinkedListElement:
  def __init__(self, val, ptr):
    self.value = val
    self.myNext = ptr
    
class LinkedListPipe:
	def __init__(self):
		self.start = None
		self.end = None
    
	def addLeft(self, n):
		if self.start == None and self.end == None:
			elem = LinkedListElement(n, self.start)
			self.end = elem
		else:
			elem = LinkedListElement(n, self.start)
			self.start = elem

	def addRight(self, n):
		if self.start == None and self.end == None:
			elem = LinkedListElement(n, None)
			self.start = elem
			self.end = elem
		else:
			elem = LinkedListElement(n, None)
			self.end.myNext = elem
			self.end = elem

	def getBeads(self):
		result = []
		current = self.start
		while current != None:
			result.append(current.value)
			current = current.myNext
		return result

def processBeads(myInput):
	myPipe = LinkedListPipe()

	for bead, direction in myInput:
		if direction == 0:
			myPipe.addLeft(bead)
		else:
			myPipe.addRight(bead)
	result = myPipe.getBeads()

	return result
