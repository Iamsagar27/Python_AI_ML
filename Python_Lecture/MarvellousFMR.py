def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True) :
            Result.append(no)
    
    return Result

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task, Element):
    Sum = 0

    for no in Element:
        Sum = Task(Sum, no)

    return Sum