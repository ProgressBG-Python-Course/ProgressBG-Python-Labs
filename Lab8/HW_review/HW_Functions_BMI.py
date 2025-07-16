def get_user_data():
    """Retrieves user data from the command line

    Returns:
        [dictionary] of the form:
            {
                "name" : "user_name",
                "height": "user height in meters",
                "weight": "user weight in kilograms"
            }
    """
    name = input("Enter your name: ")
    height = float(input("Enter your height in meters (e.g. 1.75): "))
    weight = float(input("Enter your weight in kilograms (e.g. 70): "))
    return {
        "name": name,
        "height": height,
        "weight": weight
    }

def calc_BMI(w, h):
    """Calculates the BMI

    Arguments:
        w {[float]} -- [weight]
        h {[float]} -- [height]

    Returns:
        [float] -- [calculated BMI = w / (h*h)]
    """
    return w / (h * h)

def main():
    user = get_user_data()
    bmi = calc_BMI(user["weight"], user["height"])
    print(f"{user['name']}, your BMI is: {bmi:.2f}")

if __name__ == "__main__":
    main()