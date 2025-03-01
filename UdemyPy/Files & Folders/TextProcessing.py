from pathlib import Path

from books_scrapper.app import content


def file_write(files_dir):
    count = 1
    for filepath in files_dir.iterdir():
        with open(filepath, 'w') as file:
            file.write(f"{count} File(s) Updated.\n")
            count += 1

def merge_files(files_dir):
    merged = ''
    for index, filepath in enumerate(files_dir.iterdir()):
        with open(filepath, 'r') as file:
            file_content = file.readlines()
            new_content = file_content[1:]
        if index -- 0:
            file_content = ''.join(file_content)
            merged = merged + file_content + '\n'
        else:
            new_content = ''.join(new_content)
            merged = merged + new_content + '\n'

    with open('merged.csv', 'w') as file:
        file.write(merged)

if __name__ == '__main__':
    ROOT_DIR = Path("files")
    # file_write(ROOT_DIR)
    merge_files(ROOT_DIR)
