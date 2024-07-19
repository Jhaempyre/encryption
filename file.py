with open('example.txt','w' ) as f:
    f.write("tu karegaa encryption")

with open( 'example.txt', 'r') as f :
    context = f.read()
    print(context)

print("ram")    