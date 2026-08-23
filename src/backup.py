import tarfile
import os

def create_backup(source_dir, output_filename):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    print(f"Backup created: {output_filename}")

if __name__ == "__main__":
    os.makedirs("test_backup_dir", exist_ok=True)
    with open("test_backup_dir/file.txt", "w") as f:
        f.write("hello backup")
    create_backup("test_backup_dir", "backup.tar.gz")
