import asyncio
from typing import TypedDict

from database.connect import CLIENT


async def patients():

    response = await asyncio.to_thread(
        lambda: (
            CLIENT.table("patients")
            .select("idpatient", "name", "lastname", "birth", "sex")
            .is_("active", True)
            .execute()
        )
    )
    return response.data


class PatientDataDict(TypedDict):
    name: str
    lastname: str
    birth: str
    sex: str
    patient_diseases: list[dict[str, str]]
    patient_exams: list[dict[str, str]]
    patient_potentials: None | dict[str, str]


async def patient_by_id(idpatient: str) -> PatientDataDict | None:

    response = await asyncio.to_thread(
        lambda: (
            CLIENT.table("patients")
            .select(
                "name",
                "lastname",
                "birth",
                "sex",
                "patient_diseases!left(date, disease)",
                "patient_exams!left(date, exam)",
                "patient_potentials!left(father, mother)",
            )
            .eq("idpatient", idpatient)
            .is_("active", True)
            .single()
            .execute()
        )
    )
    return response.data  # type: ignore


async def patient_old_data(idpatient: str) -> PatientDataDict | None:

    response = await asyncio.to_thread(
        lambda: (
            CLIENT.table("patient_measures")
            .select(
                "*",
                "patient!inner(*)",
            )
            .eq("idpatient", idpatient)
            .is_("active", True)
            .single()
            .execute()
        )
    )
    return response.data  # type: ignore
