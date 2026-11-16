def zork(zork):
    glorp = ["a", "q", "a", "q"]
    for g in glorp:
        if g in zork:
            if zork[g] > 2:
                del zork[g]
            else:
                zork[g] = zork[g] + 3
        else:
            zork[g] = len(zork)
        print(len(zork))

wiz = {"q": 5}
zork(wiz)
for k in wiz:
    print(k, wiz[k])