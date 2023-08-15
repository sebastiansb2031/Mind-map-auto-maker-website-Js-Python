function Ocultarmenu(entrada, salida) {
  document.querySelector(entrada).addEventListener("click", function () {
    var contenidos = document.querySelector(salida);
    if (contenidos.style.opacity == 0) {
      contenidos.style.opacity = 1;
    } else {
      contenidos.style.opacity = 0;
    }
  });
}
function presionar_enter(e) {
  // Get the input field
  var code = (e.keyCode ? e.keyCode : e.which);
  if (code == 13) { //Enter keycode
    document.getElementById('gg').submit();
  }
}
function Ocultarconsola(entrada, salida1, salida2) {
  Ocultarmenu(entrada, salida1)
  Ocultarmenu(entrada, salida2)

}

function str_to_array(cadena) {
  var Mascara1 = [];
  var aux = "";
  for (let i = 0; i < cadena.length; i++) {
    if (cadena[i] != "[" & cadena[i] != "]" & cadena[i] != '"' & cadena[i] != '\\') {

      if (cadena[i] == ",") {
        Mascara1.push(aux);
        aux = "";

      }
      else { aux = aux + cadena[i] }
    }

  }
  return Mascara1
}

function crearhijos(jerarquia = 1, lista, mainList1 = ['Elemento 1 de la lista principal', 'Elemento 2 de la lista principal', 'Elemento 3 de la lista principal'], mainList2 = [1, 1, 1], hijos=true) {
  let mainList = str_to_array(mainList1)
  let mainList3 = str_to_array(mainList2)
  let idproximo = "nivelu1-1";
  const listContainer = document.getElementById(lista);
  hpvm = "https://es.wikipedia.org/wiki/Protocolo_para_transferencia_simple_de_correo"
  hpvm2 = "https://keep.google.com/#NOTE/1lxKPbtbkiN0v_PeHakYhVAn7vrqsM_q5Nu6HGAK6lFI_o-Trh7TvpkTY_Z60fQ"
  for (let i = 0; i < mainList.length; i++) {
  const li=document.createElement("li");
  if (hijos == true) {
    const input = document.createElement("input");
    input.setAttribute("type", "checkbox");
    input.setAttribute("name", "list");
    input.setAttribute("id", "nivel" + jerarquia + "-" + (i + 1));
    const label = document.createElement("label");
    label.setAttribute("for", "nivel" + jerarquia + "-" + (i + 1));
    const link = document.createElement("a");
    link.setAttribute("href", hpvm);
    link.setAttribute("target", "blank");
    link.textContent = mainList[i];
    label.appendChild(link);
    li.appendChild(input);
    li.appendChild(label);
    const ul = document.createElement("ul");
    ul.classList.add("interior");
    ul.setAttribute("id","nivelu" + jerarquia + "-" + (i + 1));
    li.appendChild(ul);
  } else {
    const link = document.createElement("a");
    link.setAttribute("href", hpvm);
    link.setAttribute("target", "blank");
    link.textContent = mainList[i];
    li.appendChild(link);
    const ul = document.createElement("ul");
    ul.classList.add("interior");
    ul.setAttribute("id","nivelu" + jerarquia + "-" + (i + 1));
    li.appendChild(ul);
  }
  listContainer.appendChild(li);
 }
  return idproximo;
}

function crearlista(lista1, mainList1, mainList2, hijos,arra) {
   
  let lista=crearhijos(1,lista1, arra, mainList2, hijos);
  let lista2 =crearhijos(3, "nivelu1-1", mainList1, mainList2, hijos);
return lista2;
}






