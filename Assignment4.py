
# coding: utf-8

# In[16]:


class Triangle(object):
    def sides(self,a,b,c):
        a=float(a)
        b=float(b)
        c=float(c)

class area(Triangle):
    def area(self,perimeter,s):
        Perimeter = a + b + c
        s = (a + b + c) / 2
        Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

a = float(input('Please Enter the First side of a Triangle: '))
b = float(input('Please Enter the Second side of a Triangle: '))
c = float(input('Please Enter the Third side of a Triangle: '))
 

print("\n The Perimeter of Traiangle = %.2f" %Perimeter);
print(" The Semi Perimeter of Traiangle = %.2f" %s);
print(" The Area of a Triangle is %0.2f" %Area)


# In[67]:


def filter_long_words(wordlist, length):
    return (word for word in wordlist if len(word) >= length)

def main():
    words = input("Enter words, separated by spaces: ").split()
    length = int(input("Minimum length of words to keep: "))
    print("Words longer than {} are {}.".format(length,', '.join(filter_long_words(words, length))))

main()


# In[45]:


def map_list_to_len(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


if __name__ == "__main__":
    words = ['test', 'abc', 'biggest one']
print (map_list_to_len(words))


# In[66]:


def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True


if __name__ == "__main__":
    print (is_vowel('a'))
    print (is_vowel('z'))

