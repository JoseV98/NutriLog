import asyncio
from datetime import date

from database.connect import CLIENT


async def new_patient(
    user: str,
    name: str,
    lastname: str,
    birthday: date,
    sex: str,
    potential: bool,
    mother: float,
    father: float,
    is_exam: bool,
    exam: str,
    is_disease: bool,
    disease: str,
):

    response = await asyncio.to_thread(
        lambda: CLIENT.rpc(
            "insert_new_patient",
            {
                "r_user": user,
                "new_name": name,
                "new_lastname": lastname,
                "new_birth": birthday.strftime("%Y-%m-%d"),
                "new_sex": sex,
                "new_potential": potential,
                "new_mother": mother,
                "new_father": father,
                "new_exam": is_exam,
                "new_exam_report": exam,
                "new_disease": is_disease,
                "new_disease_report": disease,
            },
        ).execute()
    )

    return response.data
