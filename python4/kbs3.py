import mysql.connector

# Fungsi untuk menghubungkan ke database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Ganti dengan username database Anda
            password='',  # Ganti dengan password database Anda
            database='kbs'  # Ganti dengan nama database Anda
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Fungsi untuk mengambil data dari database
def fetch_data(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tempat_wisatakbs")  # Ganti dengan nama tabel Anda
    data = cursor.fetchall()
    cursor.close()
    return data

# Fungsi untuk menerapkan forward chaining dengan aturan if-then-else
def forward_chaining(data, location, place_type, indoor_outdoor):
    recommendations = []

    # Aturan berbasis lokasi
    for place in data:
        if place['lokasi'].lower() == location.lower():
            # Aturan berbasis jenis tempat
            if place['type'].lower() == place_type.lower():
                # Aturan berbasis indoor/outdoor
                if place['outdoor_indoor'].lower() == indoor_outdoor.lower():
                    recommendations.append(place)
                else:
                    # Jika indoor/outdoor tidak cocok, bisa menambahkan aturan lain
                    if indoor_outdoor.lower() == "indoor" and place['outdoor_indoor'].lower() == "outdoor":
                        continue  # Tidak merekomendasikan tempat outdoor jika pengguna memilih indoor
                    elif indoor_outdoor.lower() == "outdoor" and place['outdoor_indoor'].lower() == "indoor":
                        continue  # Tidak merekomendasikan tempat indoor jika pengguna memilih outdoor

    return recommendations

# Main program
def main():
    # Menghubungkan ke database
    connection = connect_to_database()
    if connection is None:
        return

    # Mengambil data dari database
    data = fetch_data(connection)

    # Mengambil input dari pengguna
    locations = input("Masukkan lokasi (pisahkan dengan koma jika lebih dari satu): ")
    place_type = input("Masukkan jenis tempat wisata: ")
    indoor_outdoor = input("Masukkan indoor atau outdoor: ")

    # Memisahkan lokasi berdasarkan koma dan menghapus spasi
    location_list = [loc.strip() for loc in locations.split(',')]

    recommendations = []

    # Rekomendasi berdasarkan kombinasi input
    for location in location_list:
        recommendations += forward_chaining(data, location, place_type, indoor_outdoor)

    # Menampilkan hasil rekomendasi
    if recommendations:
        print("\nRekomendasi Tempat Wisata:")
        for place in recommendations:
            print(f"- {place['nama']} (Rating: {place['vote_average']})")
            print(f"  Deskripsi: {place['description']}")
            print(f"  Gambar: {place['gambar']}\n")
    else:
        print("Tidak ada tempat wisata yang sesuai dengan kriteria Anda.")

    # Menutup koneksi database
    connection.close()

if __name__ == "__main__":
    main()
