
# --------------------
# Membuat kode start dan exit
# --------------
def program_bodywise():
    nama = input("\nKetik 'start' untuk memulai: ")
    if nama.lower() == "exit":
        return "exit"
    nama = nama.title()


# --------------------
# Meminta nilai input nama dari pengguna
# --------------------
    nama = input("\nMasukkan nama anda: ")
    nama = nama.title()


# --------------------
# Membuat variabel kategori usia
# --------------------
    kategori_usia_1 = "Kategori anda adalah bayi"
    kategori_usia_2 = "Kategori anda adalah balita"
    kategori_usia_3 = "Kategori anda adalah anak-anak"
    kategori_usia_4 = "Kategori anda adalah remaja"
    kategori_usia_5 = "Kategori anda adalah dewasa"
    kategori_usia_6 = "Kategori anda adalah lansia"


# --------------------
# Meminta nilai input umur dari pengguna
# --------------------
    while True:
        try:
             umur = int(input("\nMasukkan umur anda: "))
        except ValueError:
            print("\nMaaf, input harus angka bulat positif, bukan huruf!")
            continue


# --------------------
# Membuat conditional statemen untuk kategori usia
# --------------------
        if umur > 0 and umur <= 1:
            kategori = kategori_usia_1
            break
        elif umur >= 2 and umur <=5:
            kategori = kategori_usia_2
            break
        elif umur >= 6 and umur <= 10:
            kategori = kategori_usia_3
            break
        elif umur >= 11 and umur <= 19:
            kategori = kategori_usia_4
            break
        elif umur >= 20 and umur <= 60:
            kategori = kategori_usia_5
            break
        elif umur >= 61 and umur <= 100:
            kategori = kategori_usia_6
            break
        else:
            print("\nMaaf, hanya bisa memasukkan bilangan bulat positif(1-100)")
            continue


# --------------------
# Meminta nilai input gender dari pengguna
# --------------------
    while True:
        gender= input("\nMasukkan gender anda: ")
        gender = gender.lower()
        if gender == "laki-laki" or gender == "perempuan":
            break
        else:
            print("\nMaaf, hanya bisa memasukkan gender laki-laki dan perempuan")
            continue


# --------------------
# Meminta nilai input berat badan dari pengguna
# --------------------
    while True:
        try:
            berat_badan = float(input("\nMasukkan berat badan anda (kg): "))
            if berat_badan < 0:
                print("\nMaaf, berat badan tidak boleh negatif!")
                continue 
            if berat_badan == 0:
                print("\nMaaf, berat badan tidak boleh 0!")
                continue  
            break 
        except ValueError:
            print("\nMaaf, input harus angka, bukan huruf!")


# --------------------
# Meminta nilai input tinggi badan dari pengguna
# --------------------
    while True:
        try:
            tinggi_badan = float(input("\nMasukkan tinggi badan anda(cm): "))        
            if tinggi_badan < 0:
                print("\nMaaf, tinggi badan tidak boleh negatif!")
                continue
            if tinggi_badan == 0:
                print("\nMaaf, tinggi badan tidak boleh 0!")
                continue
            break  
        except ValueError:
            print("nMaaf, input harus bilangan positif, bukan huruf!")


# --------------------
# Membuat variabel BMI
# --------------------
    tinggi_badan = tinggi_badan / 100
    BMI = berat_badan / (tinggi_badan ** 2)


# --------------------
# Membuat variabel untuk z_score
# --------------------
    bmi_z = -4
    bmi_a = -3
    bmi_b = -2
    bmi_c = -1
    bmi_d = 0
    bmi_e = 1
    bmi_f = 2
    bmi_g = 3
    bmi_h = 4


