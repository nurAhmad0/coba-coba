import psycopg2 
import pandas as pd
from tabulate import tabulate

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
                logincustomer()
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
    while True:
        kursor, conn = koneksiDB()
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

def logincustomer():
    while True:
        kursor, conn = koneksiDB()
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

def loginkaryawan():
    while True:
        kursor, conn = koneksiDB()
        username_karyawan = input('Masukkan Username Anda: ')
        password_karyawan = input('Masukkan Password Anda: ')
        query = "select id_akun from akun where username = %s and password = %s and role_id_role = 3"
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

def cek_username(username):
    kursor, conn = koneksiDB()
    simbol =['!','@','#','$','%','^','&','*','(',')',',']
    while True:
        try:
            query = "select * from akun where username = %s"
            kursor.execute(query, (username))
            cocok = kursor.fetchone()
            if cocok is not none:
                print('Username Tidak Sesuai')
                username = input('Masukkan Username: ')
                continue
            if any(s in username for s in simbol):
                print('Username Tidak Sesuai')
                username = input('Masukkan Username: ')
                continue
        break
    return username

def cek_password(password):
    while True:
        if len(password) < 6:
            print('Password  Minimal 6 Karater')
            password = input('Masukkan Password Anda: ')
            continue
        if password.isalpha() == True:
            print('Password Gabungan Huruf dan Angka')
            password = input('Masukkan Password Anda: ')
            continue
        if password.isnumeric() == True:
            print('Password Gabungan Huruf dan Angka')
            password = input('Masukkan Password Anda: ')
            continue
        break
    return password

def cek_email(email):
    while True:
        try:
            if email.endwith('@gmail.com') == False:
                print('Email harus mengunakan @gmail.com')
                email = input('Masukkan Email Anda: ')
                continue
            break
        except:
            print('Inputan Tidak Valid')
    return email

def cek_no_telp(no_telp):
    while True:
        try:
            if not (len(no_telp) >= 10 and len(no_telp) <= 13):
                print('Nomer Telp harus 10-13 digit')
                no_telp = input('Masukkan NO TELPON Anda: ')
                continue
            if no_telp.isalpha() == False:
                print('Nomer Telp harus angka semua')
                no_telp = input('Masukkan NO TELPON Anda: ')
                continue
            break
        except:
            print('Inputan Tidak Valid')
    return no_telp



def buat_akun_customer():
    while True:
        kursor, conn = koneksiDB()
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







































konto










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

