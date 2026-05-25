$(document).ready(function () {

    
  //Display speak Message
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate("start");
  }

  //Display Hood
  eel.expose(ShowHood);
  function ShowHood() {
    $("#oval").attr("hidden", false);
    $("#siriwave").attr("hidden", true);
  }
});
