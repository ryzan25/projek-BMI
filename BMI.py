# --------------------
# Meminta nilai input nama dari pengguna
# --------------------
nama = input("Masukkan nama anda: ")
nama = nama.title()


# --------------------
# Meminta nilai input umur dari pengguna
# --------------------
kategori_usia_1 = "Kategori anda adalah bayi"
kategori_usia_2 = "Kategori anda adalah balita"
kategori_usia_3 = "Kategori anda adalah anak-anak"
kategori_usia_4 = "Kategori anda adalah remaja"
kategori_usia_5 = "Kategori anda adalah dewasa"
kategori_usia_6 = "Kategori anda adalah lansia"

while True:
    try:
         umur = int(input("Masukkan umur anda: "))
    except ValueError:
        print("Maaf, input harus angka bulat positif, bukan huruf!")
        continue
     
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
        print("Maaf, hanya bisa memasukkan bilangan bulat positif(1-100)")
        continue


# --------------------
# Meminta nilai input gender dari pengguna
# --------------------
while True:
    gender= input("Masukkan gender anda: ")
    gender = gender.lower()
    
    if gender == "laki-laki" or gender == "perempuan":
        break
    else:
        print("Maaf, hanya bisa memasukkan gender laki-laki dan perempuan")
        continue
       
               
# --------------------
# Meminta nilai input berat badan dari pengguna
# --------------------
while True:
    try:
        berat_badan = float(input("Masukkan berat badan anda (kg): "))
        if berat_badan < 0:
            print("Maaf, berat badan tidak boleh negatif!")
            continue 
        if berat_badan == 0:
            print("Maaf, berat badan tidak boleh 0!")
            continue  
        break 
    except ValueError:
        print("Maaf, input harus angka, bukan huruf!")

# --------------------
# Meminta nilai input tinggi badan dari pengguna
# --------------------
while True:
    try:
        tinggi_badan = float(input("Masukkan tinggi badan anda(cm): "))        
        if tinggi_badan < 0:
        	print("Maaf, tinggi badan tidak boleh negatif!")
        	continue
        if tinggi_badan == 0:
        	print("Maaf, tinggi badan tidak boleh 0!")   
        	continue
        break  
    except ValueError:
        print("Maaf, input harus bilangan positif, bukan huruf!")
        
        
tinggi_badan = tinggi_badan / 100
BMI = berat_badan / (tinggi_badan ** 2)





# --------------------
# Membuat kategori untuk bayi
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

kategori_bayi_1 = "Malnutrisi"
kategori_bayi_2 = "Underweight"
kategori_bayi_3 = "Normal"
kategori_bayi_4 = "Risiko overweight"
kategori_bayi_5 = "Overweight"
kategori_bayi_6 = "Obesitas"

# bayi laki-laki
if kategori == "Kategori anda adalah bayi" and gender == "laki-laki" and umur == 1:
    if BMI < 12.7:
        z_score = bmi_z
    elif BMI >= 12.7 and BMI < 13.5:
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
    elif BMI >= 12.9 and BMI < 13.35:
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
    elif BMI > 18.9 and BMI <= 19.65:
        z_score = bmi_f
    elif BMI > 19.65 and BMI <= 20.6:
        z_score = bmi_g
    elif BMI > 20.6:
        z_score = bmi_h    
elif kategori == "Kategori anda adalah balita" and gender == "laki-laki" and umur == 3:
    if BMI < 12.4:
        z_score = bmi_z
    elif BMI >= 12.4 and BMI < 12.9:
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
    elif BMI >= 12.1 and BMI < 12.6:
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
    elif BMI >= 12.0 and BMI < 12.45:
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
elif kategori == "Kategori anda adalah anak-anak" and gender == "laki-laki" and umur == 6:
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
elif kategori == "Kategori anda adalah remaja" and gender == "laki-laki" and umur == 11:
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
elif kategori == "Kategori anda adalah anak-anak" and gender == "perempuan" and umur == 6:
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
elif kategori == "Kategori anda adalah remaja" and gender == "perempuan" and umur == 11:
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
                 
if z_score == -4:
    kategori_bayi = kategori_bayi_1
elif z_score == -3 and z_score == -2:
    kategori_bayi = kategori_bayi_2
elif z_score == -1 and z_score == 0 and z_score == 1:
    kategori_bayi = kategori_bayi_3
elif z_score == 2:
    kategori_bayi = kategori_bayi_4
elif z_score == 3:
    kategori_bayi = kategori_bayi_5
elif z_score == 4:
    kategori_bayi = kategori_bayi_6
    


# --------------------
# Membuat kategori untuk dewasa dan lansia
# --------------------
if kategori == "Kategori anda adalah dewasa":
    if BMI < 18.5:
        kategori_BMI = "underweight"           
    elif BMI >=18.5 and BMI <= 24.9:
        kategori_BMI = "normal"                       
    elif BMI >= 25 and BMI <= 29.9:
        kategori_BMI = "overweight"                 
    elif BMI >=30:
        kategori_BMI = "obesitas"                      
elif kategori == "Kategori anda adalah lansia":
    if BMI < 22:
        kategori_BMI = "malnutrisi"                   
    elif BMI >= 22 and BMI <=27:
        kategori_BMI = "normal"                    
    elif BMI >=27.1 and BMI < 30:
        kategori_BMI = "overweight"                 
    elif BMI >= 30:
        kategori_BMI = "obesitas"
               

                                                        
                                                                                                              
                                                                                                                                    
# --------------------
# Mengoutputkan BMI
# --------------------
print("-" * 20)
print("Nama: ", nama)
print("Gender: ", gender)
print("Umur: ", umur)
print("Kategori: ", kategori)
print("Berat badan: ", berat_badan)
print("Tinggi badan: ", tinggi_badan)
print("BMI: ", BMI)
if kategori == "Kategori anda adalah bayi" or kategori == "Kategori anda adalah balita" or kategori == "Kategori anda adalah anak-anak" or kategori == "Kategori anda adalah remaja":
	print("Kategori BMI: ", kategori_bayi)
elif kategori == "Kategori anda adalah dewasa" or kategori == "Kategori anda adalah lansia":
	print("Kategori BMI: ", kategori_BMI)
print("-" * 20)
