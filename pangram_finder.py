
data_in = input()
L = set(data_in.lower())

k = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
if k <= L:
    print("pangram")
else:
    print("not pangram")