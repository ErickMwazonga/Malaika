$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-doctor").modal("show");
      },
      success: function (data) {
        $("#modal-doctor .modal-content").html(data.html_form);
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
          $("#doctor-table tbody").html(data.html_doctor_list);
          $("#modal-doctor").modal("hide");
        }
        else {
          $("#modal-doctor .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */
  // Create doctor
  $(".js-create-doctor").click(loadForm);
  $("#modal-doctor").on("submit", ".js-doctor-create-form", saveForm);
  // Update doctor
  $("#doctor-table").on("click", ".js-update-doctor", loadForm);
  $("#modal-doctor").on("submit", ".js-doctor-update-form", saveForm);
  // Delete doctor
  $("#doctor-table").on("click", ".js-delete-doctor", loadForm);
  $("#modal-doctor").on("submit", ".js-doctor-delete-form", saveForm);

});
