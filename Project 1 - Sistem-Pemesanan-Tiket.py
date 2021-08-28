# Kelompok 5 - Project 1
# Deskripsi: Sistem Pemesanan Tiket Pesawat
# Materi yang digunakan :
# - Fungsi
# - Percabangan
# - Perulangan (For & While)
# - Import Module

import os

loop = True

def menu() :
	print("===============================")
	print("-------Tujuan Penerbangan-------")
	print("================================")
	print("1. Bandung - Jogjakarta")
	print("2. Bandung - Jakarta")
	print("3. Bandung - Medan")
	print("4. Bandung - Bali")
	print("===============================")
	
def pesan():
	os.system('cls')
	print("----------------------------------------------")
	print("Anda telah berhasil melakukan pemesanan tiket ")
	print("----------------------------------------------")
	print ("Nama Pemesan : "+nama)
	print("Tanggal Pesanan",tgl)
	print("Kode Pesawat",no_pesawat)
	print("Total Tagihan","Rp.",(harga))
	

print("===============================")
print("Program Penjualan Tiket Pesawat")
print("------Bandara Merah Putih------")
print("===============================")
nama = input("Nasukan Nama Pemesan: ")
tgl = input("Masukkan Tanggal Pemesan (D,M,Y): ")
os.system('cls')
while loop :
	menu()
	tujuan = int(input("Masukan Pilihan [1-5] : "))


	if ((tujuan) == 1):
		print("-------------------------------------------------------")
		print("Kode  Nama\tKota\t\tHarga")
		print("      Pesawat\tTujuan\t\tTiket")
		print("-------------------------------------------------------")
		print("101.  Garuda\tJogjakarta \tRp.1.500.000")
		print("\n102.  Lion Air\tJogjakarta \tRp.800.000")
		print("\n103.  Sriwijaya\tJogjakarta \tRp.750.000")
		print("-------------------------------------------------------")
		no_pesawat = int(input("Masukan kode penerbangan : "))
		
		
		if ((no_pesawat) == 101):
			harga = 1500000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break		
			
			
		elif ((no_pesawat) == 102):
			harga = 800000
			print("")
			print("---------------------------------")
			print("anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		elif ((no_pesawat) == 103):
			harga = 750000
			print("")
			print("---------------------------------")
			print("anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		else :
			os.system('cls')
			print("kode penerbangan tidak ada dalam daftar")
			
			
	elif ((tujuan) == 2):
		print("----------------------------------------------------------")
		print("Kode  Nama\tKota\t\tHarga")
		print("      Pesawat\tTujuan\t\tTiket")
		print("----------------------------------------------------------")
		print("201. Citilink\tJakarta \tRp.2.000.000")
		print("\n202. NAM air\tJakarta \tRp.900.000")
		print("\n203. Garuda\tJakarta \tRp.1.200.000")
		print("----------------------------------------------------------")
		no_pesawat = int(input("Masukan kode penerbangan :"))
		
		if ((no_pesawat) == 201):
			harga = 2000000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		elif ((no_pesawat) == 202):
			harga = 900000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		elif ((no_pesawat) == 203):
			harga = 1200000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		else :
			os.system('cls')
			print("Kode penerbangan tidak ada dalam daftar")
			
			
			
	elif ((tujuan) == 3):
		print("-------------------------------------------------------")
		print("Kode  Nama\tKota\t\tHarga")
		print("      Pesawat\tTujuan\t\tTiket")
		print("-------------------------------------------------------")
		print("301. Citilink\tMedan \tRp.1.000.000")
		print("\n302. Lion Air\tMedan \tRp.800.000")
		print("\n303. Garuda\tMedan \tRp.1.600.000")
		print("-------------------------------------------------------")
		no_pesawat = int(input("Masukan kode penerbangan :"))
		
		if ((no_pesawat) == 301):
			harga = 1000000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		elif ((no_pesawat) == 302):
			harga = 800000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		elif ((no_pesawat) == 303):
			harga = 1600000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		else :
			os.system('cls')
			print("Kode penerbangan tidak ada dalam daftar")
			
			
			
	elif ((tujuan) == 4):
		print("-------------------------------------------------------")
		print("Kode  Nama\tKota\t\tHarga")
		print("      Pesawat\tTujuan\t\tTiket")
		print("-------------------------------------------------------")
		print("401. Garuda\tBali \tRp.1.200.000")
		print("\n402. Lion Air\tBali \tRp.1.000.000")
		print("\n403. Merpati\tBali \tRp.1.800.000")
		print("-------------------------------------------------------")
		no_pesawat = int(input("Masukan kode penerbangan :"))
		

		
		if ((no_pesawat) == 401):
			harga = 1000000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		elif ((no_pesawat) == 402):
			harga = 800000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		elif ((no_pesawat) == 403):
			harga = 800000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			break
			
		else :
			os.system('cls')
			print("Kode penerbangan tidak ada dalam daftar")
			
			
			
	elif ((tujuan) == 5):
		os.system('cls')
		exit()
		

	else :
		os.system('cls')
		print("***Pilihan tidak ada dalam daftar***")
	

print('========================================')
print('-----------Proses Pembayaran------------')
print("========================================")	
bayar = int(input("Silahkan Masukkan Uang Rp."))

kembalian = bayar - harga

while(bayar<harga):
	print("Uang yang anda masukkan kurang")
	tambahan = int(input("Masukkan Uang Kembali: Rp. "))
	bayar = bayar + tambahan
	kembalian = bayar-harga

print("----------------------------------------")    
print("Kembalian anda sebesar Rp.",kembalian)

print("\nTerimakasih Transaksi Berhasil")

		
		
	

		
		


