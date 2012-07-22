toggle_add_field = ->


$(document).ready ->
  $('#add-field').on('click', (evt) ->
    $("#add-field-form").modal()
    return
  )

  $("#add-field-submit").on("click", (evt) ->
    dict = { field_type: $('#add-field-type').val(), field_value: $('#add-field-value').val()}
    
    $.post('/field', dict, (res) ->
      console.log(res)
      $('#card .fields').append(res)
    )
    $("#add-field-form").modal('hide')
    return
  )