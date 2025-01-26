class VaccineError(Exception):
    """ Class for errors"""


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "your vaccine out date"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "you not wearing masks"
