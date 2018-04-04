$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-diagnose").modal("show");
      },
      success: function (data) {
        $("#modal-diagnose .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#diagnose-table tbody").html(data.html_diagnose_list);
          $("#modal-diagnose").modal("hide");
        }
        else {
          $("#modal-diagnose .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var loadFormRoom = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-room").modal("show");
      },
      success: function (data) {
        $("#modal-room .modal-content").html(data.html_form);
      }
    });
  };

  var saveFormRoom = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#room-table tbody").html(data.html_room_list);
          $("#modal-room").modal("hide");
        }
        else {
          $("#modal-room .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */
  // Create diagnose
  $(".js-create-diagnose").click(loadForm);
  $("#modal-diagnose").on("submit", ".js-diagnose-create-form", saveForm);
  // Update diagnose
  $("#diagnose-table").on("click", ".js-update-diagnose", loadForm);
  $("#modal-diagnose").on("submit", ".js-diagnose-update-form", saveForm);
  // Delete diagnose
  $("#diagnose-table").on("click", ".js-delete-diagnose", loadForm);
  $("#modal-diagnose").on("submit", ".js-diagnose-delete-form", saveForm);


  /* Binding */
  // Create room
  $(".js-create-room").click(loadFormRoom);
  $("#modal-room").on("submit", ".js-room-create-form", saveFormRoom);
  // Update room
  $("#room-table").on("click", ".js-update-room", loadFormRoom);
  $("#modal-room").on("submit", ".js-room-update-form", saveFormRoom);
  // Delete room
  $("#room-table").on("click", ".js-delete-room", loadFormRoom);
  $("#modal-room").on("submit", ".js-room-delete-form", saveFormRoom);

});
