'''Lab 1: Introduction to Python'''
'''Name: Bradley Sumoge'''

'''Problem 1'''
if __name__ == "__main__":
    print("Hello, world!")
   
'''Problem 2'''
def sphere_volume(r):
    return (4/3)*3.14159*r**3

'''Problem 3'''
def isolate(a,b,c,d,e):
    print(a,b,c,sep= '     ',end= ' ')
    print(d,e)
    return

'''Problem 4'''
def first_half(string):
    x = (len(string)//2)
    print(string[0:x])
    return

def reverse(string2):
    print(string2[::-1])
    return

'''Problem 5'''
def list_ops():
    my_list = ['bear','ant','cat','dog']
    my_list.append('eagle')
    my_list[2] = 'fox'
    my_list.remove(my_list[1])
    my_list = sorted(my_list,reverse=True)
    f = my_list.index('eagle')
    my_list[f] = 'hawk'
    my_list.append('hunter')
    return my_list

'''Problem 6'''
def pig_latin(string3):
    if 'a' in string3[0]:
        string3 = string3 + 'hay'
        return string3
    elif 'e' in string3[0]:
        string3 = string3 + 'hay'
        return string3
    elif 'i' in string3[0]:
        string3 = string3 + 'hay'
        return string3
    elif 'o' in string3[0]:
        string3 = string3 + 'hay'
        return string3
    elif 'u' in string3[0]:
        string3 = string3 + 'hay'
        return string3    
    else:
        string4 = string3[1:]
        string3 = string4 + string3[0] + 'ay'
        return string3