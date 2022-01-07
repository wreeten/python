class Solutions(object):
	def commonChar(self, A):
		result = listA.Counter(A[0])
		for i in A:
			result &= listA.Counter(a)
		return listA(result.elements())
