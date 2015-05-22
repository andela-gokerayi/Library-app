//javascript file for general 
//jquery manipulation for the dom

$(document).ready(function(){

      $('.modal-trigger').leanModal({
          dismissible: true, // Modal can be dismissed by clicking outside of the modal
          opacity: .5, // Opacity of modal background
          in_duration: 300, // Transition in duration
          out_duration: 200, // Transition out duration
      });

      $('.dropdown-button').dropdown({
          inDuration: 300,
          outDuration: 225,
          constrain_width: false, // Does not change width of dropdown to that of the activator
          hover: true, // Activate on hover
          gutter: 0, // Spacing from edge
          belowOrigin: false // Displays dropdown below the button
      });

      $('select').material_select();

      $(".dropdown-button").dropdown();

      //detect changes when the borrowed 
      // date changes and update the due_date
      var borrowed_date = $("#borrowed_date").val();
      $("#borrowed_date").change(function(){
        var changed_date = new Date($("#borrowed_date").val());
        changed_date.setDate(changed_date.getDate() + 14);
        
        var day = ("0" + changed_date.getDate()).slice(-2);
        var month = ("0" + (changed_date.getMonth() + 1)).slice(-2);

        var due_date = changed_date.getFullYear()+"-"+(month)+"-"+(day);
        
        $("#due_date").val(due_date);
      });
});