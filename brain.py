
file_name = "input.txt" #change this to whatever file name
out_name = "output.txt" #change this to output file name
total_numbers = 9 #total numbers in a single line of text



class Scanner:
	def __init__(self, numbers):
		self.__buffer = []
		self.__square = 0
		self.__max_square = numbers * 3 - 1
		self.__bin = ""
		self.__output = ""

	def fetch(self, stripe):
		i = self.__square
		for x in range(0, 3):
			for y in range(i, i+3):
				if(stripe[x][y] != " "):
					self.__buffer.append("1")
				else:
					self.__buffer.append("0")
		self.__bin = "".join(self.__buffer)
		#print(self.__bin)

	def clear_buffer(self):
		self.__buffer = None
		self.__buffer = []
		self.__bin = None
		self.__bin = ""

	def match_digit(self):
		dig_dict = {
			"010101111": 0,
			"000001001": 1,
			"010011110": 2,
			"010011011": 3,
			"000111001": 4,
			"010110011": 5,
			"010110111": 6,
			"010001001": 7,
			"010111111": 8,
			"010111011": 9
		}
		output = str(dig_dict[self.__bin])
		return output

	def recognise(self, stripe, out_file):
		max = self.__max_square
		self.__square = 0
		self.__output = ""
		for i in range(0, max+1, 3):
			self.__square = i
			self.fetch(stripe)
			output = self.match_digit()
			self.__output += output
			self.clear_buffer()
		out_file.write(self.__output + "\n")


#a stripe is a 3 parallel line read. Like a 3-line book for cursive writing.

def stripe_read(in_file):
	content = []
	for i in range(1, 4):
		content.append(in_file.readline())
	return content


in_file = open(file_name, "r")
out_file = open(out_name, "w")
s = Scanner(total_numbers)

num_lines = 0

for line in in_file:
	num_lines += 1

num_lines //= 4

in_file.seek(0, 0)

print("\nProcessing digits..")

for i in range(0, num_lines):
	stripe = stripe_read(in_file)
	in_file.readline()
	print(".", end="")
	s.recognise(stripe, out_file)

out_file.close()
in_file.close()