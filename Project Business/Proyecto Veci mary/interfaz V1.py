from tkinter import*

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

root = tk.Tk()


root.geometry("800x650")
#root.pack_propagate(False)
#root.resizable(0,0)

#Frame  for treeview


frame1 = tk.LabelFrame(root,text="Visualizador de la base de datos")
frame1.grid(row=1, columnspan=2)

frame4 = tk.LabelFrame(root,text="Visualizador de cliente y Productos")
frame4.place(relx = 1, x =-2, y = 2)

#Frame para busqueda
file_frame=tk.LabelFrame(root,text="Cambio dentro de la base de datos")
file_frame.place(height=100,width=400,rely=0.50,relx=0.10)

frame4 = tk.LabelFrame(root,text="Visualizador de la base de datos")
frame4.grid(row=1,column=4)

#Frame for open file dialog
file_frame=tk.LabelFrame(root,text="Cambio dentro de la base de datos")
file_frame.place(height=100,width=400,rely=0.50,relx=0.10)


boton3= tk.Button(file_frame,text="Inventario",padx=20,pady=10, command=lambda:cambio_cliente_inventario())
boton3.place(rely=0.15,relx=0.60)
boton4= tk.Button(file_frame,text="Clientes",padx=20,pady=10, command=lambda:Load_excel_data())
boton4.place(rely=0.15,relx=0.10)


#Frame for open file dialog
file_frame2=tk.LabelFrame(root,text="Base de Datos en uso")
file_frame2.place(height=100,width=400,rely=0.65,relx=0.10)

#buttons


button1 =tk.Button(file_frame2,text="Buscar la base de datos",command=lambda:File_dialog())#TODO :Command
button1.place(rely=0.65,relx=0.60)

button2 =tk.Button(file_frame2, text="Cargar la base de datos",command=lambda:Load_excel_data())
button2.place(rely=0.65,relx=0.10)



label_file= ttk.Label(file_frame2,text=" \U0001F915 Ninguna base de datos esta conectada \U0001F915")
label_file.place(rely=0.35,relx=0)



##Treeviiew Widget

tv1 =ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)

tv2 =ttk.Treeview(frame4)
tv2.place(relheight=2, relwidth=4)


treescrolly=tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
treescrollx=tk.Scrollbar(frame1,orient="horizontal",command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom",fill="x")
treescrolly.pack(side="right",fill="y")


def __init__(self,window):
    self.wind = window
    self.wind.title("Products Application")
    self.tree=ttk.Treeview(height=10,columns = 2)
    self.tree.grid(row=4,column=0, columnspan=2)

def File_dialog():
    filename=filedialog.askopenfilename(initialdir="/",
                                        title="Select A File",filetype=(("xlsx files","*.xlsx"),("All files","*.*")))
    label_file["text"]=filename

def Load_excel_data():
    file_path=label_file["text"]
    try:
        excel_filename=r"{}".format(file_path)
        df=pd.read_excel(excel_filename)
    except ValueError:
        tk.messagebox.showerror("Information","El documento selecionado no es valido")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No ha seleccionado la base de datos .{file_path}")
        return None
    clear_data()
    tv1["column"]=list(df.columns)
    tv1["show"]="headings"
    for column in tv1["columns"]:
        tv1.heading(column,text=column)
    df_rows =df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("","end",values=row)
    return None



def clear_data():
    tv1.delete(*tv1.get_children())
    
def cambio_cliente_inventario():
    
    file_path=label_file["text"]
    try:
        excel_filename=r"{}".format(file_path)
        df1=pd.read_excel(excel_filename,sheet_name="Productos",dtype=col_types)
    except ValueError:
        tk.messagebox.showerror("Information","El documento selecionado no es valido")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No ha seleccionado la base de datos .{file_path}")
        return None
    clear_data()
    tv1["column"]=list(df1.columns)
    tv1["show"]="headings"
    for column in tv1["columns"]:
        tv1.heading(column,text=column)
    df1_rows =df1.to_numpy().tolist()
    for row in df1_rows:
        tv1.insert("","end",values=row)
    return None
 

root.mainloop()
