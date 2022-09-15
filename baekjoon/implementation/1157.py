alphabetL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetU = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
count = [0] * 26

alphabet = input()

for i in range(26):
    for a in alphabet :
        if a == alphabetL[i] or a == alphabetU[i] :
            count[i] += 1


maxvalue = max(count)
index = list(filter(lambda i: count[i] == maxvalue, range(26)))

if len(index) == 1 :
    print(alphabetU[index[0]])
else:
    print('?')
