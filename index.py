
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>문호 스트레이독스 RPG</title>
<style>
* { box-sizing: border-box; }

body {
  margin: 0;
  min-height: 100vh;
  background: #15171c;
  color: #e8e5e0;
  font-family: "Noto Serif KR", serif;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 24px;
}

.game {
  width: 100%;
  max-width: 680px;
  padding: 38px;
  background: #20232a;
  border: 1px solid #45434a;
  border-radius: 12px;
}

.subtitle {
  color: #aaa3a0;
  letter-spacing: 4px;
  font-size: 11px;
}

h1 {
  font-size: 30px;
  margin: 14px 0;
}

.line {
  height: 1px;
  background: #514d50;
  margin: 24px 0;
}

#story {
  white-space: pre-line;
  line-height: 2;
  min-height: 130px;
}

button {
  display: block;
  width: 100%;
  padding: 15px;
  margin-top: 12px;
  background: #30343e;
  color: #eee;
  border: 1px solid #595b63;
  border-radius: 5px;
  cursor: pointer;
  text-align: left;
}

button:hover {
  background: #48434a;
}

#choices { margin-top: 24px; }

.small {
  font-size: 11px;
  color: #999;
  text-align: center;
  margin-top: 28px;
}
</style>
</head>

<body>
<main class="game">
  <div class="subtitle">BUNGO STRAY DOGS · ORIGINAL RPG</div>
  <h1>문호 스트레이독스</h1>
  <div class="line"></div>

  <div id="story">
    이야기가 시작된다.

    당신의 선택은 이 이야기의 결말을 바꿀 것이다.
  </div>

  <div id="choices">
    <button onclick="startGame()">이야기 시작하기</button>
  </div>

  <div class="small">
    ORIGINAL CHARACTER RPG
  </div>
</main>

<script>
let affection = 0;
let eventNumber = 0;

const story = document.getElementById("story");
const choices = document.getElementById("choices");

function showEvent(text, options) {
  story.textContent = text;
  choices.innerHTML = "";

  options.forEach(option => {
    const button = document.createElement("button");
    button.textContent = option.text;

    button.onclick = () => {
      affection += option.point;
      eventNumber++;
      option.action();
    };

    choices.appendChild(button);
  });
}

function startGame() {
  affection = 0;
  eventNumber = 0;

  showEvent(
    "요코하마의 어느 평범한 하루.\n\n당신은 익숙한 거리에서 낯선 인물을 발견했다.",
    [
      {
        text: "먼저 말을 건다.",
        point: 2,
        action: nextEvent
      },
      {
        text: "조금 더 지켜본다.",
        point: 1,
        action: nextEvent
      },
      {
        text: "그대로 지나친다.",
        point: -1,
        action: nextEvent
      }
    ]
  );
}

function nextEvent() {
  showEvent(
    "상대는 당신을 바라보았다.\n\n\"무슨 일이야?\"",
    [
      {
        text: "솔직하게 대답한다.",
        point: 2,
        action: ending
      },
      {
        text: "적당히 둘러댄다.",
        point: 0,
        action: ending
      },
      {
        text: "대답하지 않는다.",
        point: -1,
        action: ending
      }
    ]
  );
}

function ending() {
  story.textContent =
    "이야기의 끝에 도달했다.\n\n" +
    (affection >= 3
      ? "ENDING 01 · 새로운 인연"
      : affection >= 0
      ? "ENDING 02 · 평범한 만남"
      : "ENDING 03 · 엇갈린 시선");

  choices.innerHTML = "";

  const button = document.createElement("button");
  button.textContent = "다시 시작하기";
  button.onclick = startGame;

  choices.appendChild(button);
}
</script>
</body>
</html>
