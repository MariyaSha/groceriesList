function check_me(input_id){
	
	// change label style of checked item
	var checked_label = document.querySelector("label[name=" + input_id +"]"); 
	checked_label.style.textDecoration = "line-through";

	// change "remove items" button style
    btn = document.getElementById("remove_btn");
    btn.value = "REMOVE ITEMS";
    btn.style.backgroundColor = "#FE7575";
    btn.style.color = "#FFFFFF";
    btn.style.cursor = "pointer";
}
