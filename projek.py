import psycopg2 
from tabulate import tabulate
import datetime as dt
import questionary

def koneksiDB():
    nilaihost = 'localhost'
    nilaiDB = 'ambasda2'
    nilaiuser = 'postgres'
    nilaipass = 'SUNGKEM0711'
    nilaiport = '5432'
    try:
        conn = psycopg2.connect(
                host = nilaihost,
                database = nilaiDB,  
                user = nilaiuser,
                password = nilaipass,
                port = nilaiport
            )
        kursor = conn.cursor()
        return kursor, conn
    except:
        print('Koneksi ke Database Gagal, Silahkan Check Lagi')

def batas():
    print('='*64)

def login():
    while True:
        print('======LOGIN AKUN SEBAGAI======')
        print('(1).Login Sebagai Admin\n(2). Login Sebagai Customer\n(3). Login Sebagai Karyawan')
        akunpengguna = input('Pilih Login Sebagai >> ')
        try:
            if akunpengguna == '1':
                loginadmin()
                break
            elif akunpengguna == '2':
                pilihan_login_cust()
                break
            elif akunpengguna == '3':
                loginkaryawan()
                break
        except:
            print('Pilihan Login Yang Anda Masukkan Salah\nSilahkan Masukkan Pilihan Login lagi ')

def pilihan_login_cust():
    while True:
        print('======LOGIN AKUN CUSTOMER======')
        print('(1). Sudah Punya Akun\n(2). Belum Punya Akun')
        akun_customer = input('Masukkan Pilihan Akun')
        try:
            if akun_customer == '1':
                logincustomer()
                break
            elif akun_customer == '2':
                buat_akun_customer()
            else:
                print('Pilihan Tidak Ada')
        except:
            print('Inputan Yang Dimasukkan Tidak Valid')

def loginadmin():
    kursor, conn = koneksiDB()
    while True:
        username_admin = input('Masukkan Username Anda: ')
        password_admin = input('Masukkan Password Anda: ')
        query = "select id_akun from akun where username = %s and password = %s and role_id_role = 1"
        try:
            kursor.execute(query, (username_admin, password_admin))
            cek_akun = kursor.fetchone()
            if cek_akun is not None:
                print('======LOGIN BERHASIL======')
                idakun = cek_akun[0]
                menu_admin(idakun)
                conn.close()
                break
            else:
                print('======LOGIN GAGAL======\nKesalahan Pada Username atau Password, Silahkan Ulangi Lagi')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        finally:
            kursor.close()
            conn.close()

def logincustomer():
    kursor, conn = koneksiDB()
    while True:
        username_customer = input('Masukkan Username Anda: ')
        password_customer = input('Masukkan Password Anda: ')
        query = "select id_akun from akun where username = %s and password = %s and role_id_role = 3"
        try:
            kursor.execute(query, (username_customer, password_customer))
            cek_akun = kursor.fetchone()
            if cek_akun is not None:
                print('======LOGIN BERHASIL======')
                idcustomer = cek_akun[0]
                menu_customer(idcustomer)
                conn.close()
                break
            else:
                print('======LOGIN GAGAL======\nKesalahan Pada Username atau Password, Silahkan Ulangi Lagi')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        finally:
            kursor.close()
            conn.close()

def loginkaryawan():
    kursor, conn = koneksiDB()
    while True:
        username_karyawan = input('Masukkan Username Anda: ')
        password_karyawan = input('Masukkan Password Anda: ')
        query = "select id_akun from akun where username = %s and password = %s and role_id_role = 2"
        try:
            kursor.execute(query, (username_karyawan, password_karyawan))
            cek_akun = kursor.fetchone()
            if cek_akun is not None:
                print('======LOGIN BERHASIL======')
                idkaryawan = cek_akun[0]
                menu_karyawan(idkaryawan)
                conn.close()
                break
            else:
                print('======LOGIN GAGAL======\nKesalahan Pada Username atau Password, Silahkan Ulangi Lagi')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        finally:
            kursor.close()
            conn.close()

def cek_nama(nama):
    simbol =['!','@','#','$','%','^','&','*','(',')',',']
    while True:
        try:
            if any(s in username for s in simbol):
                print('Username Tidak Sesuai Harus Terdiri Dari Huruf dan Angka')
                username = input('Masukkan Username: ')
                continue
            if len(username) < 2:
                print("Username minimal 3 karakter")
                username = input("Masukkan Username: ")
                continue
            if not username.strip():
                print("Username tidak boleh kosong atau spasi saja!")
                username = input("Masukkan Username: ")
                continue
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        break
    return nama

