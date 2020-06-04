class Solution:
	def counting(self,arr):
		dict={}
		for i in arr:
			dict[i]=1
		result=0
		for x in arr:
			if x+1 in dict:
				result+=1
		return result
