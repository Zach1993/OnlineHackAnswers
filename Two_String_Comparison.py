num_str = input()
num = int(num_str) # convert string to int

def compare_str(num):
        while num >= 0:
            a = input()
            b = input()
            j = 0 # incrementing variable for while loop
            length_a = len(a) # stop point for slicing a string
            while j < length_a:
                if a[j] in b:
                    print("YES")
                    return compare_str(num-1) #stop at the first finding of a matching character
                else:
                    j+=1 # if character is not contained in other string, iterate to next character
            else:
                print("NO")
                return compare_str(num-1)

compare_str(num)