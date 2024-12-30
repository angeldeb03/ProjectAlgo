# Data Skripsi
skripsi = [
    # Tahun 2021
    {"nama": "Farista Egistian", "nim": "160120201044", "judul": "RANCANG BANGUN PASANG SURUT AIR LAUT SECARA REAL TIME BERBASIS SENSOR TEKANAN DAN GDM SIM900A", "tahun": 2021},
    {"nama": "Unai Sunardi", "nim": "160120201027", "judul": "RANCANGAN BANGUN INSTRUMEN OTOMASI PENYARINGAN AIR SISA PENULISAN PENCUCIAN SURIMI", "tahun": 2021},
    {"nama": "Fauzan Ikhsanur Susanto", "nim": "150120201017", "judul": "SISTEM KONTROL PLC PADA PENGANGKATAN DAN TEMPAT SAMPAH PINTAR BERBASIS SMS GATEWAY", "tahun": 2021},
    {"nama": "Hendra Permana", "nim": "160120201041", "judul": "PROTOTIPE AUTONOMOUS SURFACE VEHICLE (ASV) MENGGUNAKAN PIXYCAM UNTUK MENENTUKAN RUTE KAPAL DENGAN ALGORITMA PID", "tahun": 2021},
    {"nama": "Hessen Agustinus J.G. Sitorus", "nim": "160120201014", "judul": "IMPLEMENTASI MOTOR BRUSHED DIRECT CURRENT (DC MOTOR) PADA SEPEDA LISTRIK", "tahun": 2021},
    # Tahun 2019
    {"nama": "Pingkan Maharani E.L", "nim": "140120201018", "judul": "PERANCANGAN PERANGKAT KOMUNIKASI DATA DALAM AIR BERBASIS VISIBLE LIGHT COMMUNICATION (VLC)", "tahun": 2019},
    {"nama": "Prayogo", "nim": "150120201009", "judul": "PERANGKAT PENDETEKSI KADAR LOGAM BERAT TEMBAGA (Cu) DALAM AIR BERBASIS MIKROKONTROLER", "tahun": 2019},
    {"nama": "Imal Nurdin", "nim": "140120201009", "judul": "PENGEMBANGAN TURBIN ANGIN POROS VERTIKAL JENIS SAVONIUS TIPE L DENGAN VARIASI OVERLAP SUDU", "tahun": 2019},
    {"nama": "Leonardo Wibawa Tambunan", "nim": "150120201033", "judul": "ANALISIS PERBANDINGAN KUALITAS JARINGAN 3G DAN 4G OPERATOR TELKOMSEL, AXIS, DAN INDOSAT MENGGUNAKAN METODE DRIVE TEST DAN SOFTWARE G-NETTRACK PRO DI WILAYAH PESISIR KABUPATEN BINTAN", "tahun": 2019},
    {"nama": "Septian Muhammad", "nim": "140120201805", "judul": "PERANCANGAN ROBOT WALL FOLLOWER PEMINDAH OBYEK DENGAN METODE PROPORTIONAL INTEGRAL DERIVATIVE (PID) BERBASIS ARDUINO MEGA 2560", "tahun": 2019},
    # Tahun 2023
    {"nama": "Johan Jeques Junior", "nim": "190120201055", "judul": "SISTEM PEMANTAUAN DAN KENDALI OMNIDIRECTIONAL ROBOT BERBASIS WIB IoT MENGGUNAKAN PROTOKOL WEBSOCKET", "tahun": 2023},
    {"nama": "Leo Fablo Silalahi", "nim": "160120201023", "judul": "RANCANG BANGUN APLIKASI MONITORING KANDUNGAN ZAT LOGAM PADA AIR TAWAR BERBASIS INTERNET OF THINGS DALAM MOBILE iOS", "tahun": 2023},
    {"nama": "Ajay", "nim": "180120201044", "judul": "RANCANG BANGUN PENETAS TELUR OTOMATIS BERBASIS MIKROKONTROLER ARDUINO MEGA2560", "tahun": 2023},
    {"nama": "Charles Yosua Barus", "nim": "180120201048", "judul": "RANCANG BANGUN PROTEKSI KELEBIHAN BEBAN PADA INSTALASI RUMAH BERBASIS MIKROKONTROLER PLC OUTSEAL", "tahun": 2023},
    {"nama": "Tauriq Fuji Nur Akbar", "nim": "180120201026", "judul": "RANCANG BANGUN MONITORING SUHU AIR PADA KOLAM BUDIDAYA LOBSTER AIR TAWAR MENGGUNAKAN PLATFORM ANTARES", "tahun": 2023},
    # Tahun 2020
    {"nama": "Restu Al-Khariti", "nim": "140120201004", "judul": "PENERAPAN HIGH POWER LED (HPL) SEBAGAI PENARIK DATANGNYA IKAN BERBASIS MIKROKONTROLER", "tahun": 2020},
    {"nama": "Muhammad Bayu Purnama", "nim": "160120201006", "judul": "PENDETEKSI KABUT ASAP BERBASIS INTERNET OF THINGS SEBAGAI UPAYA PENGOPTIMALAN SISTEM INFORMASI PADA KINERJA LEVEL MANAGEMENT VTS CENTER BATAM", "tahun": 2020},
    {"nama": "Sumantri", "nim": "160120201001", "judul": "SISTEM MONITORING SUHU DAN TINGKAT KEBISINGAN DI KAMAR MESIN KAPAL BERBASIS INTERNET OF THINGS (IoT)", "tahun": 2020},
    {"nama": "Muhamad Salihin", "nim": "140120201029", "judul": "PERANCANGAN SISTEM IDENTIFIKASI ADUS DAN PASANG SURUT AIR LAUT UNTUK NELAYAN TRADISIONAL", "tahun": 2020},
    {"nama": "Zarwin", "nim": "140120201046", "judul": "PERANCANGAN SISTEM DETEKSI KELAYAKAN AIR MINUM DALAM KEMASAN MENGGUNAKAN MIKROKONTROLER ARDUINO MEGA 2560", "tahun": 2020},
    # Tahun 2022
    {"nama": "Lilis Agustina Sinaga", "nim": "180120201030", "judul": "PERANCANGAN JARINGAN FIBER OPTIK DI KELURAHAN DAIK KABUPATEN LINGGA KEPULAUAN RIAU STUDI KASUS DI PT. TELKOM RIKEP", "tahun": 2022},
    {"nama": "Riandra Putra", "nim": "150120201035", "judul": "RANCANGAN BANGUN SIMULATOR PASANG SURUT DI LABORATORIUM ENERGI BARU TERBARUKAN", "tahun": 2022},
    {"nama": "Reno Apriano", "nim": "150120201027", "judul": "RANCANGAN BANGUN PENGOLAHAN AIR LAUT MENJADI GARAM MENGGUNAKAN PARABOLIC TROUGH", "tahun": 2022},
    {"nama": "Ronaldo Lumban Tobing", "nim": "180120201034", "judul": "RANCANGAN BANGUN GERBANG GARASI MOBIL OTOMATIS MENGGUNAKAN MOTOR 3 PHASA DAN SENSOR PROXIMITY BERBASIS PLC OUTSEAL", "tahun": 2022},
    {"nama": "Allysia Shafira", "nim": "180120201037", "judul": "SISTEM MONITORING BERBASIS IoT MENGGUNAKAN TENAGA SURYA PADA PERTANIAN URBAN HORTIKULTURA", "tahun": 2022},
]

