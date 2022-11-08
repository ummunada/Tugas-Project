print("-------*** PROGRAM MENGHITUNG BODY MASS INDEX ***-------")

x = float(input("Masukkan Tinggi Badan : ")) / 100 #dibagi 100 agar menjadi (m)
y = float(input("Masukkan Berat Badan : "))
#BMI = berat badan (kg) / (tinggi badan (m)^2)
nilai_bmi = y / (x**2)
print("Nilai BMI : ", nilai_bmi)

if nilai_bmi < 18.5:
    print("Underweight")
elif nilai_bmi >= 18.5 and nilai_bmi <= 24.9:
    print("Normal weight")
elif nilai_bmi >= 25.0 and nilai_bmi <= 29.9:
    print("Overweight")
elif nilai_bmi >= 30.0 and nilai_bmi <= 34.9:
    print("Obesity Class I")
elif nilai_bmi >= 35.0 and nilai_bmi <= 39.9:
    print("Obesity Clas II")
if nilai_bmi >= 40:
    print("Obesity Class III")