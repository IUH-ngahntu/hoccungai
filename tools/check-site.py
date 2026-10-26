#!/usr/bin/env python3
"""Kiểm tra tĩnh: liên kết nội bộ, alt, width/height, cấu trúc trang, tương phản, số dòng JS.
Chạy trong thư mục gốc dự án: python3 tools/check-site.py"""
import re, sys, os, glob
from html.parser import HTMLParser
from urllib.parse import urldefrag, unquote
PAGES = sorted(glob.glob('*.html')); fails = []; stats = {'links': 0, 'ok': 0}
def fail(m): fails.append(m); print('  LỖI:', m)
class P(HTMLParser):
    def __init__(s): super().__init__(); s.refs = []; s.ids = set(); s.tags = []; s.imgs = []; s.cur = 0; s.h1 = 0; s.style = 0; s.title = ''; s._t = False; s.lang = None; s.charset = False
    def handle_starttag(s, t, a):
        a = dict(a); s.tags.append(t)
        if 'id' in a: s.ids.add(a['id'])
        if t == 'html': s.lang = a.get('lang')
        if t == 'meta' and 'charset' in a: s.charset = a['charset'].lower() == 'utf-8'
        if t == 'h1': s.h1 += 1
        if t == 'title': s._t = True
        if 'style' in a: s.style += 1
        if a.get('aria-current') == 'page': s.cur += 1
        if t == 'img': s.imgs.append(a)
        for k in ('href', 'src', 'poster'):
            if k in a: s.refs.append(a[k])
        for k in ('srcset',):
            if k in a: s.refs += [x.strip().split()[0] for x in a[k].split(',') if x.strip()]
    def handle_data(s, d):
        if s._t: s.title += d
    def handle_endtag(s, t):
        if t == 'title': s._t = False
parsed = {}
for f in PAGES:
    p = P(); p.feed(open(f, encoding='utf8').read()); parsed[f] = p
for f, p in parsed.items():
    print(f'[{f}]')
    if p.lang != 'vi': fail(f'{f}: thiếu lang="vi"')
    if not p.charset: fail(f'{f}: thiếu meta charset UTF-8')
    if p.h1 != 1: fail(f'{f}: có {p.h1} thẻ h1')
    if not p.title.strip(): fail(f'{f}: thiếu title')
    for t in ('header', 'nav', 'main', 'footer'):
        if t not in p.tags: fail(f'{f}: thiếu <{t}>')
    if p.cur != 1: fail(f'{f}: có {p.cur} aria-current="page" (menu hoặc breadcrumb; cần đúng 1)')
    if p.style: fail(f'{f}: có {p.style} thuộc tính style inline')
    for im in p.imgs:
        if 'alt' not in im: fail(f'{f}: ảnh {im.get("src")} thiếu alt')
        if 'width' not in im or 'height' not in im: fail(f'{f}: ảnh {im.get("src")} thiếu width/height')
    for r in p.refs:
        if re.match(r'(https?:|mailto:|data:)', r): continue
        stats['links'] += 1; path, frag = urldefrag(r); path = unquote(path)
        tgt = path or f
        if not os.path.exists(tgt): fail(f'{f}: liên kết hỏng → {r}'); continue
        if frag and tgt.endswith('.html') and frag not in parsed[tgt].ids and not (frag.startswith('i-') or 'icons.svg' in path): fail(f'{f}: không có id #{frag} trong {tgt}')
        else: stats['ok'] += 1
# srcset: ít nhất 1 ảnh có ≥3 kích cỡ
three = any(len(re.findall(r'\d+w', open(f, encoding='utf8').read())) >= 3 for f in PAGES)
print('Ảnh có ≥ 3 kích cỡ srcset:', 'có' if three else 'KHÔNG'); three or fail('không có ảnh nào có 3 kích cỡ')
for f in glob.glob('js/*.js'):
    n = len(open(f, encoding='utf8').read().splitlines()); print(f'{f}: {n} dòng'); n > 60 and fail(f'{f} dài {n} dòng (> 60)')
# tương phản WCAG
def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]; return .2126*c[0] + .7152*c[1] + .0722*c[2]
def cr(a, b): x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)
pairs = [('Chữ thường / nền trắng', '#1e293b', '#ffffff'), ('Chữ phụ (figcaption) / nền trắng', '#475569', '#ffffff'), ('Liên kết / nền trắng', '#9a3412', '#ffffff'),
         ('Nút: chữ trắng / nền cam', '#ffffff', '#c2410c'), ('Menu: chữ xanh navy / nền peach (trang hiện tại)', '#0b2545', '#fed7aa'), ('Tiêu đề / nền trắng', '#0b2545', '#ffffff'),
         ('Hero: chữ trắng / nền navy', '#ffffff', '#0b2545'), ('Chân trang: chữ #e2e8f0 / nền navy', '#e2e8f0', '#0b2545'), ('Liên kết / nền kem (thẻ)', '#9a3412', '#fff7ed'), ('Chữ phụ / nền kem', '#475569', '#fff7ed'), ('Thanh điều khiển: chữ trắng / navy', '#ffffff', '#0b2545')]
print('Tương phản chữ/nền (yêu cầu ≥ 4,5:1):')
for n, a, b in pairs:
    r = cr(a, b); print(f'  {r:5.2f}:1  {n}'); r < 4.5 and fail(f'tương phản thấp: {n} = {r:.2f}')
print(f'\nLiên kết/tệp đã kiểm: {stats["links"]}; hợp lệ: {stats["ok"]}')
print('KẾT QUẢ:', 'ĐẠT' if not fails else f'{len(fails)} lỗi'); sys.exit(1 if fails else 0)
