from importlib.resources import as_file, files
import secrets

import words


def new():
    word_list = []
    with as_file(files(words)) as data_dir:
        for word_file in sorted(data_dir.glob("*.data")):
            word_list.append(
                secrets.choice(
                    word_file.read_text().splitlines()
                ).capitalize()
            )
    return '-'.join(word_list)


if __name__ == '__main__':
    wokeword = new()
    print(wokeword)
