import pandas as pd
import tkinter as tk


##### Main: read in data
##### Functions: Query a room





class Application(tk.Frame):
  def __init__(self, master):
    """This initializes the frame"""
    super(Application, self).__init__(master)
    self.grid()

    self.df = pd.read_csv('rooms.csv')
    self.room_list = list(self.df['room'])

    self.x = tk.StringVar(self)
    self.x.set(self.room_list[0])
    self.create_widgets()


  def create_widgets(self):
    self.menu = tk.OptionMenu(self, self.x, *self.room_list)
    self.menu.grid(row=0, column=0)

    self.select = tk.Button(self, text='Run', command=self.button_press)
    self.select.grid(row=1, column=1)

    self.text_area = tk.Text(self, width=30, height=3, wrap=tk.WORD)
    self.text_area.grid(row=2, column=0, columnspan=3)



  def button_press(self):
    '''Called When room is selected
  
      Performs a query on the .csv file'''
      
    selected = self.x.get()
    raw_data = self.df.loc[self.df.room == selected][['capacity', 'computers']].values[0]

    text = '{} has a capacity of {}, with {} computers.'.format(selected,
                                                              raw_data[0],
                                                              raw_data[1])

    self.text_area.delete(0.0, tk.END)
    self.text_area.insert(0.0, text)






root = tk.Tk()
root.title("Tester GUI")
root.geometry("300x300")
root = Application(root)
root.mainloop()
