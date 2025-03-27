import unittest
import text_editor
from tkinter import Tk, Text
from io import StringIO
import sys

class TestTextEditor(unittest.TestCase):
    
    def setUp(self):
        self.window = Tk()
        self.text_area = Text(self.window)
        self.text_area.pack()
    
    def tearDown(self):
        self.window.destroy()
        
    def test_font_change(self):
        self.text_area.config(font=("Arial", 14, "normal"))
        self.assertEqual(self.text_area.cget("font"), "Arial 14 normal")
        
        self.text_area.config(font=("Times New Roman", 12, "bold"))
        self.assertEqual(self.text_area.cget("font"), "{Times New Roman} 12 bold")
    
    def test_change_font_color(self):

        self.text_area.config(fg="red")
        self.assertEqual(self.text_area.cget("fg"), "red")
        
        self.text_area.config(fg="green")
        self.assertEqual(self.text_area.cget("fg"), "green")

        
    def test_text_input(self):
        self.text_area.insert("1.0", "Hello, world!")
        self.assertEqual(self.text_area.get("1.0", "end-1c"), "Hello, world!")
        
if __name__ == "__main__":
    unittest.main()