# --------------------
# Membuat conditional statemen untuk z_score
# --------------------
    if kategori == "Kategori anda adalah bayi" and gender == "laki-laki" and umur == 1:
        if BMI < 12.7:
            z_score = bmi_z
        elif BMI >= 12.7 and BMI <= 13.5:
            z_score = bmi_a
        elif BMI > 13.5 and BMI <= 14.1:
            z_score = bmi_b
        elif BMI > 14.1 and BMI <= 15.2:
            z_score = bmi_c
        elif BMI > 15.2 and BMI <= 16.45:
            z_score = bmi_d
        elif BMI > 16.45 and BMI <= 17.85:
            z_score = bmi_e
        elif BMI > 17.85 and BMI <= 19.45:
            z_score = bmi_f
        elif BMI > 19.45 and BMI <= 20.3:
            z_score = bmi_g
        elif BMI > 20.3:
            z_score = bmi_h
    elif kategori == "Kategori anda adalah bayi" and gender == "perempuan" and umur == 1:
        if BMI < 12.2:
            z_score = bmi_z
        elif BMI >= 12.2 and BMI <= 12.65:
            z_score = bmi_a
        elif BMI > 12.65 and BMI <= 13.65:
            z_score = bmi_b
        elif BMI > 13.65 and BMI <= 14.8:
            z_score = bmi_c
        elif BMI > 14.8 and BMI <= 16.15:
            z_score = bmi_d
        elif BMI > 16.15 and BMI <= 17.7:
            z_score = bmi_e
        elif BMI > 17.7 and BMI <= 19.45:
            z_score = bmi_f
        elif BMI > 19.45 and BMI <= 20.4:
            z_score = bmi_g
        elif BMI > 20.4:
            z_score = bmi_h         
    elif kategori == "Kategori anda adalah balita" and gender == "laki-laki" and umur == 2:
        if BMI < 12.9:
            z_score = bmi_z
        elif BMI >= 12.9 and BMI <= 13.35:
            z_score = bmi_a
        elif BMI > 13.35 and BMI <= 14.30:
            z_score = bmi_b
        elif BMI > 14.30 and BMI <= 15.40:
            z_score = bmi_c
        elif BMI > 15.40 and BMI <= 16.65:
            z_score = bmi_d
        elif BMI > 16.65 and BMI <= 18.10:
            z_score = bmi_e
        elif BMI > 18.10 and BMI <= 19.75:
            z_score = bmi_f
        elif BMI > 19.75 and BMI <= 20.6:
            z_score = bmi_g
        elif BMI > 20.6:
            z_score = bmi_h  
    elif kategori == "Kategori anda adalah balita" and gender == "perempuan" and umur == 2:
        if BMI < 12.4:
            z_score = bmi_z
        elif BMI >= 12.4 and BMI <= 12.85:
            z_score = bmi_a
        elif BMI > 12.85 and BMI <= 13.85:
            z_score = bmi_b
        elif BMI > 13.85 and BMI <= 15.05:
            z_score = bmi_c
        elif BMI > 15.05 and BMI <= 16.4:
            z_score = bmi_d
        elif BMI > 16.4 and BMI <= 17.9:
            z_score = bmi_e
        elif BMI > 17.9 and BMI <= 19.65:
            z_score = bmi_f
        elif BMI > 19.65 and BMI <= 20.6:
            z_score = bmi_g
        elif BMI > 20.6:
            z_score = bmi_h    
    elif kategori == "Kategori anda adalah balita" and gender == "laki-laki" and umur == 3:
        if BMI < 12.4:
            z_score = bmi_z
        elif BMI >= 12.4 and BMI <= 12.9:
            z_score = bmi_a
        elif BMI > 12.9 and BMI <= 13.9:
            z_score = bmi_b
        elif BMI > 13.9 and BMI <= 15.0:
            z_score = bmi_c
        elif BMI > 15.0 and BMI <= 16.25:
            z_score = bmi_d
        elif BMI > 16.25 and BMI <= 17.65:
            z_score = bmi_e
        elif BMI > 17.65 and BMI <= 19.2:
            z_score = bmi_f
        elif BMI > 19.2 and BMI <= 20.0:
            z_score = bmi_g
        elif BMI > 20.0:
            z_score = bmi_h                       
    elif kategori == "Kategori anda adalah balita" and gender == "perempuan" and umur == 3:
        if BMI < 12.1:
            z_score = bmi_z
        elif BMI >= 12.1 and BMI <= 12.6:
            z_score = bmi_a
        elif BMI > 12.6 and BMI <= 13.65:
            z_score = bmi_b
        elif BMI > 13.65 and BMI <= 14.8:
            z_score = bmi_c
        elif BMI > 14.8 and BMI <= 16.1:
            z_score = bmi_d
        elif BMI > 16.1 and BMI <= 17.6:
            z_score = bmi_e
        elif BMI > 17.6 and BMI <= 19.35:
            z_score = bmi_f
        elif BMI > 19.35 and BMI <= 20.3:
            z_score = bmi_g
        elif BMI > 20.3:
            z_score = bmi_h    
    elif kategori == "Kategori anda adalah balita" and gender == "laki-laki" and umur == 4:
        if BMI < 12.1:
            z_score = bmi_z
        elif BMI >= 12.1 and BMI <= 12.6:
            z_score = bmi_a
        elif BMI > 12.6 and BMI <= 13.6:
            z_score = bmi_b
        elif BMI > 13.6 and BMI <= 14.7:
            z_score = bmi_c
        elif BMI > 14.7 and BMI <= 16.0:
            z_score = bmi_d
        elif BMI > 16.0 and BMI <= 17.45:
            z_score = bmi_e
        elif BMI > 17.45 and BMI <= 19.05:
            z_score = bmi_f
        elif BMI > 19.05 and BMI <= 19.9:
            z_score = bmi_g
        elif BMI > 19.9:
            z_score = bmi_h     
    elif kategori == "Kategori anda adalah balita" and gender == "perempuan" and umur == 4:
        if BMI < 11.8:
            z_score = bmi_z
        elif BMI >= 11.8 and BMI <= 12.3:
            z_score = bmi_a
        elif BMI > 12.3 and BMI <= 13.4:
            z_score = bmi_b
        elif BMI > 13.4 and BMI <= 14.65:
            z_score = bmi_c
        elif BMI > 14.65 and BMI <= 16.05:
            z_score = bmi_d
        elif BMI > 16.05 and BMI <= 17.65:
            z_score = bmi_e
        elif BMI > 17.65 and BMI <= 19.55:
            z_score = bmi_f
        elif BMI > 19.55 and BMI <= 20.6:
            z_score = bmi_g
        elif BMI > 20.6:
            z_score = bmi_h     
    elif kategori == "Kategori anda adalah balita" and gender == "laki-laki" and umur == 5:
        if BMI < 12.0:
            z_score = bmi_z
        elif BMI >= 12.0 and BMI <= 12.45:
            z_score = bmi_a
        elif BMI > 12.45 and BMI <= 13.45:
            z_score = bmi_b
        elif BMI > 13.45 and BMI <= 14.6:
            z_score = bmi_c
        elif BMI > 14.6 and BMI <= 15.9:
            z_score = bmi_d
        elif BMI > 15.9 and BMI <= 17.45:
            z_score = bmi_e
        elif BMI > 17.45 and BMI <= 19.3:
            z_score = bmi_f
        elif BMI > 19.3 and BMI <= 20.3:
            z_score = bmi_g
        elif BMI > 20.3:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah balita" and gender == "perempuan" and umur == 5:
        if BMI < 11.6:
            z_score = bmi_z
        elif BMI >= 11.6 and BMI <= 12.15:
            z_score = bmi_a
        elif BMI > 12.15 and BMI <= 13.3:
            z_score = bmi_b
        elif BMI > 13.3 and BMI <= 14.6:
            z_score = bmi_c
        elif BMI > 14.6 and BMI <= 16.1:
            z_score = bmi_d
        elif BMI > 16.1 and BMI <= 17.85:
            z_score = bmi_e
        elif BMI > 17.85 and BMI <= 19.95:
            z_score = bmi_f
        elif BMI > 19.95 and BMI <= 21.1:
            z_score = bmi_g
        elif BMI > 21.1:
            z_score = bmi_h   

    if kategori == "Kategori anda adalah anak-anak" and gender == "laki-laki" and umur == 6:
        if BMI < 12.1:
            z_score = bmi_z
        elif BMI >= 12.1 and BMI <= 12.55:
            z_score = bmi_a
        elif BMI > 12.55 and BMI <= 13.55:
            z_score = bmi_b
        elif BMI > 13.55 and BMI <= 14.7:
            z_score = bmi_c
        elif BMI > 14.7 and BMI <= 16.05:
            z_score = bmi_d
        elif BMI > 16.05 and BMI <= 17.65:
            z_score = bmi_e
        elif BMI > 17.65 and BMI <= 19.6:
            z_score = bmi_f
        elif BMI > 19.6 and BMI <= 20.7:
            z_score = bmi_g
        elif BMI > 20.7:
            z_score = bmi_h   
    elif kategori == "Kategori anda adalah anak-anak" and gender == "laki-laki" and umur == 7:
        if BMI < 12.3:
            z_score = bmi_z
        elif BMI >= 12.3 and BMI <= 12.7:
            z_score = bmi_a
        elif BMI > 12.7 and BMI <= 13.65:
            z_score = bmi_b
        elif BMI > 13.65 and BMI <= 14.85:
            z_score = bmi_c
        elif BMI > 14.85 and BMI <= 16.25:
            z_score = bmi_d
        elif BMI > 16.25 and BMI <= 18.0:
            z_score = bmi_e
        elif BMI > 18.0 and BMI <= 20.3:
            z_score = bmi_f
        elif BMI > 20.3 and BMI <= 21.6:
            z_score = bmi_g
        elif BMI > 21.6:
            z_score = bmi_h     
    elif kategori == "Kategori anda adalah anak-anak" and gender == "laki-laki" and umur == 8:
        if BMI < 12.4:
            z_score = bmi_z
        elif BMI >= 12.4 and BMI <= 12.85:
            z_score = bmi_a
        elif BMI > 12.85 and BMI <= 13.85:
            z_score = bmi_b
        elif BMI > 13.85 and BMI <=15.05:
            z_score = bmi_c
        elif BMI > 15.05 and BMI <= 16.55:
            z_score = bmi_d
        elif BMI > 16.55 and BMI <= 18.55:
            z_score = bmi_e
        elif BMI > 18.55 and BMI <= 21.25:
            z_score = bmi_f
        elif BMI > 21.25 and BMI <= 22.8:
            z_score = bmi_g
        elif BMI > 22.8:
            z_score = bmi_h  
    elif kategori == "Kategori anda adalah anak-anak" and gender == "laki-laki" and umur == 9:
        if BMI < 12.6:
            z_score = bmi_z
        elif BMI >= 12.6 and BMI <= 13.05:
            z_score = bmi_a
        elif BMI > 13.05 and BMI <= 14.05:
            z_score = bmi_b
        elif BMI > 14.05 and BMI <= 15.30:
            z_score = bmi_c
        elif BMI > 15.30 and BMI <= 16.95:
            z_score = bmi_d
        elif BMI > 16.95 and BMI <= 19.20:
            z_score = bmi_e
        elif BMI > 19.20 and BMI <= 22.40:
            z_score = bmi_f
        elif BMI > 22.40 and BMI <= 24.3:
            z_score = bmi_g
        elif BMI > 24.3:
            z_score = bmi_h            
    elif kategori == "Kategori anda adalah anak-anak" and gender == "laki-laki" and umur == 10:
        if BMI < 12.8:
            z_score = bmi_z
        elif BMI >= 12.8 and BMI <= 13.25:
            z_score = bmi_a
        elif BMI > 13.25 and BMI <= 14.30:
            z_score = bmi_b
        elif BMI > 14.30 and BMI <= 15.65:
            z_score = bmi_c
        elif BMI > 15.65 and BMI <= 17.45:
            z_score = bmi_d
        elif BMI > 17.45 and BMI <= 19.95:
            z_score = bmi_e
        elif BMI > 19.95 and BMI <= 23.75:
            z_score = bmi_f
        elif BMI > 23.75 and BMI <= 26.1:
            z_score = bmi_g
        elif BMI > 26.1:
            z_score = bmi_h   

    if kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 11:
        if BMI < 13.1:
            z_score = bmi_z
        elif BMI >= 13.1 and BMI <= 13.6:
            z_score = bmi_a
        elif BMI > 13.6 and BMI <= 14.7:
            z_score = bmi_b
        elif BMI > 14.7 and BMI <= 16.1:
            z_score = bmi_c
        elif BMI > 16.1 and BMI <= 18.05:
            z_score = bmi_d
        elif BMI > 18.05 and BMI <= 20.85:
            z_score = bmi_e
        elif BMI > 20.85 and BMI <= 25.25:
            z_score = bmi_f
        elif BMI > 25.25 and BMI <= 28.0:
            z_score = bmi_g
        elif BMI > 28.0:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 12:
        if BMI < 13.4:
            z_score = bmi_z
        elif BMI >= 13.4 and BMI <= 13.95:
            z_score = bmi_a
        elif BMI > 13.95 and BMI <= 15.15:
            z_score = bmi_b
        elif BMI > 15.15 and BMI <= 16.65:
            z_score = bmi_c
        elif BMI > 16.65 and BMI <= 18.70:
            z_score = bmi_d
        elif BMI > 18.70 and BMI <= 21.75:
            z_score = bmi_e
        elif BMI > 21.75 and BMI <= 26.80:
            z_score = bmi_f
        elif BMI > 26.80 and BMI <= 30.0:
            z_score = bmi_g
        elif BMI > 30.0:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 13:
        if BMI < 13.8:
            z_score = bmi_z
        elif BMI >= 13.8 and BMI <= 14.35:
            z_score = bmi_a
        elif BMI > 14.35 and BMI <= 15.65:
            z_score = bmi_b
        elif BMI > 15.65 and BMI <= 17.30:
            z_score = bmi_c
        elif BMI > 17.30 and BMI <= 19.50:
            z_score = bmi_d
        elif BMI > 19.50 and BMI <= 22.80:
            z_score = bmi_e
        elif BMI > 22.80 and BMI <= 28.25:
            z_score = bmi_f
        elif BMI > 28.25 and BMI <= 31.7:
            z_score = bmi_g
        elif BMI > 31.7:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 14:
        if BMI < 14.3:
            z_score = bmi_z
        elif BMI >= 14.3 and BMI <= 14.90:
            z_score = bmi_a
        elif BMI > 14.90 and BMI <= 16.25:
            z_score = bmi_b
        elif BMI > 16.25 and BMI <= 18.0:
            z_score = bmi_c
        elif BMI > 18.0 and BMI <= 20.40:
            z_score = bmi_d
        elif BMI > 20.40 and BMI <= 23.85:
            z_score = bmi_e
        elif BMI > 23.85 and BMI <= 29.50:
            z_score = bmi_f
        elif BMI > 29.50 and BMI <= 33.1:
            z_score = bmi_g
        elif BMI > 33.1:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 15:
        if BMI < 14.7:
            z_score = bmi_z
        elif BMI >= 14.7 and BMI <= 15.35:
            z_score = bmi_a
        elif BMI > 15.35 and BMI <= 16.80:
            z_score = bmi_b
        elif BMI > 16.80 and BMI <= 18.70:
            z_score = bmi_c
        elif BMI > 18.70 and BMI <= 21.25:
            z_score = bmi_d
        elif BMI > 21.25 and BMI <= 24.85:
            z_score = bmi_e
        elif BMI > 24.85 and BMI <= 30.55:
            z_score = bmi_f
        elif BMI > 30.55 and BMI <= 34.1:
            z_score = bmi_g
        elif BMI > 34.1:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 16:
        if BMI < 15.1:
            z_score = bmi_z
        elif BMI >= 15.1 and BMI <= 15.80:
            z_score = bmi_a
        elif BMI > 15.80 and BMI <= 17.35:
            z_score = bmi_b
        elif BMI > 17.35 and BMI <= 19.35:
            z_score = bmi_c
        elif BMI > 19.35 and BMI <= 22.0:
            z_score = bmi_d
        elif BMI > 22.0 and BMI <= 25.70:
            z_score = bmi_e
        elif BMI > 25.70 and BMI <= 31.35:
            z_score = bmi_f
        elif BMI > 31.35 and BMI <= 34.8:
            z_score = bmi_g
        elif BMI > 34.8:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 17:
        if BMI < 15.4:
            z_score = bmi_z
        elif BMI >= 15.4 and BMI <= 16.15:
            z_score = bmi_a
        elif BMI > 16.15 and BMI <= 17.85:
            z_score = bmi_b
        elif BMI > 17.85 and BMI <= 19.95:
            z_score = bmi_c
        elif BMI > 19.95 and BMI <= 22.70:
            z_score = bmi_d
        elif BMI > 22.70 and BMI <= 26.45:
            z_score = bmi_e
        elif BMI > 26.45 and BMI <= 31.90:
            z_score = bmi_f
        elif BMI > 31.90 and BMI <= 35.2:
            z_score = bmi_g
        elif BMI > 35.2:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 18:
        if BMI < 15.7:
            z_score = bmi_z
        elif BMI >= 15.7 and BMI <= 16.50:
            z_score = bmi_a
        elif BMI > 16.50 and BMI <= 18.25:
            z_score = bmi_b
        elif BMI > 18.25 and BMI <= 20.45:
            z_score = bmi_c
        elif BMI > 20.45 and BMI <= 23.30:
            z_score = bmi_d
        elif BMI > 23.30 and BMI <= 27.05:
            z_score = bmi_e
        elif BMI > 27.05 and BMI <= 32.30:
            z_score = bmi_f
        elif BMI > 32.30 and BMI <= 35.4:
            z_score = bmi_g
        elif BMI > 35.4:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 19:
        if BMI < 15.9:
            z_score = bmi_z
        elif BMI >= 15.9 and BMI <= 16.75:
            z_score = bmi_a
        elif BMI > 16.75 and BMI <= 18.60:
            z_score = bmi_b
        elif BMI > 18.60 and BMI <= 20.90:
            z_score = bmi_c
        elif BMI > 20.90 and BMI <= 23.80:
            z_score = bmi_d
        elif BMI > 23.80 and BMI <= 27.55:
            z_score = bmi_e
        elif BMI > 27.55 and BMI <= 32.60:
            z_score = bmi_f
        elif BMI > 32.60 and BMI <= 35.5:
            z_score = bmi_g
        elif BMI > 35.5:
            z_score = bmi_h  

    if kategori == "Kategori anda adalah anak-anak" and gender == "perempuan" and umur == 6:
        if BMI < 11.7:
            z_score = bmi_z
        elif BMI >= 11.7 and BMI <= 12.2:
            z_score = bmi_a
        elif BMI > 12.2 and BMI <= 13.3:
            z_score = bmi_b
        elif BMI > 13.3 and BMI <= 14.6:
            z_score = bmi_c
        elif BMI > 14.6 and BMI <= 16.15:
            z_score = bmi_d
        elif BMI > 16.15 and BMI <= 18.1:
            z_score = bmi_e
        elif BMI > 18.1 and BMI <= 20.65:
            z_score = bmi_f
        elif BMI > 20.65 and BMI <= 22.1:
            z_score = bmi_g
        elif BMI > 22.1:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah anak-anak" and gender == "perempuan" and umur == 7:
        if BMI < 11.8:
            z_score = bmi_z
        elif BMI >= 11.8 and BMI <= 12.25:
            z_score = bmi_a
        elif BMI > 12.25 and BMI <= 13.3:
            z_score = bmi_b
        elif BMI > 13.3 and BMI <= 14.65:
            z_score = bmi_c
        elif BMI > 14.65 and BMI <= 16.35:
            z_score = bmi_d
        elif BMI > 16.35 and BMI <= 18.55:
            z_score = bmi_e
        elif BMI > 18.55 and BMI <= 21.55:
            z_score = bmi_f
        elif BMI > 21.55 and BMI <= 23.3:
            z_score = bmi_g
        elif BMI > 23.3:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah anak-anak" and gender == "perempuan" and umur == 8:
        if BMI < 11.9:
            z_score = bmi_z
        elif BMI >= 11.9 and BMI <= 12.4:
            z_score = bmi_a
        elif BMI > 12.4 and BMI <= 13.5:
            z_score = bmi_b
        elif BMI > 13.5 and BMI <= 14.9:
            z_score = bmi_c
        elif BMI > 14.9 and BMI <= 16.7:
            z_score = bmi_d
        elif BMI > 16.7 and BMI <= 19.15:
            z_score = bmi_e
        elif BMI > 19.15 and BMI <= 22.7:
            z_score = bmi_f
        elif BMI > 22.7 and BMI <= 24.8:
            z_score = bmi_g
        elif BMI > 24.8:
            z_score = bmi_h     
    elif kategori == "Kategori anda adalah anak-anak" and gender == "perempuan" and umur == 9:
        if BMI < 12.1:
            z_score = bmi_z
        elif BMI >= 12.1 and BMI <= 12.6:
            z_score = bmi_a
        elif BMI > 12.6 and BMI <= 13.75:
            z_score = bmi_b
        elif BMI > 13.75 and BMI <= 15.25:
            z_score = bmi_c
        elif BMI > 15.25 and BMI <= 17.2:
            z_score = bmi_d
        elif BMI > 17.2 and BMI <= 19.9:
            z_score = bmi_e
        elif BMI > 19.9 and BMI <= 24.0:
            z_score = bmi_f
        elif BMI > 24.0 and BMI <= 26.5:
            z_score = bmi_g
        elif BMI > 26.5:
            z_score = bmi_h     
    elif kategori == "Kategori anda adalah anak-anak" and gender == "perempuan" and umur == 10:
        if BMI < 12.4:
            z_score = bmi_z
        elif BMI >= 12.4 and BMI <= 12.95:
            z_score = bmi_a
        elif BMI > 12.95 and BMI <= 14.15:
            z_score = bmi_b
        elif BMI > 14.15 and BMI <= 15.7:
            z_score = bmi_c
        elif BMI > 15.7 and BMI <= 17.8:
            z_score = bmi_d
        elif BMI > 17.8 and BMI <= 20.8:
            z_score = bmi_e
        elif BMI > 20.8 and BMI <= 25.5:
            z_score = bmi_f
        elif BMI > 25.5 and BMI <= 28.4:
            z_score = bmi_g
        elif BMI > 28.4:
            z_score = bmi_h 

    if kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 11:
        if BMI < 12.7:
            z_score = bmi_z
        elif BMI >= 12.7 and BMI <= 13.3:
            z_score = bmi_a
        elif BMI > 13.3 and BMI <= 14.6:
            z_score = bmi_b
        elif BMI > 14.6 and BMI <= 16.25:
            z_score = bmi_c
        elif BMI > 16.25 and BMI <= 18.55:
            z_score = bmi_d
        elif BMI > 18.55 and BMI <= 21.8:
            z_score = bmi_e
        elif BMI > 21.8 and BMI <= 26.95:
            z_score = bmi_f
        elif BMI > 26.95 and BMI <= 30.2:
            z_score = bmi_g
        elif BMI > 30.2:
            z_score = bmi_h        
    elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 12:
        if BMI < 13.2:
            z_score = bmi_z
        elif BMI >= 13.2 and BMI <= 13.8:
            z_score = bmi_a
        elif BMI > 13.8 and BMI <= 15.2:
            z_score = bmi_b
        elif BMI > 15.2 and BMI <= 17.0:
            z_score = bmi_c
        elif BMI > 17.0 and BMI <= 19.4:
            z_score = bmi_d
        elif BMI > 19.4 and BMI <= 22.9:
            z_score = bmi_e
        elif BMI > 22.9 and BMI <= 28.45:
            z_score = bmi_f
        elif BMI > 28.45 and BMI <= 31.9:
            z_score = bmi_g
        elif BMI > 31.9:
            z_score = bmi_h                
    elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 13:
        if BMI < 13.6:
            z_score = bmi_z
        elif BMI >= 13.6 and BMI <= 14.25:
            z_score = bmi_a
        elif BMI > 14.25 and BMI <= 15.75:
            z_score = bmi_b
        elif BMI > 15.75 and BMI <= 17.7:
            z_score = bmi_c
        elif BMI > 17.7 and BMI <= 20.3:
            z_score = bmi_d
        elif BMI > 20.3 and BMI <= 24.0:
            z_score = bmi_e
        elif BMI > 24.0 and BMI <= 29.8:
            z_score = bmi_f
        elif BMI > 29.8 and BMI <= 33.4:
            z_score = bmi_g
        elif BMI > 33.4:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 14:
        if BMI < 14.0:
            z_score = bmi_z
        elif BMI >= 14.0 and BMI <= 14.7:
            z_score = bmi_a
        elif BMI > 14.7 and BMI <= 16.3:
            z_score = bmi_b
        elif BMI > 16.3 and BMI <= 18.4:
            z_score = bmi_c
        elif BMI > 18.4 and BMI <= 21.15:
            z_score = bmi_d
        elif BMI > 21.15 and BMI <= 25.0:
            z_score = bmi_e
        elif BMI > 25.0 and BMI <= 31.0:
            z_score = bmi_f
        elif BMI > 31.0 and BMI <= 34.7:
            z_score = bmi_g
        elif BMI > 34.7:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 15:
        if BMI < 14.4:
            z_score = bmi_z
        elif BMI >= 14.4 and BMI <= 15.15:
            z_score = bmi_a
        elif BMI > 15.15 and BMI <= 16.85:
            z_score = bmi_b
        elif BMI > 16.85 and BMI <= 19.0:
            z_score = bmi_c
        elif BMI > 19.0 and BMI <= 21.85:
            z_score = bmi_d
        elif BMI > 21.85 and BMI <= 25.85:
            z_score = bmi_e
        elif BMI > 25.85 and BMI <= 31.85:
            z_score = bmi_f
        elif BMI > 31.85 and BMI <= 35.5:
            z_score = bmi_g
        elif BMI > 35.5:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 16:
        if BMI < 14.6:
            z_score = bmi_z
        elif BMI >= 14.6 and BMI <= 15.4:
            z_score = bmi_a
        elif BMI > 15.4 and BMI <= 17.2:
            z_score = bmi_b
        elif BMI > 17.2 and BMI <= 19.45:
            z_score = bmi_c
        elif BMI > 19.45 and BMI <= 22.4:
            z_score = bmi_d
        elif BMI > 22.4 and BMI <= 26.5:
            z_score = bmi_e
        elif BMI > 26.5 and BMI <= 32.5:
            z_score = bmi_f
        elif BMI > 32.5 and BMI <= 36.1:
            z_score = bmi_g
        elif BMI > 36.1:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 17:
        if BMI < 14.7:
            z_score = bmi_z
        elif BMI >= 14.7 and BMI <= 15.55:
            z_score = bmi_a
        elif BMI > 15.55 and BMI <= 17.4:
            z_score = bmi_b
        elif BMI > 17.4 and BMI <= 19.7:
            z_score = bmi_c
        elif BMI > 19.7 and BMI <= 22.75:
            z_score = bmi_d
        elif BMI > 22.75 and BMI <= 26.9:
            z_score = bmi_e
        elif BMI > 26.9 and BMI <= 32.8:
            z_score = bmi_f
        elif BMI > 32.8 and BMI <= 36.3:
            z_score = bmi_g
        elif BMI > 36.3:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 18:
        if BMI < 14.7:
            z_score = bmi_z
        elif BMI >= 14.7 and BMI <= 15.55:
            z_score = bmi_a
        elif BMI > 15.55 and BMI <= 17.5:
            z_score = bmi_b
        elif BMI > 17.5 and BMI <= 19.95:
            z_score = bmi_c
        elif BMI > 19.95 and BMI <= 23.05:
            z_score = bmi_d
        elif BMI > 23.05 and BMI <= 27.15:
            z_score = bmi_e
        elif BMI > 27.15 and BMI <= 32.9:
            z_score = bmi_f
        elif BMI > 32.9 and BMI <= 36.3:
            z_score = bmi_g
        elif BMI > 36.3:
            z_score = bmi_h      
    elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 19:
        if BMI < 14.7:
            z_score = bmi_z
        elif BMI >= 14.7 and BMI <= 15.6:
            z_score = bmi_a
        elif BMI > 15.6 and BMI <= 17.6:
            z_score = bmi_b
        elif BMI > 17.6 and BMI <= 20.05:
            z_score = bmi_c
        elif BMI > 20.05 and BMI <= 23.2:
            z_score = bmi_d
        elif BMI > 23.2 and BMI <= 27.35:
            z_score = bmi_e
        elif BMI > 27.35 and BMI <= 32.95:
            z_score = bmi_f
        elif BMI > 32.95 and BMI <= 36.2:
            z_score = bmi_g
        elif BMI > 36.2:
            z_score = bmi_h    


