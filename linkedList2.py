"""
주문 관리 시스템
주문생성: 고객이 쇼핑몰에서 주문을 하게 되면 이 주문은 고유의 주문번호를 갖게 되고, 이 주문번호가 주문 관리 시스템에 등록
주문취소: 주문이 취소될 경우에는 그 주문은 주문 관리 시스템으로부터 삭제
주문조회: 주문이 몇 번째로 처리가 될지를 알려줌
"""

class LinkedListElement :
	def __init__(self, data, myPrev, myNext) :
			self.data = data
			self.myPrev = myPrev
			self.myNext = myNext

class orderManager :
	def __init__(self) :
			self.start = None
			self.end = None
			self.elems = {}

	def addOrder(self, orderId) :
			elem = LinkedListElement(orderId, None, None)
			
			self.elems[orderId] = elem
			
			if self.start == None and self.end == None:
					self.start = elem
					self.end = elem
			else:
					self.end.myNext = elem
					elem.myPrev = self.end
					self.end = elem

	def removeOrder(self, orderId) :
			if self.start == None and self.end == None:
					return
			
			cur = self.elems[orderId]
			if self.start == cur and self.end == cur:
					self.start = None
					self.end = None
			elif self.start == cur:
					self.start = cur.myNext
					cur.myNext.myPrev = None
			elif self.end == cur:
					self.end = cur.myPrev
					cur.myPrev.myNext = None
			else:
					cur.myPrev.myNext = cur.myNext
					cur.myNext.myPrev = cur.myPrev

	def getOrder(self, orderId) :
			cnt = 1
			cur = self.start
			
			while cur != None:
					if cur.data == orderId:
							return cnt
					cur = cur.myNext
					cnt += 1
			return -1
