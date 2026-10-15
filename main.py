from maps.k25058kkOsusume import k25058kkOsusume
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [k25058kkOsusume(), ]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()