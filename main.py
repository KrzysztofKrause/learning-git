print ("lista_zakupow")
class Solution:
	def arrangeCoins(self, n: int) -> int:

		result = 0

		stairs_number = 1

		while n > 0:
			n = n - stairs_number
			stairs_number = stairs_number + 1
			if n >= 0:
				result = result + 1

		return result
	