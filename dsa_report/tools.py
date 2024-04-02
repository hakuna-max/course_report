import pandas as pd


def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"file {file_path} does not found")
        return None
    except Exception as e:
        print(f"Loading data error: {e}")
        return None


def main():
    pass


if __name__ == "__main__":
    main()
