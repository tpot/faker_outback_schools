from random import choice
from faker.providers import BaseProvider

name_list = [
    "Wombat Wobble",
    "Crikey Creek",
    "Boomerang Bungles",
    "Snag Sizzle Flat",
    "Esky Downs",
    "Vegemite Valley",
    "Chook Chase Junction",
    "Bogan Billabong",
    "Dunny Hollow",
    "G’day Gap",
    "Cockatoo Cackle Creek",
    "Goanna Gully",
    "Bilby Burrow Bend",
    "Dingo Disco Creek",
    "Galah Guffaw Gorge",
    "Platypus Pancake Creek",
    "Emu Snooze Lagoon",
    "Kangaroo Kazoo Flats",
]

school_type_list = [
    "Academy",
    "District School",
    "High School",
    "Learning Center",
    "Primary School",
    "Public School",
    "Schoolhouse",
    "Secondary College",
    "Bush School",
    "School of Hard Knocks",
    "Hard Yakka Institute",
    "Excellence Academy",
    "Station School",
]


class OutbackSchoolProvider(BaseProvider):
    """
    A Provider for outback school name test data.

    >>> from faker import Faker
    >>> from faker_airtravel import OutbackSchoolProvider
    >>> fake = Faker()
    >>> fake.add_provider(OutbackSchoolProvider)
    """

    def outback_school_name(self) -> str:
        return choice(name_list) + " " + choice(school_type_list)
