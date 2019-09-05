# ------------------------------------------------------------

# --------- NO MODIFICAR ESTE CÓDIGO, SOLO EJECUTAR ----------

# ------------------------------------------------------------

import os, pickle, random, time

def descargar():
    ruta_canciones = os.path.join("data_base", "canciones.csv")
    ruta_artistas = os.path.join("data_base", "artistas.csv")
    ruta_usuarios = os.path.join("data_base", "usuarios.csv")
    ruta_ratings = os.path.join("data_base", "ratings.csv")

    if os.path.exists("data_base") and os.path.exists(ruta_ratings):
        return
    print("Conectando con el servidor de yoNube®")
    time.sleep(1)


    print("Descargando bases de datos...")
    os.mkdir("data_base")

    songs = []
    ratings = []

    with open("data_base.iTunes", "rb") as file:
        db = pickle.load(file)
        with open(ruta_canciones, "w", encoding="utf-8") as file:
            for line in db[0].split("{"):
                file.write(line + "\n")
                songs.append(line.split(",")[0])
        with open(ruta_artistas, "w", encoding="utf-8") as file:
            for line in db[1].split("{"):
                file.write(line + "\n")
        with open(ruta_usuarios, "w", encoding="utf-8") as file:
            for line in db[2].split("{"):
                file.write(line + "\n")
                cant = random.randint(0, 10)

                for i in range(cant):
                    op = random.choice(songs)
                    rating = random.choice(["r","q","u","e","t"])

                    ratings.append((line.split(",")[1], op, str(rating)))

    with open(ruta_ratings, "w", encoding="utf-8") as file:
        for rating in ratings:
            file.write(",".join(rating) + "\n")

    print("Descargando un regalito de Pear")
    time.sleep(1)

    with open(".gitignore", "w", encoding="utf-8") as file:
        git = ["data_base/**", "yoNube.py", "data_base.iTunes", "*.csv"]
        for line in git:
            file.write(line + "\n")
    #os.system("git add .gitignore")
    print(".gitignore completo")

    print("Descarga completa ✅")


if __name__ == "__main__":
    descargar()