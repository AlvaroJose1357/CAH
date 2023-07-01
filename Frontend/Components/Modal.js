export function Modal() {
  const $modal = document.createElement("article");
  $modal.classList.add("modal");
  $modal.innerHTML = `
    <h2>Estas seguro de eliminar la oferta 10212</h2>
    <div>
      <button class="button">ACEPTAR</button>
      <button class="button cancelar-modal">CANCELAR</button>
    </div>
  `;
  return $modal;
}
