"""
Central place for simulation parameters (soil, crop, weather, episode settings).

We'll fill these in as each curriculum step introduces the numbers it needs.
Using a dataclass (not a plain dict) so parameter names are IDE-discoverable
and typo'd field names fail loudly instead of silently returning None.
"""

from dataclasses import dataclass


@dataclass
class SoilParams:
    # TODO (Step 2 - bucket model): fill these in.
    # s_max: float        # max plant-available water depth, mm (bucket capacity)
    # s_init: float       # starting soil water depth, mm
    # stress_threshold: float  # fraction of s_max below which K_s < 1
    pass


@dataclass
class CropParams:
    # TODO (Step 3 - crop growth stages): fill these in.
    # kc_by_stage: dict    # crop coefficient per growth stage
    # stage_lengths: dict  # days per growth stage
    pass


@dataclass
class WeatherParams:
    # TODO (Step 4 - weather generation): fill these in.
    pass


@dataclass
class EpisodeParams:
    # TODO: episode length in days, random seed, etc.
    # n_days: int
    # seed: int
    pass
