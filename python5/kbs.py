import mysql.connector
from typing import List, Dict, Any

# ========================
# 1. KNOWLEDGE BASE MODULE
# ========================
class KnowledgeBase:
    def __init__(self):
        self.connection = None
        self.rules = []
        self.facts = {}

    def connect_db(self):
        """Koneksi ke database"""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='kbs'
            )
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            raise

    def load_places(self) -> List[Dict[str, Any]]:
        """Load semua data tempat wisata dari database"""
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tempat_wisatakbs")
        data = cursor.fetchall()
        cursor.close()
        return data

    def load_rules(self):
        """Definisi aturan-aturan dalam bentuk fungsi untuk forward chaining"""
        self.rules = [
            {
                "name": "lokasi_cocok",
                "apply": self.rule_lokasi_cocok
            },
            {
                "name": "jenis_cocok", 
                "apply": self.rule_jenis_cocok
            },
            {
                "name": "indoor_outdoor_cocok",
                "apply": self.rule_indoor_outdoor_cocok
            }
        ]

    def rule_lokasi_cocok(self, user_facts, places):
        """Aturan pencocokan lokasi"""
        for place in places:
            cocok = False
            if not user_facts['lokasi']:
                cocok = True
            else:
                for loc in user_facts['lokasi']:
                    if place['lokasi'] and place['lokasi'].lower() == loc.lower():
                        cocok = True
                        break
            self.facts.setdefault(place['nama'], {})
            self.facts[place['nama']]['lokasi_cocok'] = cocok

    def rule_jenis_cocok(self, user_facts, places):
        """Aturan pencocokan jenis wisata"""
        for place in places:
            cocok = False
            if not user_facts['type']:
                cocok = True
            else:
                if place['type'] and place['type'].lower() == user_facts['type'].lower():
                    cocok = True
            self.facts.setdefault(place['nama'], {})
            self.facts[place['nama']]['jenis_cocok'] = cocok

    def rule_indoor_outdoor_cocok(self, user_facts, places):
        """Aturan pencocokan indoor/outdoor"""
        for place in places:
            cocok = False
            if not user_facts['outdoor_indoor']:
                cocok = True
            else:
                if place['outdoor_indoor'] and place['outdoor_indoor'].lower() == user_facts['outdoor_indoor'].lower():
                    cocok = True
            self.facts.setdefault(place['nama'], {})
            self.facts[place['nama']]['indoor_outdoor_cocok'] = cocok

# ========================
# 2. FILTER ENGINE
# ========================
class FilterEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def filter_places(self, user_facts: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Proses forward chaining dengan menerapkan aturan satu per satu"""
        places = self.kb.load_places()
        self.kb.facts = {}

        # Terapkan aturan secara berurutan (forward chaining)
        for rule in self.kb.rules:
            rule['apply'](user_facts, places)

        # Setelah aturan semua diterapkan, cek tempat yang memenuhi semua fakta cocok = True
        recommendations = []
        for place in places:
            fakta_tempat = self.kb.facts.get(place['nama'], {})
            # Semua kondisi harus True supaya rekomendasi
            if all(fakta_tempat.get(cond, False) for cond in ['lokasi_cocok', 'jenis_cocok', 'indoor_outdoor_cocok']):
                recommendations.append(place)

        return recommendations

# ========================
# 3. MAIN SYSTEM
# ========================
class TourismRecommendationSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.filter_engine = FilterEngine(self.kb)

    def run(self):
        try:
            # Inisialisasi knowledge base dan aturan
            self.kb.connect_db()
            self.kb.load_rules()

            # Input user - hanya 3 pertanyaan
            print("\n=== Sistem Rekomendasi Wisata ===")
            lokasi_input = input("Masukkan lokasi (pisahkan koma jika banyak): ").strip()
            jenis_input = input("Masukkan jenis tempat (kosongkan jika tidak penting): ").strip()
            io_input = input("Masukkan indoor/outdoor (kosongkan jika tidak penting): ").strip()

            # Bangun fakta user
            user_facts = {
                'lokasi': [loc.strip() for loc in lokasi_input.split(',')] if lokasi_input else None,
                'type': jenis_input if jenis_input else None,
                'outdoor_indoor': io_input if io_input else None
            }

            # Proses filter forward chaining
            recommendations = self.filter_engine.filter_places(user_facts)

            # Tampilkan hasil sesuai format yang diminta
            if recommendations:
                print("\n=== Rekomendasi Tempat Wisata ===")
                for rec in recommendations:
                    print(f"\n- {rec['nama']} (Rating: {rec.get('vote_average', 'N/A')})")
                    print(f"  Lokasi: {rec.get('lokasi', 'N/A')}")
                    print(f"  Deskripsi: {rec.get('description', 'Tidak ada deskripsi')}")
                    if rec.get('gambar'):
                        print(f"  Gambar: {rec['gambar']}")
                    print(f"  Lokasi Map: {rec.get('maps', 'N/A')}")
                    print(f"  Jenis: {rec.get('type', 'N/A')}")
                    print(f"  Indoor/Outdoor: {rec.get('outdoor_indoor', 'N/A')}")
            else:
                print("Tidak ditemukan rekomendasi yang sesuai.")

        except Exception as e:
            print(f"System Error: {e}")
        finally:
            if self.kb.connection:
                self.kb.connection.close()

# ========================
# RUN SYSTEM
# ========================
if __name__ == "__main__":
    system = TourismRecommendationSystem()
    system.run()