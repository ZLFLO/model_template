def get_abs_data_path(name, version, location) -> str:
    # Pseudocode for getting data from https://github.com/ZLFLO/data
    # 1. Check if the dataset exists locally in a predefined directory.
    # 2. If not, clone or download the dataset from the ZLFLO/data GitHub repository.
    # 3. Construct the absolute path to the requested dataset version and location.
    # 4. Return the absolute path.

    # For now, just return a mock path as a placeholder.
    return f"/mock/path/{name}_v{version}_{location}"
