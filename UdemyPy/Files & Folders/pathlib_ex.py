from pathlib import Path
from datetime import datetime

import random, zipfile


def create_blank(root_dir, filenum):
    for i in range(1, int(filenum) + 1):
        filename = str(i) + '.txt'
        filepath = root_dir / Path(filename)
        filepath.touch()


def write_random():
    p1 = Path('files/file.txt')
    p1.parent.mkdir(parents=True, exist_ok=True)

    if not p1.exists():
        with open(p1, 'w') as file:
            file.write(f'Content {random.randint(99999,999999)}')


def rename_files(root_dir):
    file_paths = root_dir.iterdir()

    for path in file_paths:
        new_filename = "new-" + path.stem + path.suffix
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)


def date_as_filename(root_dir):
    for path in root_dir.glob('**/*'):
        if path.is_file():
            cr_date = datetime.fromtimestamp(path.stat().st_ctime)
            cr_date_str = cr_date.strftime("%Y-%m-%d")
            new_file_name = cr_date_str + '_' + path.name
            new_filepath = path.with_name(new_file_name)
            path.rename(new_filepath)


def archive_files(root_dir):
    archive_path = root_dir / Path('archive.zip')

    with zipfile.ZipFile(archive_path, 'w') as zf:
        for path in root_dir.rglob("*.txt"):
            zf.write(path)
            path.unlink()


def unzip_files(root_dir):
    destination_path = Path('unzipped')

    for path in root_dir.glob("*.zip"):
        with zipfile.ZipFile(path, 'r') as zf:
            final_path = destination_path / Path(path.stem)
            zf.extractall(path=final_path)


def main():
    root_dir = Path('files')

    # write_random()
    # create_blank(root_dir, filenum=3)
    # rename_files(root_dir)
    # date_as_filename(root_dir)
    # archive_files(root_dir)
    unzip_files(root_dir)


if __name__ == '__main__':
    main()


"""
Other Methods
-------------
path.glob("**/*")
path.is_file()
path.parts
"-".join(subfolders)
"""