def cek_username(username):
    kursor, conn = koneksiDB()
    simbol =['!','@','#','$','%','^','&','*','(',')',',']
    while True:
        try:
            if any(s in username for s in simbol):
                print('Username Tidak Sesuai Harus Terdiri Dari Huruf dan Angka')
                username = input('Masukkan Username: ')
                continue
            if len(username) < 2:
                print("Username minimal 3 karakter")
                username = input("Masukkan Username: ")
                continue
            if not username.strip():
                print("Username tidak boleh kosong atau spasi saja!")
                username = input("Masukkan Username: ")
                continue
            query = "select * from akun where username = %s"
            kursor.execute(query, (username,))
            cocok = kursor.fetchone()
            if cocok is not None:
                print('Username Tidak Sesuai')
                username = input('Masukkan Username: ')
                continue
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        break
    kursor.close()
    conn.close()
    return username

def cek_nama_produk(nama_produk):
    kursor, conn = koneksiDB()
    simbol =['!','@','#','$','%','^','&','*','(',')',',']
    while True:
        try:
            if any(s in nama_produk for s in simbol):
                print('nama_produk Tidak Sesuai Harus Terdiri Dari Huruf dan Angka')
                username = input('Masukkan nama_produk: ')
                continue
            if len(nama_produk) < 2:
                print("nama_produk minimal 3 karakter")
                username = input("Masukkan nama_produk: ")
                continue
            if not nama_produk.strip():
                print("nama_produk tidak boleh kosong atau spasi saja!")
                username = input("Masukkan nama_produk: ")
                continue
            query = "select * from produk where nama_produk = %s"
            kursor.execute(query, (nama_produk,))
            cocok = kursor.fetchone()
            if cocok is not None:
                print('nama_produk Sudah Dipakai')
                nama_produk = input('Masukkan nama_produk: ')
                continue
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        break
    kursor.close()
    conn.close()
    return nama_produk

def cek_password(password):
    while True:
        try:
            if not password.strip():
                print("Password tidak boleh kosong atau spasi saja!")
                password = input("Masukkan Password Anda: ")
                continue
            if len(password) < 6:
                print('Password  Minimal 6 Karater')
                password = input('Masukkan Password Anda: ')
                continue
            if password.isalpha():
                print('Password Gabungan Huruf dan Angka')
                password = input('Masukkan Password Anda: ')
                continue
            if password.isnumeric():
                print('Password Gabungan Huruf dan Angka')
                password = input('Masukkan Password Anda: ')
                continue
        except:
            print('Input tidak Valid')
        break
    return password

def cek_email(email):
    while True:
        try:
            if email.endwith('@gmail.com') == False:
                print('Email harus mengunakan @gmail.com')
                email = input('Masukkan Email Anda: ')
                continue
            if not email.strip():
                print("Email tidak boleh kosong atau spasi saja!")
                email = input("Masukkan Email Anda: ")
                continue
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    return email

def cek_no_telp(no_telp):
    while True:
        try:
            if no_telp.isalpha() == False:
                print('Nomer Telp harus angka semua')
                no_telp = input('Masukkan NO Telp Anda: ')
                continue
            if not no_telp.strip():
                print("Nomer Telp tidak boleh kosong atau spasi saja!")
                no_telp = input("Masukkan NO Telp Anda: ")
                continue
            if not (len(no_telp) >= 10 and len(no_telp) <= 13):
                print('Nomer Telp harus 10-13 digit')
                no_telp = input('Masukkan NO Telp Anda: ')
                continue
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    return no_telp

def cek_tanggal(tanggal):
    while True:
        try:
            if not tanggal.strip():
                print("Tanggal Tidak Boleh Kosong")
                tanggal = questionary.text("Tanggal: ").ask()
                continue
            tanggal = int(tanggal)
            if not(tanggal in range(1,32)):
                print('Tanggal Yang Anda Harus 1-31')
                tanggal = questionary.text("Tanggal: ").ask()
                continue
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            print('Tanggal Harus Angka')
            tanggal = questionary.text("Tanggal: ").ask()
    return tanggal

def cek_bulan(bulan):
    while True:
        try:
            if not bulan.strip():
                print("bulan Tidak Boleh Kosong")
                bulan = questionary.text("bulan: ").ask()
                continue
            bulan = int(bulan)
            if not(bulan in range(1,13)):
                print('bulan Yang Anda Harus 1-12')
                bulan = questionary.text("bulan: ").ask()
                continue
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            print('Tanggal Harus Angka')
            bulan = questionary.text("bulan: ").ask()
    return bulan