# --------------------
# Membuat variabel kategori_bayi dari conditional statemen 
# --------------------
    if umur >= 1 and umur <= 20 and z_score == -4:
        kategori_bayi = "Malnutrisi"
    elif umur >= 1 and umur <= 20 and z_score in [-3, -2]:
        kategori_bayi = "Underweight"
    elif umur >= 1 and umur <= 20 and  z_score in [-1, 0, 1]:
        kategori_bayi = "Normal"
    elif umur >= 1 and umur <= 20 and  z_score == 2:
        kategori_bayi = "Risiko overweight"
    elif umur >= 1 and umur <= 20 and  z_score == 3:
        kategori_bayi = "Overweight"
    elif umur >= 1 and umur <= 20 and  z_score == 4:
        kategori_bayi = "Obesitas"


# --------------------
# Membuat variabel kategori_bmi  untuk dewasa dan lansia
# --------------------
    if kategori == "Kategori anda adalah dewasa":
        if BMI < 18.5:
            kategori_BMI = "Underweight"          
        elif BMI >=18.5 and BMI <= 24.9:
            kategori_BMI = "Normal"                    
        elif BMI >= 25 and BMI <= 29.9:
            kategori_BMI = "Overweight"             
        elif BMI >=30:
            kategori_BMI = "Obesitas"                 
    elif kategori == "Kategori anda adalah lansia":
        if BMI < 22:
            kategori_BMI = "Malnutrisi"               
        elif BMI >= 22 and BMI <=27:
            kategori_BMI = "Normal"                    
        elif BMI >=27.1 and BMI < 30:
            kategori_BMI = "Overweight"             
        elif BMI >= 30:
            kategori_BMI = "Obesitas"


