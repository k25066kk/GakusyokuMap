from maps import K25066_Osusume, MakibaOsusume, hyatoOsusume, k25058kkOsusume
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [
    hyatoOsusume.GakushokuSample(),
    k25058kkOsusume.GakushokuSample(),
    K25066_Osusume.K25066_osusume(),
    MakibaOsusume.GakushokuSample(),
]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
