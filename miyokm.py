from tkinter import *

window=Tk()
window.title("miles to km converter")
window.config(padx=20,pady=20)


def calculate():
  miles=float(miles_entry.get())
  km=round(miles*1.609)
  kilometer_result.config(text=f"{km} km")

miles_entry=Entry(width=10)
miles_entry.grid(row=1,column=2)


miles_label=Label(text="miles")
miles_label.grid(row=1,column=3)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(row=3,column=1)

kilometer_result=Label(text="0")
kilometer_result.grid(row=3,column=2)

kilometer_label=Label(text="KM")
kilometer_label.grid(row=3,column=3)


button=Button(text="CALCULATE",width=10,command=calculate)
button.config(padx=10,pady=10)
button.grid(row=2,column=2)







window.mainloop()
