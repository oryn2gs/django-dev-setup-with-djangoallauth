const btn = document.getElementById("btn");

console.log(btn);

btn.addEventListener("click", (e) => {
  console.log("clicked", e.target);
});