def cek_tahun(tahun):
    while True:
        try:
            if not tahun.strip():
                print("Tahun tidak boleh kosong atau spasi saja")
                tahun = questionary.text("Tanggal: ").ask()
                continue
            tahun = int(tahun)
            tanggal_sekarang = datetime.date.today()
            tahun_saja = tanggal_sekarang.year
            if tahun <= tahun_saja:
                print('Tahun Yang Anda Masukkan Salah')
                tahun = questionary.text("Tanggal: ").ask()
                continue
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            print('Tahun Harus Berupa Angka')
            tahun = questionary.text("Tanggal: ").ask()
    return tahun

def cek_harga(harga):
    while True:
        try:
            if not harga.strip():
                print('Harga Tidak Boleh Kosong') 
                harga = (input('Masukkan Harga Produk(ex:3000): '))
                continue
            harga = int(harga)
            if len(harga) > 4:
                print('Harga Terlalu Rendah')
                harga = (input('Masukkan Harga Produk(ex:3000): '))
                continue
            if harga.isnumeric() == False:
                print('Harga harus terdiri dari angka')
                harga = (input('Masukkan Harga Produk(ex:3000): '))
        except:
            print('Harga harus terdiri dari angka')
            harga = (input('Masukkan Harga Produk(ex:3000): '))

def buat_akun_customer():
    kursor, conn = koneksiDB()
    while True:
        username_customer = input('Masukkan Username Anda: ')
        password_customer = input('Masukkan Password Anda: ')
        gmail_customer = input('Masukkan Email Anda: ')
        no_telp_customer = input('Masukkan NO_Telp Anda: ')
        username_customer = cek_username(username_customer)
        password_customer = cek_password(password_customer)
        gmail_customer = cek_email(gmail_customer)
        no_telp_customer = cek_no_telp(no_telp_customer)
        query1 = "insert into customer (no_telp, email, akun_id_akun) values (%s, %s, %s);"
        query2 = "insert into akun (username, password, role_id_role) values (%s, %s, 3) returning id_akun;"
        # query3 = "select id_akun from akun where username = %s and password = %s"
        try:    
            kursor.execute(query2, (username_customer, password_customer))
            # kursor.execute(query3, (username_customer, password_customer))
            cocokan = kursor.fetchone()
            id_akun = cocokan[0]
            kursor.execute(query1, (no_telp_customer, gmail_customer, id_akun))
            conn.commit()
            print('BUAT AKUN BERHASIL')
            conn.close()
            break
        except Exception as e:
            conn.rollback()
            print(f"Terjadi Kesalahan : {e}")

def menu_admin(idakun):
    print('======MENU ADMIN======')
    print("""
    (1). Melihat Produk
    (2). Memperbarui Produk
    (3). Laporan
    (4). Melihat pesanan
    (5). Melihat Detail Pesanan
    (6). Detail Karyawan
    (7). Diskon
    (8). Exit
    """)
    while True:
        input_admin = input('Pilih Menu Yang Diinginkan >> ')
        if input_admin == '1':
            lihat_produkA(idakun)
        elif input_admin == '2':
            perbarui_produk(idakun)
        elif input_admin == '3':
            laporan(idakun)
        elif input_admin == '4':
            lihat_pesanan(idakun)
        elif input_admin == '5':
            lihat_detail_pesanan(idakun)
        elif input_admin == '6':
            detail_karyawan(idakun)
        elif input_admin == '7':
            diskon(idakun)
        elif input_admin == '8':
            break
        else:
            print("Pilihan Tidak Ada")

def laporan(idakun):
    kursor, conn = koneksiDB()
    query1 = "select p.nama_produk, sum(dp.harga * dp.quantity) as jumlah_terjual from produk p join detail_pesanan dp using (produk_id) where p.status_pruduk = 'Aktif' group by p.nama_produk order by sum(dp.harga * dp.quantity)"
    while True:
        try:
            kursor.execute(query1)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print (tabulate(data, headers=header, tablefmt='psql'))
            print("=====MENU LAPORAN=====")
            print("(1). Tampilkan 5 Produk Terlaris 1 Minggu Terkhir\n(2). Tampilkan 5 Produk Terlaris 1 Bulan Terakhir\n(3). Tampilkan 5 Produk Kurang Diminati 1 Minggu Terakhir\n(4). Tampilkan 5 Produk Kurang Diminati 1 Bulan Terakhir\n(5). Exit")
            admin_pilih = input('Masukkan Pilihan Anda >> ')
            if admin_pilih == '1':
                produk_laris_1minggu(idakun)
                continue
            elif admin_pilih == '2':
                produk_laris_1bulan(idakun)
                continue
            elif admin_pilih == '3':
                produk_kurang_1minggu(idakun)
                continue
            elif admin_pilih == '4':
                produk_kurang_1bulan(idakun)
                continue
            elif admin_pilih == '5':
                break
            else:
                print('Pilihan Tidak Ada')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")

