import pandas as pd
import matplotlib.pyplot as plt

# โหลดไฟล์
df = pd.read_csv("singapore_pertussis_2012-2025_weekly.csv")

print(df.head())

# ===== 1) TREND รายปี =====
yearly = df.groupby("year")["patients"].sum().reset_index()

plt.figure()
plt.plot(yearly["year"], yearly["patients"], marker="o")
plt.title("Pertussis Cases by Year")
plt.xlabel("Year")
plt.ylabel("Total Patients")
plt.grid(True)
plt.savefig("trend_year.png")
plt.show()

# ===== 2) Seasonality รายสัปดาห์ =====
weekly_avg = df.groupby("week")["patients"].mean().reset_index()

plt.figure()
plt.plot(weekly_avg["week"], weekly_avg["patients"])
plt.title("Average Cases by Week (Seasonality)")
plt.xlabel("Week")
plt.ylabel("Average Patients")
plt.grid(True)
plt.savefig("seasonality_week.png")
plt.show()

# ===== 3) Moving Average รายสัปดาห์ล่าสุด =====
df = df.sort_values(["year", "week"])
df["ma_4week"] = df["patients"].rolling(4).mean()

plt.figure()
plt.plot(df["patients"].values, label="Weekly cases")
plt.plot(df["ma_4week"].values, label="4-week Moving Avg")
plt.legend()
plt.title("Weekly Cases + Moving Average")
plt.savefig("moving_avg.png")
plt.show()
