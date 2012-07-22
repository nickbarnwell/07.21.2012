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
    toggle_add_field()

    return
  )