def produk_laris_1minggu(idakun):
    kursor, conn = koneksiDB()
    query1 = "select p.nama_produk, sum(dp.harga * dp.quantity) as jumlah_terjual from produk p join detail_pesanan dp using (id_produk) where p.status_produk = 'Aktif' and tanggal_pesanan <= %s and tanggal_pesanan >= %s group by p.nama_produk order by sum(dp.harga * dp.quantity) desc limit 5"
    try:
        tanggal_awal = dt.date.today()
        tanggal_akhir = tanggal_awal - dt.timedelta(days=7)
        kursor.execute(query1, (tanggal_awal, tanggal_akhir))
        data = kursor.fetchall()
        header= [d[0]for d in kursor.description]
        print (tabulate(data, headers=header, tablefmt='psql'))
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")
    finally:
        kursor.close()
        conn.close()

def produk_laris_1bulan(idakun):
    kursor, conn = koneksiDB()
    query1 = "select p.nama_produk, sum(dp.harga * dp.quantity) as jumlah_terjual from produk p join detail_pesanan dp using (id_produk) where p.status_produk = 'Aktif' and tanggal_pesanan <= %s and tanggal_pesanan >= %s group by p.nama_produk order by sum(dp.harga * dp.quantity) desc limit 5"
    try:
        tanggal_awal = dt.date.today()
        tanggal_akhir = tanggal_awal - dt.timedelta(days=30)
        kursor.execute(query1, (tanggal_awal, tanggal_akhir))
        data = kursor.fetchall()
        header= [d[0]for d in kursor.description]
        print (tabulate(data, headers=header, tablefmt='psql'))
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")
    finally:
        kursor.close()
        conn.close()

def produk_kurang_1minggu(idakun):
    kursor, conn = koneksiDB()
    query1 = "select p.nama_produk, sum(dp.harga * dp.quantity) as jumlah_terjual from produk p join detail_pesanan dp using (id_produk) where p.status_produk = 'Aktif' and tanggal_pesanan <= %s and tanggal_pesanan >= %s group by p.nama_produk order by sum(dp.harga * dp.quantity) asc limit 5"
    try:
        tanggal_awal = dt.date.today()
        tanggal_akhir = tanggal_awal - dt.timedelta(days=7)
        kursor.execute(query1, (tanggal_awal, tanggal_akhir))
        data = kursor.fetchall()
        header= [d[0]for d in kursor.description]
        print (tabulate(data, headers=header, tablefmt='psql'))
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")
    finally:
        kursor.close()
        conn.close()

def produk_kurang_1bulan(idakun):
    kursor, conn = koneksiDB()
    query1 = "select p.nama_produk, sum(dp.harga * dp.quantity) as jumlah_terjual from produk p join detail_pesanan dp using (id_produk) where p.status_produk = 'Aktif' and tanggal_pesanan <= %s and tanggal_pesanan >= %s group by p.nama_produk order by sum(dp.harga * dp.quantity) asc limit 5"
    try:
        tanggal_awal = dt.date.today()
        tanggal_akhir = tanggal_awal - dt.timedelta(days=30)
        kursor.execute(query1, (tanggal_awal, tanggal_akhir))
        data = kursor.fetchall()
        header= [d[0]for d in kursor.description]
        print (tabulate(data, headers=header, tablefmt='psql'))
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")
    finally:
        kursor.close()
        conn.close()

def lihat_produkA(idakun):
    kursor, conn = koneksiDB()
    query = "select * from produk order by status_produk"
    try:
        kursor.execute(query)
        data = kursor.fetchall()
        header= [d[0]for d in kursor.description]
        print (tabulate(data, headers=header, tablefmt='psql'))
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")
    kursor.close()
    conn.close()

