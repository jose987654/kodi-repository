import hashlib

zip_path = 'repository.seedr/repository.seedr-1.0.0.zip'
md5_path = 'repository.seedr/repository.seedr-1.0.0.zip.md5'

with open(zip_path, 'rb') as f:
    md5 = hashlib.md5(f.read()).hexdigest()

with open(md5_path, 'w') as f:
    f.write(md5)

print(f"MD5 for {zip_path}: {md5}") 