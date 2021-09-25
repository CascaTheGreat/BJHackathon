$(document).ready(function() {
  var typingTimer; //timer identifier
  var doneTypingInterval = 2000; //time in ms, 5 second for example
  var $input = $("#searchbar");

  //on keyup, start the countdown
  $input.on("keyup", function() {
    clearTimeout(typingTimer);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
  });

  //on keydown, clear the countdown
  $input.on("keydown", function() {
    clearTimeout(typingTimer);
  });

  function doneTyping() {
    var dvPassport = document.getElementById("symptom-list");
    dvPassport.style.visiblity = "hidden";
    dvPassport.style.opacity = "1";
  }
  $(window).keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
  });
});
