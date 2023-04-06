def is_magic(nr):
	if (nr % 3 == 0) & (nr % 2 != 0) :
		print("True")
	else:
		print("False")

print("part 1 ex 1")
print("Test1")
is_magic(9)
print("Test2")
is_magic(6)
print("Test3")
is_magic(7)

def is_magic_list(nr):
	for x in nr:
		if (x % 3 == 0) & (x % 2 != 0) :
			print("True")
		else:
			print("False")

print("part 1 ex 2")
print("Test1")
is_magic_list([ 3, 9, 15])
print("Test2")
is_magic_list([ 3, 9, 12, 19])

def get_magic_numbers_to_limit(N):
	nr = range(3,int(N),3)
	result=[]
	for x in nr:
		if (x % 3 == 0) & (x % 2 != 0) :
			result.append(x)
	print(result)
	
print("part 1 ex 3")
print("Test1")
get_magic_numbers_to_limit(20)

input()