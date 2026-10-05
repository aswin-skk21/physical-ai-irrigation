"""
Gym-style irrigation environment: reset() / step() interface tying together
SoilBucket, the weather generator, and crop growth/yield.

TODO (Step 5): implement IrrigationEnv with:
    - reset() -> initial observation
    - step(action) -> (observation, reward, done, info)
where `action` is the irrigation depth (mm) applied that day, and
`observation` exposes whatever state the agent needs (soil water, day of
season, recent weather, crop stage, etc.).
"""

# Placeholder - implemented in Step 5. Depends on soil.py, weather.py, crop.py.
