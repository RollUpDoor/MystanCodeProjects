"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the key in numbers
	:return: int, the biggest digit
	"""
	if n < 0: # 用來轉換負數
		n = n*-1

	ans = largest_helper(n, 0) # ans 去接收 largest_helper回傳的值 largest
	return ans # 把 find_largest_digit回傳 (最大值)


def largest_helper(n, largest): # n是key in的數字，largest 一開始是 0
	# base case
	if n == 0: # 如果 n 等於 0 之後，結束
		return largest # 回傳最大值
	else:
		return largest_helper(n//10, max(n%10, largest))  # 一開始largest是0，挑取最大的數字回傳給 helper(largest紀錄)




if __name__ == '__main__':
	main()
