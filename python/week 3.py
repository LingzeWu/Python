#baseexpbaseexpbaseexp===(base2)exp2base⋅baseexp−11ifexp>0andexpisevenifexp>0andexpisoddifexp=0
def recurPower(base,exp):
    if exp % 2 == 1 :
        if exp == 0 :
            return 1
        else:
            return base*recurPower(base,exp-1)
    elif exp % 2 == 0 :
        if exp ==0 :
            return 1
        else:
            return recurPower(base**2,exp/2)
