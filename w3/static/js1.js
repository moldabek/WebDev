var cnt = 0;
const myInput = document.getElementById("myInput");
const list = document.getElementById("list");

function newElement(toDo){
		const text = `<li class="item">
				<i class="co fa fa-circle-thin" job="complete"></i>
				<p class="text "> ${toDo}  </p>
				<i class="de fa fa-trash-o" job="delete"></i>
				</li>`
		const position = "beforeend";

		list.innerHTML += text;
}

newElement("drinkCofee")
newElement("avdfvdsfvsdv")

