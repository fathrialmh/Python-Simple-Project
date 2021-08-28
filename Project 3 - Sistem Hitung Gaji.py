import tkinter as tk

def Hasil():
    a = ent_a.get()
    b = variable.get()
    c = ent_c.get()
    jml_anak = ent_d.get()

    if b =='Rektor':
        gaji_pokok=10000000
        jab="Rektor"

    elif b=='Dekan':
        gaji_pokok=8500000
        jab="Dekan"
    
    elif b=='Kepala Prodi':
        gaji_pokok=6000000
        jab="Kepala Prodi"

    elif b=='Dosen':
        gaji_pokok=4000000
        jab="Dosen"

    else:
        gaji_pokok=3000000
        jab="Staff Lain"
    
    if(jml_anak>='5'):
        tunjangan=1000000

    elif(jml_anak <='3'):
        tunjangan=750000

    else:
        tunjangan=500000
    
    pajak = gaji_pokok * 0.15
    gaji_bersih = gaji_pokok + tunjangan

    hasil_nama["text"] = "Nama : "+a
    hasil_jabatan["text"] ="Jabatan : "+ jab
    hasil_alamat["text"] ="Alamat : "+ c
    hasil_gaji["text"]="Gaji Bersih : ",gaji_bersih

window = tk.Tk()

window.title("Menghitung Gaji Pegawai")
window.resizable(width=50, height=50)

frm_entry = tk.Frame(master=window)
lbl_a = tk.Label(master=frm_entry, text="Nama")
lbl_b = tk.Label(master=frm_entry, text="Jabatan")
lbl_c = tk.Label(master=frm_entry, text="Alamat")
lbl_d = tk.Label(master=frm_entry, text="Jumlah Anak")

ent_a = tk.Entry(master=frm_entry, width=25)
ent_c = tk.Entry(master=frm_entry, width=25)
ent_d = tk.Entry(master=frm_entry, width=25)

lbl_a.grid(row=0, column=0)         
lbl_b.grid(row=1, column=0)         
lbl_c.grid(row=2, column=0)         
lbl_d.grid(row=3, column=0) 

ent_a.grid(row=0, column=1,pady=10)
ent_c.grid(row=2, column=1,pady=10)
ent_d.grid(row=3, column=1)

OPTIONS = [
"Rektor",
"Dekan",
"Kepala Prodi",
"Dosen",
"Staff Lain"
] 

variable = tk.StringVar(frm_entry)
variable.set("Silahkan Pilih") # default value

w = tk.OptionMenu(frm_entry, variable, *OPTIONS)
w.grid(row=1, column=1,padx=50)
btn_hasil = tk.Button(
    master=window,
    text="Hasil",
    command=Hasil
)
hasil_nama = tk.Label(master=window)
hasil_jabatan = tk.Label(master=window)
hasil_alamat = tk.Label(master=window)
hasil_gaji = tk.Label(master=window)

btn_hasil.grid(row=2, column=0)
frm_entry.grid(row=0, column=0)

frm_hasil = tk.Frame(window)

frm_hasil.grid(row=3, column=0)
hasil_nama.grid(row=3, column=0)
hasil_jabatan.grid(row=4, column=0)
hasil_alamat.grid(row=5, column=0)
hasil_gaji.grid(row=6, column=0)


window.mainloop()