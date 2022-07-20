def get_filename_no_ext(filepath: str) -> str:
    return filepath.split('\\')[-1].split('.')[0]