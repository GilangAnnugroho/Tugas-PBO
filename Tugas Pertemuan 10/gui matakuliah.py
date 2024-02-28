import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,N,NE,E,StringVar,messagebox
from matakuliah import matakuliah

class FormMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode MK:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtkodemk = Entry(mainFrame) 
        self.txtkodemk.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkodemk.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama MK:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtnamamk = Entry(mainFrame) 
        self.txtnamamk.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='SKS:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = StringVar()
        self.satu = Radiobutton(mainFrame, text='1', value='1', variable=self.txtSKS)
        self.satu.grid(row=2, column=0, padx=1, pady=1, sticky=E)
        self.satu.select() # set pilihan yg pertama
        self.dua = Radiobutton(mainFrame, text='2', value='2', variable=self.txtSKS)
        self.dua.grid(row=2, column=1, padx=1, pady=1)
        self.tiga = Radiobutton(mainFrame, text='3', value='3', variable=self.txtSKS)
        self.tiga.grid(row=2, column=2, padx=1, pady=1, sticky=W)        
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idmk', 'kodemk', 'namamk','sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmk', text='ID')
        self.tree.column('idmk', width="30")
        self.tree.heading('kodemk', text='kodemk')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='namamk')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='sks')
        self.tree.column('sks', width="30")

        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtkodemk.delete(0,END)
        self.txtkodemk.insert(END,"")
        self.txtnamamk.delete(0,END)
        self.txtnamamk.insert(END,"")       
        self.txtSKS.set("1")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data matakuliah
        mk = matakuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = matakuliah()
        res = mk.getBykodemk(kodemk)
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtnamamk.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = matakuliah()
        res = mk.getBykodemk(kodemk)
        self.txtnamamk.delete(0,END)
        self.txtnamamk.insert(END,mk.namamk)
        sks = mk.sks
        if(sks=="2"):
            self.dua.select()
        elif(sks=="3"):
            self.tiga.select()
        else:
            self.satu.select()
        
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtkodemk.get()
        namamk = self.txtnamamk.get()
        sks = self.txtSKS.get()        
        mk = matakuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if(self.ditemukan==True):
            res = mk.updateBykodemk(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = matakuliah()
        res = mk.getBykodemk(kodemk)
        rec = mk.affected

        if rec > 0:
            # Jika data ditemukan, munculkan konfirmasi untuk menghapus
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data?")
            if confirm:
                res = mk.deleteBykodemk(kodemk)
                rec = mk.affected
                if rec > 0:
                    messagebox.showinfo("showinfo", "Data Berhasil dihapus")
                else:
                    messagebox.showwarning("showwarning", "Gagal menghapus data")
        else:
            # Jika data tidak ditemukan, tampilkan pesan peringatan
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")

        self.onClear()

    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMatakuliah(root, "Aplikasi Data Mata Kuliah")
    root.mainloop() 