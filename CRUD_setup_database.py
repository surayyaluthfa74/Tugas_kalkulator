def connect_db(): 
    conn=sqlite3.connect("data_siswa.db") 
    cursor = conn.cursor() 
    cursor.execute(
    """
    
    CREATE TABLE IF NOT EXISTS Siswa(
        id INTEGER PRIMARY KEY AUTOINCREMENTC,
        nama TEXT NOT NULL
        umur INTEGER
    )
"""
 )
    conn.commit() 
    conn.close()


def create_data(): 
    if not entry_nama.get() or not entry_umur.get(): 
        messagebox.showwarning("Peringatan", "Semua kolom harus diisi!") 
        return 
    conn = sqlite3.connect("data_siswa.db") 
    cursor = conn.cursor() 
    cursor.execute( 
        "INSERT siswa (nama, umur) VALUES (?, ?)", 
        (entry_nama.get(), entry_umur.get()), 
    ) 
    conn.commit() 
    conn.close() 
    messagebox.showinfo("Sukses", "Data berhasil ditambahkan") 
    clear_form() 
    read_data()
    
def read_data(): 
    for i in tree.get_children(): 
        tree.delete(i) 
    conn = sqlite3.connect("data_siswa.db") 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM siswa") 
    rows = cursor.fetchall() 
    for row in rows: 
        tree.insert("", tk.END, values=row) 
    conn.close()  
    
def update_data():
    Selected_item = tree.selection()
    if not Selected_item:
        messegebox.showwarning("peringatan", "Pilih data yang ingin diubah!")
        return
    item_id = tree.item(Selected_item,"values")[0]
    conn = sqlite3.cennect("data_siswa.db")
    cursor = conn.cursor()
    cursor.execute(
           "update siswa SET nama=?, umur=? WHERE id=?", 
        (entry_nama.get(), entry_umur.get(), item_id),
    )
      
def delete_data(): 
    selected_item = tree.selection() 
    if not selected_item: 
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!") 
        return 
    item_id = tree.item(selected_item, "values")[0] 
    conn = sqlite3.connect("data_siswa.db") 
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM siswa WHERE id=?", (item_id,)) 
    conn.commit() 
    conn.close() 
    messagebox.showinfo("Sukses", "Data berhasil dihapus") 
    clear_form() 
    read_data()
    
def clear_form(): 
    entry_nama.delete(0, tk.END) 
    entry_umur.delete(0, tk.END)    

root = tk.Tk()
root = tittle("Aplikasi CRUD Database Siswa")
root.geometry("500x450,")

tk.Label(root, text="Nama:").pack(pady=5) 
entry_nama = tk.Entry(root, width=40) 
entry_nama.pack()

tk.Label(root, text="Umur:").pack(pady=5) 
entry_umur = tk.Entry(root, width=40) 
entry_umur.pack()

frame_btn = tk.Frame(root) 
frame_btn.pack(pady=10) 
tk.Button(frame_btn, text="Simpan", command=create_data, width=10).grid( 
row=0, column=0, padx=5 
) 
tk.Button(frame_btn, text="Ubah", command=update_data, width=10).grid( 
row=0, column=1, padx=5 
) 
tk.Button(frame_btn, text="Hapus", command=delete_data, width=10).grid( 
row=0, column=2, padx=5 
) 
tk.Button(frame_btn, text="Reset", command=clear_form, width=10).grid( 
row=0, column=3, padx=5 
)

columns = ("ID", "Nama", "Umur") 
tree = ttk.Treeview(root, columns=columns, show="headings") 
tree.heading("ID", text="ID") 
tree.heading("Nama", text="Nama") 
tree.heading("Umur", text="Umur") 
tree.pack(pady=10, fill=tk.BOTH, expand=True)

connect_db() 
read_data() 
root.mainloop()