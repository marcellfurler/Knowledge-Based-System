import csv

def read_data(file_path):
    try:
        data = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        # print(f"File tidak ditemukan: {file_path}")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

# Fungsi untuk merekomendasikan tempat wisata
def recommend_places(data, location, place_type, indoor_outdoor):
    recommendations = []
    for place in data:
        if (place['lokasi'].lower() == location.lower() and
            place['type'].lower() == place_type.lower() and
            place['outdoor_indoor'].lower() == indoor_outdoor.lower()):
            recommendations.append(place)
    return recommendations

# Main program
def main():
    # Membaca data dari CSV
    data = read_data('data_set.csv')

    lokasi = ["Kota Yogyakarta", "Sleman", "Magelang", "Bantul", "Kulon Progo", "Gunung Kidul", "Klaten"]
    type = ["Sejarah", "Kebun Binatang", "Pantai", "Wisata", "Alam", "Wisata Air", "Buatan", "Agrowisata"]
    oi = ["Indoor", "Outdoor"]

    # Mengambil input dari pengguna

    for i in lokasi:
        print(i)
    locations = input("Masukkan lokasi (pisahkan dengan koma jika lebih dari satu): ")
    
    for i in type:
        print(i)
    place_type = input("Masukkan jenis tempat wisata: ")

    indoor_outdoor = input("Masukkan indoor atau outdoor: ")

    # Memisahkan lokasi berdasarkan koma dan menghapus spasi
    location_list = [loc.strip() for loc in locations.split(',')]

    recommendations = []

    # Rekomendasi berdasarkan kombinasi input
    for location in location_list:
        if location.lower() == "sleman":
            if place_type.lower() == "sejarah":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Sleman", "Sejarah", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Sleman", "Sejarah", "outdoor")
            elif place_type.lower() == "wisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Sleman", "Wisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Sleman", "Wisata", "outdoor")
            elif place_type.lower() == "kebun binatang":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Sleman", "Kebun Binatang", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Sleman", "Kebun Binatang", "outdoor")
            elif place_type.lower() == "pantai":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Sleman", "Pantai", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Sleman", "Pantai", "outdoor")
            elif place_type.lower() == "alam":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Sleman", "Alam", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Sleman", "Alam", "outdoor")
            elif place_type.lower() == "wisata air":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Sleman", "Wisata Air", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Sleman", "Wisata Air", "outdoor")
            elif place_type.lower() == "buatan":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Sleman", "Buatan", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Sleman", "Buatan", "outdoor")
            elif place_type.lower() == "agrowisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Sleman", "Agrowisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Sleman", "Agrowisata", "outdoor")

        elif location.lower() == "kota yogyakarta":
            if place_type.lower() == "sejarah":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Sejarah", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Sejarah", "outdoor")
            elif place_type.lower() == "wisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Wisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Wisata", "outdoor")
            elif place_type.lower() == "kebun binatang":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Kebun Binatang", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Kebun Binatang", "outdoor")
            elif place_type.lower() == "pantai":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Pantai.", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Pantai", "outdoor")
            elif place_type.lower() == "alam":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Alam", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Alam", "outdoor")
            elif place_type.lower() == "wisata air":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Wisata Air", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Wisata Air", "outdoor")
            elif place_type.lower() == "buatan":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Buatan", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Buatan", "outdoor")
            elif place_type.lower() == "agrowisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Agrowisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kota Yogyakarta", "Agrowisata", "outdoor")

        elif location.lower() == "magelang":
            if place_type.lower() == "sejarah":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Magelang", "Sejarah", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Magelang", "Sejarah", "outdoor")
            elif place_type.lower() == "wisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Magelang", "Wisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Magelang", "Wisata", "outdoor")
            elif place_type.lower() == "kebun binatang":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Magelang", "Kebun Binatang", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Magelang", "Kebun Binatang", "outdoor")
            elif place_type.lower() == "pantai":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Magelang", "Pantai.", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Magelang", "Pantai", "outdoor")
            elif place_type.lower() == "alam":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Magelang", "Alam", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Magelang", "Alam", "outdoor")
            elif place_type.lower() == "wisata air":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Magelang", "Wisata Air", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Magelang", "Wisata Air", "outdoor")
            elif place_type.lower() == "buatan":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Magelang", "Buatan", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Magelang", "Buatan", "outdoor")
            elif place_type.lower() == "agrowisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Magelang", "Agrowisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Magelang", "Agrowisata", "outdoor")

        elif location.lower() == "bantul":
            if place_type.lower() == "sejarah":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Bantul", "Sejarah", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Bantul", "Sejarah", "outdoor")
            elif place_type.lower() == "wisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Bantul", "Wisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Bantul", "Wisata", "outdoor")
            elif place_type.lower() == "kebun binatang":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Bantul", "Kebun Binatang", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Bantul", "Kebun Binatang", "outdoor")
            elif place_type.lower() == "pantai":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Bantul", "Pantai.", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Bantul", "Pantai", "outdoor")
            elif place_type.lower() == "alam":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Bantul", "Alam", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Bantul", "Alam", "outdoor")
            elif place_type.lower() == "wisata air":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Bantul", "Wisata Air", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Bantul", "Wisata Air", "outdoor")
            elif place_type.lower() == "buatan":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Bantul", "Buatan", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Bantul", "Buatan", "outdoor")
            elif place_type.lower() == "agrowisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Bantul", "Agrowisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Bantul", "Agrowisata", "outdoor")

        elif location.lower() == "kulon progo":
            if place_type.lower() == "sejarah":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Sejarah", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Sejarah", "outdoor")
            elif place_type.lower() == "wisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Wisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Wisata", "outdoor")
            elif place_type.lower() == "kebun binatang":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Kebun Binatang", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Kebun Binatang", "outdoor")
            elif place_type.lower() == "pantai":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Pantai.", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Pantai", "outdoor")
            elif place_type.lower() == "alam":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Alam", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Alam", "outdoor")
            elif place_type.lower() == "wisata air":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Wisata Air", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Wisata Air", "outdoor")
            elif place_type.lower() == "buatan":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Buatan", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Buatan", "outdoor")
            elif place_type.lower() == "agrowisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Agrowisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Kulon Progo", "Agrowisata", "outdoor")

        elif location.lower() == "gunung kidul":
            if place_type.lower() == "sejarah":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Sejarah", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Sejarah", "outdoor")
            elif place_type.lower() == "wisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Wisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Wisata", "outdoor")
            elif place_type.lower() == "kebun binatang":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Kebun Binatang", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Kebun Binatang", "outdoor")
            elif place_type.lower() == "pantai":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Pantai.", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Pantai", "outdoor")
            elif place_type.lower() == "alam":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Alam", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Alam", "outdoor")
            elif place_type.lower() == "wisata air":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Wisata Air", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Wisata Air", "outdoor")
            elif place_type.lower() == "buatan":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Buatan", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Buatan", "outdoor")
            elif place_type.lower() == "agrowisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Agrowisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Gunung Kidul", "Agrowisata", "outdoor")

        elif location.lower() == "klaten":
            if place_type.lower() == "sejarah":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Klaten", "Sejarah", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Klaten", "Sejarah", "outdoor")
            elif place_type.lower() == "wisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Klaten", "Wisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Klaten", "Wisata", "outdoor")
            elif place_type.lower() == "kebun binatang":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Klaten", "Kebun Binatang", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Klaten", "Kebun Binatang", "outdoor")
            elif place_type.lower() == "pantai":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Klaten", "Pantai.", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Klaten", "Pantai", "outdoor")
            elif place_type.lower() == "alam":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Klaten", "Alam", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Klaten", "Alam", "outdoor")
            elif place_type.lower() == "wisata air":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Klaten", "Wisata Air", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Klaten", "Wisata Air", "outdoor")
            elif place_type.lower() == "buatan":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Klaten", "Buatan", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Klaten", "Buatan", "outdoor")
            elif place_type.lower() == "agrowisata":
                if indoor_outdoor.lower() == "indoor":
                    recommendations += recommend_places(data, "Klaten", "Agrowisata", "indoor")
                elif indoor_outdoor.lower() == "outdoor":
                    recommendations += recommend_places(data, "Klaten", "Agrowisata", "outdoor")
    # Menampilkan hasil rekomendasi
    if recommendations:
        print("\nRekomendasi Tempat Wisata:")
        for place in recommendations:
            print(f"- {place['nama']} (Rating: {place['vote_average']})")
            print(f"  Deskripsi: {place['description']}")
            print(f"  Gambar: {place['gambar']}\n")
    else:
        print("Tidak ada tempat wisata yang sesuai dengan kriteria Anda.")

if __name__ == "__main__":
    main()
