class ShareField < ActiveRecord::Base
  include ShareFieldTypes
  validates :field_type, inclusion: {in: TYPES}
  belongs_to :user
  
  def disable!
    share = false
    save!
  end

  def enable!
    share = true
    save!
  end

  def link_value
    if field_type =~ /mail-*/
      return  "<a href='mailto: #{value}'>#{value}</a>"
    elsif field_type =~ /tel-*/
      return "<a href='tel:#{value}'>#{value}</a>"
    end

    case field_type
    when 'twitter'
      return "<a href='http://twitter.com/#{value}'>#{value}</a>"
    when 'facebook'
      return "<a href='#{user.raw['link']}'>#{user.name}</a>"
    end

  end
end
