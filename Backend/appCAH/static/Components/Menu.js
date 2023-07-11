export function Menu() {
  const $menu = document.createElement("section");
  $menu.classList.add("menu-despegable");
  $menu.innerHTML = `
    <a href="/bodega">bodegas</a>
    <a href="/bodega">Agricultor</a>
    <a href="/bodega">Transporte</a>
    `;
  return $menu;
}
