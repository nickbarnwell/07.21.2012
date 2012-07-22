module ShareFieldTypes
  TYPES = [
    'mail-work',
    'mail-personal',
    'tel-mobile',
    'tel-work',
    'tel-home',
    'twitter',
    'facebook',
    'linkedin'
  ]

  def icon
    return type+'.png'
  end
end