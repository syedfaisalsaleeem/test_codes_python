s1 = "hellon"
s2 = "nollhe"
x = len(s2)-1
count = 0
for i in s1:
	if(i==s2[x]):
		count +=1

	x -=1

print(count)
