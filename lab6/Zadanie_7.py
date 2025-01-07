import matplotlib.pyplot as plt


kategorie = ['Elektronika', 'Odzież', 'Żywność', 'Książki', 'Zabawki']
sprzedaz = [120, 80, 150, 60, 100]


plt.figure(figsize=(7, 7))
plt.pie(sprzedaz, labels=kategorie, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Procentowy udział kategorii w sprzedaży', fontsize=14)
plt.show()
