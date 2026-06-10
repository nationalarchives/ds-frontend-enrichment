document.querySelectorAll(".tna-logo--adornable").forEach(($logo) => {
  /* eslint-disable-next-line no-magic-numbers */
  for (let firework = 0; firework < 3; firework += 1) {
    const $firework = document.createElement("span");
    $firework.classList.add("tna-logo__firework");
    $logo.appendChild($firework);
  }
});
