/**
 * Hub backdrop (bg-canvas, grid-lines, noise) for panel pages.
 * Custom cursor when <html class="hub-custom-cursor"> (landing) or
 * <html class="hub-panel-cursor"> (panel apps).
 */
(function () {
  function useHubCursor() {
    const h = document.documentElement;
    return h.classList.contains("hub-custom-cursor") || h.classList.contains("hub-panel-cursor");
  }

  function ensureBackdrop() {
    if (document.querySelector(".bg-canvas")) return;
    const bg = document.createElement("div");
    bg.className = "bg-canvas";
    const grid = document.createElement("div");
    grid.className = "grid-lines";
    const noise = document.createElement("div");
    noise.className = "noise";
    document.body.appendChild(bg);
    document.body.appendChild(grid);
    document.body.appendChild(noise);
  }

  function ensureCursor() {
    if (!useHubCursor()) return;
    if (document.getElementById("cursor")) return;
    const cursor = document.createElement("div");
    cursor.id = "cursor";
    const ring = document.createElement("div");
    ring.id = "cursor-ring";
    document.body.appendChild(cursor);
    document.body.appendChild(ring);
  }

  function runCursorLoop() {
    const cursor = document.getElementById("cursor");
    const ring = document.getElementById("cursor-ring");
    if (!cursor || !ring) return;

    let mx = 0;
    let my = 0;
    let rx = 0;
    let ry = 0;

    document.addEventListener("mousemove", (e) => {
      mx = e.clientX;
      my = e.clientY;
    });

    function frame() {
      cursor.style.left = mx + "px";
      cursor.style.top = my + "px";
      rx += (mx - rx) * 0.12;
      ry += (my - ry) * 0.12;
      ring.style.left = rx + "px";
      ring.style.top = ry + "px";
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  function init() {
    ensureBackdrop();
    ensureCursor();
    runCursorLoop();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
