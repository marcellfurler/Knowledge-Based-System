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
        """Definisi aturan-aturan dalam bentuk rule-based system"""
        self.rules = [
            {
                "name": "rule_lokasi",
                "condition": self.check_lokasi,
                "action": self.action_lokasi_match
            },
            {
                "name": "rule_jenis_wisata",
                "condition": self.check_jenis_wisata,
                "action": self.action_jenis_match
            },
            {
                "name": "rule_outdoor_indoor",
                "condition": self.check_outdoor_indoor,
                "action": self.action_outdoor_indoor_match
            },
            {
                "name": "rule_hari_kunjungan",
                "condition": self.check_hari_kunjungan,
                "action": self.action_hari_match
            }
        ]

    # Rule Conditions with IF-THEN-ELSE Logic
    def check_lokasi(self, user_facts, place):
        """Rule Lokasi dengan IF-THEN-ELSE"""
        user_lokasi = user_facts.get('lokasi', '').lower()
        place_lokasi = place.get('lokasi', '').lower()
        
        # IF user tidak menentukan lokasi
        if not user_lokasi:
            # THEN tempat manapun bisa direkomendasikan
            return True
        # ELSE IF lokasi user sama dengan lokasi tempat
        elif user_lokasi == place_lokasi:
            # THEN tempat cocok
            return True
        # ELSE lokasi tidak cocok
        else:
            # THEN tempat tidak cocok
            return False

    def check_jenis_wisata(self, user_facts, place):
        """Rule Jenis Wisata dengan IF-THEN-ELSE"""
        user_jenis = user_facts.get('jenis_wisata', '').lower()
        place_jenis = place.get('type', '').lower()
        
        # IF user tidak menentukan jenis wisata
        if not user_jenis:
            # THEN tempat dengan jenis apapun bisa direkomendasikan
            return True
        # ELSE IF jenis wisata user sama dengan jenis tempat
        elif user_jenis == place_jenis:
            # THEN tempat cocok
            return True
        # ELSE jenis wisata tidak cocok
        else:
            # THEN tempat tidak cocok
            return False

    def check_outdoor_indoor(self, user_facts, place):
        """Rule Outdoor/Indoor dengan IF-THEN-ELSE"""
        user_preferensi = user_facts.get('outdoor_indoor', '').lower()
        place_preferensi = place.get('outdoor_indoor', '').lower()
        
        # IF user tidak menentukan preferensi outdoor/indoor
        if not user_preferensi:
            # THEN tempat dengan preferensi apapun bisa direkomendasikan
            return True
        # ELSE IF preferensi user sama dengan preferensi tempat
        elif user_preferensi == place_preferensi:
            # THEN tempat cocok
            return True
        # ELSE preferensi tidak cocok
        else:
            # THEN tempat tidak cocok
            return False

    def check_hari_kunjungan(self, user_facts, place):
        """Rule Hari Kunjungan dengan IF-THEN-ELSE"""
        user_hari = user_facts.get('hari_kunjungan', '').lower()
        operasional = place.get('operasional_hari', 'all').lower()
        
        # IF user tidak menentukan hari kunjungan
        if not user_hari:
            # THEN tempat dengan hari operasional apapun bisa direkomendasikan
            return True
        # ELSE IF tempat buka setiap hari
        elif operasional == 'all':
            # THEN tempat cocok untuk hari apapun
            return True
        # ELSE IF user pilih weekday dan tempat buka weekday
        elif user_hari == 'weekday' and 'weekday' in operasional:
            # THEN tempat cocok
            return True
        # ELSE IF user pilih weekend dan tempat buka weekend
        elif user_hari == 'weekend' and 'weekend' in operasional:
            # THEN tempat tidak cocok
            return True
        # ELSE hari tidak cocok dengan operasional
        else:
            # THEN tempat tidak cocok
            return False

    def check_ukuran_grup(self, user_facts, place):
        """Rule Ukuran Grup dengan IF-THEN-ELSE"""
        user_grup = user_facts.get('ukuran_grup', '').lower()
        cocok_untuk = place.get('cocok_untuk', 'all').lower()
        
        # IF user tidak menentukan ukuran grup
        if not user_grup:
            # THEN tempat dengan kapasitas apapun bisa direkomendasikan
            return True
        # ELSE IF tempat cocok untuk semua ukuran grup
        elif cocok_untuk == 'all':
            # THEN tempat cocok untuk grup apapun
            return True
        # ELSE IF ukuran grup user sesuai dengan yang cocok untuk tempat
        elif user_grup in cocok_untuk:
            # THEN tempat cocok
            return True
        # ELSE ukuran grup tidak cocok
        else:
            # THEN tempat tidak cocok
            return False

    # Rule Actions
    def action_lokasi_match(self, place_name, result):
        """Action ketika rule lokasi terpenuhi"""
        self.facts.setdefault(place_name, {})
        self.facts[place_name]['lokasi_match'] = result

    def action_jenis_match(self, place_name, result):
        """Action ketika rule jenis wisata terpenuhi"""
        self.facts.setdefault(place_name, {})
        self.facts[place_name]['jenis_match'] = result

    def action_outdoor_indoor_match(self, place_name, result):
        """Action ketika rule outdoor/indoor terpenuhi"""
        self.facts.setdefault(place_name, {})
        self.facts[place_name]['outdoor_indoor_match'] = result

    def action_hari_match(self, place_name, result):
        """Action ketika rule hari kunjungan terpenuhi"""
        self.facts.setdefault(place_name, {})
        self.facts[place_name]['hari_match'] = result

    def action_grup_match(self, place_name, result):
        """Action ketika rule ukuran grup terpenuhi"""
        self.facts.setdefault(place_name, {})
        self.facts[place_name]['grup_match'] = result

    def get_unique_lokasi(self) -> List[str]:  
        cursor = self.connection.cursor()
        cursor.execute("SELECT DISTINCT lokasi FROM tempat_wisatakbs")
        results = cursor.fetchall()
        cursor.close()
        
        return [row[0] for row in results if row[0]]
    
    def get_unique_jenis_wisata(self) -> List[str]:
        """Mengambil semua jenis wisata unik dari database"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT DISTINCT type FROM tempat_wisatakbs")
        results = cursor.fetchall()
        cursor.close()
        
        return [row[0] for row in results if row[0]]



# ========================
# 2. RULE ENGINE
# ========================
class RuleEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def apply_rules(self, user_facts: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Menerapkan semua rules pada setiap tempat wisata"""
        places = self.kb.load_places()
        self.kb.facts = {}
        recommendations = []

        print("\n=== Menjalankan Rule Engine ===")
        
        for place in places:
            # Terapkan setiap rule dengan IF-THEN-ELSE logic
            all_rules_satisfied = True
            
            for rule in self.kb.rules:
                # Cek kondisi rule dengan IF-THEN-ELSE
                condition_result = rule['condition'](user_facts, place)
                
                # Jalankan action rule
                rule['action'](place['nama'], condition_result)
                
                # Jika ada rule yang tidak terpenuhi, tempat ini tidak direkomendasikan
                if not condition_result:
                    all_rules_satisfied = False
            
            # Hasil akhir evaluasi
            if all_rules_satisfied:
                recommendations.append(place)

        return recommendations

