import json
import pandas as pd

# 1. Baca file JSON
with open("Akmal_Mustaqim_V3925039.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 2. Buat file Excel
with pd.ExcelWriter("Data_Output.xlsx") as writer:
    # Loop setiap kategori di JSON (Hewan, Buah, Kendaraan, Negara)
    for kategori, isi in data.items():
        # Ubah ke DataFrame
        df = pd.DataFrame(isi)
        # Simpan ke sheet dengan nama sesuai kategori
        df.to_excel(writer, sheet_name=kategori, index=False)

print("✅ Berhasil diubah ke Excel: Data_Output.xlsx")
