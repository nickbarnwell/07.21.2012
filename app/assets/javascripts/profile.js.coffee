toggle_add_field = ->


$(document).ready ->
  toggle_matte = ->
    $('#matte').toggle('fast')
    return

  toggle_add_field = ->
    $('#add-field-form').toggle('fast');
    return

  $('#add-field').on('click', (evt) ->

    toggle_matte()
    $("#add-field-form").modal()

    return
  )