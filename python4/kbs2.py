import pandas as pd

def read_data(file_path):
    try:
        data = pd.read_csv(file_path, delimiter=';')
        return data
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return pd.DataFrame()

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print("Input tidak boleh kosong.")
        elif user_input.lower() not in [option.lower() for option in valid_options]:
            print(f"Input tidak valid. Pilihan yang tersedia: {', '.join(valid_options)}")
        else:
            return user_input

def recommend_places(data, filters):
    for key, value in filters.items():
        if value:
            data = data[data[key].str.lower() == value.lower()]
    return data

def main():
    data = read_data('data_set.csv')

    if data.empty:
        return

    # Ambil daftar opsi unik dari dataset
    lokasi_options = data['lokasi'].dropna().unique().tolist()
    type_options = data['type'].dropna().unique().tolist()
    indoor_outdoor_options = data['outdoor_indoor'].dropna().unique().tolist()

    # Validasi input user
    location = get_valid_input("Masukkan lokasi: ", lokasi_options)
    place_type = get_valid_input("Masukkan jenis tempat wisata: ", type_options)
    indoor_outdoor = get_valid_input("Masukkan indoor atau outdoor: ", indoor_outdoor_options)

    filters = {
        'lokasi': location,
        'type': place_type,
        'outdoor_indoor': indoor_outdoor
    }

    recommendations = recommend_places(data, filters)

    if not recommendations.empty:
        print("\nRekomendasi Tempat Wisata:")
        for index, place in recommendations.iterrows():
            print(f"- {place['nama']} (Rating: {place['vote_average']})")
            print(f"  Deskripsi: {place['description']}")
            print(f"  Gambar: {place['gambar']}\n")
    else:
        print("Tidak ada tempat wisata yang sesuai dengan kriteria Anda.")

if __name__ == "__main__":
    main()
