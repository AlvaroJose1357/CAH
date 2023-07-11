// import { App } from "../../../Frontend/App.js";
import { Modal } from "./Components/Modal.js";
import { Menu } from "./Components/Menu.js";

const d = document,
  $main = d.querySelector("main");

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

  //Para cerrar sesion
  if (e.target.matches(".cerrar-sesion")) {
    alert("Sesion Cerrada");
    d.cookie = "user_id =; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  }

  //Para abrir menu
  if (e.target.matches(".click-menu")) {
    const $active = d.querySelector(".menu-despegable");
    if ($active) {
      $active.remove();
    } else {
      const $mainIco = d.querySelector(".menu");
      $mainIco.classList.add("active");
      $mainIco.appendChild(Menu());
    }
  }
});
