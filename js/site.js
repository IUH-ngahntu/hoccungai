// site.js – menu di động, trình phát tùy biến và nút «Xem thêm» (tổng ≤ 60 dòng).
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const fmt = t => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, '0')}`;
  document.documentElement.classList.add('js');
  const toggle = $('.nav-toggle'), menu = $('#menu');
  toggle?.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', open);
    menu.classList.toggle('open', open);
  });
  document.querySelectorAll('[data-player]').forEach(box => {
    const v = $('video', box), track = v.textTracks[0];
    v.removeAttribute('controls');                       // thay bằng thanh điều khiển tùy biến
    const bar = document.createElement('div');
    bar.className = 'ctrl';
    bar.innerHTML = '<button type="button" class="pp">Phát</button>' +
      '<input class="seek" type="range" min="0" max="100" step="0.1" value="0" aria-label="Thanh tiến độ">' +
      '<span class="time">0:00</span><button type="button" class="cc" aria-pressed="true">Phụ đề</button>';
    const msg = document.createElement('p');
    msg.className = 'err'; msg.setAttribute('role', 'alert'); msg.hidden = true;
    box.insertBefore(bar, $('figcaption', box)); box.append(msg);
    const [pp, seek, time, cc] = ['.pp', '.seek', '.time', '.cc'].map(s => $(s, bar));
    const fail = text => { msg.textContent = text; msg.hidden = false; };
    if (track) track.mode = 'showing';
    pp.addEventListener('click', () => {
      if (!v.paused) return v.pause();
      msg.hidden = true;
      v.play().catch(e => fail(`Không phát được video (${e.name}). Hãy đọc bản chữ hoặc nghe bản âm thanh.`));
    });
    v.addEventListener('play', () => { pp.textContent = 'Tạm dừng'; });
    v.addEventListener('pause', () => { pp.textContent = 'Phát'; });
    v.addEventListener('timeupdate', () => {
      if (v.duration) seek.value = (v.currentTime / v.duration) * 100;
      time.textContent = `${fmt(v.currentTime)} / ${fmt(v.duration || 0)}`;
    });
    seek.addEventListener('input', () => { if (v.duration) v.currentTime = (seek.value / 100) * v.duration; });
    cc.addEventListener('click', () => {
      if (!track) return; const on = track.mode !== "showing";
      track.mode = on ? 'showing' : 'hidden'; cc.setAttribute('aria-pressed', on);
    });
    $('source:last-of-type', v).addEventListener('error', () => fail('Không tải được video. Hãy đọc bản chữ bên dưới.'));
    v.addEventListener('error', () => fail('Video bị lỗi khi đang phát. Hãy tải lại trang hoặc đọc bản chữ.'));
  });
  const more = $('#more-btn');                           // «Xem thêm»: nạp media.json bằng fetch
  more?.addEventListener('click', async () => {
    const status = $('#more-status'); more.disabled = true; status.textContent = 'Đang tải…';
    try {
      const res = await fetch('media/media.json');
      if (!res.ok) throw new Error(res.status);
      const rest = (await res.json()).items.slice(3);
      $('#media-list').insertAdjacentHTML('beforeend', rest.map(i =>
        `<li class="card"><h3><a href="${i.href}">${i.title}</a></h3><p>${i.type} · ${i.size_kb} KB</p></li>`).join(''));
      more.hidden = true; status.textContent = `Đã nạp thêm ${rest.length} mục.`;
    } catch (e) { more.disabled = false; status.textContent = 'Không nạp được danh sách. Vui lòng thử lại.'; }
  });
})();
