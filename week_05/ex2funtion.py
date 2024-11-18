def irainee(INPUT,sumplus,summinus):
    if INPUT > 0 :
        sumplus += INPUT
        return sumplus
    elif INPUT < 0:
        summinus += INPUT
        return summinus
    return 0
   