import random


def draw_grid(canvas, border, matr):
    height = canvas.winfo_reqheight()
    width = canvas.winfo_reqwidth()
    n = len(matr)
    a = (height - (n + 1) * border) / n
    b = (width - (n + 1) * border) / n
    canvas.delete('all')
    for i in range(n):
        for j in range(n):
            canvas.create_rectangle((j + 1) * border + j * b, (i + 1) * border + i * a, (j + 1) * border + (j + 1) * b,
                                    (i + 1) * border + (i + 1) * a,
                                    outline="#eee8aa", fill="#eee8aa")
            if matr[i][j] != 0:
                # num = tk.StringVar(value=str(matr[i][j]))
                canvas.create_text((j + 1) * border + j * b + b / 2, (i + 1) * border + i * a + a / 2,
                                   text=str(matr[i][j]),
                                   font=('Calibri', int(2/5 * a)),
                                   fill='#B8860B')


def matr_init(n, num2):
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(0)
    for i in range(num2):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        while m[x][y] != 0:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
        m[x][y] = 2
    return m


def print_matr(m):
    l = len(m)
    for i in range(l):
        for j in range(l):
            if m[i][j] == 0:
                print("-\t", end='')
            else:
                print(str(m[i][j]) + "\t", end='')
        print("")


def input_dir():
    dir = input("insert a direction (wasd), \"e\" to exit: ")
    while not (dir == "a" or dir == "s" or dir == "d" or dir == "w" or dir == "e"):
        print("input not valid")
        dir = input("insert a direction (wasd), \"e\" to exit: ")
    return dir


def move(m, dir):
    l = len(m)
    m_new = []
    for i in range(l):
        m_new.append([])
        for j in range(l):
            m_new[i].append(0)

    if dir == "w":
        v_matr = []
        for j in range(l):
            v_matr.append([])
            for i in range(l):
                if m[i][j] != 0:
                    v_matr[j].append(m[i][j])
        v_matr = double(v_matr)
        for j in range(l):
            for i in range(len(v_matr[j])):
                m_new[i][j] = v_matr[j][i]
    elif dir == "s":
        v_matr = []
        for j in range(l):
            v_matr.append([])
            for i in range(l):
                if m[l - i - 1][j] != 0:
                    v_matr[j].append(m[l - 1 - i][j])
        v_matr = double(v_matr)
        for j in range(l):
            for i in range(len(v_matr[j])):
                m_new[l - 1 - i][j] = v_matr[j][i]
    elif dir == "d":
        v_matr = []
        for i in range(l):
            v_matr.append([])
            for j in range(l):
                if m[i][l - j - 1] != 0:
                    v_matr[i].append(m[i][l - j - 1])
        v_matr = double(v_matr)
        for i in range(l):
            for j in range(len(v_matr[i])):
                m_new[i][l - j - 1] = v_matr[i][j]
    elif dir == "a":
        v_matr = []
        for i in range(l):
            v_matr.append([])
            for j in range(l):
                if m[i][j] != 0:
                    v_matr[i].append(m[i][j])
        v_matr = double(v_matr)
        for i in range(l):
            for j in range(len(v_matr[i])):
                m_new[i][j] = v_matr[i][j]
    if m_new == m:
        print("invalid move")
    else:
        m_new = spawn2(m_new)
    return m_new


def double(v_matr):
    n = len(v_matr)
    for i in range(n):
        if len(v_matr[i]) != 1:
            for j in range(len(v_matr[i]) - 1):
                if j >= len(v_matr[i]) - 1:
                    break
                if v_matr[i][j] == v_matr[i][j + 1]:
                    # score += v_matr[i][j]
                    v_matr[i][j] *= 2
                    del v_matr[i][j + 1]
    return v_matr


def spawn2(m):
    n = len(m)
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    while m[x][y] != 0:
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
    m[x][y] = 2
    return m


def noRoom(m):
    n = len(m)
    s = True
    for i in range(n):
        for j in range(n):
            if m[i][j] == 0:
                s = False
                return s
    return s
