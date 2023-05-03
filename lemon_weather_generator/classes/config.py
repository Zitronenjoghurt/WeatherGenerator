class Config:
    def __init__(self, effects):
        self.effects = effects

    def __eq__(self, other):
        if isinstance(other, Config):
            return (self.effects == other.effects)
        return False