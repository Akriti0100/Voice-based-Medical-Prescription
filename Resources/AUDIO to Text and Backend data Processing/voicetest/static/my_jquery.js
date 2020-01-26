$(document).ready(function() {
    $("#send").click(function(event){
          $.ajax({
              type:"POST",
              url:"/audio_data/",
              data: {
                      send : $('#result').html()
                      },
              success: function(){
                  alert("Audio succesfully Submitted");
              }
          });
    });
  });