def lihat_pesanan(idakun):
    try:
        kursor, conn = koneksiDB()
        query = "select * from pesanan"
        kursor.execute(query)
        data = kursor.fetchall()
        header= [d[0]for d in kursor.description]
        print (tabulate(data, headers=header, tablefmt='psql'))
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")

def lihat_detail_pesanan(idakun):
    try:
        kursor, conn = koneksiDB()
        query = "select * from detail_pesanan"
        kursor.execute(query)
        data = kursor.fetchall()
        header= [d[0]for d in kursor.description]
        print (tabulate(data, headers=header, tablefmt='psql'))
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")

def detail_karyawan(idakun):
    kursor, conn = koneksiDB()
    query = "select * from karyawan where status_karyawan = 'Aktif' and jabatan_id_jabata <> 'owner'"
    while True:
        try:
            kursor.execute(query)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print (tabulate(data, headers=header, tablefmt='psql'))
            print('=====MENU KARYAWAN=====')
            print("""
            (1). Melihat Semua Karyawan
            (2). Menambahkan Karyawan
            (3). Memecat Karyawan
            (4). Exit
            """)
            data = input('Masukkan Pilihan Menu >> ')
            if data == '1':
                lihat_karyawan(idakun)
            elif data == '2':
                tambah_karyawan(idakun)
            elif data == '3':
                pecat_karyawan(idakun)
            elif data == '4':
                break
            else:
                print('Pilihan Tidak Ada')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")

def lihat_karyawan(idakun):
    try:
        kursor, conn = koneksiDB()
        query = "select * from karyawan"
        kursor.execute(query)
        data = kursor.fetchall()
        header= [d[0]for d in kursor.description]
        print (tabulate(data, headers=header, tablefmt='psql'))
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")

def pecat_karyawan(idakun):
    try:
        kursor, conn = koneksiDB()
        query1 = "select * from karyawan where status_karyawan = 'Aktif' and jabatan_id_jabata <> 5"
        query2 = "select id_karyawan from karyawan where status_karyawan = 'Aktif' and jabatan_id_jabata <> 5"
        query3 = "update karyawan set status_karyawan = 'Tidak Aktif' where id_karyawan = %s"
        while True:
            kursor.execute(query1)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print (tabulate(data, headers=header, tablefmt='psql'))
            kursor.execute(query2)
            data = kursor.fetchall()
            data_list = [i[0] for i in data]
            print('======Id Karyawan======')
            for i in data:
                print(f'id karyawan {i[0]}')
            try:
                admin_input = int(input('Pilih Id Karyawan yang mau dipecat: '))
                while True:
                    if admin_input not in data_list:
                        print('Id Karyawan yang anda masukkan salah')
                        admin_input = int(input('Pilih Id Karyawan yang mau dipecat: '))
                        continue
                    break
            except ValueError:
                print("Input harus berupa angka!")
                continue
            kursor.execute(query3, (admin_input,))
            conn.commit()
            print('Pemecatan Berhasil')
            break
    except Exception as e:
        print(f"Terjadi Kesalahan : {e}")
    finally:
        kursor.close()
        conn.close()

def tambah_karyawan(idakun):
    kursor, conn = koneksiDB()
    while True:
        nama_karyawan = input('Masukkan Nama Karyawan: ')
        ttl_karyawan = tanggal_karyawan()
        email_karyawan = input('Masukkan email karyawan: ')
        no_telp_karyawan = input('Masukkan NO Telp karyawan: ')
        password_karyawan = input('Masukkan Password karyawan: ')
        jabatan = questionary.select(
        "Jabatan Karyawan:",
        choices=["Pengantar", "Kasir", "kebersihan", "koki"]
        ).ask()
        if jabatan == "Pengantar":
            jabatan_id = 1
        elif jabatan == "kasir":
            jabatan_id = 2
        elif jabatan == "kebersihan":
            jabatan_id = 3
        elif jabatan == "koki":
            jabatan_id = 4
        nama_karyawan = cek_username(nama_karyawan)
        password_karyawan = cek_password(password_karyawan)
        email_karyawan = cek_email(email_karyawan)
        no_telp_karyawan = cek_no_telp(no_telp_karyawan)
        ttl_karyawan = cek_tanggal(ttl_karyawan)
        query1 = "insert into karyawan (nama_karyawan, tanggal_lahir, email, no_telp, akun_id_akun, jabatan_id_jabatan) values (%s, %s, %s, %s, %s, %s);"
        query2 = "insert into akun (username, password, role_id_role) values (%s, %s, 2) returning id_akun;"
        try:
            kursor.execute(query2, (nama_karyawan, password_karyawan))
            cocokan = kursor.fetchone()
            id_akun = cocokan[0]
            kursor.execute(query1, (nama_karyawan, ttl_karyawan, email_karyawan, no_telp_karyawan, id_akun, jabatan_id))
            conn.commit()
            print('BUAT AKUN BERHASIL')
            break
        except Exception as e:
            conn.rollback()
            print(f"Terjadi Kesalahan : {e}")
        finally:
            kursor.close()
            conn.close()

