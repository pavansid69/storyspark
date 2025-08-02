from typing import List, Dict

class CharacterProfile:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def to_dict(self) -> Dict:
        return {"name": self.name, "description": self.description}

class CharacterRegistry:
    def __init__(self):
        self.profiles: Dict[str, CharacterProfile] = {}

    def add_character(self, name: str, description: str):
        self.profiles[name] = CharacterProfile(name, description)

    def get_all_characters(self) -> List[Dict]:
        return [profile.to_dict() for profile in self.profiles.values()]

    def get_character_names(self) -> List[str]:
        return list(self.profiles.keys())

    def get_character(self, name: str) -> Dict:
        return self.profiles.get(name).to_dict() if name in self.profiles else None

# Instance to be used by other modules
character_registry = CharacterRegistry()