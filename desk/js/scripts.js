function addVote(x){
    $.post("addVote","id="+x,function(response){
        console.log(response);
    });
    
    var $voted = $("#voted"+x);
    $voted.attr("style","width: 100%");
    
    /*var $up = $("#up"+x);
    var $down = $("#down"+x);
    console.log($up);
    console.log($down);
    
    var upval = parseInt($up.val())+1;
    var downval = parseInt($down.val());
    console.log(upval);
    console.log(downval);
    
    $up.html(upval);
    
    var upval100 = 100*upval/(upval+downval);
    var downval100 = 100 - upval;
    console.log(upval100);
    console.log(downval100);
    
    $up.attr("style","width: " + upval100 + "%");
    $down.attr("style","width: " + downval100 + "%");*/
}

function delVote(x){
    $.post("delVote","id="+x,function(response){
        console.log(response);
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

        splited = $code.val().split(":");
        var name = splited[0];
        var notes = splited[1]+":"+splited[2];

        var song = {
            name: name,
            notes: notes,
        };

        /*$.ajax({
            type: 'POST',
            url: 'createSong',
            data: song,
            success: function(){
                $alerts.append('<div class="alert alert-success pull-right" role="alert">Música enviada com sucesso!</div>'); //add a succss alert
                $code.val(""); //cleans the input area
            }
        })*/

        $.post("createSong",song,function(response){
            console.log(response);
            if(response == "Sucess"){
                $alerts.append('<div class="alert alert-success pull-right" role="alert">Música enviada com sucesso!</div>'); //add a succss alert
                $code.val(""); //cleans the input area
            }
            else{
                $alerts.append('<div class="alert alert-success pull-right" role="alert">ERRRRRRRROR!</div>'); //add a succss alert
                $code.val(""); //cleans the input area
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

        console.log($songs);
        console.log($effects);
        console.log($songs.find(":selected")[0]);
        console.log($effects.find(":selected")[0]);
        console.log($songs.find(":selected").attr("value"));
        console.log($effects.find(":selected").attr("value"));

        var interpretation = {
            name: $name.val(),
            id: $songs.find(":selected").attr("value"),
            effects: $effects.find(":selected").attr("value"),
            registration: $registration.val(),
        };

        $.post("createInterpretation",interpretation,function(response){
            console.log(response);
            if(response == "Sucess"){
                $alerts.append('<div class="alert alert-success pull-right" role="alert">Interpretação enviada com sucesso!</div>'); //add a succss alert
                $name.val(""); //cleans the input area
                $registration.val("");
            }
            else{
                $alerts.append('<div class="alert alert-success pull-right" role="alert">ERRRRROR!</div>'); //add a succss alert
                $name.val(""); //cleans the input area
                $registration.val("");
            }
        });

        /*$.ajax({
            type: 'POST',
            url: 'createInterpretation',
            data: interpretation,
            success: function(){
                $alerts.append('<div class="alert alert-success pull-right" role="alert">Interpretação enviada com sucesso!</div>'); //add a succss alert
                $name.val(""); //cleans the input area
                $registration.val("");
            }
        })*/
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