# Fungsi Bubble Sort
def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Fungsi Merge Sort
def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left, key)
        merge_sort(right, key)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][key] < right[j][key]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    return data

# Fungsi Quick Sort
def quick_sort(data, key):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = [x for x in data[1:] if x[key] <= pivot[key]]
    greater = [x for x in data[1:] if x[key] > pivot[key]]
    return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

# Fungsi Menampilkan Data
def tampilkan_data(data):
    print(f"{'Tahun':<6} {'Penulis':<30} {'Judul':<80}")
    print("=" * 120)
    for item in data:
        print(f"{item['tahun']:<6} {item['nama']:<30} {item['judul']:<80}")

# Menu Utama
def main():
    print("Program Pengurutan Data Skripsi Berdasarkan Tahun")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    pilihan = int(input("Pilih metode pengurutan (1/2/3): "))

    if pilihan == 1:
        sorted_data = bubble_sort(skripsi, "tahun")
        print("\nHasil Pengurutan dengan Bubble Sort:")
    elif pilihan == 2:
        sorted_data = merge_sort(skripsi, "tahun")
        print("\nHasil Pengurutan dengan Merge Sort:")
    elif pilihan == 3:
        sorted_data = quick_sort(skripsi, "tahun")
        print("\nHasil Pengurutan dengan Quick Sort:")
    else:
        print("Pilihan tidak valid.")
        return

    tampilkan_data(sorted_data)

# Jalankan Program
if name == "main":
    main()