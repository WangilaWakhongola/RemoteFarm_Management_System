"""
farm_models.py
Simple data models for the Remote Farm Management System.
Represents core entities: Farm, Field, Crop, and LivestockAnimal.
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Crop:
    """Represents a crop planted in a field."""
    name: str
    planted_date: date
    expected_harvest_date: date
    health_status: str = "healthy"  # healthy | at_risk | diseased

    def days_to_harvest(self) -> int:
        delta = self.expected_harvest_date - date.today()
        return max(delta.days, 0)

    def __str__(self) -> str:
        return (
            f"Crop({self.name}, planted={self.planted_date}, "
            f"harvest in {self.days_to_harvest()} days, status={self.health_status})"
        )


@dataclass
class Field:
    """Represents a field on a farm."""
    field_id: str
    area_hectares: float
    crop: Optional[Crop] = None
    last_irrigated: Optional[date] = None

    def is_planted(self) -> bool:
        return self.crop is not None

    def days_since_irrigation(self) -> Optional[int]:
        if self.last_irrigated is None:
            return None
        return (date.today() - self.last_irrigated).days

    def __str__(self) -> str:
        crop_info = str(self.crop) if self.crop else "unplanted"
        irrigation = self.days_since_irrigation()
        irr_str = f"{irrigation} days ago" if irrigation is not None else "never"
        return (
            f"Field({self.field_id}, {self.area_hectares} ha, "
            f"crop={crop_info}, last irrigated={irr_str})"
        )


@dataclass
class LivestockAnimal:
    """Represents a livestock animal on the farm."""
    animal_id: str
    species: str
    breed: str
    birth_date: date
    health_status: str = "healthy"  # healthy | sick | under_observation
    weight_kg: float = 0.0

    def age_years(self) -> float:
        return round((date.today() - self.birth_date).days / 365.25, 1)

    def __str__(self) -> str:
        return (
            f"Animal({self.animal_id}, {self.species}/{self.breed}, "
            f"age={self.age_years()}y, weight={self.weight_kg}kg, status={self.health_status})"
        )


@dataclass
class Farm:
    """Represents the entire farm."""
    farm_id: str
    name: str
    owner: str
    location: str
    fields: list[Field] = field(default_factory=list)
    livestock: list[LivestockAnimal] = field(default_factory=list)

    def add_field(self, f: Field):
        self.fields.append(f)

    def add_animal(self, animal: LivestockAnimal):
        self.livestock.append(animal)

    def summary(self) -> dict:
        return {
            "farm": self.name,
            "owner": self.owner,
            "location": self.location,
            "total_fields": len(self.fields),
            "planted_fields": sum(1 for f in self.fields if f.is_planted()),
            "total_livestock": len(self.livestock),
            "sick_animals": sum(1 for a in self.livestock if a.health_status == "sick"),
        }

    def __str__(self) -> str:
        s = self.summary()
        return (
            f"Farm: {s['farm']} | Owner: {s['owner']} | Location: {s['location']}\n"
            f"  Fields: {s['total_fields']} total, {s['planted_fields']} planted\n"
            f"  Livestock: {s['total_livestock']} total, {s['sick_animals']} sick"
        )


# --- Demo ---
if __name__ == "__main__":
    farm = Farm("F001", "Green Valley Farm", "John Wakhongola", "Western Region")

    wheat = Crop("Wheat", date(2025, 3, 1), date(2025, 8, 15))
    maize = Crop("Maize", date(2025, 4, 10), date(2025, 9, 1), health_status="at_risk")

    farm.add_field(Field("A1", 5.0, crop=wheat, last_irrigated=date(2025, 6, 20)))
    farm.add_field(Field("A2", 3.5, crop=maize, last_irrigated=date(2025, 6, 15)))
    farm.add_field(Field("B1", 4.0))  # unplanted

    farm.add_animal(LivestockAnimal("C001", "Cattle", "Friesian", date(2022, 5, 1), weight_kg=450.0))
    farm.add_animal(LivestockAnimal("C002", "Cattle", "Angus", date(2021, 8, 12), weight_kg=480.0, health_status="sick"))
    farm.add_animal(LivestockAnimal("G001", "Goat", "Boer", date(2023, 1, 20), weight_kg=65.0))

    print(farm)
    print("\n--- Fields ---")
    for f in farm.fields:
        print(" ", f)
    print("\n--- Livestock ---")
    for a in farm.livestock:
        print(" ", a)
