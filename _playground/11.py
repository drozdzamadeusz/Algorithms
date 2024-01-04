s = [[0,0], [0, 1]]



v = set([0, 0])



# for vc, vr in v:
#     print(vc, vr)

for cc, cr in s:
    if [cc, cr] in v:
        continue
    print(cc, cr)

