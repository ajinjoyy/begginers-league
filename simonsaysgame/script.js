document.addEventListener('DOMContentLoaded', () => {
  const colors = ["red", "green", "blue", "yellow"];
  let sequence = [];
  let userSequence = [];
  let level = 0;
  let acceptingInput = false;

  const startBtn = document.getElementById("start");
  const gameEl = document.getElementById("game");
  const levelTitle = document.getElementById("level-title");

  startBtn.addEventListener("click", () => {
    startBtn.classList.add("hide");   
    gameEl.classList.remove("hide");  
    startGame();
  });

  function startGame() {
    sequence = [];
    userSequence = [];
    level = 0;
    nextLevel();
  }

  function nextLevel() {
    level++;
    levelTitle.innerText = `Level: ${level}`;
    sequence = [];
    userSequence = [];
    for (let i = 0; i < level + 2; i++) generateNextColor();
    playSequence();
  }

  function generateNextColor() {
    const rand = Math.random();
    if (rand < 0.25) sequence.push("red");
    else if (rand < 0.5) sequence.push("green");
    else if (rand < 0.75) sequence.push("blue");
    else sequence.push("yellow");
  }

  function playSequence() {
    acceptingInput = false;
    let i = 0;
    const interval = setInterval(() => {
      glow(sequence[i]);
      i++;
      if (i >= sequence.length) {
        clearInterval(interval);
        setTimeout(() => { acceptingInput = true; }, 500);
      }
    }, 800);
  }

  function glow(color) {
    const btn = document.querySelector(`.${color}`);
    btn.classList.add("glow");
    setTimeout(() => btn.classList.remove("glow"), 200);
  }

  document.querySelectorAll(".button").forEach(btn => {
    btn.addEventListener("click", () => {
      if (!acceptingInput) return;
      const color = btn.dataset.color;
      glow(color);
      userSequence.push(color);

      if (!checkUserMove()) {
        alert("Wrong! Game Over");
        acceptingInput = false;
        startBtn.classList.remove("hide"); // show start again
        gameEl.classList.add("hide");      // hide game
        return;
      }

      if (userSequence.length === sequence.length) {
        setTimeout(() => nextLevel(), 1000);
      }
    });
  });

  function checkUserMove() {
    const idx = userSequence.length - 1;
    return userSequence[idx] === sequence[idx];
  }
});





