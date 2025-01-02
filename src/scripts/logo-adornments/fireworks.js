document.querySelectorAll(".tna-logo--adornable").forEach(($logo) => {
  for (let i = 0; i < 3; i++) {
    const $firework = document.createElement("span");
    $firework.classList.add("tna-logo__firework");
    $logo.appendChild($firework);
  }
});
