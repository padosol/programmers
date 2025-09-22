def solution(str1, str2):
    answer = 0
    g_up = []
    g1 = [(str1[i:i+2]) for i in range(len(str1)-1)]
    g2 = [(str2[i:i+2]) for i in range(len(str2)-1)]
    g1 = [((i.isalpha())*i).lower() for i in g1]
    g2 = [((i.isalpha())*i).lower() for i in g2]
    g1 = [i for i in g1 if i != '']
    g2 = [i for i in g2 if i != '']

    for e in g1:
        if e in g2 : g_up.append(e); g2.remove(e)
    g1.extend(g2)

    if (len(g1) == 0) and (len(g_up) == 0): return 1 * 65536

    return int((len(g_up)/len(g1)) * 65536)