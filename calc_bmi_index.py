"""
Задание: 
Зная формулу расчтета индекса массы тела запросить и пользователя 
из консоли массу тела и рост, рассчитать по формуле
BMI = MASS / HEIGHT^2

И дать совет исходя из таблицы:
Underweight = <18.5
Normal = 18.5<25
Overweight = 25<30
Obesity = 30<

Например:
mass = 84
height = 180
Overweight 3 kg
"""

def validator_factory(type_, type_err_msg, min=None, max=None):
    def validate(value):
        try:
            value = type_(value)
        except ValueError:
            raise ValueError(type_err_msg)
        if min is not None:
            if value < min:
                raise ValueError(f'value should be greater than {min}')
        if max is not None:
            if value > max:
                raise ValueError(f'value should be less than {max}')
        return value
    return validate


def ask(question, validator):
    while True:
        try:
            return validator(input(question))
        except ValueError as ex:
            print(ex)


def make_advice(bmi, mass, height):
    normal_lower_limit = 18.5
    normal_high_limit = 25
    overweight_hight_limit = 30

    tips_by_bmi = {
        'Underweight': lambda x: x < normal_lower_limit,
        'Normal': lambda x: normal_lower_limit < x < normal_high_limit,
        'Overweight': lambda x: normal_high_limit < x < overweight_hight_limit,
        'Obesity': lambda x: x >= overweight_hight_limit
    }

    result = next(tip for tip, check_func in tips_by_bmi.items() if check_func(bmi))
    if result != 'Normal':
        if bmi > normal_high_limit:
            norm_diff = mass - round(normal_high_limit * (height / 100) ** 2)
        else:
            norm_diff = round(normal_lower_limit * (height / 100) ** 2) - mass
        return f'{result} {norm_diff} kg'
    return result


mass = ask('mass (in kg.) = ',
           validator_factory(int, 'mass shuold be an integer', min=10, max=300))
height = ask('height (in sm.) = ',
             validator_factory(int, 'height shuold be an integer', min=50, max=250))

bmi = round(mass / (height/100)**2)

print(f'bmi: {bmi}: {make_advice(bmi, mass, height)}')
