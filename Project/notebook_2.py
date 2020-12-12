import tkinter as tk
from playsound import playsound


blank_space = ' '
f = 0
title_color = ['#FFDB8B', '#87CEEB']
bg_color = ['#FFFACD', '#B0C4DE']


def click_btn_use():
	playsound('click_sound.mp3')
	print('Use!')


def click_btn_style():
	playsound('click_sound.mp3')
	print('Вы изменили стиль')


def button_1():
	screen_1 = tk.Tk()
	screen_1.geometry('640x360')


	screen_1['bg'] = bg_color[f%2]
	screen_1.title(90*blank_space + 'Mode №_1')
	screen_1.resizable(width = False, height = False)


	Title = tk.Label(screen_1, text = 'Настройте параметры', bg = title_color[f%2], font = '32')
	text_func = tk.Label(screen_1, text = 'Введите функцию', font = '28', bg = '#FFFFFF')
	function = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	text_power = tk.Label(screen_1, text = 'Введите степень', font = '28', bg = '#FFFFFF')
	power = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	text_point = tk.Label(screen_1, text = 'Точка разложения и радиус', font = '28', bg = '#FFFFFF')
	point = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	radius = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	btn_use = tk.Button(screen_1, text = 'Применить', command = click_btn_use)
	btn_style = tk.Button(screen_1, text = 'Сменить стиль', command = click_btn_style)

	# Левая часть
	Title.pack(anchor = 'n', padx = 10, pady = 5)

	text_func.pack(anchor = 'w', padx = 10, pady = 5)
	function.pack(anchor = 'w', padx = 10, pady = 5)

	text_power.pack(anchor = 'w', padx = 10, pady = 5)
	power.pack(anchor = 'w', padx = 10, pady = 5)


	# Правая часть
	text_point.pack(anchor = 'w', padx = 10, pady = 5)
	point.pack(anchor = 'w', padx = 10, pady = 5)
	radius.pack(anchor = 'w', padx = 10, pady = 5)

	btn_use.pack(anchor = 'w', padx = 10, pady = 5)
	btn_style.pack(anchor = 'w', padx = 10, pady = 5)


	screen_1.mainloop()

button_1()