def tanggal_karyawan(idakun):
    tanggal = questionary.text("Tanggal: ").ask()
    bulan = questionary.text("Bulan: ").ask()
    tahun = questionary.text("Tahun: ").ask()
    try:
        tanggal = cek_tanggal(tanggal)
        bulan = cek_bulan(bulan)
        tahun = cek_tahun(tahun)
        karyawan_date = dt.date(tahun, bulan, tanggal)
        return karyawan_date
    except Exception as e:
            print(f"Terjadi Kesalahan : {e}")

def perbarui_produk(idakun):
    kursor, conn = koneksiDB()
    query1 = "select id_produk, nama_produk, harga, stock from produk where status_produk = 'Aktif' order by id_produk;"
    try:
        while True:
            print('=====PRODUK DIJUAL=====')
            kursor.execute(query1)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print (tabulate(data, headers=header, tablefmt='psql'))
            print('=====PILIH MENU PRODUK=====')
            print('(1). Hapus Produk\n(2). Kembalikan Produk\n(3). Tambah Produk\n(4). Ubah Harga Produk\n(5). Exit')
            admin_input = input('Masukkan Pilihan Anda >> ')
            if admin_input == '1':
                hapus_produk(idakun)
                continue
            elif admin_input == '2':
                kembali_produk(idakun)
                continue
            elif admin_input == '3':
                tambah_produk(idakun)
                continue
            elif admin_input == '4':
                ubah_harga(idakun)
            elif admin_input == '5':
                break
            else:
                print('Pilhan Tidak Ada')
    except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
    kursor.close()
    conn.close()

def hapus_produk(idakun):
    kursor, conn = koneksiDB()
    query1 = "select id_produk, nama_produk, harga, stock from produk where status_produk = 'Aktif' order by id_produk;"
    query2 = "select id_produk from produk where status_produk = 'Aktif' order by id_produk;"
    query3 = "update produk set status_produk = 'Tidak Aktif' where id_produk = %s"
    while True:
        try:
            kursor.execute(query1)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print(tabulate(data, headers=header, tablefmt='psql'))
            kursor.execute(query2)
            data = kursor.fetchall()
            data_list = [i[0] for i in data]
            print('===PILIH ID PRODUK YANG MAU DIUBAH===')
            for i in data:
                print(f'id karyawan {i[0]}')
            try:
                admin_input = int(input('Pilih Id Produk yang mau dihilangkan: '))
                while True:
                    if admin_input not in data_list:
                        print('Id Karyawan yang anda masukkan salah')
                        admin_input = int(input('Pilih Id Produk yang mau dihilangkan: '))                            
                        continue
                    break
            except ValueError:
                print("Input harus berupa angka!")
                continue
            kursor.execute(query3, (admin_input,))
            conn.commit()
            print('Penghapusan Berhasil')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        finally:
            kursor.close()
            conn.close()

def kembali_produk(idakun):
    kursor, conn = koneksiDB()
    query1 = "select id_produk, nama_produk, harga, stock from produk where status_produk = 'Tidak Aktif' order by id_produk;"
    query2 = "select id_produk from produk where status_produk = 'Tidak Aktif' order by id_produk;"
    query3 = "update produk set status_produk = 'Aktif' where id_produk = %s"
    while True:
        try:
            kursor.execute(query1)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print(tabulate(data, headers=header, tablefmt='psql'))
            kursor.execute(query2)
            data = kursor.fetchall()
            data_list = [i[0] for i in data]
            print('===PILIH ID PRODUK YANG MAU DIUBAH===')
            for i in data:
                print(f'id karyawan {i[0]}')
            while True:
                try:
                    admin_input = int(input('Pilih Id Produk yang mau dikembalikan: '))
                    while True:
                        if admin_input not in data_list:
                            print('Id Karyawan yang anda masukkan salah')
                            admin_input = int(input('Pilih Id Produk yang mau dikembalikan: '))
                            continue
                        break
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
                break
            kursor.execute(query3, (admin_input,))
            conn.commit()
            print('Pengembalian Berhasil')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        finally:
            kursor.close()
            conn.close()

