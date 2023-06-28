export function Footer() {
  const $footer = document.createElement("article");
  $footer.innerHTML = `
    <section>
        <h2>Lorem</h2>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptate tempora nemo, quaerat rerum totam
          et.Lorem
          ipsum dolor sit, amet consectetur adipisicing elit. Voluptate tempora nemo, quaerat rerum totam et.</p>
      </section>
      <section>
        <h2>CONTACTANOS</h2>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptate tempora nemo, quaerat rerum totam et.</p>
        <img src="../assets/img/logo.png" alt="logo">
      </section>
  `;
  return $footer;
}
