from pathlib import Path

# define directory for downloaded files
download_dir = Path('../modeldata/downloads')
download_dir.mkdir(parents=True, exist_ok=True)

# extent of the model
extent = [24500, 25000, 398500, 398900]