def tambah_produk(idakun):
    kursor, conn = koneksiDB()
    nama_produk = input('Masukkan Nama Produk Yang Mau Ditambahkan: ')
    harga = input('Masukkan Harga Produk: ')
    query = "insert into produk (nama_produk, harga, stock, status_produk) values (%s, %s, 0, 'Aktif)"
    while True:
        try:
            nama_produk = cek_nama_produk(nama_produk)
            harga = cek_harga(harga)
            kursor.execute(query)
            conn.commit()
            print('Penambahan Produk Berhasil')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
        finally:
            kursor.close()
            conn.close()

def ubah_harga(idakun):
    kursor, conn = koneksiDB()
    query1 = "select id_produk, nama_produk, harga from produk where status_produk = 'Aktif' order by id_produk;"
    query2 = "update produk set harga = %s where id_produk = %s"
    query3 = "select id_produk from produk where status_produk = 'Aktif' order by id_produk;"
    while True:
        try:
            harga_admin = 0
            kursor.execute(query1)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print (tabulate(data, headers=header, tablefmt='psql'))
            kursor.execute(query3)
            data = kursor.fetchall()
            data_list = [i[0] for i in data]
            print('======Id Produk======')
            for i in data:
                print(f'id Produk {i[0]}')
            try:
                admin_input = int(input('Pilih Id Produk yang mau diubah Harganya: '))
                while True:
                    if admin_input not in data_list:
                        print('Id Produk yang anda masukkan salah')
                        admin_input = int(input('Pilih Id Produk yang mau diubah Harganya: '))
                        continue
                    break
            except ValueError:
                print("Input harus berupa angka!")
                continue
            harga_admin = input('Masukkan harga Terbaru: ')
            while True:
                try:
                    if not harga_admin.strip():
                        print("Harga tidak boleh kosong atau spasi saja!")
                        harga_admin = input("Masukkan harga Terbaru: ")
                        continue
                    harga_admin = int(harga_admin)
                    if harga_admin < 1000:
                        print('Harga Terlalu Rendah')
                        harga_admin = input("Masukkan harga Terbaru: ")
                        continue
                    break
                except:
                    print('Harga Harus Berupa Angka')
                    harga_admin = input("Masukkan harga Terbaru: ")
            kursor.execute(query2, (harga_admin, admin_input))
            conn.commit()
            print('Perubahan Harga Berhasil')
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
            continue
        ubah_lagi = questionary.select(
        "Apakah Mau Lanjut Ubah Harga:",
        choices=["Lanjut", "Tidak"]
        ).ask()
        if ubah_lagi == 'Lanjut':
            continue
        elif ubah_lagi == 'Tidak':
            break
    kursor.close()
    conn.close()

def menu_customer(idakun):
    kursor, conn = koneksiDB()
    query1 = "select id_produk, nama_produk, harga from produk where status_produk = 'Aktif order by id_produk'"
    while True:
        try:
            kursor.execute(query1)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print (tabulate(data, headers=header, tablefmt='psql'))
            print("=====Menu Customer=====")
            pilih_menu = questionary.select(
            "Mau tambah Produk:",
            choices=["Pilih Produk", "Lihat Pesanan", "Keluar"]
            ).ask()
            if pilih_menu == "Pilih Produk":
                pesanan_customer(idakun)
                continue
            elif pilih_menu == "Lihat Pesanan":
                continue
            elif pilih_menu == "Keluar":
                break
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
            continue

