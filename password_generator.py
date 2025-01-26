import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
import json
import os
from datetime import datetime

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TButton', padding=5)
        self.style.configure('TCheckbutton', padding=5)
        
        # Variables
        self.password_length = tk.IntVar(value=12)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        self.min_numbers = tk.IntVar(value=1)
        self.min_symbols = tk.IntVar(value=1)
        self.exclude_similar = tk.BooleanVar(value=True)
        self.password_history = []
        
        # Load saved passwords
        self.load_password_history()
        
        self.setup_ui()
        
    def setup_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both')
        
        # Generator tab
        generator_frame = ttk.Frame(notebook, padding=10)
        notebook.add(generator_frame, text='Generator')
        
        # Title
        title_label = ttk.Label(generator_frame, text="Advanced Password Generator", 
                              font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=10)
        
        # Length frame
        length_frame = ttk.LabelFrame(generator_frame, text="Password Length", padding=10)
        length_frame.pack(fill='x', pady=5)
        
        length_control_frame = ttk.Frame(length_frame)
        length_control_frame.pack(fill='x')
        
        self.length_entry = ttk.Entry(length_control_frame, width=5, justify='center')
        self.length_entry.pack(side='left', padx=5)
        self.length_entry.insert(0, str(self.password_length.get()))
        
        length_scale = ttk.Scale(length_control_frame, from_=4, to=100, orient='horizontal',
                               variable=self.password_length, command=self.update_length_entry)
        length_scale.pack(side='left', fill='x', expand=True, padx=5)
        
        self.length_entry.bind('<FocusOut>', self.validate_length_entry)
        self.length_entry.bind('<Return>', self.validate_length_entry)
        
        # Character Options frame
        options_frame = ttk.LabelFrame(generator_frame, text="Character Options", padding=10)
        options_frame.pack(fill='x', pady=5)
        
        # Basic options
        ttk.Checkbutton(options_frame, text="Uppercase Letters (A-Z)",
                       variable=self.include_uppercase).pack(anchor='w')
        ttk.Checkbutton(options_frame, text="Lowercase Letters (a-z)",
                       variable=self.include_lowercase).pack(anchor='w')
        ttk.Checkbutton(options_frame, text="Numbers (0-9)",
                       variable=self.include_numbers).pack(anchor='w')
        ttk.Checkbutton(options_frame, text="Symbols (!@#$%^&*)",
                       variable=self.include_symbols).pack(anchor='w')
        ttk.Checkbutton(options_frame, text="Exclude Similar Characters (1,l,I,0,O)",
                       variable=self.exclude_similar).pack(anchor='w')
        
        # Minimum requirements frame
        min_frame = ttk.LabelFrame(generator_frame, text="Minimum Requirements", padding=10)
        min_frame.pack(fill='x', pady=5)
        
        ttk.Label(min_frame, text="Minimum numbers:").pack(side='left', padx=5)
        ttk.Spinbox(min_frame, from_=0, to=10, width=3, textvariable=self.min_numbers).pack(side='left', padx=5)
        ttk.Label(min_frame, text="Minimum symbols:").pack(side='left', padx=5)
        ttk.Spinbox(min_frame, from_=0, to=10, width=3, textvariable=self.min_symbols).pack(side='left', padx=5)
        
        # Password display
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(generator_frame, textvariable=self.password_var,
                                 font=('Courier', 12), justify='center')
        password_entry.pack(fill='x', pady=10)
        
        # Buttons frame
        buttons_frame = ttk.Frame(generator_frame)
        buttons_frame.pack(fill='x', pady=5)
        
        ttk.Button(buttons_frame, text="Generate Password",
                  command=self.generate_password).pack(side='left', expand=True, padx=5)
        ttk.Button(buttons_frame, text="Copy to Clipboard",
                  command=self.copy_to_clipboard).pack(side='left', expand=True, padx=5)
        ttk.Button(buttons_frame, text="Save Password",
                  command=self.save_password).pack(side='left', expand=True, padx=5)
        
        # History tab
        history_frame = ttk.Frame(notebook, padding=10)
        notebook.add(history_frame, text='Password History')
        
        # History list
        self.history_tree = ttk.Treeview(history_frame, columns=('Password', 'Date'), show='headings')
        self.history_tree.heading('Password', text='Password')
        self.history_tree.heading('Date', text='Date Generated')
        self.history_tree.pack(fill='both', expand=True)
        
        self.update_history_display()
        
    def generate_password(self):
        try:
            if not any([self.include_uppercase.get(), self.include_lowercase.get(),
                       self.include_numbers.get(), self.include_symbols.get()]):
                messagebox.showerror("Error", "Please select at least one character type")
                return
            
            length = self.password_length.get()
            min_numbers = self.min_numbers.get()
            min_symbols = self.min_symbols.get()
            
            if min_numbers + min_symbols > length:
                messagebox.showerror("Error", "Minimum requirements exceed password length")
                return
            
            # Character pools
            chars = ''
            required_chars = []
            
            if self.include_uppercase.get():
                chars += string.ascii_uppercase
            if self.include_lowercase.get():
                chars += string.ascii_lowercase
            if self.include_numbers.get():
                nums = string.digits
                if self.exclude_similar.get():
                    nums = nums.replace('0', '').replace('1', '')
                chars += nums
                required_chars.extend(random.choices(nums, k=min_numbers))
            if self.include_symbols.get():
                symbols = string.punctuation
                chars += symbols
                required_chars.extend(random.choices(symbols, k=min_symbols))
            
            if self.exclude_similar.get():
                chars = chars.replace('l', '').replace('I', '').replace('0', '').replace('O', '')
            
            # Generate remaining characters
            remaining_length = length - len(required_chars)
            password_chars = required_chars + [random.choice(chars) for _ in range(remaining_length)]
            random.shuffle(password_chars)
            
            password = ''.join(password_chars)
            self.password_var.set(password)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def save_password(self):
        password = self.password_var.get()
        if password and password != "Please select at least one option":
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.password_history.append({"password": password, "date": timestamp})
            self.save_password_history()
            self.update_history_display()
    
    def update_history_display(self):
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        for entry in self.password_history:
            self.history_tree.insert('', 'end', values=(entry['password'], entry['date']))
    
    def load_password_history(self):
        try:
            if os.path.exists('password_history.json'):
                with open('password_history.json', 'r') as f:
                    self.password_history = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load password history: {str(e)}")
    
    def save_password_history(self):
        try:
            with open('password_history.json', 'w') as f:
                json.dump(self.password_history, f)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save password history: {str(e)}")
    
    def update_length_entry(self, *args):
        """Update the entry box when slider is moved"""
        self.length_entry.delete(0, tk.END)
        self.length_entry.insert(0, str(self.password_length.get()))
    
    def validate_length_entry(self, *args):
        """Validate and update the password length when entry is changed"""
        try:
            length = int(self.length_entry.get())
            if length < 4:
                length = 4
            elif length > 100:
                length = 100
            self.password_length.set(length)
            self.length_entry.delete(0, tk.END)
            self.length_entry.insert(0, str(length))
        except ValueError:
            # If invalid input, revert to current slider value
            self.length_entry.delete(0, tk.END)
            self.length_entry.insert(0, str(self.password_length.get()))

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password and password != "Please select at least one option":
            pyperclip.copy(password)

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 