# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pre = {
        0: {0: 2, 1: 0, 2: 0},
        1: {0: 0, 1: 1, 2: 0},
        2: {0: 0, 1: 0, 2: 1},
        3: {0: 1, 1: 0, 2: 1}
    }
    post = {
        0: {0: 0, 1: 1, 2: 0},
        1: {0: 0, 1: 0, 2: 1},
        2: {0: 0, 1: 1, 2: 0},
        3: {0: 3, 1: 0, 2: 0}
    }
    m0 = {0: 3, 1: 0, 2: 0}
    mg = dict()
    ml = [0]
    m = {
        0: {0: 3, 1: 0, 2: 0}
    }
    while ml:
        pointeur = ml[0]
        ml.remove(pointeur)
        #print(pointeur)
        if pointeur not in mg:
            mg[pointeur] = {}

        for i in range(len(pre)):
            accessible = True
            for j in range(len(pre[i])):
                # print("valeur:" + str(pre[i][j]))
                # print(str(m[pointeur][j]) + "<" + str(pre[i][j]) + "?")
                if m[pointeur][j] < pre[i][j]:
                    accessible = False
            # print(accessible)

            if accessible:
                mm = dict()
                for j in range(len(pre[i])):
                    mm[j] = m[pointeur][j] - pre[i][j] + post[i][j]
                #print("avec transition " + str(i) + ':' + str(mm))
                same = False
                for k in range(len(m)):
                    if mm == m[k]:
                        same = True
                        name = k
                if not same:
                    name = len(mg)
                    print("new moment matrice mg")
                    ml.append(name)
                    m[name]=mm
                else:
                    print("ajouter moment matrice mg")
                mg[pointeur][name] = i
    print(m)
    print(mg)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
