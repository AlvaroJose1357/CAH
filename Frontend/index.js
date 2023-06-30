import { App } from "./App.js";
import { Modal } from "./Components/Modal.js";

const d = document,
  $main = d.querySelector("main");

// ** Eventos globales ------------------------------------------------------------------
d.addEventListener("DOMContentLoaded", App);

// ** Eventos oferta ---------------------------------------------------------------------
// Evento para abrir la modificacion de una oferta
const $botonModificar = d.querySelector(".boton-modificar-oferta"),
  $botonEliminar = d.querySelector(".boton-eliminar-oferta");

function openModificarOferta() {
  open("./modificar-oferta.html", "_self");
  console.log("hola");
}

$botonModificar.addEventListener("click", openModificarOferta);

// Evento para abrir la ventana modal de confirmal eliminacion de una oferta

$botonEliminar.addEventListener("click", () => {
  $main.appendChild(Modal());
  //Cancelar modal
  const $modal = $main.lastElementChild,
    $cancelarModal = d.querySelector(".cancelar-modal");
  function elimiminarModal() {
    $modal.remove();
  }
  $cancelarModal.addEventListener("click", elimiminarModal);
});
