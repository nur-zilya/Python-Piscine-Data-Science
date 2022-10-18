class Research:
	def file_reader(self):
		file = open("../ex02/data.csv", "r")
		tmp = file.read()
		return tmp

if __name__ == "__main__":
	res = Research()
	print(res.file_reader())
