def trans(new_tabl,new_tabl_):
    for i in range(len(new_tabl[0])):
        row = []
        for item in new_tabl:
            row.append(item[i])
        new_tabl_.append(row)
    return new_tabl_

def f23(tabl):
    pr = []
    for i in range(1,101):
        pr.append(str(i) + '%')
    for i in range(len(tabl)):
        for j in range(len(tabl[i])):
            if tabl[j][i] == None:
                continue
            if tabl[j][i] == 'Не выполнено':
                tabl[j][i] = 'Нет'
            if tabl[j][i] == 'Выполнено':
                tabl[j][i] = 'Да'
            for k in range(len(pr)):
                if tabl[j][i] == pr[k]:
                    tabl[j][i] = str("{:f}".format(int(pr[k][:-1]) * 0.01))[:-4]
            tabl[j][i] = tabl[j][i].replace('(', "")
            tabl[j][i] = tabl[j][i].replace(')', "")
            tabl[j][i] = tabl[j][i].replace('-', "")
            tabl[j][i] = tabl[j][i].replace(' ', "")
    for i in range(len(tabl)):
        tabl[i] = list(filter(None, tabl[i]))
    new_tabl = tabl.copy()
    new_tabl_ = []
    trans(new_tabl,new_tabl_)
    for i in range(len(new_tabl_)):
        new_tabl_[i].reverse()
    return new_tabl_

f23()