// import { App } from "../../../Frontend/App.js";
import { Modal } from "./Components/Modal.js";

const d = document,
  $main = d.querySelector("main");

// // ** Eventos globales ------------------------------------------------------------------
// d.addEventListener("DOMContentLoaded", App);

// ** Delegacion de eventos, click-----------------------------------------------------
d.addEventListener("click", (e) => {
  //  Eventos oferta ---------------------------------------------------------------------
  //Para abrir modal de confirmacion eliminar oferta
  if (e.target.matches(".boton-eliminar-oferta")) {
    $main.appendChild(Modal());
  }
  //Para cerrar modal
  if (e.target.matches(".modal .cancelar-modal")) {
    d.querySelector(".modal").remove();
  }

  //  Eventos vehiculo ---------------------------------------------------------------------

  //Para abrir modal de confirmacion eliminar vehiculo
  if (e.target.matches(".boton-eliminar-vehiculo")) {
    $main.appendChild(Modal());
  }
  //Para cerrar modal
  if (e.target.matches(".modal .cancelar-modal")) {
    d.querySelector(".modal").remove();
  }
});
