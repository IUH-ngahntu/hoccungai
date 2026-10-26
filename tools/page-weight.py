#!/usr/bin/env python3
"""Đo dung lượng trang (byte thực tế, chưa nén và gzip). Dùng: python3 tools/page-weight.py [--detail index.html]
Kịch bản xấu nhất = màn 1280 px, đã cuộn hết trang (ảnh lazy được tải) và đã bấm phát video."""
import os, gzip, glob, sys
from html.parser import HTMLParser
HERO = {'desk': 'img/hero-1280.webp', 'mob': 'img/hero-360.webp'}
class R(HTMLParser):
    def __init__(s): super().__init__(); s.eager = []; s.lazy = []; s.media = []; s.pic = False
    def handle_starttag(s, t, a):
        a = dict(a); u = None; bucket = s.eager
        if t == 'link' and a.get('rel') in ('stylesheet', 'icon'): u = a['href']
        elif t == 'script' and a.get('src'): u = a['src']
        elif t == 'img':
            u = a.get('src'); bucket = s.lazy if a.get('loading') == 'lazy' else s.eager
            if u == 'img/hero-1280.jpg': u = 'HERO'          # trình duyệt hiện đại chọn WebP trong <picture>
            if a.get('srcset'): u = 'img/' + a['srcset'].split(',')[-1].strip().split()[0].split('/')[-1]  # bản lớn nhất
        elif t == 'video' and a.get('poster'): u = a['poster']
        elif t == 'source' and a.get('src', '').endswith('.mp4'): u = a['src']; bucket = s.media
        elif t == 'track': u = a['src']; bucket = s.media
        if u: bucket.append(u)
def sz(p): return os.path.getsize(p)
def gzs(p): return len(gzip.compress(open(p, 'rb').read(), 6))
def collect(f, kind):
    r = R(); r.feed(open(f, encoding='utf8').read())
    fix = lambda L: [HERO[kind] if x == 'HERO' else x for x in L]
    return [f] + fix(r.eager), fix(r.lazy), r.media
detail = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == '--detail' else None
print(f'{"Trang":24}{"Màn":5}{"Số tệp":>7}{"Ban đầu (B)":>13}{"gzip (B)":>10}{"Lazy (B)":>10}{"Media (B)":>11}{"Worst (KB)":>12}')
for f in sorted(glob.glob('*.html')):
    for k in ('desk', 'mob'):
        e, l, m = collect(f, k); a = sum(map(sz, e)); g = sum(map(gzs, e)); lz = sum(map(sz, l)); md = sum(map(sz, m))
        print(f'{f:24}{k:5}{len(e)+len(l)+len(m):>7}{a:>13}{g:>10}{lz:>10}{md:>11}{(a+lz+md)/1000:>12.1f}')
        if detail == f and k == 'desk':
            for grp, name in ((e, 'ban đầu'), (l, 'lazy'), (m, 'media (khi bấm phát)')):
                for x in grp: print(f'      [{name}] {x}: {sz(x)} B')
