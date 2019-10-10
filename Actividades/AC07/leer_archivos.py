
def generate_dict(line, headers):
    values = {
        key: value for key, value in zip(
            headers, line.strip().split(",")
        )
    }
    return values


def read_file():
    with open(f"ayudantes.csv", "r", encoding="utf-8") as file:
        headers = file.readline().strip().split(",")
        ayudantes = [generate_dict(line, headers) for line in file]
    return ayudantes
