$(document).ready(function () {
    

    $('.text').textillate({
        loop: true,
        sync : true,
        in: {
            effect: 'bounceIn',
        },
        out: {
            effect: 'bounceOut',
        }

    });





//siri configuration

var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style: "ios9",
    amplitude: "2",
    speed: "0.1",
    frequency: 6,
    color: "#fff",
    autostart: true,
});

//siri messsage animation
$('p.siri-message').textillate({
        loop: true,
        sync : true,
        in: {
            effect: 'fadeInUp',
            sync: true,
        },
        out: {
            effect: 'fadeOutDown',
            sync: true,
        }

    });


// mic button click event 
$('#MicBtn').click(function(e) {
    eel.playAssistantSound() 
    $('#oval').attr('hidden', true);
    $('#siriwave').attr('hidden', false);
    eel.allCommands()

})

function doc_keyup(e) {
    if (e.key === 'j' && e.metaKey) {
        eel.playAssistantSound
        $('#oval').attr('hidden', true);
        $('#siriwave').attr('hidden', false);
        eel.allCommands()
    }
}
    document.addEventListener('keyup', doc_keyup, false);


});