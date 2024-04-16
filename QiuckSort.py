
QList=[1,23,3,21,32,436,56,4,5,4,2,4,5,6,7,9,54,3]


def Quick(Input):
    if len(Input) <= 1:
        return Input
    else:
        pivot=Input[0]
    Left=[]
    middel=[]
    Right=[]
    for s in Input:
        if s < pivot:
            Left.append(s)
        elif s == pivot:
            middel.append(s)
        else:
            Right.append(s)
    return Quick(Left) + middel + Quick(Right)
   

i=Quick([34,3,2,3,4,1,3,4,56,7,6,5,4,1,4,5,2,3,2,32,23])
print(i)

