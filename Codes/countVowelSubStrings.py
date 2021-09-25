
def countString(a):
    arr=[a[i:j] for i in range(len(a)-1) for j in range(i,len(a)+1) if len(a[i:j])>0]
    array=[ x for x in arr 
            if all(
                [
                    'a' in x,
                    'e' in x,
                    'i' in x,
                    'o' in x,
                    'u' in x,  
                    all(
                        [
                            True if i in 'aeiou' else False for i in x
                        ]
                    )
                ]         
            )
        ]

    print(array)
    print(len(array))

if __name__=="__main__":
    a="aeouisddaaeeiouua"
    countString(a)