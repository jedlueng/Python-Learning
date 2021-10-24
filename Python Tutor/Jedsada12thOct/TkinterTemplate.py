import tkinter as tk


class Application(tk.Frame):
  def __init__(self, master):
      """Inheriting from Tkinter"""
      super(Application, self).__init__(master)
      self.grid() # Calling the grid method from Tkinter

      #### Customise!!!
      self.create_widgets() # Calling a method

  def create_widgets(self):
    '''Method to create all content on the screen'''

    ### First Name Area
    self.firstname_lbl = tk.Label(self, text='first name:  ', font='arial12')
    self.firstname_lbl.grid(row=0, column=0, pady=10)

    self.first_entry_field = tk.Entry(self)
    self.first_entry_field.grid(row = 0, column = 1, pady=10)

    ### Last Name Area
    self.lastname_lbl = tk.Label(self, text='last name:  ', font='arial12')
    self.lastname_lbl.grid(row=1, column=0, pady=10)

    self.last_entry_field = tk.Entry(self)
    self.last_entry_field.grid(row = 1, column = 1, pady=10)


    self.combine_bttn = tk.Button(self, text = "Combine", command=self.combine)
    self.combine_bttn.grid(row = 2, column = 0)

    self.delete_bttn = tk.Button(self, text = "Delete", command=self.delete)
    self.delete_bttn.grid(row = 2, column = 1)
    

    self.text_box = tk.Text(self, width = 25, height = 3, wrap = tk.WORD)
    self.text_box.grid(row = 3, column = 0, columnspan=4, pady=20)


  def combine(self):
    first_text = self.first_entry_field.get()
    second_text = self.last_entry_field.get()
    if len(first_text) > 1 and len(second_text) > 1: 
      full_name = 'Hello, ' +  first_text + ' '+ second_text
      self.text_box.delete(0.0, tk.END)
      self.text_box.insert(0.0, full_name)


  def delete(self):
    self.text_box.delete(0.0, tk.END)


root = tk.Tk()
root.title("My App")
root.geometry("400x400")
root = Application(root)
root.mainloop() # Keeps the window running
