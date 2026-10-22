(() => {
  "use strict";
  const doc = document;
  const root = doc.documentElement;
  const $ = (q, base = doc) => base.querySelector(q);
  const $$ = (q, base = doc) => [...base.querySelectorAll(q)];

  const toast = $("#toast");
  let toastId;
  function notify(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("show");
    clearTimeout(toastId);
    toastId = setTimeout(() => toast.classList.remove("show"), 3300);
  }

  const theme = $("#themeToggle");
  function setTheme(next) {
    root.setAttribute("data-theme", next);
    if (theme) {
      theme.setAttribute("aria-label", next === "light" ? "Switch to dark theme" : "Switch to light theme");
      theme.setAttribute("title", next === "light" ? "Switch to dark theme" : "Switch to light theme");
    }
    try { localStorage.setItem("agastya-evidence-theme", next); } catch (_) {}
  }
  try { const saved = localStorage.getItem("agastya-evidence-theme"); if (saved === "light" || saved === "dark") setTheme(saved); } catch (_) {}
  theme?.addEventListener("click", () => setTheme(root.getAttribute("data-theme") === "light" ? "dark" : "light"));

  const menu = $("#menuToggle"), nav = $("#primaryNavigation");
  menu?.addEventListener("click", () => {
    const isOpen = nav?.classList.toggle("open") ?? false;
    menu.setAttribute("aria-expanded", String(isOpen));
    menu.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
  });
  $$("#primaryNavigation a").forEach(link => link.addEventListener("click", () => {
    nav?.classList.remove("open");
    menu?.setAttribute("aria-expanded", "false");
  }));

  async function copyText(value) {
    if (!value) return false;
    try {
      await navigator.clipboard.writeText(value);
      return true;
    } catch (_) {
      try {
        const ta = doc.createElement("textarea");
        ta.value = value; ta.setAttribute("readonly", "");
        ta.style.position = "fixed";ta.style.opacity = "0";
        doc.body.appendChild(ta);ta.select();
        const ok = doc.execCommand("copy");ta.remove();
        return ok;
      } catch (_) { return false; }
    }
  }
  $$("[data-copy]").forEach(el => el.addEventListener("click", async () => {
    const ok = await copyText(el.getAttribute("data-copy"));
    notify(ok ? "Copied to clipboard" : "Copy unavailable. Select the visible text instead.");
  }));

  let activeFilter = "all";
  const search = $("#artifactSearch");
  const list = $$(".artifact[data-category]");
  const empty = $("#vaultEmpty");
  const count = $("#vaultCount");
  function runFilter() {
    const query = (search?.value || "").trim().toLocaleLowerCase();
    let n = 0;
    for (const card of list) {
      const categories = (card.dataset.category || "").split(" ");
      const filterMatch = activeFilter === "all" || categories.includes(activeFilter);
      const hay = ((card.dataset.title || "") + " " + (card.textContent || "")).toLocaleLowerCase();
      const matches = filterMatch && (!query || hay.includes(query));
      card.hidden = !matches;
      if (matches) n++;
    }
    if (empty) empty.hidden = n > 0;
    if (count) count.textContent = n+" of "+list.length+" records";
  }
  search?.addEventListener("input", runFilter);
  $$("[data-filter]").forEach(button => button.addEventListener("click", () => {
    activeFilter = button.dataset.filter || "all";
    $$("[data-filter]").forEach(el => el.setAttribute("aria-pressed", String(el === button)));
    runFilter();
  }));
  runFilter();

  const verifyInput = $("#certificateInput");
  const result = $("#verifyResult");
  verifyInput?.addEventListener("change", async () => {
    const file = verifyInput.files?.[0];
    if (!file || !result) return;
    result.className = "";
    result.textContent = "Computing file SHA-256 locally. The PDF is not uploaded.";
    const expected = (verifyInput.dataset.sha256 || "").toLowerCase();
    if (!/^[a-f0-9]{64}$/.test(expected)) {
      result.className = "fail";
      result.textContent = "Verifier configuration is unavailable; use the published SHA256SUMS file.";
      return;
    }
    if (file.size > 12 * 1024 * 1024 || file.size < 5000) {
      result.className = "fail";
      result.textContent = "This file size does not match the expected evidence certificate.";
      return;
    }
    if (!globalThis.crypto?.subtle) {
      result.className = "fail";
      result.textContent = "Secure file hashing is unavailable in this browser. Use sha256sum or Get-FileHash.";
      return;
    }
    try {
      const contents = await file.arrayBuffer();
      const digest = await crypto.subtle.digest("SHA-256", contents);
      const actual = [...new Uint8Array(digest)].map(x => x.toString(16).padStart(2, "0")).join("");
      if (actual === expected) {
        result.className = "pass";
        result.textContent = "INTEGRITY MATCH — This file is byte-for-byte identical to the published certificate. This is not independent validation of the underlying training claims.";
      } else {
        result.className = "fail";
        result.textContent = "HASH MISMATCH — This is not the exact published PDF (computed "+actual.slice(0, 16)+"…). Check the download source or file changes.";
      }
    } catch (e) {
      result.className = "fail";
      result.textContent = "Could not calculate SHA-256 in this browser. Use the downloadable checksum file.";
    }
  });
  const year = $("#footerYear");
  if (year) year.textContent = String(new Date().getFullYear());
})();