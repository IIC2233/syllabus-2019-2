def cargar_archivos(path):
    with open(path, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            user, name, following = line.strip().split(",")
            following = following.split(";")
            yield user, name, following
