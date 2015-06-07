function refreshJSON () {
    location.reload();
};

$.ajax({
	type: 'GET',
	url: '/listNotes',
	success: function(notes){
		var $notesInt = $('#notesInt');
		var $notesPlay = $('#notesPlay');
		for (var i = 0; i < notes.length; i++) {
			$notesInt.append('<option value="'+notes[i].id+'">'+notes[i].name+'</option>');
			$notesPlay.append('<option value="'+notes[i].id+'">'+notes[i].name+'</option>');
		};
	}
});

function upVote (id) {
	var x = "id="+id;
	$.post("addVote",x,function(response){
	});

	alert("Gosto enviado com sucesso!");
}

function downVote (id) {
	var x = "id="+id;
	$.post("delVote",x,function(response){
	});

	alert("Não gosto enviado com sucesso!");
}

function MusicMenu () {
	music = ""+document.getElementById("notesPlay").value;
	for (var i = 1; i < id.length; i++) {
		if (id[i].charAt(0) == music) {
			$('#'+id[i]).slideDown();
			$('#PlaySubmit').hide();
		};
	};
}

$.ajax({
	type: 'GET',
	url: 'listSongs',
	success: function(songs){
		var $songs= $('#songs');
		id = ["test"];
		for (var i = 0; i < songs.length; i++) {
			$songs.append('<div id="'+songs[i].id_music+''+songs[i].id+'" data-role="collapsible" data-collapsed-icon="carat-d" data-expanded-icon="carat-u" style="text-align: center"><div class="ui-grid-solo"><div class="ui-block-a"><h4>'+songs[i].upvotes+' gosto(s) e '+songs[i].downvotes+' não gosto(s)</h4></div></div><div class="ui-grid-a" style="text-align: center"><div class="ui-block-a"><input type="button" data-icon="star" value="Gosto" onclick="upVote('+songs[i].id+')"></div><div class="ui-block-b"><input type="button" onclick="downVote('+songs[i].id+')"data-icon="delete" value="Não gosto"></div></div><div class="ui-grid-solo"><div class="ui-block-a"><a data-rel="popup" href="#img'+songs[i].id_music+'" class="ui-btn ui-shadow ui-corner-all">Imagem</a></div><div id="img'+songs[i].id_music+'" data-role="popup" data-overlay-theme="a" class="ui-content"><img style="width:300px" src="/img/'+songs[i].id_music+'.jpg"></img></div></div><h4>'+songs[i].name+'</h4><audio controls><source src="http://localhost:8080/audio/'+songs[i].id+'.wav" type="audio/wav"></audio></div>');
			id.push(songs[i].id_music+''+songs[i].id);
		};

		for (var i = 1; i < id.length; i++) {
			$('#'+id[i]).hide();
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
			document.getElementById("himynameis").innerHTML = "Musica enviada com sucesso!";
		}
		else{
			document.getElementById("himynameis").innerHTML = "Error!";
		}
	});
}

function addMusic () {
	var id = document.getElementById("notesInt").value;
	var registo = document.getElementById("registo").value;
	var efeito = document.getElementById("efeito").value;
	var nome = document.getElementById("nome").value;
	var x = "registration="+registo+"&id="+id+"&effects="+efeito+"&name=+"+nome;

	$.post("createInterpretation",x,function(response){
		if(response == "Sucess"){
			document.getElementById("himynameis2").innerHTML = "Musica enviada com sucesso!";
		}
		else{
			document.getElementById("himynameis2").innerHTML = "Error!";
		}
	});
}
