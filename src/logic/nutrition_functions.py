def calc_bmr_harris_benedict(weight: str, height: str, age: int, sex: str) -> str:
    result = 0

    if sex == "m":
        result = (10 * float(weight)) + (6.25 * float(height) * 100) - (5 * age) + 5
    else:
        result = (10 * float(weight)) + (6.25 * float(height) * 100) - (5 * age) - 161

    return str(round(result, 2))


def calc_bmr_schofield(weight: str, age: int, sex: str, minor_text: str) -> str:
    result = 0

    if 19 <= age <= 29:
        if sex == "m":
            result = (15.057 * float(weight)) + 692.2
        else:
            result = (14.818 * float(weight)) + 486.6
    elif 30 <= age <= 59:
        if sex == "m":
            result = (11.472 * float(weight)) + 872.1
        else:
            result = (8.126 * float(weight)) + 845.6
    elif age >= 60:
        if sex == "M":
            result = (11.711 * float(weight)) + 587.1
        else:
            result = (9.082 * float(weight)) + 658.5
    else:
        return minor_text

    return str(round(result, 2))


def calc_bmi(weight: str, height: str):
    imc = 0
    classification = ""

    imc = float(weight) / (float(height) ** 2)

    if imc < 18.5:
        classification = "l"
    elif 18.5 <= imc < 25:
        classification = "n"
    elif 25 <= imc < 30:
        classification = "h"
    elif 30 <= imc:
        classification = "vh"

    return str(round(imc, 2)), classification


def calc_ideal_weight(height: str, sex: str) -> str:
    result = 0

    if sex == "m":
        result = 50 + (0.75 * ((float(height) * 100) - 150))
    else:
        result = 50 + (0.6 * ((float(height) * 100) - 150))

    return str(round(result, 2))


def genenticPotential(sex, fHeight, mHeight):
    ds = 12.7
    result = 0
    range = 0

    if sex == "m":
        result = (((fHeight * 100) + ds) + (mHeight * 100)) / 2
        range = 0.1
    else:
        result = (((mHeight * 100) - ds) + (fHeight * 100)) / 2
        range = 0.09

    return round(result / 100, 2), range


def sumFolds(folds):
    threeFolds = None
    sixFolds = None

    if folds[0] != None and folds[4] != None and folds[5] != None:
        threeFolds = round(folds[0] + folds[4] + folds[5], 2)
        if folds[1] != None and folds[6] != None and folds[7] != None:
            sixFolds = round(
                folds[0] + folds[4] + folds[5] + folds[1] + folds[6] + folds[7], 2
            )

    return threeFolds, sixFolds
