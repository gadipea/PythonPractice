

def permutations(lst):
    print("Starting List",lst)
    if len(lst) == 0:
        print("Ending with Empty List",lst)
        return []
    if len(lst) == 1:
        print("Last one List",lst)
        return [lst]
    l=[]
    for i in range(len(lst)):
        print("Progressing List with Index :",i)
        m=lst[i]
        print("First Elemet considered",m)
        remLst = lst[:i] + lst[i+1:]
        print("RemaingListElemets",lst[:i],lst[i+1:])
        print("RemaingList",remLst)
        perm=permutations(remLst)
        print("Permutations of remaing list",perm)
        for p in perm:
            print("Elemets adding are",m,p)
            l.append([m]+p)
            print("List Made is",l)
    return l



if __name__=="__main__":
    array=list(map(int,input().split()))
    print(permutations(array))











# # returning list with lists of  first element and others

# lis=[1,2,3]

# out=[]

# for i in list:
#     out.append(0,others)





























