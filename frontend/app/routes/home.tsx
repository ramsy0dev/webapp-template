import type { Route } from "./+types/home";
import { Welcome } from "../welcome/welcome";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "webapp-template home page" },
    { name: "description", content: "Welcome to webapp-template Home page!" },
  ];
}

export default function Home() {
  return <Welcome />;
}
