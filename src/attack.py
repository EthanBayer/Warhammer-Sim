

from src.utils import NumericOutcome

# TODO - Need new type for values that can be a number or a dice

class Attack:

    def __init__(self, 
             attacks: NumericOutcome, 
             hit_skill int, 
             strength: int,
             ap: int,
             damage: NumericOutcome,
             **kwargs
             ):
        """
        Attack constructor
        """
        self.hit_skill = hit_skill
        self.strength = strength
        self.ap = ap

        self.rrh = kwargs.get("rrh", False)
        self.rrw = kwargs.get("rrw", False)
        self.rrd = kwargs.get("rrd", False)
        # TODO - sustained_hits must also be num or dice data structure
        self.sustained_hits = kwargs.get("sustained_hits", 0)
        self.lethal_hits = kwargs.get("letahl_hits", False)
        self.critical_hit = kwargs.get("critical_hit", 6)
        self.critical_wound = kwargs.get("critical_wound", 6)
        self.dev_wounds = kwargs.get("dev_wounds", False)
        self.torrent = kwargs.get("torrent", False)
