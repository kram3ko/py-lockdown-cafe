import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine_key = visitor.get("vaccine")
        if not vaccine_key:
            raise NotVaccinatedError
        vaccine_date = visitor["vaccine"].get("expiration_date")
        wearing_mask = visitor.get("wearing_a_mask")
        if vaccine_date < datetime.date.today():
            raise OutdatedVaccineError
        elif not wearing_mask:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"


if __name__ == "__main__":
    pass