# --------------------
# Membuat variabel penyebab, risiko, dan upaya
# --------------------
    penyebab_bayi_malnutrisi = ["ASI tidak cukup", "Teknik menyusu tidak benar (bayi tidak efektif mengisap)", "MPASI terlambat atau kurang energi", "Infeksi berulang (diare, ISPA, pneumonia)", "Berat lahir rendah", "Penyakit bawaan", "Ibu kurang gizi", "Lingkungan tidak higienis â†’ = infeksi"]    
    risiko_bayi_malnutrisi = ["Infeksi berat (pneumonia, diare akut)", "Pertumbuhan terhambat (stunting)", "Berat badan tidak naik (failure to thrive)", "Kekurangan gizi akut (wasting)", "Dehidrasi cepat", "Penurunan perkembangan otak", "Risiko kematian meningkat pada malnutrisi berat"] 
    upaya_bayi_malnutrisi = ["Perbaiki teknik & frekuensi menyusu", "Tambah volume ASI/perah bila perlu", "Susu formula sesuai anjuran dokter jika ASI tidak cukup", "MPASI energi tinggi mulai 6 bulan", "Obati infeksi", "Pantau pertumbuhan tiap bulan", "Periksakan dan konsultasi ke dokter"] 

    penyebab_bayi_underweight = ["ASI kurang atau tidak eksklusif", "Teknik menyusu tidak tepat â†’ bayi tidak mengisap optimal", "MPASI terlambat atau kurang energi", "Infeksi berulang (diare, ISPA)", "Berat lahir rendah", "Masalah bawaan (kelainan jantung, metabolik)", "Ibu kurang nutrisi"]    
    risiko_bayi_underweight = ["Pertumbuhan terhambat", "Perkembangan otak terlambat", "Infeksi berulang", "Berat sulit naik (failure to thrive)", "Dehidrasi cepat", "Risiko kematian pada malnutrisi berat"]  
    upaya_bayi_underweight = ["Optimalkan ASI (pelekatan, frekuensi)", "Tambah susu formula bila ASI tidak cukup", "MPASI tinggi energi mulai 6 bulan", "Tambahkan minyak/santan ke MPASI", "Obati infeksi", "Pantau Z-score tiap bulan", "Periksakan dan konsultasi ke dokter"]

    penyebab_bayi_normal = ["Asupan ASI atau susu formula seimbang", "Frekuensi menyusu cukup sesuai kebutuhan", "Tidak ada infeksi kronis atau masalah penyerapan nutrisi", "Pertumbuhan mengikuti kurva WHO (BB/U, PB/U, BB/PB)"]    
    risiko_bayi_normal = ["Infeksi karena sistem imun belum matang", "Risiko alergi makanan", "Pertumbuhan terhambat jika asupan menurun mendadak"]
    upaya_bayi_normal = ["ASI eksklusif 6 bulan, lalu MPASI bergizi lengkap", "Pantau berat di Posyandu tiap bulan", "Hindari pemberian makanan tinggi gula/garam", "Periksakan dan konsultasi ke dokter"]    

    penyebab_bayi_risiko_overweight = ["Formula terlalu kental atau pemberian berlebihan", "MPASI terlalu dini (<6 bulan)", "Makanan tinggi gula (biskuit manis, jus buah kemasan)", "Bayi jarang bergerak (jarang tummy time)"]     
    risiko_bayi_risiko_overweight = ["Risiko obesitas saat anakâ€“remaja", "Gangguan perkembangan motorik karena terlalu berat", "Sleep apnea"]  
    upaya_bayi_risiko_overweight = ["ASI sebagai sumber utama sampai 6 bulan", "MPASI sesuai jadwal dan porsi (bukan â€œdipaksa habisâ€)", "Batasi makanan manis", "Perbanyak aktivitas motorik (tummy time, merangkak)","Periksakan dan konsultasi ke dokter"] 

    penyebab_bayi_overweight = ["Susu formula terlalu banyak atau terlalu kental", "MPASI terlalu dini atau terlalu padat energi", "Makanan manis seperti biskuit/jus kemasan", "Minim aktivitas motorik (jarang tummy time)"]
    risiko_bayi_overweight = ["Obesitas masa kanak-kanak", "Gangguan motorik (lambat duduk/merangkak)", "Sleep apnea", "Risiko peningkatan lemak tubuh saat anak besar"]
    upaya_bayi_overweight = ["Utamakan ASI sampai 6 bulan", "MPASI sesuai aturan WHO, tanpa gula/garam", "Batasi cemilan manis", "Stimulasi gerak: tummy time, merangkak, bermain lantai", "Periksakan dan konsultasi ke dokter"]       

    penyebab_bayi_obesitas = ["Konsumsi susu formula berlebihan atau terlalu kental", "MPASI terlalu dini (<6 bulan)", "MPASI tinggi gula (bubur instan manis, biskuit manis)", "Minim aktivitas motorik (kurang tummy time)", "Pemberian makan berdasarkan â€œdipaksa habisâ€, bukan respons lapar"]
    risiko_bayi_obesitas = ["Obesitas berlanjut saat anak & remaja", "Gangguan motorik (lambat merangkak/berdiri)", "Sleep apnea", "Gangguan pernapasan (mengi)", "Risiko gangguan metabolik saat besar"]
    upaya_bayi_obesitas = ["ASI eksklusif sampai 6 bulan bila memungkinkan", "MPASI sesuai kebutuhan (bukan memaksakan porsi besar)", "Hindari gula & camilan manis", "Beri ruang aktivitas fisik: tummy time, merangkak", "Konsultasi dokter anak bila pertambahan BB terlalu cepat"]   

    penyebab_balita_malnutrisi = ["Picky eater", "Asupan tidak seimbang (hanya makan karbohidrat)", "Infeksi berulang", "Cacingan", "Pola makan tidak teratur", "Stimulasi makan buruk"] 
    risiko_balita_malnutrisi = ["Stunting (pertumbuhan terhambat)", "Lemah otot dan cepat lelah", "Perkembangan otak menurun", "Kekebalan tubuh rendah", "Mudah terkena ISPA dan diare","Gangguan belajar di masa depan", "Risiko kematian meningkat pada malnutrisi parah"]
    upaya_balita_malnutrisi = ["Tambah kalori lewat minyak, mentega, santan", "Konsumsi protein tinggi (daging, telur, ikan)", "Camilan sehat 2Ã—/hari", "Obati cacingan (sesuai usia)", "Perbaiki jadwal makan", "Pantau pertumbuhan setiap 1â€“3 bulan", "Periksakan dan konsultasi ke dokter"]         

    penyebab_balita_underweight = ["Picky eater", "Asupan rendah", "Pola makan tidak teratur", "Cacingan", "Infeksi berulang", "MPASI kurang seimbang"]   
    risiko_balita_underweight = ["Stunting (pertumbuhan terhambat)", "Sering sakit (ISPA, diare)", "Anemia", "Perkembangan otak terganggu", "Kekebalan tubuh rendah", "Berat makin turun jika tidak ditangani"]     
    upaya_balita_underweight = ["Makanan padat energi (telur, daging, ikan, keju)", "Tambahkan minyak/mentega ke makanan", "Camilan bergizi 2Ã—/hari", "Obati cacingan", "Buat jadwal makan teratur", "Pantau pertumbuhan tiap 1â€“3 bulan", "periksakan dan konsultasi ke dokter"]      

    penyebab_balita_normal = ["Konsumsi makanan seimbang (karbo, protein, lemak sehat)", "Aktivitas fisik yang cukup", "Tidak ada penyakit kronis (TBC, cacingan, diare berulang)"] 
    risiko_balita_normal = ["Anemia karena kurang zat besi (meski BB normal)", "Obesitas tersembunyi jika makan banyak makanan olahan", "Infeksi saluran napas atau pencernaan"]
    upaya_balita_normal = ["Makanan rumah, bukan ultra-proses", "Rutin imunisasi dan pemeriksaan tumbuh kembang", "Batasi gula maksimal 25 g/hari", "Periksakan dan konsultasi ke dokter"] 

    penyebab_balita_risiko_overweight = ["Konsumsi minuman manis, jajanan kemasan", "Porsi makanan terlalu besar", "Pola makan tinggi kalori rendah nutrisi", "Duduk pasif terlalu banyak (gadget >2 jam/hari)", "Kurang tidur (mengganggu hormon ghrelin & leptin)"]   
    risiko_balita_risiko_overweight = ["Prediabetes dan resistensi insulin", "Tekanan darah mulai naik", "Obesitas berlanjut saat sekolah", "Masalah napas (mengi, sleep apnea)"]
    upaya_balita_risiko_overweight = ["Ganti camilan kemasan â†’ buah, yogurt tanpa gula", "Air putih sebagai minuman utama", "Aktivitas fisik â‰¥3 jam/hari", "Tidur cukup 10â€“12 jam", "Periksakan dan konsultasi ke dokter"] 

    penyebab_balita_overweight = ["Konsumsi minuman manis dan camilan kemasan", "Porsi makan terlalu besar", "Kurang tidur", "Kurang aktivitas fisik", "Pola makan tinggi kalori, rendah gizi"]  
    risiko_balita_overweight = ["Prediabetes", "Obesitas berlanjut saat sekolah", "Asma / mengi", "Sleep apnea", "Masalah tulang & postur karena beban tubuh"]
    upaya_balita_overweight = ["Ganti camilan kemasan â†’ buah/yogurt tanpa gula", "Jaga jadwal makan 3x + 2 snack sehat", "Aktivitas fisik minimal 3 jam/hari", "Kurangi gula dan minuman manis", "Tidur cukup 10â€“12 jam", "Periksakan dan konsultasi ke dokter"]   

    penyebab_balita_obesitas = ["Minuman manis (teh manis, susu kental manis, jus kemasan)", "Camilan ultra-proses (biskuit, keripik, nugget, sosis)", "Porsi makan besar", "Kurang main fisik, lebih banyak gadget", "Tidur kurang atau tidak teratur"] 
    risiko_balita_obesitas = ["Prediabetes", "Hipertensi anak", "Sleep apnea", "Masalah pernapasan (asma / mengi)", "Obesitas menetap hingga dewasa", "Keterlambatan perkembangan motorik"] 
    upaya_balita_obesitas = ["Air putih sebagai minuman utama", "Porsi wajar, pola makan 3x + 2 snack sehat", "Aktivitas fisik total 3 jam/hari", "Batasi gula dan minuman manis", "Tidur 10â€“12 jam/hari", "Tidak melakukan diet ekstremâ€”fokus pola makan sehat", "Periksakan dan konsultasi ke dokter"] 

    penyebab_anak_malnutrisi = ["Picky eater", "Aktivitas tinggi tanpa makan cukup", "Alergi makanan", "Infeksi kronis", "Faktor psikologis (malas makan, cemas)"]  
    risiko_anak_malnutrisi = ["Konsentrasi menurun", "Anemia", "Infeksi berulang", "Pertumbuhan terhambat", "Kelelahan", "Penurunan performa sekolah", "Gangguan hormon jika berat sangat rendah"]
    upaya_anak_malnutrisi = ["Tambah kalori +300â€“500 kkal/hari", "Makan tinggi protein dan lemak sehat", "Suasana makan positif", "Cek alergi jika berat sulit naik", "Periksakan dan konsultasi ke dokter"] 

    penyebab_anak_underweight = ["Kurang makan", "Aktivitas tinggi", "Alergi makanan", "Infeksi kronis", "Masalah psikologis (malas makan, stres)"]
    risiko_anak_underweight = ["Konsentrasi menurun", "Anemia", "Mudah sakit", "Kelelahan", "Gangguan pertumbuhan", "Kinerja belajar menurun"]
    upaya_anak_underweight = ["Tambah kalori 300â€“500 kkal/hari", "Tingkatkan protein dan lemak sehat", "Tambah frekuensi makan", "Perbaiki suasana makan", "Cek alergi/anemia jika berat sulit naik", "Periksakan dan konsultasi ke dokter"]

    penyebab_anak_normal = ["Pola makan seimbang dan jam makan teratur", "Aktivitas fisik harian (minimal 60 menit)", "Tidur cukup, hormon pertumbuhan optimal"]
    risiko_anak_normal = ["Obesitas di masa depan jika kebiasaan makan buruk", "Kekurangan vitamin D atau kalsium", "Gangguan postur akibat kurang aktivitas"]
    upaya_anak_normal = ["Biasakan makan sayur/buah", "Kurangi gadget, tambah aktivitas luar ruangan", "Pantau pertumbuhan tiap 3 bulan", "Periksakan dan konsultasi ke dokter"]

    penyebab_anak_risiko_overweight = ["Pola makan tidak teratur (melewatkan sarapan lalu makan besar)", "Konsumsi makanan ultra-proses (pizza, nugget, sosis)", "Kurangnya olahraga sekolah", "Stres akademik â†’ emotional eating"]
    risiko_anak_risiko_overweight = ["Risiko diabetes tipe 2 meningkat 4â€“8 kali", "Dislipidemia (kolesterol tinggi)", "Masalah kepercayaan diri dan bullying", "Gangguan sendi karena beban berlebih"]
    upaya_anak_risiko_overweight = ["Menu seimbang (setengah piring sayur + buah)", "Olahraga 60 menit/hari", "Kurangi waktu layar <2 jam/hari", "Sarapan tinggi protein", "Periksakan dan konsultasi ke dokter"]

    penyebab_anak_overweight = ["Makan cepat saji rutin", "Porsi makan besar tanpa kontrol", "Waktu layar terlalu banyak (gadget)", "Kurang olahraga sekolah", "Tidur tidak teratur"]
    risiko_anak_overweight = ["Resistensi insulin â†’ diabetes tipe 2", "Kolesterol tinggi", "Kerusakan sendi (lutut)"] 
    upaya_anak_overweight = ["Pola makan seimbang", "Olahraga 60 menit/hari", "Batasi gadget <2 jam/hari", "Biasakan sarapan sehat", "Periksakan dan konsultasi ke dokter"]

    penyebab_anak_obesitas = ["Fast food & minuman manis", "Porsi makan besar, emotional eating", "Kurang olahraga sekolah", "Waktu layar >3â€“4 jam/hari", "Tidur tidak cukup", "Pola makan keluarga yang kurang sehat"]
    risiko_anak_obesitas = ["Diabetes tipe 2 dini", "Hipertensi", "Kolesterol tinggi", "Gangguan sendi (lutut)", "Masalah psikologis (rendah diri, bullying)"]
    upaya_anak_obesitas = ["Pola makan seimbang", "Olahraga 60 menit/hari", "Batasi gadget <2 jam/hari", "Sarapan kaya protein", "Perbaiki jam tidur (9â€“11 jam)", "Periksakan dan konsultasi ke dokter"]        

    penyebab_remaja_malnutrisi = ["Lonjakan pertumbuhan (growth spurt)", "Diet ketat karena body image", "Olahraga berat", "Stres akademik", "Gangguan hormon (tiroid)", "Penyakit kronis", "Gangguan makan (anoreksia/bulimia)"]
    risiko_remaja_malnutrisi = ["Menstruasi tidak teratur (wanita)", "Tulang rapuh (osteopenia/osteoporosis dini)", "Anemia", "Tidak fokus belajar", "Gangguan kekuatan otot", "Penurunan sistem imun", "Gangguan mental (ansietas, depresi)"]  
    upaya_remaja_malnutrisi = ["Tambah 400â€“700 kkal/hari", "Latihan beban untuk menaikkan massa otot", "Pola makan tinggi protein", "Konsultasi psikolog jika ada gangguan makan", "Cek hormon tiroid bila perlu", "Periksa dan konsultasi ke dokter"]

    penyebab_remaja_underweight = ["Lonjakan pertumbuhan (growth spurt) tanpa cukup nutrisi", "Diet ketat karena body image", "Olahraga berat", "Gangguan hormon (terutama tiroid)", "Gangguan makan (anoreksia, bulimia)", "Stres akademik"]
    risiko_remaja_underweight = ["Tulang rapuh (osteoporosis dini)", "Menstruasi tidak teratur (wanita)", "Anemia", "Kelelahan", "Penurunan sistem imun", "Gangguan hormon", "Gangguan mental jika penyebab psikologis"]
    upaya_remaja_underweight = ["Tambah kalori 400â€“700 kkal/hari", "Perbanyak protein", "Latihan beban untuk meningkatkan massa otot", "Tidur cukup", "Konsultasi psikolog jika ada gangguan makan", "Periksa tiroid jika berat susah naik", "Periksakan dan konsultasi ke dokter"]

    penyebab_remaja_normal = ["Keseimbangan antara kebutuhan hormon pubertas dan asupan nutrisi", "Aktivitas fisik tinggi di sekolah", "Pola makan tidak berlebihan"]
    risiko_remaja_normal = ["Anemia, terutama perempuan", "Gangguan pola makan (bulimia, anoreksia) meski BB normal", "Skinny-fat (lemak visceral tinggi)"]
    upaya_remaja_normal = ["Pola makan tinggi protein dan mikronutrien", "Olahraga teratur (kombinasi kardio + kekuatan)", "Hindari diet ekstrem", "Periksakan dan konsultasi ke dokter"] 

    penyebab_remaja_risiko_overweight = ["Perubahan hormon pubertas â†’ nafsu makan meningkat", "Fast food dan minuman manis", "Kurang aktivitas fisik", "Begadang â†’ gangguan hormon lapar"]     
    risiko_remaja_risiko_overweight = ["Obesitas dewasa (kemungkinan 70%)", "Hipertensi remaja", "PCOS pada perempuan", "Gangguan psikis (depresi, body image issues)"]
    upaya_remaja_risiko_overweight = ["Pola makan tinggi protein, rendah gula", "Tidur 8â€“10 jam", "Latihan kekuatan + kardio 5x/minggu", "Pendidikan gizi (tidak dilarang makan, tapi dikontrol)", "Periksakan dan konsultasi ke dokter"] 

    penyebab_remaja_overweight = ["Fast food dan minuman manis", "Kurang tidur (begadang)", "Perubahan hormon pubertas â†’ nafsu makan meningkat", "Kurang olahraga", "Citra diri buruk â†’ emotional eating"]
    risiko_remaja_overweight = ["Obesitas dewasa (70% berlanjut)", "Hipertensi remaja", "Diabetes tipe 2", "PCOS pada perempuan", "Masalah mental (depresi, body image)"]
    upaya_remaja_overweight = ["Diet tinggi protein, rendah gula", "Perbaiki jadwal tidur 8â€“10 jam", "Olahraga 5 hari/minggu (kardio + kekuatan)", "Kurangi minuman manis (boba, soda)", "Pendidikan gizi tanpa melarang ekstrem", "Periksakan dan konsultasi ke dokter"]

    penyebab_remaja_obesitas = ["Fast food, boba, minuman manis", "Begadang & kurang tidur", "Penurunan aktivitas fisik", "Stress sekolah/emosi â†’ makan berlebih", "Perubahan hormon pubertas", "Gaya hidup sedentari (game/gadget berjam-jam)"]
    risiko_remaja_obesitas = ["Diabetes tipe 2", "PCOS pada remaja perempuan", "Hipertensi remaja", "Kolesterol tinggi", "Gangguan mental: kecemasan, depresi", "Obesitas dewasa (70% berlanjut dari remaja)"]     
    upaya_remaja_obesitas = ["Diet tinggi protein, batasi gula", "Olahraga 5 hari/minggu (kardio + latihan kekuatan)", "Tidur 8â€“10 jam", "Kurangi makanan ultra-proses", "Edukasi body-image yang sehat", "Hindari diet ekstrem karena mengganggu tumbuh kembang", "Periksakan dan konsultasi ke dokter"]

    penyebab_dewasa_malnutrisi = ["Kurang makan (jam makan tidak teratur)", "Stress, depresi", "Penyakit metabolik (hipertiroid, diabetes tipe 1)", "Masalah lambung/pencernaan", "Aktivitas fisik tinggi", "Kebiasaan melewatkan makan"]
    risiko_dewasa_malnutrisi = ["Lemah, lelah", "Otot mengecil", "Ritme jantung tidak normal", "Tekanan darah rendah", "Infeksi berulang", "Osteoporosis", "Penyembuhan luka lambat", "Penurunan fungsi kognitif jika parah"]
    upaya_dewasa_malnutrisi = ["Tambah 300â€“700 kkal/hari", "Tingkatkan protein & lemak sehat", "Latihan kekuatan", "Tidur cukup", "Cek penyakit dasar jika berat tetap tidak naik", "Periksakan dan konsultasi ke dokter"]

    penyebab_dewasa_underweight = ["Kurang makan / pola makan tidak teratur", "Masalah mental (stres, depresi)", "Penyakit metabolik (hipertiroid)", "Masalah pencernaan (malabsorbsi)", "Aktivitas tinggi", "Penyakit kronis"]  
    risiko_dewasa_underweight = ["Lemah dan cepat lelah", "Otot mengecil", "Tekanan darah rendah", "Gangguan detak jantung", "Sistem imun turun", "Osteoporosis", "Luka sulit sembuh", "Penurunan fungsi otak pada malnutrisi berat"]
    upaya_dewasa_underweight = ["Tambah kalori 300â€“700 kkal/hari", "Perbanyak protein (telur, susu, daging, tempe)", "Latihan beban teratur", "Tidur berkualitas", "Periksa penyebab medis jika berat tidak naik dalam 4â€“6 minggu", "Periksakan dan konsultasi ke dokter"]

    penyebab_dewasa_normal = ["Kebutuhan kalori sesuai aktivitas", "Metabolisme masih relatif stabil", "Pola hidup aktif"]
    risiko_dewasa_normal = ["Diabetes tipe 2 (jika lemak visceral tinggi)", "Hipertensi jika konsumsi garam tinggi", "Dislipidemia genetis", "Penyakit jantung pada perokok"]
    upaya_dewasa_normal = ["Diet seimbang: 45â€“65% karbo, 20â€“30% lemak sehat, 15â€“25% protein", "Olahraga 150â€“300 menit/minggu", "Cukup tidur 7â€“9 jam", "Kelola stres", "Periksakan dan konsultasi ke dokter"]     

    penyebab_dewasa_risiko_overweight = ["Kelebihan kalori harian", "Stres â†’ makan berlebih", "Kurang aktivitas (banyak duduk)", "Konsumsi gula, roti manis, minuman boba", "Metabolisme menurun setelah usia 30", "Obat tertentu (steroid, antidepresan)"]
    risiko_dewasa_risiko_overweight = ["Diabetes tipe 2", "Hipertensi", "Penyakit jantung", "Stroke", "Fatty liver (perlemakan hati)", "Sleep apnea"]
    upaya_dewasa_risiko_overweight = ["Defisit kalori ringan: -300 sampai -500 kcal/hari", "Tingkatkan aktivitas harian (â‰¥8.000 langkah/hari)", "Olahraga 150â€“300 menit/minggu", "Diet seimbang", "Kurangi gula â†’ maksimal 25 g/hari"]

    penyebab_dewasa_overweight = ["Pola makan tinggi kalori dan gula", "Kebiasaan makan malam besar", "Aktivitas fisik rendah (banyak duduk)", "Stres â†’ makan emosional", "Obat-obatan seperti steroid dan antidepresan", "Metabolisme menurun mulai usia 30-an"] 
    risiko_dewasa_overweight = ["Diabetes tipe 2", "Penyakit jantung & stroke", "Hipertensi", "Fatty liver (lemak hati)", "Sleep apnea", "Gangguan sendi, nyeri punggung"]
    upaya_dewasa_overweight = ["Defisit kalori ringan: 300â€“500 kcal/hari", "Perbanyak protein (20â€“30%)", "Olahraga 150â€“300 menit/minggu", "Perbanyak langkah: minimal 8.000â€“10.000/hari", "Kurangi gula sampai <25 g/hari", "Perbaiki pola tidur dan manajemen stres", "Periksakan dan konsultasi ke dokter"]

    penyebab_dewasa_obesitas = ["Konsumsi gula & minuman manis", "Makan lewat malam berulang-ulang", "Aktivitas fisik rendah (banyak duduk)", "Stres â†’ emotional eating", "Metabolisme menurun setelah usia 30", "Obat-obatan (kortikosteroid, antidepresan)", "Gangguan hormon (hipotiroid, Cushing)"] 
    risiko_dewasa_obesitas = ["Diabetes tipe 2", "Penyakit jantung & stroke", "Hipertensi", "Fatty liver (lemak hati)", "Sleep apnea", "Nyeri sendi, osteoarthritis", "Kanker tertentu (payudara, usus besar)"]
    upaya_dewasa_obesitas = ["Defisit kalori 300â€“500 kcal/hari (aman & stabil)", "Perbanyak protein (20â€“30%)", "Olahraga minimal 150â€“300 menit/minggu", "Latihan kekuatan 2â€“3x/minggu", "Kurangi gula sampai <25 g/hari", "Perbaiki pola tidur & manajemen stres", "Konsisten 3â€“6 bulan â†’ hasil signifikan"]   

    penyebab_lansia_malnutrisi = ["Nafsu makan turun", "Sulit mengunyah (gigi hilang)", "Depresi atau kesepian", "Penyakit kronis", "Efek samping obat", "Penyerapan nutrisi menurun", "Kelemahan fisik â†’ makan jadi sedikit"]
    risiko_lansia_malnutrisi = ["Penurunan massa otot (sarkopenia)", "Rapuh & mudah jatuh", "Osteoporosis", "Infeksi berulang", "Luka sulit sembuh", "Penurunan daya ingat", "Risiko kematian lebih tinggi pada malnutrisi berat"]
    upaya_lansia_malnutrisi = ["Porsi kecil tapi sering", "Makanan lunak tinggi kalori (bubur daging, sup ayam, smoothie)", "Tambah suplemen nutrisi cair", "Evaluasi obat yang menurunkan nafsu makan", "Cek kondisi gigi", "Pantau berat tiap 2 minggu", "Periksakan dan konsultasi ke dokter"]

    penyebab_lansia_underweight = ["Nafsu makan menurun", "Sulit mengunyah (gigi hilang)", "Penyakit kronis", "Depresi atau kesepian", "Efek samping obat", "Masalah penyerapan nutrisi"]
    risiko_lansia_underweight = ["Kehilangan massa otot (sarkopenia)", "Mudah jatuh dan patah tulang", "Gizi buruk kronis", "Infeksi berulang", "Luka sulit sembuh", "Penurunan daya ingat dan fungsi otak", "Risiko kematian meningkat pada malnutrisi berat"]
    upaya_lansia_underweight = ["Makanan lembut tinggi kalori (bubur daging, sup, smoothie)", "Tambahan suplemen nutrisi cair", "Evaluasi obat yang menurunkan nafsu makan", "Pantau berat tiap 2 minggu", "Periksakan dan konsultasi ke dokter"]      

    penyebab_lansia_normal = ["Asupan makanan cukup meski nafsu makan berkurang", "Aktivitas fisik teratur", "Tidak ada penyakit penyebab wasting (misal gagal jantung, kanker)"]
    risiko_lansia_normal = ["Sarcopenia (hilang massa otot) meski BMI normal", "Osteoporosis karena kurang kalsium/vitamin D", "Risiko jatuh dan fraktur"]
    upaya_lansia_normal = ["Prioritaskan protein tinggi (1â€“1.2 g/kg/hari)", "Latihan kekuatan ringan (resistance training)", "Paparan sinar matahari teratur", "Pantau berat dan lingkar lengan atas (LLA)", "Periksakan dan konsultasi ke dokter"]

    penyebab_lansia_risiko_overweight = ["Aktivitas fisik sangat rendah", "Pola makan tinggi karbo sederhana", "Perubahan hormon metabolik", "Gangguan mobilitas atau nyeri sendi", "Obat-obatan (beta-blocker, insulin dosis tinggi)"]
    risiko_lansia_risiko_overweight = ["Penyakit jantung dan stroke", "Hipertensi", "Osteoarthritis (kerusakan sendi)", "Sleep apnea", "Penurunan kognitif jika disertai inflamasi kronis"]
    upaya_lansia_risiko_overweight = ["Fokus pada pola makan seimbang, bukan diet ketat", "Latihan kekuatan ringan untuk mempertahankan otot", " Latihan kekuatan ringan untuk mempertahankan otot", "Jalan kaki 30â€“45 menit/hari", "Kurangi makanan tinggi gula dan gorengan", "Pemantauan rutin gula darah, kolesterol, tekanan darah", "Periksakan dan konsultasi ke dokter"]         

    penyebab_lansia_overweight = ["Aktivitas fisik rendah", "Pola makan tinggi karbo sederhana", "Penurunan metabolisme", "Efek samping obat (beta-blocker, insulin)", "Gangguan mobilitas"]
    risiko_lansia_overweight = ["Penyakit jantung & stroke", "Hipertensi", "Sleep apnea", "Gangguan napas", "Osteoarthritis (sendi rusak)", "Penurunan fungsi kognitif"]  
    upaya_lansia_overweight = ["Makan teratur, seimbang, tidak terlalu ketat", "Fokus pada protein (1â€“1.2 g/kgBB/hari)", "Jalan kaki 30â€“45 menit/hari", "Latihan kekuatan ringan untuk mencegah kehilangan otot", "Kurangi gula dan gorengan", "Pemeriksaan rutin tekanan darah, gula darah, kolesterol", "Periksakan dan konsultasi ke dokter"] 

    penyebab_lansia_obesitas = ["Metabolisme sangat menurun", "Aktivitas fisik kurang (karena nyeri sendi / mobilitas)", "Pola makan tinggi karbo sederhana", "Efek samping obat (beta-blocker, insulin)", "Kurang tidur", "Isolasi sosial â†’ emotional eating"]
    risiko_lansia_obesitas = ["Penyakit jantung dan stroke", "Diabetes tipe 2", "Nyeri lutut/osteoporosis", "Fatty liver.", "Gangguan napas / sleep apnea", "Penurunan fungsi kognitif"]
    upaya_lansia_obesitas = ["Pola makan seimbang, tidak terlalu ketat", "Konsumsi protein cukup (1â€“1.2 g/kgBB/hari)", "Jalan kaki 30â€“45 menit/hari", "Latihan kekuatan ringan untuk menjaga otot", "Pantau rutin: gula darah, kolesterol, tekanan darah", "Batasi gula, gorengan, dan makanan tinggi garam", "Periksakan dan konsultasi ke dokter"]              


