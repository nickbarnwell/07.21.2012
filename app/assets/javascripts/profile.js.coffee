toggle_add_field = ->


$(document).ready ->
  $('#add-field').on('click', (evt) ->
    $("#add-field-form").modal()
    return
  )

  $("#add-field-submit").on("click", (evt) ->
    field_type = $('#add-field-type').val()
    field_value = $('#add-field-value').val()
    console.log(field_value, field_type)

    
    return
   )