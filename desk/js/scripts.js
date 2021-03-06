//function to tell the server to do a upvote
function addVote(x){
    $.post("addVote","id="+x,function(response){
    });
    
    var $voted = $("#voted"+x);
    $voted.attr("style","width: 100%");
}

//function to tell the server to do a downvote
function delVote(x){
    $.post("delVote","id="+x,function(response){
    });
    
    var $voted = $("#voted"+x);
    $voted.attr("style","width: 100%");
}

$(function(){
    //function to send a song to the server
    $('#send-song').on('click', function(){

        var $code = $('#code');
        var $alerts = $('#alerts');
        $alerts.empty(); //removes any previous allerts
        $alerts.append('<div class="alert alert-info pull-right" role="alert">A enviar...</div>');

        splited = $code.val().split(":");
        var name = splited[0];
        var notes = splited[1]+":"+splited[2];

        var song = {
            name: name,
            notes: notes,
        };

        $.post("createSong",song,function(response){
            $alerts.empty(); //removes any previous allerts
            if(response == "Sucess"){
                $alerts.append('<div class="alert alert-success pull-right" role="alert">Música enviada com sucesso!</div>'); //add a succss alert
                $code.val(""); //cleans the input area
            }
            else{
                $alerts.append('<div class="alert alert-danger pull-right" role="alert">Ocorreu um erro. Por favor, insere valores válidos.</div>'); //add a succss alert
            }
        });
    });

    //function to send a interpretation to the server
    $('#send-interpretation').on('click', function(){

        var $name = $('#name');
        var $songs = $('#noteslist');
        var $effects = $('#efeitos');
        var $registration = $('#registration');
        var $alerts = $('#alerts');
        $alerts.empty(); //removes any previous allerts
        $alerts.append('<div class="alert alert-info pull-right" role="alert">A enviar...</div>');

        var interpretation = {
            name: $name.val(),
            id: $songs.find(":selected").attr("value"),
            effects: $effects.find(":selected").attr("value"),
            registration: $registration.val(),
        };

        $.post("createInterpretation",interpretation,function(response){
            $alerts.empty(); //removes any previous allerts
            if(response == "Sucess"){
                $alerts.append('<div class="alert alert-success pull-right" role="alert">Interpretação enviada com sucesso!</div>'); //add a succss alert
                $name.val(""); //cleans the input area
                $registration.val("");
            }
            else{
                $alerts.append('<div class="alert alert-danger pull-right" role="alert">Ocorreu um erro. Por favor, insere valores válidos.</div>'); //add a succss alert
            }
        });

    });

    //function to get the list of musics
    $.ajax({
        type: 'GET',
        url: '/listNotes',
        success: function(data) {

            var $list = $('#noteslist');

            for (var i = 0; i < data.length; i++) {
                $list.append('<option value="'+data[i].id+'">'+data[i].name+'</option>');
            }

        }

    });
    
});
