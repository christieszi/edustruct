// game.js
document.addEventListener("DOMContentLoaded", function () {
  const character = document.getElementById("character");

  const speed = 10;

  document.addEventListener("keydown", function (event) {
    switch (event.key) {
      case "ArrowUp":
        moveCharacter(0, -speed);
        break;
      case "ArrowDown":
        moveCharacter(0, speed);
        break;
      case "ArrowLeft":
        moveCharacter(-speed, 0);
        break;
      case "ArrowRight":
        moveCharacter(speed, 0);
        break;
    }
  });

  function moveCharacter(deltaX, deltaY) {
    const characterRect = character.getBoundingClientRect();
    const maxX = window.innerWidth - characterRect.width;
    const maxY = window.innerHeight - characterRect.height;

    let newX = characterRect.left + deltaX;
    let newY = characterRect.top + deltaY;

    newX = Math.min(Math.max(newX, 0), maxX);
    newY = Math.min(Math.max(newY, 0), maxY);

    character.style.left = newX + "px";
    character.style.top = newY + "px";
  }
});