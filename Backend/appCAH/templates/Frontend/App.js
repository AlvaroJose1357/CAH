import { Nav } from "./components/Nav.js";
import { Footer } from "./components/Footer.js";

export function App() {
  const d = document,
    $header = d.querySelector(".header"),
    $footer = d.querySelector(".footer");
  $header.appendChild(Nav());
  $footer.appendChild(Footer());
}
