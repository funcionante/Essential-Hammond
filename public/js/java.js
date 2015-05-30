$.ajax({
	type: 'GET',
	url: '/listNotes',
	success: function(notes){
		var $notesInt = $('#notesInt');
		var $notesPlay = $('#notesPlay');
		x = notes[0].name;
		for (var i = 0; i < notes.length; i++) {
			$notesInt.append('<option value="'+i+'">'+notes[i].name+'</option>');
			$notesPlay.append('<option value="'+i+'">'+notes[i].name+'</option>');
		};
	}
});


function myFunction() {
	var elem = document.getElementById("text");
	var nice = elem.value;
	var all = nice.replace(/"/g, "");
	var all = all.split(":");
	var name = all[0];
	var notas = all[1]+":"+all[2];
	if(name > 0 && notes > 0){
		document.getElementById("name").value = name;
		document.getElementById("notes").value = notas;
	}
	else{
		alert("Try again")
	}
}
