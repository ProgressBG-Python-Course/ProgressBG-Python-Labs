def get_user_data():
    """retrieves user data from the command line"""
    user_data = {}
    user_name = input('Въведете Вашето име:')
    user_weight = float(input("Тегло в килограми:")) #тегло в килограми
    user_height = float(input("Височина в метри: ")) # височина в метри
    user_data['name'] = user_name
    user_data['height'] = user_height
    user_data['weight'] = user_weight

    return user_data

    """Returns:
        [dictionary] of the form:
            {
                "name" : "user_name",
                "height": "user heigth in meters",
                "weight": "user weight in kilograms"
            }
    """


def calc_BMI(w,h):
    """calculates the BMI"""
    bmi = w / (h ** 2) # изчисляване на BMI
    round_bmi = round(bmi,2)
    return round_bmi

    """Arguments:
        w {[float]} -- [weight]
        h {[float]} -- [height]

    Returns:
        [float] -- [calculated BMI = w / (h*h)]
    """

def calc_BMI_category(bmi):
    """Calculates the BMI category"""

    """Arguments:
        bmi {[float]} -- [the bmi number index]

    Returns:
        [string] -- [bmi category]
    """
    if bmi < 18.5:
        #print('Поднормено тегло')
        user_category = 'поднормено тегло'
    elif bmi <= 24.9:
        #print('Нормално тегло')
        user_category = 'нормално тегло'
    elif bmi >= 25 and bmi <= 29.9:
       # print('Наднормено тегло')
        user_category = 'наднормено тегло'
    else:
        #print('Затлъстяване!!!')
        user_category = 'затлъстяване!!!'
    return user_category




def print_results(bmi_category):
    """[Prints the BMI category to the user ]"""

    """Arguments:
        bmi_category {[string]} -- []"""
    print(f'Вие сте {user_data["name"]} с тегло от {user_data["weight"]} кг, ръст от {user_data["height"]} м и индекс на телесната маса - {bmi}.' )
    print(f'Вие сте с {bmi_category}.')


def cm_to_meters(cm):
    """converts centimetres to meters"""

    """Arguments:
        cm {[int]}

    Returns:
        [float]
    """
    cm_height = int(input("Ръст в сантиметри: "))
    meter_height = cm_height / 100
    print(f'Резултат в метри: {meter_height:.2f}')
    return meter_height


user_data = get_user_data()
#print(user_data)
bmi = calc_BMI(user_data["weight"],user_data["height"] )

bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)



