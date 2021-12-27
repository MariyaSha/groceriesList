
console.log("testing")

function check_me(my_id){
	console.log(my_id);
	var checked = document.getElementById(my_id);
	var checked_label = document.querySelector("label[name=" + my_id +"]"); 
	checked_label.style.textDecoration = "line-through";

    btn = document.getElementById("remove2");
    btn.value = "REMOVE ITEMS";
    btn.style.backgroundColor = "#01A88A";
    btn.style.color = "#FFFFFF";
    btn.style.cursor = "pointer";

    // data = "I want to send this to backend"
    // document.getElementById("myButton2").value = data;
	

	// checked.value = "print this pleeeeeeeease";
	// document.getElementById("myButton2").value = "or maybe print this";

	//temporarily hide elements
	//but later on - update server and resend vals
	// checked.remove();
	// checked_label.remove();

	// const test = new XMLHttpRequest();
	// send = JSON.stringify([4,5,6],[1,2,3]);
	// test.open('POST', '/test_me');
	// test.send(send);
}

// function remove_me() {
//         data = "I want to send this to backend";
// 		document.getElementById("remove").value = data;
//     }

// ***************************** UPDATE DB *********************************
// https://stackoverflow.com/questions/70231327/flask-get-checkbox-value-without-submit-button

// function ajaxRequest(my_id) {
//   const checked = document.getElementById(str(my_id)).checked;
//   console.log("Sending data to the server that the checkbox is", checked);
  
//   // Use the XMLHttpRequest API
//   const xhttp = new XMLHttpRequest();
//   xhttp.onload = function() {
//     console.log("Result sent to server!");
//   }
//   xhttp.open("POST", "/", true);
//   xhttp.send();
// }