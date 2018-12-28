import unittest
from unittest.mock import MagicMock
import notepad
from tkinter import *

class Test(unittest.TestCase):
	text = MagicMock()
	new_file = notepad.Window.new_file
	select_all = notepad.Window.select_all
	toggle_highlight = notepad.Window.toggle_highlight
	SEL = 'sel'
	END = 'end'
	def test_new_file(self):
		self.new_file()
		self.text.delete.assert_called_with('1.0', END)
	
	def test_select_all(self):
		self.select_all()
		self.text.tag_add.assert_called_with(SEL, '1.0', END)
		
	def test_toggle_highlight(self):
		self.assertIsNotNone(self.toggle_highlight)

if __name__ == '__main__':
	unittest.main()