def pesanan_customer(idakun):
    kursor, conn = koneksiDB()
    query1 = "select id_produk, nama_produk, harga from produk where status_produk = 'Aktif' order by id_produk"
    query2 = "select id_produk from produk where status_produk = 'Aktif' order by id_produk"
    query3 = "select nama_produk from produk where id_produk = %s"
    query4 = "select stock from produk where id_produk = %s"
    produk_dipesan = []
    id_produk = []
    jumlah = []
    sisa_stock = []
    while True:
        try:
            kursor.execute(query1)
            data = kursor.fetchall()
            header= [d[0]for d in kursor.description]
            print (tabulate(data, headers=header, tablefmt='psql'))
            kursor.execute(query2)
            data = kursor.fetchall()
            data_list = [i[0] for i in data]
            print(f"Produk yang Sudah Dipesan : {produk_dipesan}")
            print(f"Jumlah yang Sudah Dipesan : {jumlah}")
            print('=====PILIH ID PRODUK YANG MAU DIPESAN=====')
            while True:
                try:
                    customer_input = int(input('Masukkan ID Produk Yang Mau Dibeli >> '))
                    if customer_input not in data_list:
                        print('Inputan ID Produk Tidak valid')
                        continue
                    if customer_input in id_produk:
                        print('ID Produk Sudah Dipilih')
                        continue
                    break
                except:
                    print("Input Harus Berupa ID Produk(angka)")
                    continue
            id_produk.append(customer_input)
            kursor.execute(query3, (customer_input,))
            data1 = kursor.fetchone()
            produk_dipesan.append(data1[0])
            kursor.execute(query4, (customer_input,))
            data2 = kursor.fetchone()
            jumlah_stock = data2[0]
            while True:
                try:
                    banyak_produk = int(input('Masukkan Berapa Banyak yang mau dibeli >> '))
                    if banyak_produk == 0:
                        print('Pesanan Tidak Boleh 0')
                        continue
                    if banyak_produk>jumlah_stock:
                        print('Stock Tiidak Mencukupi')
                        continue
                    break
                except:
                    print("Input Harus Berupa Angka")
                    continue
            jumlah.append(banyak_produk)
            data_update = jumlah_stock - banyak_produk
            sisa_stock.append(data_update)
            lanjut_pilih = questionary.select(
            "Mau tambah Produk:",
            choices=["iya,Pilih lagi", "Tidak,Cukup sudah"]
            ).ask()
            if lanjut_pilih == "iya,Pilih lagi":
                continue
            elif lanjut_pilih == "Tidak,Cukup sudah":
                transaksi_pesanan(idakun, produk_dipesan, jumlah, sisa_stock)
                break
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
            continue
    kursor.close()
    conn.close()
        
def transaksi_pesanan(idakun, produk_dipesan, jumlah, sisa_stock):
    kursor, conn = koneksiDB()
    query = "select harga from produk where nama_produk = %s"
    try:
        banyak = len(produk_dipesan)
        simpan_pesanan = []
        harga_pesanan = 0
        for i in range(banyak):
            pesanan = [produk_dipesan[i], jumlah[i]]
            simpan_pesanan.append(pesanan)
            kursor.execute(query, (produk_dipesan[i],))
            data = kursor.fetchone()
            harga_produk = data[0]
            harga_pesanan = harga_pesanan + (harga_produk * jumlah[i])
        print(tabulate(simpan_pesanan, headers =["Produk","jumlah"]))
        print(f'Total Harga Pesanan = {harga_pesanan}')
        customer_pilih = questionary.select(
            "Apakah sudaah benar Pesanan anda:",
            choices=["iya,Sudah Benar", "Tidak"]
            ).ask()
        if customer_pilih == "iya,Sudah Benar":
            nama_pemesan = input('Masukkan Pesanan Atas Nama >> ')
            nama_pemesan = cek_nama(nama_pemesan)
            alamat_pesanan = 
            simpan_data(idakun, produk_dipesan, jumlah, sisa_stock, nama_pemesan)
        elif customer_pilih == "Tidak":
            pesanan_customer(idakun)
    except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
    kursor.close()
    conn.close()

            






#bagaimana jika melebihi stock





kursor.execute(query1)
data = kursor.fetchall()
header= [d[0]for d in kursor.description]
            print (tabulate(data, headers=header, tablefmt='psql'))
            kursor.execute(query2)
            data = kursor.fetchall()
            data_list = [i[0] for i in data]
            print('======Id Karyawan======')
            for i in data:
                print(f'id karyawan {i[0]}')
            while True:
                try:
                    admin_input = int(input('Pilih Id Produk yang mau dihilangkan: '))
                    while True:
                        if admin_input not in data_list:
                            print('Id Karyawan yang anda masukkan salah')
                            admin_input = int(input('Pilih Id Produk yang mau dihilangkan: '))
                            continue
                        break
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
                break
            kursor.execute(query3, (admin_input,))
            conn.commit()
            print('Pemecatan Berhasil')









































# print('berhasil')
# cursor = conn.cursor()
# query = "SELECT * FROM public.karyawan;"
# cursor.execute(query)
# data = cursor.fetchall()
# for row in data:
#     print(row)

# cursor.close()
# conn.close()
# query = "SELECT * FROM public.karyawan;"
# df = pd.read_sql(query, conn)
# conn.close()
# print(df.head())