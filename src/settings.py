from pathlib import Path

model_name = "MODEL_NAME"  # change model name
extent = [0.0, 1.0, 0.0, 1.0]  # change extent to model extent

paths = {
    "models": Path(__file__).parent / "models",  # change path to models folder
    "download": Path(__file__).parent.parent
    / "download",  # set path to download folder
}
