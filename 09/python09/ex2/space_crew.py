from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officier"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commender"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_data: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def custom_rules(self) -> object:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        rank = [crew.rank for crew in self.crew]
        if ((Rank.COMMANDER in rank) + (Rank.CAPTAIN in rank) == 0):
            raise ValueError("Must have at least one Commander or Captain")
        try:
            avg = len(self.crew) / len([crew for crew in self.crew if
                                        crew.years_experience > 5])
        except ZeroDivisionError:
            raise ValueError('Long missions (> 365 days) need 50% experienced \
crew (5+ years)')

        if self.duration_days > 365 and avg > 2:
            raise ValueError('Long missions (> 365 days) need 50% experienced \
crew (5+ years)')
        if False in [crew.is_active for crew in self.crew]:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)
    try:
        space_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_data="1768557497",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C_01",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=42,
                    specialization="Mission Command",
                    years_experience=24
                ),
                CrewMember(
                    member_id="L_01",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=42,
                    specialization="Navigation",
                    years_experience=6
                ),
                CrewMember(
                    member_id="O_01",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=42,
                    specialization="Engineering",
                    years_experience=2
                )
            ]
        )
        print("VAlid mission created:")
        print(f"Mission: {space_mission.mission_name}")
        print(f"ID: {space_mission.mission_id}")
        print(f"Destination: {space_mission.destination}")
        print(f"Duration: {space_mission.duration_days} days")
        print(f"Budget: ${space_mission.budget_millions}")
        print(f"Crew size: {len(space_mission.crew)}")
        for member in space_mission.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")
        print()
        print("=" * 40)
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_data="1768557497",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C_01",
                    name="Sarah Connor",
                    rank=Rank.LIEUTENANT,
                    age=42,
                    specialization="Mission Command",
                    years_experience=24
                ),
                CrewMember(
                    member_id="L_01",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=42,
                    specialization="Navigation",
                    years_experience=6
                ),
                CrewMember(
                    member_id="O_01",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=42,
                    specialization="Engineering",
                    years_experience=2
                )
            ]
        )
    except ValidationError as e:
        print("\nExpected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")


if (__name__ == "__main__"):
    main()
