s = "asdfghjklzxcvbnmqwertyuiopq"
current_recurring = ""
looper = 0
for char in s:
	for i in range(len(s)-1-looper):
		i += looper
		if str(s[i+1]) == str(char):
			current_recurring += char
		if i == len(s)-2:
			looper += 1
print("\n")
if current_recurring:
	print(f"current reccuring is {current_recurring[0]}")
else:
	print("None")