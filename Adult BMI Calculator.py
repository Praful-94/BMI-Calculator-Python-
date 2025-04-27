#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import display, HTML
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Adult Body Mass Index (BMI) Calculator
# Reference: https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html

while True:
    # Input: Gender validation
    while True:
        display(HTML("<span style='color: orange; font-weight: bold;'>Enter Your Gender ('Male' / 'Female'):</span>"))
        gender = input().strip().lower()
        if gender in ['male', 'female']:
            break
        else:
            display(HTML("<span style='color: red;'>[Invalid input]. Please enter only 'Male' or 'Female'.</span>"))

    print()

    # Input: Age validation
    while True:
        try:
            display(HTML("<span style='color: orange; font-weight: bold;'>Enter Your Age (must be 18 or older):</span>"))
            age = int(input())
            if 18 <= age <= 110:
                break
            else:
                display(HTML(f"<span style='color: red;'>❌ Age {age} is invalid. You must be at least 18 years old.</span>"))
                display(HTML("<span style='color: red;'>BMI is calculated differently for children and teens.</span>"))
        except ValueError:
            display(HTML("<span style='color: red;'>[Invalid Input] Please enter numbers only.</span>"))

    print()

    # Input: Height
    while True:
        try:
            display(HTML("<span style='color: orange; font-weight: bold;'>Enter Your Height (between 20 and 280):</span>"))
            raw_height = float(input())
            if 20 <= raw_height <= 280:
                break
            else:
                display(HTML("<span style='color: red;'>[Invalid Input]. Height must be between 20 to 280.</span>"))
        except ValueError:
            display(HTML("<span style='color: red;'>[Invalid Input] Please enter a valid number.</span>"))

    print()

    # Input: Height unit
    while True:
        display(HTML("<span style='color: orange; font-weight: bold;'>Enter unit for height ('cm' or 'inch'):</span>"))
        height_unit = input().strip().lower()
        if height_unit in ['cm', 'inch']:
            break
        else:
            display(HTML("<span style='color: red;'>[Invalid input]. Enter only 'cm' or 'inch'.</span>"))

    print()

    # Input: Weight
    while True:
        try:
            display(HTML("<span style='color: orange; font-weight: bold;'>Enter your Weight:</span>"))
            raw_weight = float(input())
            if 2 <= raw_weight <= 1500:
                break
            else:
                display(HTML("<span style='color: red;'>[Invalid input]. Weight must be between 2 to 1500.</span>"))
        except ValueError:
            display(HTML("<span style='color: red;'>[Invalid Input] Please enter numbers only.</span>"))

    print()

    # Input: Weight unit
    while True:
        display(HTML("<span style='color: orange; font-weight: bold;'>Enter unit for weight ('kg' or 'pound'):</span>"))
        weight_unit = input().strip().lower()
        if weight_unit in ['kg', 'pound']:
            break
        else:
            display(HTML("<span style='color: red;'>[Invalid input]. Enter only 'kg' or 'pound'.</span>"))

    print()

    # Unit conversion
    height_cm = raw_height if height_unit == 'cm' else raw_height * 2.54
    weight_kg = raw_weight if weight_unit == 'kg' else raw_weight / 2.205

    # BMI Calculation
    bmi = weight_kg / ((height_cm / 100) ** 2)
    bmi_rounded = round(bmi, 2)

    # CDC BMI Categories
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 30 <= bmi < 35:
        category = "Obesity (Class 1)"
    elif 35 <= bmi < 40:
        category = "Obesity (Class 2)"
    else:
        category = "Extreme Obesity"

    # Display Results
    display(HTML("<h3 style='color:gray; font-weight:16x;'>🩺 BMI Report Card</h3>"))

    if gender == 'male':
        display(HTML("<span style='color: blue; font-weight: bold;'>You selected: Male</span>"))
    else:
        display(HTML("<span style='color: deeppink; font-weight: bold;'>You selected: Female</span>"))

    display(HTML(f"""
        Height   : <span style='color: blue; font-weight: bold;'>{raw_height} {height_unit}</span><br>
        Weight   : <span style='color: blue; font-weight: bold;'>{raw_weight} {weight_unit}</span><br>
        BMI      : <span style='color: blue; font-weight: bold;'>{bmi_rounded}</span><br>
        Category : <span style='color: blue; font-weight: bold;'>{category}</span>
    """))

    # Age-specific BMI guidance
    if 18 <= age <= 24:
        note = "Age Wise Normal BMI Range: 19 - 24 (Youth, fast metabolism)"
    elif 25 <= age <= 34:
        note = "Age Wise Normal BMI Range: 20 - 25 (Body fat starts increasing)"
    elif 35 <= age <= 44:
        note = "Age Wise Normal BMI Range: 21 - 26 (Muscle loss may begin)"
    elif 45 <= age <= 54:
        note = "Age Wise Normal BMI Range: 22 - 27 (Obesity risk rises)"
    elif 55 <= age <= 64:
        note = "Age Wise Normal BMI Range: 23 - 28 (Sedentary lifestyle common)"
    else:
        note = "Age Wise Normal BMI Range: 24 - 29 (Higher BMI may protect bones)"

    display(HTML(f"<span style='color: green;'>{note}</span>"))

    # Gender-specific notes
    print()
    if gender == 'male':
        print("✅ General Male Health Note:")
        print("• Body Fat : Lower (10–20%)")
        print("• Muscle Mass : Higher")
        print("• Fat Distribution : Abdomen (apple-shaped)")
        print("• Same BMI, Different Look : May appear leaner with same BMI")
        print("• Risk Thresholds : Health risks may appear at lower BMI if very muscular")
    elif gender == 'female':
        print("✅ General Female Health Note:")
        print("• Body Fat: Higher (20–30%)")
        print("• Muscle Mass: Lower")
        print("• Fat Distribution: Hips/Thighs (pear-shaped)")
        print("• Same BMI, Different Look : May have softer curves at same BMI")
        print("• Risk Thresholds : Health risks may appear at higher BMI due to natural fat storage")

    display(HTML("<span style='color: blue; font-weight: bold;'>Reference Link:</span>"))
    print("https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html")
    
    # Create Gauge Chart
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go

    # 1. Plotly Gauge Chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=bmi_rounded,
        title={'text': "🩺 BMI Gauge", 'font': {'size': 24}},
        delta={'reference': 22, 'increasing': {'color': "red"}},
        gauge={
            'axis': {'range': [0, 50], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "blue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 18.5], 'color': 'skyblue'},
                {'range': [18.5, 25], 'color': 'limegreen'},
                {'range': [25, 30], 'color': 'gold'},
                {'range': [30, 35], 'color': 'orange'},
                {'range': [35, 40], 'color': 'orangered'},
                {'range': [40, 50], 'color': 'crimson'}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': bmi_rounded
            }
        }
    ))

    fig.update_layout(
        paper_bgcolor="lavender",
        font={'color': "darkblue", 'family': "Arial"},
    )

    fig.show()


    # 2. Matplotlib Bar Chart
    categories = ['Underweight', 'Normal', 'Overweight', 'Obesity Class 1', 'Obesity Class 2', 'Extreme Obesity']
    bmi_ranges = [18.5, 24.9, 29.9, 34.9, 39.9, 50]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(categories, bmi_ranges, color=['skyblue', 'limegreen', 'gold', 'orange', 'orangered', 'crimson'])

    # Highlight user's BMI
    for bar, limit in zip(bars, bmi_ranges):
        if bmi_rounded <= limit:
            bar.set_edgecolor('black')
            bar.set_linewidth(3)
            break

    plt.axhline(y=bmi_rounded, color='blue', linestyle='--', linewidth=2, label=f'Your BMI: {bmi_rounded}')
    plt.title('BMI Categories and Your BMI')
    plt.ylabel('BMI Value')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


    
    # Ask if the user wants to calculate again
    print()
    
    display(HTML("<span style='color: orange; font-weight: bold;'> Do you want to calculate BMI again? (yes / no):</span>"))
    Again = input().strip().lower()
    
    if Again != 'yes':
        display(HTML("<span style='color: green; font-weight: bold;'>Thank you for using the BMI Calculator. Stay healthy!</span>"))
        
        break

