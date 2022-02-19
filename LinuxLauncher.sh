#!/bin/sh

## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.
## Основано на оригинальном файле renpy.sh с добавлением возможности удаления остаточных файлов Ren'Py 6-й версии.

# Директория, в которой находится данный скрипт оболочки - абсолютный путь.
ROOT=$(dirname "$SCRIPT")
ROOT=$(cd "$ROOT"; pwd)

if [ -z "$RENPY_PLATFORM" ] ; then
    RENPY_PLATFORM="$(uname -s)-$(uname -m)"

    case "$RENPY_PLATFORM" in
        Darwin-*|mac-*)
            RENPY_PLATFORM="mac-x86_64"
            ;;
        *-x86_64|amd64)
            RENPY_PLATFORM="linux-x86_64"
            ;;
        *-i*86)
            RENPY_PLATFORM="linux-i686"
            ;;
        Linux-*)
            RENPY_PLATFORM="linux-$(uname -m)"
            ;;
        *)
            ;;
    esac
fi

LIB="$ROOT/lib/$RENPY_PLATFORM"

# Удаляет папку «lib», оставшуюся от Ren'Py 6
if [ -d "$LIB/lib" ]; then
    echo "Удаление файлов Ren'Py 6 для предотвращения возникновения ошибки с модулем 'future.standard_library'."
    rm -r "$LIB/lib"
fi

SHFILE="$(ls -I "DDLC.sh" -I "LinuxLauncher.sh" "$ROOT" | grep ".sh")"

if test -z "$SHFILE"; then
    echo "Ошибка: Невозможно найти файл скрипта оболочки модификации. Откатываюсь к 'DDLC.sh'."
    SHFILE="DDLC.sh"
fi

# Название этого скрипта оболочки без «.sh» на конце.
SHNAME=$(basename "$SHFILE" .sh)

echo "Подготовка к запуску $SHNAME..."
exec "$ROOT/$SHFILE"