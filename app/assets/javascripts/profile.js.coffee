toggle_add_field = ->


$(document).ready ->

  $('#profile .card .bottom .fields > li').each (idx, item) ->
    $(item).append ("<i class='icon-remove-sign'></i>")
    return

  $('#add-field').on('click', (evt) ->
    $("#add-field-form").modal()
    return
  )

  $("#add-field-submit").on("click", (evt) ->
    dict = { field_type: $('#add-field-type').val(), field_value: $('#add-field-value').val()}
    
    $.post('/field', dict, (res) ->
      $('.bottom > .fields').append(res)
      $('.bottom li:last').append ("<i class='icon-remove-sign'></i>")

    )
    $("#add-field-form").modal('hide')
    return
  )

  $('i.icon-remove-sign').live('click', (evt) ->
    field = $(this).parent()
    $.ajax(url: '/field/'+field.attr('data-id'), type: 'delete', success: (data) ->
      field.fadeOut(300, -> remove())
    )
  )
