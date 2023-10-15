version = list(map(int,input().split(".")))
#version =[int(digit) for digit in input().split(".")]

version[-1] +=1

for index in range(len(version)-1, -1,-1):
    if version[index] > 9:
        version[index] = 0
        if index -1 >=0:
            version[index-1] += 1
# принтирае с .join , но преди това трябва числата да станат стрингове.
print(".".join(str(number) for number in version))


#input    output       вверсията трябда се увеличи с едно
# 1.2.3	 1.2.4
# 1.3.9	 1.4.0
# 3.9.9	 4.0.0
