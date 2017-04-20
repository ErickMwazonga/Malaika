$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-treatment").modal("show");
      },
      success: function (data) {
        $("#modal-treatment .modal-content").html(data.html_form);
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
          $("#treatment-table tbody").html(data.html_treatment_list);
          $("#modal-treatment").modal("hide");
        }
        else {
          $("#modal-treatment .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */
  // Create treatment
  $(".js-create-treatment").click(loadForm);
  $("#modal-treatment").on("submit", ".js-treatment-create-form", saveForm);
  // Update treatment
  $("#treatment-table").on("click", ".js-update-treatment", loadForm);
  $("#modal-treatment").on("submit", ".js-treatment-update-form", saveForm);
  // Delete treatment
  $("#treatment-table").on("click", ".js-delete-treatment", loadForm);
  $("#modal-treatment").on("submit", ".js-treatment-delete-form", saveForm);

});
