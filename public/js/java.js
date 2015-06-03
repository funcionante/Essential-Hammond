function refreshJSON () {
    location.reload();
}


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


function addNote() {
	var elem = document.getElementById("text");
	var nice = elem.value;
	var all = nice.replace(/"/g, "");
	var all = all.split(":");
	var name = all[0];
	var notas = all[1]+":"+all[2];
	var x = "name="+encodeURIComponent(name)+"&notes="+encodeURIComponent(notas);
	$.post("createSong",x,function(response){
		if(response == "Sucess"){
			document.getElementById("himynameis").innerHTML = "Sucess!";
		}
		else{
			document.getElementById("himynameis").innerHTML = "Error!";
		}
	});
}