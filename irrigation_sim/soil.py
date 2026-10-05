"""
Soil water bucket model.

Single-reservoir ("bucket") model of root-zone soil water, expressed as a
depth in mm so it's directly comparable to rainfall/irrigation/ET.

Water balance (fill in as derived in the lesson):
    S[t+1] = S[t] + P[t] + I[t] - ET[t] - D[t]

Where:
    S  - soil water storage (mm)
    P  - precipitation (mm)
    I  - irrigation applied (mm)
    ET - actual evapotranspiration (mm), capped by water availability
    D  - drainage (mm), water beyond bucket capacity

TODO (Step 2): implement SoilBucket below.
"""

from dataclasses import dataclass


@dataclass
class SoilBucket:
    s_max: float   # bucket capacity, mm
    s: float       # current soil water storage, mm

    def compute_drainage(self, s_before_cap: float) -> float:
        """
        Given storage after adding inflows (before capping), return the
        drainage (mm) that overflows the bucket, and cap storage at s_max.

        TODO: implement the overflow logic discussed in the lesson.
        """
        raise NotImplementedError

    def compute_actual_et(self, et0: float, kc: float) -> float:
        """
        Compute actual ET given reference ET (et0), crop coefficient (kc),
        and the current soil water stress level.

        TODO (Step 3 dependency): needs a stress coefficient K_s(S) that
        scales down ET as soil water approaches the wilting point.
        """
        raise NotImplementedError

    def step(self, rain: float, irrigation: float, et0: float, kc: float) -> dict:
        """
        Advance the bucket by one day. Returns a dict of the day's flows
        (useful for logging: {"et": ..., "drainage": ..., "storage": ...}).

        TODO: wire together compute_actual_et + compute_drainage + the
        mass balance update, in the order you reasoned through in the
        lesson (does order matter?).
        """
        raise NotImplementedError