# --------------------
# Mengoutputkan hasil untuk pengguna
# --------------------
    print("-" * 40)
    print("Nama           : ", nama)
    print("Gender         : ", gender)
    print("Umur           : ", umur, "tahun")
    print("Kategori       : ", kategori)
    print("Berat badan    : ", int(berat_badan), "kg")
    print("Tinggi badan   : ", int(tinggi_badan) * 100, "cm")
    print("BMI            : ", BMI)
    if kategori == "Kategori anda adalah bayi" or kategori == "Kategori anda adalah balita" or kategori == "Kategori anda adalah anak-anak" or kategori == "Kategori anda adalah remaja":
    	print("Kategori BMI   : ", kategori_bayi)
    elif kategori == "Kategori anda adalah dewasa" or kategori == "Kategori anda adalah lansia":
    	print("Kategori BMI   : ", kategori_BMI)


    if umur > 0 and umur <= 1 and kategori_bayi == "Malnutrisi":
        print("\n \033[91mPenyebab malnutrisi pada bayi, antara lain:\033[0m")
        for i, w in enumerate(penyebab_bayi_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko malnutrisi pada bayi, antara lain:\033[0m")
        for i, w in enumerate(risiko_bayi_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi malnutrisi pada bayi, antara lain:\033[0m")
        for i, w in enumerate(upaya_bayi_malnutrisi, start=1):
            print(f"{i}. {w}")
    elif umur > 0 and umur <= 1 and kategori_bayi == "Underweight":
        print("\n \033[91mPenyebab underweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(penyebab_bayi_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko underweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(risiko_bayi_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi underweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(upaya_bayi_underweight, start=1):
            print(f"{i}. {w}")
    elif umur > 0 and umur <= 1 and kategori_bayi == "Normal":
        print("\n \033[91mPenyebab status normal pada bayi, antara lain:\033[0m")
        for i, w in enumerate(penyebab_bayi_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko status normal pada bayi, antara lain:\033[0m")
        for i, w in enumerate(risiko_bayi_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mempertahankan status normal pada bayi, antara lain:\033[0m")
        for i, w in enumerate(upaya_bayi_normal, start=1):
            print(f"{i}. {w}")
    elif umur > 0 and umur <= 1 and kategori_bayi == "Risiko overweight":
        print("\n \033[91mPenyebab risiko overweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(penyebab_bayi_risiko_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(risiko_bayi_risiko_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi risiko overweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(upaya_bayi_risiko_overweight, start=1):
            print(f"{i}. {w}")
    elif umur > 0 and umur <= 1 and kategori_bayi == "Overweight":
        print("\n \033[91mPenyebab overweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(penyebab_bayi_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(risiko_bayi_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi overweight pada bayi, antara lain:\033[0m")
        for i, w in enumerate(upaya_bayi_overweight, start=1):
            print(f"{i}. {w}")
    elif umur > 0 and umur <= 1 and kategori_bayi == "Obesitas":
        print("\n \033[91mPenyebab obesitas pada bayi, antara lain:\033[0m")
        for i, w in enumerate(penyebab_bayi_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko obesitas pada bayi, antara lain:\033[0m")
        for i, w in enumerate(risiko_bayi_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi obesitas pada bayi, antara lain:\033[0m")
        for i, w in enumerate(upaya_bayi_obesitas, start=1):
            print(f"{i}. {w}")
    elif umur >= 2 and umur <= 5 and kategori_bayi == "Malnutrisi":
        print("\n \033[91mPenyebab malnutrisi pada balita, antara lain:\033[0m")
        for i, w in enumerate(penyebab_balita_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko malnutrisi pada balita, antara lain:\033[0m")
        for i, w in enumerate(risiko_balita_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi malnutrisi pada balita, antara lain:\033[0m")
        for i, w in enumerate(upaya_balita_malnutrisi, start=1):
            print(f"{i}. {w}")
    elif umur >= 2 and umur <= 5 and kategori_bayi == "Underweight":
        print("\n \033[91mPenyebab underweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(penyebab_balita_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko underweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(risiko_balita_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi underweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(upaya_balita_underweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 2 and umur <= 5 and kategori_bayi == "Normal":
        print("\n \033[91mPenyebab status normal pada balita, antara lain:\033[0m")
        for i, w in enumerate(penyebab_balita_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko status normal pada balita, antara lain:\033[0m")
        for i, w in enumerate(risiko_balita_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mempertahankan status normal pada balita, antara lain:\033[0m")
        for i, w in enumerate(upaya_balita_normal, start=1):
            print(f"{i}. {w}")
    elif umur >= 2 and umur <= 5 and kategori_bayi == "Risiko overweight":
        print("\n \033[91mPenyebab risiko overweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(penyebab_balita_risiko_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(risiko_balita_risiko_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi risiko overweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(upaya_balita_risiko_overweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 2 and umur <= 5 and kategori_bayi == "Overweight":
        print("\n \033[91mPenyebab overweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(penyebab_balita_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(risiko_balita_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi overweight pada balita, antara lain:\033[0m")
        for i, w in enumerate(upaya_balita_overweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 2 and umur <= 5 and kategori_bayi == "Obesitas":
        print("\n \033[91mPenyebab obesitas pada balita, antara lain:\033[0m")
        for i, w in enumerate(penyebab_balita_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko obesitas pada balita, antara lain:\033[0m")
        for i, w in enumerate(risiko_balita_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi obesitas pada balita, antara lain:\033[0m")
        for i, w in enumerate(upaya_balita_obesitas, start=1):
            print(f"{i}. {w}")
    elif umur >= 6 and umur <= 10 and kategori_bayi == "Malnutrisi":
        print("\n \033[91mPenyebab malnutrisi pada anak, antara lain:\033[0m")
        for i, w in enumerate(penyebab_anak_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko malnutrisi pada anak, antara lain:\033[0m")
        for i, w in enumerate(risiko_anak_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi malnutrisi pada anak, antara lain:\033[0m")
        for i, w in enumerate(upaya_anak_malnutrisi, start=1):
            print(f"{i}. {w}")
    elif umur >= 6 and umur <= 10 and kategori_bayi == "Underweight":
        print("\n \033[91mPenyebab underweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(penyebab_anak_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko underweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(risiko_anak_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi underweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(upaya_anak_underweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 6 and umur <= 10 and kategori_bayi == "Normal":
        print("\n \033[91mPenyebab status normal pada anak, antara lain:\033[0m")
        for i, w in enumerate(penyebab_anak_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko status normal pada anak, antara lain:\033[0m")
        for i, w in enumerate(risiko_anak_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mempertahankan status normal pada anak, antara lain:\033[0m")
        for i, w in enumerate(upaya_anak_normal, start=1):
            print(f"{i}. {w}")
    elif umur >= 6 and umur <= 10 and kategori_bayi == "Risiko overweight":
        print("\n \033[91mPenyebab risiko overweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(penyebab_anak_risiko_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(risiko_anak_risiko_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi risiko overweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(upaya_anak_risiko_overweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 6 and umur <= 10 and kategori_bayi == "Overweight":
        print("\n \033[91mPenyebab overweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(penyebab_anak_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(risiko_anak_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi overweight pada anak, antara lain:\033[0m")
        for i, w in enumerate(upaya_anak_overweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 6 and umur <= 10 and kategori_bayi == "Obesitas":
        print("\n \033[91mPenyebab obesitas pada anak, antara lain:\033[0m")
        for i, w in enumerate(penyebab_anak_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko obesitas pada anak, antara lain:\033[0m")
        for i, w in enumerate(risiko_anak_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi obesitas pada anak, antara lain:\033[0m")
        for i, w in enumerate(upaya_anak_obesitas, start=1):
            print(f"{i}. {w}")
    elif umur >= 11 and umur <= 19 and kategori_bayi == "Malnutrisi":
        print("\n \033[91mPenyebab malnutrisi pada remaja, antara lain:\033[0m")
        for i, w in enumerate(penyebab_remaja_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko malnutrisi pada remaja, antara lain:\033[0m")
        for i, w in enumerate(risiko_remaja_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi malnutrisi pada remaja, antara lain:\033[0m")
        for i, w in enumerate(upaya_remaja_malnutrisi, start=1):
            print(f"{i}. {w}")
    elif umur >= 11 and umur <= 19 and kategori_bayi == "Underweight":
        print("\n \033[91mPenyebab underweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(penyebab_remaja_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko underweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(risiko_remaja_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi underweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(upaya_remaja_underweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 11 and umur <= 19 and kategori_bayi == "Normal":
        print("\n \033[91mPenyebab status normal pada remaja, antara lain:\033[0m")
        for i, w in enumerate(penyebab_remaja_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko status normal pada remaja, antara lain:\033[0m")
        for i, w in enumerate(risiko_remaja_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mempertahankan status normal pada remaja, antara lain:\033[0m")
        for i, w in enumerate(upaya_remaja_normal, start=1):
            print(f"{i}. {w}")
    elif umur >= 11 and umur <= 19 and kategori_bayi == "Risiko overweight":
        print("\n \033[91mPenyebab risiko overweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(penyebab_remaja_risiko_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(risiko_remaja_risiko_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi risiko overweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(upaya_remaja_risiko_overweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 11 and umur <= 19 and kategori_bayi == "Overweight":
        print("\n \033[91mPenyebab overweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(penyebab_remaja_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(risiko_remaja_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi overweight pada remaja, antara lain:\033[0m")
        for i, w in enumerate(upaya_remaja_overweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 11 and umur <= 19 and kategori_bayi == "Obesitas":
        print("\n \033[91mPenyebab obesitas pada remaja, antara lain:\033[0m")
        for i, w in enumerate(penyebab_remaja_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko obesitas pada remaja, antara lain:\033[0m")
        for i, w in enumerate(risiko_remaja_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi obesitas pada remaja, antara lain:\033[0m")
        for i, w in enumerate(upaya_remaja_obesitas, start=1):
            print(f"{i}. {w}")
    elif umur >= 20 and umur <= 60 and kategori_BMI == "Underweight":
        print("\n \033[91mPenyebab underweight pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(penyebab_dewasa_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko underweight pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(risiko_dewasa_underweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi underweight pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(upaya_dewasa_underweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 20 and umur <= 60 and kategori_BMI == "Normal":
        print("\n \033[91mPenyebab status normal pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(penyebab_dewasa_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko status normal pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(risiko_dewasa_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mempertahankan status normal pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(upaya_dewasa_normal, start=1):
            print(f"{i}. {w}")
    elif umur >= 20 and umur <= 60 and kategori_BMI == "Overweight":
        print("\n \033[91mPenyebab overweight pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(penyebab_dewasa_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(risiko_dewasa_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi overweight pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(upaya_dewasa_overweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 20 and umur <= 60 and kategori_BMI == "Obesitas":
        print("\n \033[91mPenyebab obesitas pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(penyebab_dewasa_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko obesitas pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(risiko_dewasa_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi obesitas pada dewasa, antara lain:\033[0m")
        for i, w in enumerate(upaya_dewasa_obesitas, start=1):
            print(f"{i}. {w}")
    elif umur >= 61 and kategori_BMI == "Malnutrisi":
        print("\n \033[91mPenyebab malnutrisi pada lansia, antara lain:\033[0m")
        for i, w in enumerate(penyebab_lansia_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko malnutrisi pada lansia, antara lain:\033[0m")
        for i, w in enumerate(risiko_lansia_malnutrisi, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi malnutrisi pada lansia, antara lain:\033[0m")
        for i, w in enumerate(upaya_lansia_malnutrisi, start=1):
            print(f"{i}. {w}")
    elif umur >= 61 and kategori_BMI == "Normal":
        print("\n \033[91mPenyebab status normal pada lansia, antara lain:\033[0m")
        for i, w in enumerate(penyebab_lansia_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko status normal pada lansia, antara lain:\033[0m")
        for i, w in enumerate(risiko_lansia_normal, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mempertahankan status normal pada lansia, antara lain:\033[0m")
        for i, w in enumerate(upaya_lansia_normal, start=1):
            print(f"{i}. {w}")
    elif umur >= 61 and kategori_BMI == "Overweight":
        print("\n \033[91mPenyebab overweight pada lansia, antara lain:\033[0m")
        for i, w in enumerate(penyebab_lansia_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko overweight pada lansia, antara lain:\033[0m")
        for i, w in enumerate(risiko_lansia_overweight, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi overweight pada lansia, antara lain:\033[0m")
        for i, w in enumerate(upaya_lansia_overweight, start=1):
            print(f"{i}. {w}")
    elif umur >= 61 and kategori_BMI == "Obesitas":
        print("\n \033[91mPenyebab obesitas pada lansia, antara lain:\033[0m")
        for i, w in enumerate(penyebab_lansia_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[93mRisiko obesitas pada lansia, antara lain:\033[0m")
        for i, w in enumerate(risiko_lansia_obesitas, start=1):
            print(f"{i}. {w}")
        print("\n \033[92mCara mengatasi obesitas pada lansia, antara lain:\033[0m")
        for i, w in enumerate(upaya_lansia_obesitas, start=1):
            print(f"{i}. {w}")

    print("-" * 40)
    

# --------------------
# Membuat kode untuk mengulanh atau keluar dari program
# --------------------
    print("\nProgram selesai dijalankan untuk", nama)
    return "done"
    
while True:
    hasil = program_bodywise()
    if hasil == "exit":
        print("\nKeluar dari program...")
        break
    pilihan = input("\nIngin mengulang program? (ya/tidak): ").lower()
    if pilihan == "exit":
        print("\nKeluar dari program...")
        break
    if pilihan != "ya":
        print("\nProgram dihentikan.")
        break

print("Selesai.")
