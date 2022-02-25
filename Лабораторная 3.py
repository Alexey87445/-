a = 9
m = 4096
 
main_str = input()
 
Y = [0] * 8
Y[0] = 3019
for i in range(1,8):
    Y[i] = (a * Y[i-1]) % m
 
gamma = ""
for i in range(len(Y)):
    gamma += chr(Y[i]%26+97)
print(gamma)
 
result = ""
cnt = 0
for i in range(len(main_str)):
    result += chr((ord(main_str[i]) ^ ord(gamma[cnt]))+97)
    if cnt == 7:
        cnt = 0
print(result)
