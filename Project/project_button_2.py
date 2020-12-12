import tkinter as tk
from playsound import playsound


blank_space = ' '
title_color = ['#FFDB8B', '#87CEEB']
bg_color = ['#FFFACD', '#B0C4DE']


def click_btn_use_2():
	playsound('click_sound.mp3')
	print('Use!')


def click_btn_style_2():
	playsound('click_sound.mp3')
	print('Вы изменили стиль')


def btn_2(f=0):
	screen_2 = tk.Tk()
	screen_2.geometry('640x360')


	screen_2['bg'] = bg_color[f%2]
	screen_2.title(80*blank_space + 'Mode №_2')
	screen_2.resizable(width = False, height = False)


	Title = tk.Label(screen_2, text = 'Настройте параметры', bg = title_color[f%2], font = '32')
	text_func = tk.Label(screen_2, text = 'Введите функцию', font = '28', bg = '#FFFFFF')
	function = tk.Entry(screen_2, bg = '#FFFFFF', justify = 'center')
	text_error = tk.Label(screen_2, text = 'Введите погрешность', font = '28', bg = '#FFFFFF')
	error = tk.Entry(screen_2, bg = '#FFFFFF', justify = 'center')
	text_point = tk.Label(screen_2, text = 'Точка разложения и радиус', font = '28', bg = '#FFFFFF')
	point = tk.Entry(screen_2, bg = '#FFFFFF', justify = 'center')
	radius = tk.Entry(screen_2, bg = '#FFFFFF', justify = 'center')
	btn_use = tk.Button(screen_2, text = 'Применить', command = click_btn_use_2)
	btn_style = tk.Button(screen_2, text = 'Сменить стиль', command = click_btn_style_2)

	# Левая часть
	Title.pack(anchor = 'n', padx = 10, pady = 5)

	text_func.pack(anchor = 'w', padx = 10, pady = 5)
	function.pack(anchor = 'w', padx = 10, pady = 5)

	text_error.pack(anchor = 'w', padx = 10, pady = 5)
	error.pack(anchor = 'w', padx = 10, pady = 5)


	# Правая часть
	text_point.pack(anchor = 'w', padx = 10, pady = 5)
	point.pack(anchor = 'w', padx = 10, pady = 5)
	radius.pack(anchor = 'w', padx = 10, pady = 5)

	btn_use.pack(anchor = 'w', padx = 10, pady = 5)
	btn_style.pack(anchor = 'w', padx = 10, pady = 5)


	screen_2.mainloop()


if __name__ == "__main__":
    print("This module is not for direct call!")