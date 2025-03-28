$(document).ready(function () {

    // display audio message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');
    };

    // display hood
    eel.expose(ShowHood)
    function ShowHood(){
        $("#ovel").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

});