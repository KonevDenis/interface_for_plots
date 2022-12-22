import astropy.io.fits as pf
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import math as m
# import matplotlib.pyplot as plt
# import numpy as np
#
#
#
# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))
#
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# # Data for a three-dimensional line
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')
#
# # Data for three-dimensional scattered points
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
# plt.show()
#
#
# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# X, Y = np.meshgrid(x, y)  # создает список массивов координатных сеток
#                           # N-мерного координатного пространства для указанных
#                           # одномерных массивов координатных векторов. Координатное
#                           # пространство - это пространство N-мерных точек-координат,
#                           # причем каждой точке в таком пространстве соответствует комбинация
#                           # одного значения из каждого координатного массива.
# Z = f(X, Y)
#
# ax = plt.axes(projection='3d')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                 cmap='viridis', edgecolor='none')
# ax.set_title('surface')
# plt.show()
from tkinter import *
from tkinter.ttk import Radiobutton


# def profile(xp, yp, type):
#     global stars, R
#     srez = []
#     data_vrem = []
#     if type == "horisontal":
#         plt.plot(stars[yp][(xp - R):(xp + R)])
#         plt.title("Горизонтальный профиль")
#         plt.show()
#     if type == "vertical":
#         data_vrem = np.transpose(stars)
#         plt.plot(data_vrem[xp][(yp - R):(yp + R)])
#         plt.title("Вертикальный профиль")
#         plt.show()


def profile_x():
    Y_value = scidata[1962][440:454]
    X_value = []
    for i in range(440, 454):
        X_value.append(i)
    print(Y_value)
    print(X_value)
    star.close()
    plt.plot(Y_value, X_value)
    plt.title("Горизонтальный профиль")
    plt.show()


def profile_y():
    scidata = np.transpose(scidata)
    Y1_value = scidata[446][1956:1968]  # 1954:1970
    X1_value = []
    for i in range(1956, 1968):
        X1_value.append(i)
    print(X1_value)
    print(Y1_value)
    fig1 = plt.figure()  # создали область Figure
    ax1 = fig1.add_subplot(111)
    fig.set_facecolor('yellow')
    ax1.set(facecolor='blue')
    ax1.set_title("Заголовок")
    ax1.set_xlabel('ось абцис (XAxis)')
    ax1.set_ylabel('ось ординат (YAxis)')
    ax1.plot(X1_value, Y1_value, color='pink', linewidth=5)
    plt.show()


def clicked():
    global x, y, r, R, R_vnesh, file, star, scidata
    star = pf.open(txt.get(1.0, END).replace("\n", ""))
    scidata = star[0].data
    #print(scidata)
    star.close()
    x = int(X_coord.get(1.0, END))
    y = int(Y_coord.get(1.0, END))
    R = int(r_star.get(1.0, END))
    print(R)
    # r = int(X_coord.get(1.0, END))
    # R = int(X_coord.get(1.0, END))

    if chk_X_state.get():
        profile_x()

    if chk_Y_state.get():
        profile_y()
    # print("3")
    # snimok =


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('900x500')
#text
txt = Text(window, width=40, height=1)
txt.insert(INSERT, r'C:\v523cas60s-001.fit')
txt.grid(column=0, row=0)
#1 КООРДИНА ПО X
lbl = Label(window, text="координата X")
lbl.grid(column=0, row=1)
# поле ввода
X_coord = Text(window, width=40, height=1)
X_coord.insert(INSERT, "446")
X_coord.grid(column=1, row=1)
#2 КООРДИНАТА по Y
lbl = Label(window, text="координта Y")
lbl.grid(column=0, row=2)
# поле ввода
Y_coord = Text(window, width=40, height=1)
Y_coord.insert(INSERT, "1962")
Y_coord.grid(column=1, row=2)
#3 РАДИУС ЗВЕЗДЫ
lbl = Label(window, text="радиус звезды")
lbl.grid(column=0, row=3)
# поле ввода
R = Text(window, width=40, height=1)
R.insert(INSERT, "10")
R.grid(column=1, row=3)

#4
lbl = Label(window, text="внутр радиус звезды")
lbl.grid(column=0, row=4)
# поле ввода
r_outer = Text(window, width=40, height=1)
r_outer.insert(INSERT, "5")
r_outer.grid(column=1, row=4)

#5
lbl = Label(window, text="внеш радиус звезды")
lbl.grid(column=0, row=5)
# поле ввода
r_vnesh = Text(window, width=40, height=1)
r_vnesh.insert(INSERT, "7")
r_vnesh.grid(column=1, row=5)


# lbl = Label(window, text="внеш радиус звезды")
#1
X_coord = Text(window, width=40, height=1)
X_coord.insert(INSERT, "446")
X_coord.grid(column=1, row=1)
#2
Y_coord = Text(window, width=40, height=1)
Y_coord.insert(INSERT, "1962")
Y_coord.grid(column=1, row=2)
#3
r_star = Text(window, width=40, height=1)
r_star.insert(INSERT, "10")
r_star.grid(column=1, row=3)
#4
r_outer = Text(window, width=40, height=1)
r_outer.insert(INSERT, "5")
r_outer.grid(column=1, row=4)
# r_vnesh = Entry(window, width=100)
# r_vnesh.grid(column=1, row=4)
#5
r_vnesh = Text(window, width=40, height=1)
r_vnesh.insert(INSERT, "7")
r_vnesh.grid(column=1, row=5)

chk_X_state = IntVar()
chk_X_state.set(0)
chk_X = Checkbutton(window, text='Профиль по X', var=chk_X_state)
chk_X.grid(column=0, row=13)

chk_Y_state = IntVar()
chk_Y_state.set(0)
chk_Y = Checkbutton(window, text='Профиль по Y', var=chk_Y_state)
chk_Y.grid(column=0, row=14)

chk_3D_state = IntVar()
chk_3D_state.set(0)
chk_3D = Checkbutton(window, text='3D график      ', var=chk_3D_state)
chk_3D.grid(column=0, row=15)

btn = Button(window, text="нажми на меня!", command=clicked)
btn.grid(column=0, row=20)
window.mainloop()
