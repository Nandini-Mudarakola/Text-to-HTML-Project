import textile
import tkinter as tk

def covertToHtml():
    #fornowempty
    inp=T.get(1.0,"end-1c")
    html=textile.textile(inp)
    print("\nAfter converted to HTML: \n",html)
    lbl.config(text="Converted Html : "+html)

root=tk.Tk()
root.geometry("250x170")

# Create Text for input
T=tk.Text(root,height=5,width=52)
T.pack()
T.insert(tk.END,"""""")

# Create button for result generation
b1=tk.Button(root,text="Submit",command=covertToHtml)
b1.pack()

# Create label for result display
lbl=tk.Label(root,text="")
lbl.pack()

root.mainloop()
