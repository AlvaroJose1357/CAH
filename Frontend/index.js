import { App } from "./App.js";
import { Modal } from "./Components/Modal.js";

const d = document,
  $main = d.querySelector("main");

// ** Eventos globales ------------------------------------------------------------------
d.addEventListener("DOMContentLoaded", App);

// ** Delegacion de eventos, click-----------------------------------------------------
d.addEventListener("click", (e) => {
  //  Eventos oferta ---------------------------------------------------------------------
  //Para abrir modificar-oferta
  if (e.target.matches(".boton-modificar-oferta")) {
    open("./modificar-oferta.html", "_self");
  }
  //Para abrir modal de confirmacion eliminar oferta
  if (e.target.matches(".boton-eliminar-oferta")) {
    $main.appendChild(Modal());
  }
  //Para cerrar modal
  if (e.target.matches(".modal .cancelar-modal")) {
    d.querySelector(".modal").remove();
  }
});
