module ShareFieldTypes
  TYPES = [
    'mail-work',
    'mail-personal',
    'tel-mobile',
    'tel-work',
    'twitter',
    'facebook',
  ]

  def icon
    return field_type+'.png'
  end

  def humanized
    self.class.humanize(field_type)
  end
  
end