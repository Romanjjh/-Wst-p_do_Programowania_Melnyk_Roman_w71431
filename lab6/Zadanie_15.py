import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Term 1": [78, 85, 92, 88, 76],
    "Term 2": [80, 83, 95, 90, 78],
    "Final Exam": [85, 88, 94, 91, 82]
}
df = pd.DataFrame(data)


plt.figure(figsize=(10, 6))
for column in df.columns:
    plt.plot(df.index, df[column], label=column, marker='o')

plt.title("Grades Distribution Across Terms")
plt.xlabel("Student Index")
plt.ylabel("Grades")
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(df.index, df["Term 1"], label="Term 1", linestyle='--', color='blue', marker='s')
plt.plot(df.index, df["Term 2"], label="Term 2", linestyle='-.', color='green', marker='o')
plt.plot(df.index, df["Final Exam"], label="Final Exam", linestyle='-', color='red', marker='x')

plt.title("Grades Comparison Across Terms", fontsize=14)
plt.xlabel("Student Index", fontsize=12)
plt.ylabel("Grades", fontsize=12)
plt.legend(title="Exam Terms")
plt.grid(True)
plt.show()