# ========================
# 3. MAIN SYSTEM
# ========================
class TourismRecommendationSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.rule_engine = RuleEngine(self.kb)

    def get_user_input(self):
        """Mengambil input dari user dengan 5 pertanyaan"""
        print("\n=== Sistem Rekomendasi Wisata Rule-Based ===")

        # 1. Tampilkan lokasi
        lokasi_tersedia = self.kb.get_unique_lokasi()
        print("\n📍 Daftar lokasi yang tersedia:")
        for loc in lokasi_tersedia:
            print(f" - {loc}")
        lokasi = input("\n1. Lokasi yang diinginkan: ").strip()

        # 2. Tampilkan jenis wisata
        jenis_tersedia = self.kb.get_unique_jenis_wisata()
        print("\n🏷️ Jenis tempat wisata yang tersedia:")
        for jenis in jenis_tersedia:
            print(f" - {jenis}")
        jenis = input("2. Jenis tempat wisata: ").strip()

        # 3. Outdoor/Indoor
        print("\n🌤️ Pilihan preferensi: outdoor, indoor")
        outdoor_indoor = input("3. Preferensi outdoor/indoor: ").strip()

        # 4. Hari kunjungan
        print("\n📅 Pilihan hari: weekday, weekend")
        hari = input("4. Hari kunjungan: ").strip()


        return {
            'lokasi': lokasi.lower() if lokasi else None,
            'jenis_wisata': jenis.lower() if jenis else None,
            'outdoor_indoor': outdoor_indoor.lower() if outdoor_indoor else None,
            'hari_kunjungan': hari.lower() if hari else None,
        }



    def display_recommendations(self, recommendations):
        """Menampilkan hasil rekomendasi"""
        if recommendations:
            print("\n" + "="*50)
            print("=== HASIL REKOMENDASI TEMPAT WISATA ===")
            print("="*50)
            
            for i, rec in enumerate(recommendations, 1):
                print(f"\n{i}. {rec['nama']}")
                print(f"   Rating: {rec.get('vote_average', 'N/A')}")
                print(f"   Lokasi: {rec.get('lokasi', 'N/A')}")
                print(f"   Jenis: {rec.get('type', 'N/A')}")
                print(f"   Indoor/Outdoor: {rec.get('outdoor_indoor', 'N/A')}")
                print(f"   Deskripsi: {rec.get('description', 'Tidak ada deskripsi')}")
                if rec.get('gambar'):
                    print(f"   Gambar: {rec['gambar']}")
                print(f"   Lokasi Map: {rec.get('maps', 'N/A')}")
                print("-" * 40)
        else:
            print("\n❌ Tidak ditemukan tempat wisata yang sesuai dengan semua kriteria rule-based.")
            print("Coba ubah kriteria pencarian Anda.")

    def run(self):
        try:
            # Inisialisasi knowledge base dan rules
            self.kb.connect_db()
            self.kb.load_rules()

            # Ambil input user
            user_facts = self.get_user_input()
            
            print(f"\n=== Input User ===")
            print(f"Lokasi: {user_facts['lokasi']}")
            print(f"Jenis Wisata: {user_facts['jenis_wisata']}")
            print(f"Outdoor/Indoor: {user_facts['outdoor_indoor']}")
            print(f"Hari Kunjungan: {user_facts['hari_kunjungan']}")


            # Terapkan rules dan dapatkan rekomendasi
            recommendations = self.rule_engine.apply_rules(user_facts)

            # Tampilkan hasil
            self.display_recommendations(recommendations)

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