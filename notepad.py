import os
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE
	
class Window:
	def __init__(self):
		self.root = Tk()
		self.setup()
	
	def setup(self):
		self.root.title("Блокнот")
		self.root.geometry("600x400")

		self.text = Text(self.root, width=600, height=400)
		self.text.pack()

		self.to_highlight_line = BooleanVar()
		self.text.tag_configure('active_line', background='ivory2')

		self.menu_bar = Menu(self.root)
		self.file_menu = Menu(self.menu_bar, tearoff=0)
		self.view_menu = Menu(self.menu_bar, tearoff=0)
		self.edit_menu = Menu(self.menu_bar, tearoff=0)
		
		self.file_menu_setup()
		self.edit_menu_setup()
		self.view_menu_setup()
		self.menu_bar_setup()
		
		self.root.config(menu=self.menu_bar)
		self.root.mainloop()

	def new_file(self):
		global file_name
		file_name = "Без названия"
		self.text.delete ('1.0', END)

	def save_as(self):
		out = asksaveasfile(mode='w', defaultextension='.txt')
		data = self.text.get('1.0', END)
		try:
			out.write(data.rstrip())
		except Exception:
			messagebox.showerror("Невозможно сохранить файл")
			
	def open_file(self):
		global file_name
		inp = askopenfile(mode='r')
		if inp is None:
			file_name = "Без названия"
			return
		data = inp.read()
		self.text.delete('1.0', END)
		self.text.insert('1.0', data)

	def highlight_line(self, interval=100):
		self.text.tag_remove("active_line", 1.0, "end")
		self.text.tag_add("active_line", "insert linestart", "insert lineend+1c")
		self.text.after(interval, self.toggle_highlight)

	def undo_highlight(self):
		self.text.tag_remove("active_line", 1.0, "end")

	def toggle_highlight(self, event=None):
		if self.to_highlight_line.get():
			self.highlight_line()
		else:
			self.undo_highlight()

	def delete_all(self):
		self.text.delete('1.0', END)

	def select_all(self, event=None):
		self.text.tag_add(SEL, '1.0', END)
		return "break"

	def cut(self):
		self.text.event_generate("<<Cut>>")
		return "break"

	def copy(self):
		self.text.event_generate("<<Copy>>")
		return "break"

	def paste(self):
		self.text.event_generate("<<Paste>>")
		return "break"

	def undo(self):
		self.text.event_generate("<<Undo>>")
		return "break"

	def redo(self, event=None):
		self.text.event_generate("<<Redo>>")
		return "break"
	
	def file_menu_setup(self):
		self.file_menu.add_command(label="Новый", command=self.new_file)
		self.file_menu.add_command(label="Открыть", command=self.open_file)
		self.file_menu.add_command(label="Сохранить как", command=self.save_as)
		self.file_menu.add_separator()
		self.file_menu.add_command(label="Выйти", command=self.root.quit)
	
	def edit_menu_setup(self):
		self.edit_menu.add_command(label="Вырезать", command=self.cut)
		self.edit_menu.add_command(label="Скопировать", command=self.copy)
		self.edit_menu.add_command(label="Вставить", command=self.paste)
		self.edit_menu.add_separator()
		self.edit_menu.add_command(label="Отменить действие", command=self.undo)
		self.edit_menu.add_command(label="Повторить действие", command=self.redo)
		self.edit_menu.add_separator()
		self.edit_menu.add_command(label="Выделить все", command=self.select_all)
		self.edit_menu.add_command(label="Очистить все", command=self.delete_all)
	
	def view_menu_setup(self):
		self.view_menu.add_checkbutton(label="Выделить строку", onvalue=1, offvalue=0, variable=self.to_highlight_line, command=self.toggle_highlight)

	def menu_bar_setup(self):
		self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
		self.menu_bar.add_cascade(label="Правка", menu=self.edit_menu)
		self.menu_bar.add_cascade(label="Вид", menu=self.view_menu)


if __name__ == "__main__":
	window = Window()
	input