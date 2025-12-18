# Q1.A fitness app needs a Python program to analyze a user’s weekly exercise data.
#	Input: 7-day exercise minutes (list of integers).
#	Validate values using only conditions (no exceptions).
#	Calculate:
#	Total minutes
#	Average minutes
#	Highest and lowest workout day
#	Classify performance using if-elif-else:
#	< 70 → Poor
#	70–150 → Moderate
#	150+ → Excellent
#	Use list slicing to show first 3 days and last 3 days.
#	Use sets to remove repeated values.
#	Use a function get_summary(data_list) to return a dictionary containing:
#	“total”, “average”, “max”, “min”, “unique_values”

def get_summary(data_list):
    
    total = sum(data_list)
    average = total / len(data_list)
    max_val = max(data_list)
    min_val = min(data_list)
    unique_vals = set(data_list)

    return {
        "total": total,
        "average": average,
        "max": max_val,
        "min": min_val,
        "unique_values": unique_vals
    }

data = []

print("Enter exercise minutes for 7 days:")

for i in range(7):
    val = int(input(f"Day {i+1}: "))

    if val < 0:
        print("Invalid! Minutes cannot be negative. Enter again.")
        val = int(input(f"Day {i+1}: "))

    data.append(val)

summary = get_summary(data)

total = summary["total"]
average = summary["average"]
max_val = summary["max"]
min_val = summary["min"]
unique_vals = summary["unique_values"]

if total < 70:
    performance = "Poor"
elif 70 <= total <= 150:
    performance = "Moderate"
else:
    performance = "Excellent"

print("\n----- FITNESS SUMMARY -----")
print("Total Minutes     :", total)
print("Average Minutes   :", round(average, 2))
print("Highest Workout   :", max_val)
print("Lowest Workout    :", min_val)
print("Performance Level :", performance)

print("\nFirst 3 Days Data :", data[:3])   
print("Last 3 Days Data  :", data[-3:])  

print("Unique Values     :", unique_vals)
