from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        space_valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2023, 10, 25, 14, 30),
            is_operational=True,
        )
        print("Valid station created:")
        print(f"ID: {space_valid.station_id}")
        print(f"Name: {space_valid.name}")
        print(f"Crew: {space_valid.crew_size} people")
        print(f"Power: {space_valid.power_level}%")
        print(f"Oxygen: {space_valid.oxygen_level}%")
        status = 'Operational' if space_valid.is_operational else 'Down'
        print(f"Status: {status}")
    except ValidationError as e:
        print(f"[ERROR] {e}")
    print("=" * 40)
    try:
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=26,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2023, 10, 25, 14, 30),
            is_operational=True,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            if error['loc'][0] == 'crew_size':
                print(f"Field 'crew_size': {error['msg']}")
            else:
                print(error['msg'])


if (__name__ == "__main__"):
    main()
