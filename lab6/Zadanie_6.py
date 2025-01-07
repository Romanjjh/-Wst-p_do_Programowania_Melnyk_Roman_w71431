import matplotlib.pyplot as plt

kategorie = ['Elektronika', 'Odzież', 'Żywność', 'Książki', 'Zabawki']
ilosc_sprzedanych = [120, 80, 150, 60, 100]


plt.figure(figsize=(8, 5))
plt.bar(kategorie, ilosc_sprzedanych, color='skyblue')
plt.title('Ilość sprzedanych produktów w różnych kategoriach', fontsize=14)
plt.xlabel('Kategorie', fontsize=12)
plt.ylabel('Ilość sprzedanych produktów', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.tight_layout()
plt.show()
