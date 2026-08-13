from datetime import date


def calc_age(birthday: date) -> int:

    today = date.today()

    return (
        today.year - birthday.year - 1
        if (today.month, today.day) < (birthday.month, birthday.day)
        else today.year - birthday.year
    )
