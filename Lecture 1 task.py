Math = []
DBMS = []
DSA = []
total = []
percentage = []
avg = []

for i in range(3):
    print("\t\t\t For Student:", i+1)
    Math.append(int(input("Enter Your Maths Marks: ")))
    DBMS.append(int(input("Enter Your DBMS Marks: ")))
    DSA.append(int(input("Enter Your DSA Marks: ")))
    total_marks = Math[i] + DBMS[i] + DSA[i]
    total.append(total_marks)
    avg_marks = total_marks / 3
    avg.append(avg_marks)
    percent = (total_marks / 300) * 100
    percentage.append(percent)

for j in range(3):
    print(f"Student:{j+1} Maths Marks:", Math[j], "DBMS:", DBMS[j], "DSA:", DSA[j], "Total Marks:", total[j],
          "Average Marks:", avg[j], "Percentage:", percentage[j])
