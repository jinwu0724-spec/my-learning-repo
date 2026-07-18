file = open('test.txt', 'r')
try:
	content = file.read()
	print(content)
finally:
	file.close()


with open('test.txt', 'r') as file:
	content = file.read()
	print(content)

with open('test.txt', 'r') as infile, open('test1.txt', 'r+') as outfile:
	incontent = infile.read()
	outcontent = outfile.read()

	print("incontent:", incontent)
	print("outcontent:", outcontent)

	outfile.write(incontent.upper())
	outfile.seek(0)

	outcontent = outfile.read()
	print("outcontent_add:", outcontent)


class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"time: {self.end - self.start:.2f}s")
        return False

# forexample
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))
