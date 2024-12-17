import pandas as pd

df = pd.read_csv('demografia.csv', decimal='.', na_values=".")


maxPK = df.max()[1:]
maxP = maxPK.max()
maxPiD = maxPK.idxmax()
maxPiw =  df[maxPiD].idxmax()


print(maxP)
print(f'najwiekszy przyrost w wysokosci : {maxP}\n '
      f"mial miejsce w roku: {maxPiD} \n"
      f"w kraju: {df["KRAJE"][maxPiw]}")

