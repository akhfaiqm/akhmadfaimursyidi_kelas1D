# INPUT DATA SELEKSI KPPS
nama = input('Masukan Nama :')
jenis_kelamin = input('Jenis kelamin :')
umur =int(input ('Masukan Usia Anda :'))
tempat_tanggal_lahir = str(input('Masukan Tanggal Lahir :'))
pekerjaan = input ('masukkan pekerjaan (gunakan huruf semua): ')
wilayah_domisili = input ('Masukkan domisili kecamatan (huruf besar semua) :')

# SYARAT 
pengecualian_pekerjaan = ['TNI','POLISI','DOKTER', 'POLITIKUS']
wajib_domisili = ['JATIBARANG', 'BREBES', 'SONGGOM', 'WANASARI', 'LARANGAN',]

# PROSES SELEKSI
seleksi = 'SELAMAT ANDA DITERIMA SEBAGAI ANGGOTA KPPS' if (umur >= 17 and pekerjaan not in pengecualian_pekerjaan and wilayah_domisili in wajib_domisili ) else 'MOHON MAAF ANDA TIDAK DITERIMA ANGGOTA KPPS'
print(seleksi)