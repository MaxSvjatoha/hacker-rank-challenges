# Enter your code here. Read input from STDIN. Print output to STDOUT

phoneBook = {}
n = int(input())
for i in range(n):
    entry = input()
    entry = entry.split()
    #print(entry)
    phoneBook[entry[0]] = entry[1]

#print(phoneBook)

for i in range(n):
    try:
        search = input()
        #print(search)
        if search in phoneBook:
            out = search + "=" + str(phoneBook[search])
            print(out)
        else:
            print("Not found")
    except:
        break
