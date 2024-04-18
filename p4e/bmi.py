print('-' *40)
print('-' *12 + ' BMI Calculator ' + '-' * 12)
print('-' *40)

height = float(input('Enter your height (inches):\n'))
weight = float(input('Enter your weight (lbs):\n'))

bmi =  weight * 703 / height ** 2

body_type =  None

if bmi < 18.5:
     body_type = 'Underweight'
elif bmi < 24.9:
    body_type = 'Normal Weight'
elif bmi < 29.9:
     body_type = 'Overweight'
else:
     body_type =  'Obese'

print(f'You BMI of {bmi} is {body_type}')