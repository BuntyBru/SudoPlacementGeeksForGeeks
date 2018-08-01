#code

n = int(input())
for i in range(n):
    string = input()
    string2 = set(string)
    if len(string) != len(string2):
        print(0)
    else:
        print(1)