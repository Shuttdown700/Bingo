import glob
import os

def sort_txt_files():
    # Find all .txt files in the current directory
    files = glob.glob('*.txt')

    if not files:
        print("No .txt files found in the current directory.")
        return

    print(f"\nFound {len(files)} {"files" if len(files) != 1 else "file"}. Starting sort process...")

    for idx, file_path in enumerate(files):
        try:
            # 1. Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                # Read lines and strip whitespace to handle inconsistent spacing
                lines = [line.strip() for line in f.readlines()]

            # 2. Filter out empty lines (optional, keeps files clean)
            lines = [line for line in lines if line]

            # 3. Sort the lines alphabetically
            # use key=str.lower for case-insensitive sorting (A before b)
            lines.sort(key=str.lower)

            # 4. Write back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
                # Add a final newline at the end of the file usually best practice
                if idx < len(files) - 1:
                    f.write('\n')

            print(f"✔ Successfully sorted: {file_path}")

        except Exception as e:
            print(f"✘ Error processing {file_path}: {e}")
    print("\nSorting process completed.")

if __name__ == "__main__":
    sort_txt_files()