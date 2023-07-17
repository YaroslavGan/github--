s='АБВГ БД ВБДЕЗЖГ ГЖ ДЕ ЕЗ ЖЗ'
d={c[0]:c[1:] for c in s.split()}

def f(y,end):
    if y[-1]==end:return 1
    return sum(f(y+c,end) for c in d[y[-1]])

print(f('А','З'))
