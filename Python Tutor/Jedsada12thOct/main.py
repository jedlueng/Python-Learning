import tkinter as tk


class Application(tk.Frame):
  def __init__(self, master):
      """Inheriting from Tkinter"""
      super(Application, self).__init__(master)
      self.grid() # Calling the grid method from Tkinter
      self.create_widgets() # Calling a method
      self.study_time = 0 
      self.rest_time = 0



  def create_widgets(self):
    '''Method to create all content on the screen'''
    self.study_lbl = tk.Label(self, text='study time:  ', font='arial12')
    self.study_lbl.grid(row=0, column=0, pady=10)

    self.study_entry_field = tk.Entry(self)
    self.study_entry_field.grid(row = 0, column = 1, pady=10)

    self.rest_lbl = tk.Label(self, text='rest time:  ', font='arial12')
    self.rest_lbl.grid(row=1, column=0, pady=10)

    self.last_entry_field = tk.Entry(self)
    self.last_entry_field.grid(row = 1, column = 1, pady=10)


    self.start_bttn = tk.Button(self, text = "Start", command = self.start)
    self.start_bttn.grid(row = 2, column = 0)

    self.reset_bttn = tk.Button(self, text = "Reset ", command = self.reset)
    self.reset_bttn.grid(row = 2, column = 1)

    self.Pause_bttn = tk.Button(self, text = "Pause" , command = self.pause)
    self.Pause_bttn.grid(row = 2, column = 2)

    
    self.text_box = tk.Text(self, width = 25, height = 3, wrap = tk.WORD)
    self.text_box.grid(row = 3, column = 0, columnspan=4, pady=20)


  def start(self): 
    pass 

  def reset(self):
    pass
  def pasue(self): 
    pass 


  # def combine(self):
  #   first_text = self.first_entry_field.get()
  #   second_text = self.last_entry_field.get()
  #   if len(first_text) > 1 and len(second_text) > 1: 
  #     full_name = 'Hello, ' +  first_text + ' '+ second_text
  #     self.text_box.delete(0.0, tk.END)
  #     self.text_box.insert(0.0, full_name)


  # def delete(self):
  #   self.text_box.delete(0.0, tk.END)


root = tk.Tk()
root.title("My App")
root.geometry("400x400")
root = Application(root)
root.mainloop() # Keeps the window running
