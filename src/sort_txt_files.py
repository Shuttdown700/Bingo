import glob
import os
import sys

def sort_txt_files(directory=''):
    file_search_patterns = [
        os.path.join(directory, '*.txt'),
        os.path.join(directory, '*', '*.txt'),
    ]
    files = []
    for pattern in file_search_patterns:
        files.extend(glob.glob(pattern))
    files = sorted(set(files))

    if not files:
        print(f"No .txt files found in the directory '{directory}'.")
        return

    print(f"\nFound {len(files)} {'files' if len(files) != 1 else 'file'}. Starting sort process...")

    for idx, filepath in enumerate(files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines()]
            lines = sorted([line for line in lines if line], key=str.lower)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
                if idx < len(files) - 1:
                    f.write('\n')
            print(f"Successfully sorted: {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
    print("\nSorting process completed.")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python3 sort_txt_files.py [optional: directory]")
        sys.exit(1)
    else:
        directory = sys.argv[1] if len(sys.argv) == 2 else '.'
    sort_txt_files(directory)