
# 0imports.rpy
# В этом файле импортируются конкретные модули Python, необходимые для DDLC
# и функционирования шаблона, во время запуска игры.

python early:
    # Для DSR/DSP, эффектов
    import math 

    # Для титров
    import datetime

    # Для глитч-текста
    import random

    # Для вступительной заставки
    import re
    import os

    # Для Синего экрана смерти
    import subprocess
    import platform

init python:
    # Достижения/Галерея
    try:
        from store.achievements import achievementList, Achievement, AchievementCount
    except ModuleNotFoundError:
        pass
    
    try:
        from store.gallery import GalleryImage, galleryList
    except ModuleNotFoundError:
        pass
