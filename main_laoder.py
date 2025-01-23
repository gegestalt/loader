
import hashlib
import os
import sys
import requests

import tempfile


def generate_filename(n):
    h = hashlib.sha256()
    h.update(str(n).encode())
    digest = h.hexdigest()[0x0:0xf]
    filename = tempfile.NamedTemporaryFile(delete=False, suffix=f'__{digest}')
    return filename.name

def load_chunks(url):
    parts = {}
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        for i,chunk  in enumerate(r.iter_content(chunk_size=0x4000),start=0x1):
            if chunk:
                filename = generate_filename(len(parts))
                parts[i] = filename
                with open(filename, "wb") as fh:
                    fh.write(chunk)
    return parts

def rebuild_file(parts):
    new_filename = tempfile.NamedTemporaryFile(delete=False,   suffix=".exe")
    with open(new_filename.name, "wb") as fh:
        for part in parts.keys():
            filename = parts[part]
            data = open(filename, "rb").read()
            fh.write(data)
        return new_filename.name

def start_process(file_path):
    os.execv(file_path, ["&"])

def main():
    opts = sys.argv
    if len(opts) < 0x2:
        return
    else:
        res = load_chunks(opts[0x1])
        new_file= rebuild_file(res)
        print(new_file)

if __name__ == "__main__":
    main()