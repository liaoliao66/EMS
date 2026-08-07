function toast(msg) {
  const el = document.getElementById("toast");
  if (!el) {
    alert(msg);
    return;
  }
  el.textContent = msg;
  el.classList.add("show");
  clearTimeout(window.__toastTimer);
  window.__toastTimer = setTimeout(() => el.classList.remove("show"), 2200);
}

function confirmAction(msg) {
  if (confirm(msg || "确认执行该操作？")) toast("操作已确认（原型）");
}

function confirmDelete(hasRef) {
  if (hasRef) {
    toast("存在关联数据，无法删除");
    return;
  }
  if (confirm("确认删除该数据？")) toast("已删除（原型）");
}

function ensureLightboxHost() {
  let host = document.getElementById("lightboxHost");
  if (host) return host;
  host = document.createElement("div");
  host.id = "lightboxHost";
  host.className = "lightbox-host";
  host.innerHTML = `
    <div class="lightbox-frame-wrap">
      <button type="button" class="lightbox-close" title="关闭" aria-label="关闭" onclick="closeLightbox()">
        <i class="fa-solid fa-xmark"></i>
      </button>
      <iframe id="lightboxFrame" title="业务弹窗"></iframe>
    </div>`;
  host.addEventListener("click", (e) => {
    if (e.target === host) closeLightbox();
  });
  document.body.appendChild(host);
  return host;
}

function openLightbox(url) {
  if (window.parent && window.parent !== window && typeof window.parent.openLightbox === "function") {
    window.parent.openLightbox(url);
    return;
  }
  const host = ensureLightboxHost();
  const frame = document.getElementById("lightboxFrame");
  const join = url.includes("?") ? "&" : "?";
  frame.src = url + join + "embed=1";
  host.classList.add("show");
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  if (window.parent && window.parent !== window && typeof window.parent.closeLightbox === "function") {
    window.parent.closeLightbox();
    return;
  }
  const host = document.getElementById("lightboxHost");
  if (!host) return;
  host.classList.remove("show");
  const frame = document.getElementById("lightboxFrame");
  if (frame) frame.src = "about:blank";
  document.body.style.overflow = "";
}

function closeModalOrBack(fallbackUrl) {
  if (window.parent && window.parent !== window && typeof window.parent.closeLightbox === "function") {
    window.parent.closeLightbox();
    return;
  }
  if (fallbackUrl) location.href = fallbackUrl;
  else history.back();
}

function saveAndClose(fallbackUrl) {
  toast("已保存；如需审批将提交平台（原型）");
  setTimeout(() => closeModalOrBack(fallbackUrl), 500);
}
