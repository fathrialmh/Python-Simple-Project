import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #self.geometry('400x250')
        self.title('Sistem Perhitungan Luas Bangun Datar')
        self._frame = None
        self.switch_frame(StartPage)

    def Luas_Persegi(self):
        a=self.ent_a.get()
        b=self.ent_b.get()
        persegi = float(a)*float(b)
        self.lbl_result1["text"] = f"Luas Persegi = {round(persegi, 2)} Cm"

    def Luas_Persegi_Panjang(self):
        a=self.ent_a.get()
        b=self.ent_b.get()
        persegi_panjang = float(a)*float(b)
        self.lbl_result2["text"] = f"Luas Persegi Panjang = {round(persegi_panjang, 2)} Cm"

    def Luas_Segitiga(self):
        a=self.ent_a.get()
        b=self.ent_b.get()
        segitiga =(1/2)*float(a)*float(b)
        self.lbl_result3["text"] = f"Luas Segitiga = {round(segitiga, 2)} Cm"

    def Luas_Jajar_Genjang(self):
        a=self.ent_a.get()
        b=self.ent_b.get()
        jajargenjang =float(a)*float(b)
        self.lbl_result4["text"] = f"Luas Jajar Genjang = {round(jajargenjang, 2)} Cm"
      
    def set_text(self,text):
        self.e.insert(0,text)
        return
    
    def tambah(self,data):
        #self.x_result.insert(0,data)
        #ori_text=int(ori_text) +1
        self.x_result = (0,0,0,0)
        #self.x_result.insert(0,data)
        self.x_result[data] += 1
        return
        
    def switch_frame(self, frame_class):
        """Untuk Pindah Ke Halaman Baru"""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Sistem Perhitungan Luas Bangun Datar",font=('Arial',15,'bold')).pack()
        tk.Label(self, text="Silahkan Pilih Bangun Datar",font=('Arial',10)).pack(side="top", fill="x", pady=10)
        persegi = tk.Button(self, text="Luas Persegi",
                  command=lambda:[master.set_text("Luas Persegi"),master.switch_frame(PageOne),master.tambah(0)]).pack(fill="x")
        persegi_panjang = tk.Button(self, text="Luas Persegi Panjang",
                  command=lambda: [master.set_text("Luas Persegi Panjang"),master.switch_frame(PageTwo)]).pack(fill="x")
        segitiga = tk.Button(self, text="Luas Segitiga",
                  command=lambda: [master.set_text("Luas Persegi Segitiga"),master.switch_frame(PageThree)]).pack(fill="x")
        jajar_genjang= tk.Button(self, text="Luas Jajar Genjang",
                  command=lambda: [master.set_text("Luas Jajar Genjang"),master.switch_frame(PageFour)]).pack(fill="x")
        tk.Button(self, text="History",
                  command=lambda: [master.set_text("History"),master.switch_frame(History)]).pack(fill="x")
       # tk.Label(self, text="History",font=('Arial',12,'bold')).pack(side="top", fill="x", pady=10)
        master.e = tk.Entry(self, text='test')
        master.e.pack(fill="x")
        
        master.x_list = ['Luas_Persegi','Luas_Persegi_Panjang','Luas_Segitiga','Luas_Jajar_Genjang']
        master.tambah(1)
        result = self.x_result.get()
        #master.x_result = (0,0,0,0)
        
           
        
        master.figure1 = plt.Figure(figsize=(4,3), dpi=100)
        master.ax1 = master.figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(master.figure1,self)
        bar1.get_tk_widget().pack()
        lines = master.ax1.plot(master.x_list,result)
        print(result)
        master.ax1.set_title('Riwayat Penggunaan')
        
    def tambah(self,data):
        #self.x_result.insert(0,data)
        #ori_text=int(ori_text) +1
        self.x_result = [0,0,0,0]
        self.x_result.insert(0,data)
        #self.x_result[data] += 1
        return   
        
        
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Perhitungan Luas Persegi").pack(side="top", fill="x", pady=10)
        frm_entry = tk.Frame(self)
        
        lbl_a = tk.Label(self, text="Sisi").pack()
        master.ent_a = tk.Entry(self, width=20)
        master.ent_b = tk.Entry(self,text="Lebar", width=20)

        master.ent_a.pack(pady=10)
        lbl_b = tk.Label(self, text="Sisi").pack()
        master.ent_b.pack(pady=10)
       
        frm_entry.pack()
        btn_luas1 = tk.Button(
            self,
            text="Hitung",
            command=master.Luas_Persegi
        )
        master.lbl_result1 = tk.Label(self)
        btn_luas1.pack()
        master.lbl_result1.pack(pady=10)
        
        tk.Button(self, text="Kembali",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Perhitungan Luas Persegi Panjang").pack(side="top", fill="x", pady=10)

        lbl_a = tk.Label(self, text="Panjang").pack()
        master.ent_a = tk.Entry(self, width=20)
        master.ent_b = tk.Entry(self, width=20)

        master.ent_a.pack(pady=10)
        lbl_b = tk.Label(self, text="Lebar").pack()
        master.ent_b.pack()

        btn_luas2 = tk.Button(
            self,
            text="Hitung",
            command=master.Luas_Persegi_Panjang
        )
        master.lbl_result2 = tk.Label(self)
        btn_luas2.pack()
        master.lbl_result2.pack(pady=10)
        tk.Button(self, text="Kembali",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Perhitungan Luas Segitiga").pack(side="top", fill="x", pady=10)

        lbl_a = tk.Label(self, text="Alas").pack()
        master.ent_a = tk.Entry(self, width=20)
        master.ent_b = tk.Entry(self, width=20)
        
        master.ent_a.pack(pady=10)
        lbl_b = tk.Label(self, text="Tinggi").pack()
        master.ent_b.pack()
        
        btn_luas3 = tk.Button(
            self,
            text="Hitung",
            command=master.Luas_Segitiga
        )
        master.lbl_result3 = tk.Label(self)
        btn_luas3.pack()
        master.lbl_result3.pack(pady=10)
        tk.Button(self, text="Kembali",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Perhitungan Luas Jajar Genjang").pack(side="top", fill="x", pady=10)

        lbl_a = tk.Label(self, text="Alas").pack()
        master.ent_a = tk.Entry(self, width=20)
        master.ent_b = tk.Entry(self, width=20)
        
        master.ent_a.pack(pady=10)
        lbl_a = tk.Label(self, text="Tinggi").pack()
        master.ent_b.pack()
        
        btn_luas4 = tk.Button(
            self,
            text="Hitung",
            command=master.Luas_Jajar_Genjang
        )
        master.lbl_result4 = tk.Label(self)
        btn_luas4.pack()
        master.lbl_result4.pack(pady=10)
        tk.Button(self, text="Kembali",
                  command=lambda: master.switch_frame(StartPage)).pack()

class History(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Perhitungan Luas Jajar Genjang").pack(side="top", fill="x", pady=10)
        
        master.x_list = ['Luas_Persegi','Luas_Persegi_Panjang','Luas_Segitiga','Luas_Jajar_Genjang']
        master.x_result = [0,0,0,0]
        
        figure1 = plt.Figure(figsize=(4,3), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1,master)
        bar1.get_tk_widget().pack()
        lines = ax1.plot(master.x_list,master.x_result)
        
        ax1.set_title('Riwayat Penggunaan')

        
        tk.Button(self, text="Kembali",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()