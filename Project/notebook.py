import tkinter as tk


blank_space = ' '


def button_1():
	screen_1 = tk.Tk()
	screen_1.geometry('640x360')


	screen_1['bg'] = '#FFFACD'
	screen_1.title(90*blank_space + 'Mode №_1')
	screen_1.resizable(width = False, height = False)


	Title = tk.Label(screen_1, text = 'Настройте параметры', bg = '#FFDB8B', font = '32')
	space_1 = tk.Label(screen_1, text = blank_space, bg = '#FFFACD')
	space_2 = tk.Label(screen_1, text = blank_space)
	space_3 = tk.Label(screen_1, text = blank_space, bg = '#FFFACD')
	space_4 = tk.Label(screen_1, text = blank_space, bg = '#FFFACD')
	space_5 = tk.Label(screen_1, text = blank_space, bg = '#FFFACD')
	text_func = tk.Label(screen_1, text = 'Введите функцию', font = '28', bg = '#FFFFFF')
	function = tk.Entry(screen_1, bg = '#FFFFFF')
	text_power = tk.Label(screen_1, text = 'Введите степень', font = '28', bg = '#FFFFFF')
	power = tk.Entry(screen_1, bg = '#FFFFFF')
	text_point = tk.Label(screen_1, text = 'Точка разложения и радиус', font = '28', bg = '#FFFFFF')
	point = tk.Entry(screen_1, bg = '#FFFFFF')
	radius = tk.Entry(screen_1, bg = '#FFFFFF')
	btn_use = tk.Button(screen_1, text = 'Применить')
	btn_style = tk.Button(screen_1, text = 'Сменить стиль')

	# Левая часть
	Title.grid(row = 0, column = 4, columnspan = 4, padx = 10, pady = 5)

	space_1.grid(row = 1, column = 0, columnspan = 6)

	text_func.grid(row = 2, column = 2, columnspan = 4, padx = 10, pady = 5)
	function.grid(row = 3, column = 2, columnspan = 4, padx = 10, pady = 5)

	space_2.grid(row = 4, column = 0, rowspan = 2, columnspan = 5)

	text_power.grid(row = 6, column = 2, columnspan = 4, padx = 10, pady = 5)
	power.grid(row = 7, column = 2, columnspan = 4, padx = 10, pady = 5)


	# Пространство в середние
	space_3.grid(row = 2, column = 5, rowspan = 8, columnspan = 2, sticky = 'SN')


	# Правая часть
	space_4.grid(row = 1, column = 5, columnspan = 6)

	text_point.grid(row = 2, column = 7, columnspan = 4, padx = 10, pady = 5)
	point.grid(row = 3, column = 6, columnspan = 2, padx = 10, pady = 5)
	radius.grid(row = 3, column = 10, columnspan = 2, padx = 10, pady = 5)

	space_5.grid(row = 4, column = 5, rowspan = 2, columnspan = 5)

	btn_use.grid(row = 6, column = 7, sticky = 'E', padx = 10, pady = 5)
	btn_style.grid(row = 6, column = 10, sticky = 'W', padx = 10, pady = 5)


	screen_1.mainloop()

button_1()
'''
if __name__ == "__main__":
    print("This module is not for direct call!")

'''