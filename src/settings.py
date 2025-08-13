from pathlib import Path

model_name = "MODEL_NAME"  # change model name
extent = [0.0, 1.0, 0.0, 1.0]  # change extent to model extent

paths = {
    "data": Path(__file__).parent / "data",  # set path to data folder
    "models": Path(__file__).parent / "models",  # change path to models folder
}
