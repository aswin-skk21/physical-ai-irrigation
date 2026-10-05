# Physical AI Irrigation Research

An irrigation decision agent trained using simulations from **AquaCrop-OSPy**. The objective is to maximize crop yield. AquaCrop provides the soil–crop–water simulation; this project will provide scenario setup, irrigation controllers, data collection, and agent evaluation.

## Current status

The repository currently contains Python scaffolding only. AquaCrop integration, simulation runs, dataset generation, and agent training are not implemented. The existing soil bucket and crop-physics stubs reflect an earlier learning plan; AquaCrop replaces those proposed custom physics components.

## Simulation inputs

- Daily weather data: minimum and maximum temperature, precipitation, and reference evapotranspiration.
- Soil profile and hydraulic properties.
- Crop parameters and planting date.
- Simulation start and end dates.
- Initial soil water content.
- Irrigation management: a schedule or decisions supplied by a controller. This is the input the future AI agent will control.

Use ISO dates (`YYYY-MM-DD`) in project datasets and convert them as required by the simulator.

## Outputs in scope: crop growth and yield

We will retain relevant daily crop growth results and seasonal yield summaries. Exact available columns must be checked against the installed AquaCrop-OSPy version.

| Result | Purpose |
| --- | --- |
| Daily biomass | Track crop growth during the season. |
| Daily canopy cover | Track canopy development; preserve the simulator's units. |
| Harvest index, when available | Describe the relationship between harvested yield and biomass; explicitly distinguish fractions from percentages. |
| Final dry yield (tonne/ha) | Primary seasonal outcome for training-data selection and evaluation. |
| Final biomass | Record end-of-season biomass from crop-growth output, aligned to harvest. |

The upstream implementation separates daily results into `crop_growth`, `water_storage`, and `water_flux`; it does not define one combined `daily` output. Its seasonal `final_stats` includes `Dry yield (tonne/ha)`, `Fresh yield (tonne/ha)`, and `Yield potential (tonne/ha)`. Biomass and harvest index should not be assumed to be columns in `final_stats`. Prefer public result accessors where available and verify schemas before exporting.

Water-flux and stress outputs are outside the initial reporting scope. The future irrigation agent still needs decision-time soil and weather observations; those inputs are distinct from the growth/yield outcomes retained for reporting.

## Workflow

1. Configure weather, soil, crop, dates, initial water, and irrigation management.
2. Run growing seasons in AquaCrop with baseline irrigation strategies or candidate schedules.
3. Save relevant crop growth and final yield outcomes alongside scenario identifiers, decision-time observations, and irrigation actions.
4. Build training demonstrations from selected strategies. AquaCrop supplies consequences; a controller or search procedure supplies action labels.
5. Export training data to a separate NVIDIA GPU machine for local LLM fine-tuning using LoRA/QLoRA.
6. Connect the trained LLM to a daily observation–decision–simulation loop.
7. Evaluate on held-out seasons against baseline controllers, using final dry yield as the primary outcome.

Split data by complete scenarios/seasons before constructing daily examples. Future realized weather and final yield must not appear in decision-time observations. Supervised fine-tuning on baseline actions teaches imitation; improving beyond the baseline requires stronger demonstrations or a further optimization method.

## Project structure

- `irrigation_sim/config.py`: existing parameter stubs; future scenario configuration.
- `irrigation_sim/env.py`: planned interface around AquaCrop for daily interaction.
- `irrigation_sim/weather.py`: placeholder for weather input preparation.
- `irrigation_sim/soil.py`, `crop.py`: legacy custom-model learning stubs.
- `irrigation_sim/agents/baseline.py`: planned demonstration and comparison controller.
- `scripts/run_episode.py`: placeholder for running one season.
- `data/`: generated datasets, excluded from Git for CSV/JSONL files.
- `tests/`: reserved for future checks.

## Setup

The current `requirements.txt` lists only the original scaffold dependencies (`numpy`, `pyyaml`). It does not yet install AquaCrop-OSPy. A tested simulator version and dependency setup will be added during integration. There is no runnable simulation command yet.

## References

- [FAO AquaCrop](https://www.fao.org/aquacrop)
- [AquaCrop-OSPy source and documentation](https://github.com/aquacropos/aquacrop)
- [Upstream output definitions](https://github.com/aquacropos/aquacrop/blob/master/aquacrop/entities/output.py)
