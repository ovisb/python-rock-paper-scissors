class FileHandler:
    def __init__(self, file_name: str):
        self.__file_name = file_name

    def load(self) -> dict:
        names = {}
        try:
            with open(self.__file_name, "r") as f:
                for line in list(f):
                    name, score = line.strip().split()
                    names[name] = int(score)
        except FileNotFoundError:
            raise FileNotFoundError("File not found. Please add 'rating.txt' file.")

        return names

    def save(self, names: dict) -> None:
        with open(self.__file_name, "w") as f:
            for name, score in names.items():
                f.write(f"{name} {score}\n")
