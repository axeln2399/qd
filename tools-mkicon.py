import zlib, struct, math

BG   = (0x17, 0x19, 0x1C)
INK  = (0xE7, 0xE8, 0xE4)
ASK  = (0xC0, 0x55, 0x3F)
BID  = (0x4E, 0x94, 0x69)

CX, CY = 228.0, 228.0
R_OUT, R_IN = 132.0, 98.0
BX, BY = 292.0, 292.0          # tail origin, just inside the bowl
TAIL_LEN, TAIL_W, TAIL_OFF = 148.0, 28.0, 23.0
C45 = math.cos(math.radians(45.0))
S45 = math.sin(math.radians(45.0))

def in_bar(x, y, off):
    """Point in the rotated tail bar offset perpendicular by `off`."""
    dx, dy = x - BX, y - BY
    u =  dx * C45 + dy * S45          # along the tail
    v = -dx * S45 + dy * C45          # across it
    return 0.0 <= u <= TAIL_LEN and abs(v - off) <= TAIL_W / 2.0

def sample(x, y):
    if in_bar(x, y, -TAIL_OFF):
        return ASK
    if in_bar(x, y, TAIL_OFF):
        return BID
    d = math.hypot(x - CX, y - CY)
    if R_IN <= d <= R_OUT:
        return INK
    return BG

def render(S, ss=3):
    u = 512.0 / S
    step = u / ss
    half = step / 2.0
    inv = 1.0 / (ss * ss)
    rows = []
    for py in range(S):
        row = bytearray()
        for px in range(S):
            r = g = b = 0
            for sy in range(ss):
                yy = (py * u) + sy * step + half
                for sx in range(ss):
                    xx = (px * u) + sx * step + half
                    c = sample(xx, yy)
                    r += c[0]; g += c[1]; b += c[2]
            row += bytes((int(r * inv), int(g * inv), int(b * inv)))
        rows.append(bytes(row))
    return rows

def png(path, S):
    raw = b"".join(b"\x00" + r for r in render(S))
    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    out = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", S, S, 8, 2, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    open(path, "wb").write(out)
    print(path, S, len(out), "bytes")

png("icon-512.png", 512)
png("icon-192.png", 192)
png("apple-touch-icon.png", 180)
