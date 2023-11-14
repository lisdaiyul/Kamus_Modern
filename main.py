modern_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")


if word in modern_dict.keys():
    print("Masksud dari kata", word,"adalah", modern_dict[word])
else:
    print("Maaf kamusnya kurang lengkap. (￢_￢)")
