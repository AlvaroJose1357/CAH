export function Nav() {
  const $nav = document.createElement("nav");
  $nav.innerHTML = `
    <img src="../assets/img/logo.png" alt="logo">
      <section class="nav-items">
        <a href="#">Inicio</a>
        <a href="#"><img src="../assets/img/user.png" alt=""></a>
        <div class = "container-cart-icon">
          <a href="../CarritoCompra/carritoCompra.html"><img src="../assets/img/cart.png" alt=""></a>
        </div>
        <a href="#"><img src="../assets/img/menu.png" alt=""></a>
      </section>
  `;
  return $nav;
}
