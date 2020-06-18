function sidebar_open() {
  document.getElementById("sidebarCollapse").style.left = "0px";
  document.getElementById("sidebarSmallPanel").style.visibility = "hidden";
}

function sidebar_close() {
  document.getElementById("sidebarCollapse").style.left = "-500px";
  document.getElementById("sidebarSmallPanel").style.visibility = "visible";
}
