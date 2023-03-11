from zipfile import ZipFile, ZIP_DEFLATED
from zipper_env import EXTRAS
import sys
import os

PRIMARY_NAME = "DDLCModTemplate-"
EXCLUDE_LIST = [
    ".github",
    ".git",
    ".gitattributes",
    ".gitignore",
    "requirements.txt",
    "ZIPs",
    "Additional Mod Features",
    "zipper.py",
    "zipper_env.py",
    "__pycache__",
]


def main():
    try:
        version = sys.argv[1]
    except IndexError:
        raise Exception("Не указан номер версии.")

    if len(tuple(version.strip().split("."))) != 3:
        raise Exception('Некорректный номер версии. Допустимое значение: "X.X.X".')

    print("Сегодня вечером мы собираем Py3-пакет.\n")

    # Создание каталога для ZIP-архивов
    if not os.path.exists("./ZIPs"):
        os.makedirs("./ZIPs")

    main_zip_name = f"{PRIMARY_NAME}{version}-Py3"

    print("Создаю ZIP-файл шаблона.")
    with ZipFile(
        os.path.join(".", "ZIPs", f"{main_zip_name}.zip"),
        "w",
        ZIP_DEFLATED,
        compresslevel=5,
    ) as main_template:
        for src, dirs, files in os.walk("."):
            for f in files:
                path = os.path.join(src, f)
                validLocation = True
                for x in EXCLUDE_LIST:
                    if x in path:
                        validLocation = False
                if validLocation:
                    main_template.write(path)

    print("Запись ZIP-пакета мод-шаблона завершена.\n")

    if EXTRAS:
        print("Создаю ZIP-файл доп. контента шаблона.")
        extras_zip_name = f"{PRIMARY_NAME}{version}-Py3Extras"

        with ZipFile(
            os.path.join(".", "ZIPs", f"{extras_zip_name}.zip"),
            "w",
            ZIP_DEFLATED,
            compresslevel=5,
        ) as extras_template:
            for src, dirs, files in os.walk("."):
                for f in files:
                    path = os.path.join(src, f)
                    if "Additional Mod Features" in path:
                        extras_template.write(path)

        print("Запись ZIP-пакета доп. контента шаблона завершена.\n")

    print("Упаковка завершена.")


if __name__ == "__main__":
    main()
