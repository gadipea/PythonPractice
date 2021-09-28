

def checkVowels(string):
    return True if any([True if isVowel(x) else False for x in string]) else False

def isVowel(ch):
    return True if any([ch=='a',ch=='e',ch=='i',ch=='o',ch=='u']) else False

def count(temp):
    count=0
    for ch in temp:
        if isVowel(ch):
            count+=1
    return count

def vowelStrings(string,number):
    stringArray=[string[i:j] for i in range(len(string)-1) for j in range(i,len(string)+1) if len(string[i:j])==number ]
    vString=[x for x in stringArray  if checkVowels(x)]
    if not vString:
        return "Not Found"
    print(vString)
    dictStrings={x:count(x) for x in vString }
    print(dictStrings)
    out=[x for x in dictStrings if dictStrings[x]==max(dictStrings.values()) ]
    return out[0] if len(out)>1 else string.index(out[0])



if __name__=="__main__":
    array=input("Enetr a word:")
    number=int(input("Enter a number"))
    print(vowelStrings(array,number))

