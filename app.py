<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Scopri cosa fai</title>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      font-family: Arial, sans-serif;
      background: radial-gradient(circle at top, #23346b 0%, #12182f 45%, #070b16 100%);
    }

    .container {
      position: relative;
      z-index: 2;
      width: 400px;
      max-width: 92vw;
      padding: 32px 24px;
      border-radius: 24px;
      text-align: center;
      background: rgba(255,255,255,0.10);
      border: 1px solid rgba(255,255,255,0.14);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      box-shadow: 0 20px 60px rgba(0,0,0,0.35);
      animation: fadeInUp 0.8s ease;
    }

    h1 {
      margin: 0 0 10px;
      color: #fff;
      font-size: 28px;
    }

    .sub {
      margin: 0 0 24px;
      color: rgba(255,255,255,0.8);
      font-size: 15px;
    }

    button {
      border: none;
      border-radius: 14px;
      padding: 16px 26px;
      font-size: 18px;
      font-weight: bold;
      color: white;
      cursor: pointer;
      background: linear-gradient(135deg, #00a2ff, #005eff);
      box-shadow: 0 12px 28px rgba(0, 102, 255, 0.35);
      transition: transform 0.15s ease, box-shadow 0.2s ease;
    }

    button:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 16px 34px rgba(0, 102, 255, 0.42);
    }

    button:active {
      transform: scale(0.97);
    }

    #risultato {
      margin-top: 28px;
      min-height: 70px;
      font-size: 48px;
      font-weight: 900;
      color: #ff3a3a;
      text-shadow:
        0 0 12px rgba(255, 58, 58, 0.35),
        0 0 28px rgba(255, 58, 58, 0.20);
      opacity: 0;
      transform: scale(0.5);
      visibility: hidden;
    }

    #risultato.show {
      opacity: 1;
      visibility: visible;
      transform: scale(1);
      animation: popIn 0.65s cubic-bezier(.2,1.4,.3,1);
    }

    .confetti-layer {
      position: fixed;
      inset: 0;
      pointer-events: none;
      overflow: hidden;
      z-index: 10;
    }

    .confetti {
      position: absolute;
      top: -20px;
      width: 12px;
      height: 18px;
      opacity: 0.95;
      animation-name: fall;
      animation-timing-function: linear;
      animation-fill-mode: forwards;
    }

    .confetti.ribbon {
      width: 6px;
      height: 24px;
      border-radius: 3px;
    }

    .flash {
      position: fixed;
      inset: 0;
      background: rgba(255,255,255,0);
      pointer-events: none;
      z-index: 9;
    }

    .flash.active {
      animation: flashAnim 0.35s ease;
    }

    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(24px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes popIn {
      0% {
        transform: scale(0.5);
        opacity: 0;
      }
      60% {
        transform: scale(1.18);
        opacity: 1;
      }
      100% {
        transform: scale(1);
        opacity: 1;
      }
    }

    @keyframes fall {
      0% {
        transform: translateY(0) rotate(0deg);
      }
      100% {
        transform: translateY(110vh) rotate(720deg);
      }
    }

    @keyframes flashAnim {
      0%   { background: rgba(255,255,255,0); }
      40%  { background: rgba(255,255,255,0.12); }
      100% { background: rgba(255,255,255,0); }
    }
  </style>
</head>
<body>
  <div class="flash" id="flash"></div>
  <div class="confetti-layer" id="confettiLayer"></div>

  <div class="container">
    <h1>Scopri cosa fai</h1>
    <p class="sub">Premi il pulsante e guarda cosa succede.</p>

    <button id="btnScopri">Clicca qui</button>

    <div id="risultato">Vommetà!</div>
  </div>

  <script>
    const btn = document.getElementById("btnScopri");
    const risultato = document.getElementById("risultato");
    const confettiLayer = document.getElementById("confettiLayer");
    const flash = document.getElementById("flash");

    let alreadyShown = false;
    let audioCtx = null;

    function playSuspense() {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (!AudioContextClass) return;

      if (!audioCtx) {
        audioCtx = new AudioContextClass();
      }

      if (audioCtx.state === "suspended") {
        audioCtx.resume();
      }

      const now = audioCtx.currentTime;

      const master = audioCtx.createGain();
      master.gain.setValueAtTime(0.0001, now);
      master.gain.exponentialRampToValueAtTime(0.16, now + 0.03);
      master.gain.exponentialRampToValueAtTime(0.0001, now + 0.9);
      master.connect(audioCtx.destination);

      const notes = [523.25, 659.25, 783.99];

      notes.forEach((freq, index) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();

        osc.type = "triangle";
        osc.frequency.setValueAtTime(freq, now + index * 0.08);

        gain.gain.setValueAtTime(0.0001, now + index * 0.08);
        gain.gain.exponentialRampToValueAtTime(0.12, now + index * 0.08 + 0.01);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + index * 0.08 + 0.22);

        osc.connect(gain);
        gain.connect(master);

        osc.start(now + index * 0.08);
        osc.stop(now + index * 0.08 + 0.22);
      });

      const finalOsc = audioCtx.createOscillator();
      const finalGain = audioCtx.createGain();

      finalOsc.type = "square";
      finalOsc.frequency.setValueAtTime(1046.5, now + 0.28);

      finalGain.gain.setValueAtTime(0.0001, now + 0.28);
      finalGain.gain.exponentialRampToValueAtTime(0.10, now + 0.30);
      finalGain.gain.exponentialRampToValueAtTime(0.0001, now + 0.5);

      finalOsc.connect(finalGain);
      finalGain.connect(master);

      finalOsc.start(now + 0.28);
      finalOsc.stop(now + 0.5);
    }

    function randomColor() {
      const colors = [
        "#ff4d4d", "#ffd93d", "#6bffb0",
        "#4dc3ff", "#c47dff", "#ff7ad9",
        "#ffffff", "#ff9f1c"
      ];
      return colors[Math.floor(Math.random() * colors.length)];
    }

    function createConfettiBurst() {
      confettiLayer.innerHTML = "";

      for (let i = 0; i < 120; i++) {
        const piece = document.createElement("div");
        const isRibbon = Math.random() > 0.5;

        piece.className = isRibbon ? "confetti ribbon" : "confetti";
        piece.style.left = Math.random() * 100 + "vw";
        piece.style.background = randomColor();
        piece.style.animationDuration = (2.8 + Math.random() * 2.2) + "s";
        piece.style.animationDelay = (Math.random() * 0.6) + "s";
        piece.style.opacity = 0.75 + Math.random() * 0.25;

        if (!isRibbon) {
          const size = 8 + Math.random() * 10;
          piece.style.width = size + "px";
          piece.style.height = (size * 1.3) + "px";
        }

        confettiLayer.appendChild(piece);
      }

      setTimeout(() => {
        confettiLayer.innerHTML = "";
      }, 6500);
    }

    function showResult() {
      flash.classList.remove("active");
      void flash.offsetWidth;
      flash.classList.add("active");

      risultato.classList.remove("show");
      void risultato.offsetWidth;
      risultato.classList.add("show");

      createConfettiBurst();
    }

    btn.addEventListener("click", () => {
      playSuspense();

      if (alreadyShown) {
        showResult();
        return;
      }

      alreadyShown = true;

      setTimeout(() => {
        showResult();
      }, 900);
    });
  </script>
</body>
</html>
