# Blocks
a = ("Y","S","I","E","T","C")
b = ("B","E","X","A","S","!")
c = ("B","V","T","F","O","E")
d = ("A","E","G","P","O","J")
e = ("T","O","D","Y","E","R")
f = ("'","<3","L","P","S","E")
g = ("D","H","M","W","E","A")
h = ("Z","I","W","C","T","?")
i = ("R","D","F","K","S","G")
j = ("J","O","U","H","I","S")
k = ("L","E","N","R","C","K")
l = ("S","M","R","N","L","Y")
m = ("Z","O","T","L","A","N")
n = ("F","A","H","E","I","N")
o = ("M","V","H","U","N","O")
p = ("S","A","C","G","T","Q")

# Count of letter frequency within blcoks
block_set = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
all_faces = [face for block in block_set for face in block]
freq = {letter:all_faces.count(letter) for letter in set(all_faces)}

def ordered_term(search_term):
    return sorted(search_term, key=lambda letter: freq[letter])

if __name__ == '__main__':
    print(ordered_term(['T','T','Y','<3','A']))
