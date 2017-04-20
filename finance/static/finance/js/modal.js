$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-billing").modal("show");
      },
      success: function (data) {
        $("#modal-billing .modal-content").html(data.html_form);
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
          $("#billing-table tbody").html(data.html_billing_list);
          $("#modal-billing").modal("hide");
        }
        else {
          $("#modal-billing .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */
  // Create billing
  $(".js-create-billing").click(loadForm);
  $("#modal-billing").on("submit", ".js-billing-create-form", saveForm);
  // Update billing
  $("#billing-table").on("click", ".js-update-billing", loadForm);
  $("#modal-billing").on("submit", ".js-billing-update-form", saveForm);
  // Delete billing
  $("#billing-table").on("click", ".js-delete-billing", loadForm);
  $("#modal-billing").on("submit", ".js-billing-delete-form", saveForm);

});
