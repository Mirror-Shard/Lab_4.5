#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Разработайте аналог утилиты tree в Linux.
Используйте возможности модуля argparse для управления отображением дерева
каталогов файловой системы. Добавьте дополнительные уникальные возможности в
данный программный продукт.
"""

import argparse
import pathlib
from pathlib import WindowsPath as Path


def tree(directory: Path, dir: bool, pattern: str, sep: str) -> None:
    if dir:
        pattern: str = '.'
    for path in sorted(directory.rglob(pattern)):
        depth: int = len(path.relative_to(directory).parts)
        spacer: str = '\t' * depth
        print(spacer + sep + ' ' + path.name)


def main(command_line=None):
    # Основной парсер командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", default=pathlib.Path.cwd())
    parser.add_argument("--dir", default=False)
    parser.add_argument("--pattern", default='*')
    parser.add_argument("--separator", default="|--")

    # Работа программы
    args = parser.parse_args(command_line)
    filepath = pathlib.Path(args.filepath)
    tree(filepath, args.dir, args.pattern, args.separator)


if __name__ == "__main__":
    main()
