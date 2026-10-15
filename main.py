from maps import hyatoOsusume, k25058kkOsusume, MakibaOsusume, MakibaOsusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [
    MakibaOsusume.GakushokuSample(),
    hyatoOsusume.GakushokuSample(),
    k25058kkOsusume.GakushokuSample(),
    MakibaOsusume.GakushokuSample(),
    ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
