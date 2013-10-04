def move_n_chickens(n, t1, t2, temp): 
	if n == 1: 
		t2.append(t1.pop())
		return t2
	move_n_chickens(n - 1, t1, temp, t2)
	t2.append(t1.pop())
	move_n_chickens(n - 1, temp, t2, t1)




start = [5,4,3,2,1]
end = []
buff = []
move_n_chickens(5, start, end, buff)
print start
print end 
print buff