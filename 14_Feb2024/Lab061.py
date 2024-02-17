def makepizza(*top,base="Wheat"): 
    for t in top:
        print(t)
    return top,base

swathi_t,swathi_base = makepizza("onion","tomato","sweetcorn", base="thin crust")
#pramod = makepizza("onion","tomato","sweetcorn")

print(swathi_t)
print(swathi_base)