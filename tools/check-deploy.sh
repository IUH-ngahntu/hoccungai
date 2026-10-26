#!/bin/sh
# Kiểm tra bản đã xuất bản: HTTPS, Content-Type, tua video (Accept-Ranges/206).
# Dùng: sh tools/check-deploy.sh https://TENBAN.github.io/hoccungai   (hoặc http://localhost:8080)
BASE="${1:-http://localhost:8080}"; BASE="${BASE%/}"; FAIL=0
case "$BASE" in https://*) echo "HTTPS: có";; http://localhost*) echo "HTTPS: bỏ qua (localhost)";; *) echo "HTTPS: KHÔNG – bật Enforce HTTPS"; FAIL=1;; esac
chk() { # đường dẫn, content-type mong đợi
  H=$(curl -sIL "$BASE/$1" | tr -d '\r'); S=$(echo "$H" | awk '/^HTTP/{s=$2}END{print s}')
  T=$(echo "$H" | awk 'tolower($1)=="content-type:"{t=$2}END{print t}')
  if echo "$T" | grep -Eq "^($2)"; then R="ĐẠT"; else R="LỖI"; FAIL=1; fi
  printf "%-26s HTTP %s  %-28s (cần %s) %s\n" "$1" "$S" "$T" "$2" "$R"; }
chk index.html text/html; chk css/site.css text/css; chk js/site.js "application/javascript|text/javascript"
chk video/intro.mp4 video/mp4; chk video/intro.webm video/webm; chk video/bai-2.vi.vtt text/vtt
chk audio/bai-2.mp3 audio/mpeg; chk audio/bai-2.ogg audio/ogg; chk img/hero-1280.webp image/webp; chk media/media.json application/json
AR=$(curl -sI "$BASE/video/bai-2.mp4" | tr -d '\r' | awk 'tolower($1)=="accept-ranges:"{print $2}')
RS=$(curl -s -o /dev/null -w "%{http_code}" -H "Range: bytes=0-1023" "$BASE/video/bai-2.mp4")
echo "Accept-Ranges: ${AR:-không có} | Range 0-1023 → HTTP $RS (cần 206)"; [ "$RS" = 206 ] || FAIL=1
[ $FAIL = 0 ] && echo "KẾT QUẢ: ĐẠT" || echo "KẾT QUẢ: CÓ LỖI"; exit $FAIL
