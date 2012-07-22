class ShareField < ActiveRecord::Base
  include ShareFieldTypes
  validates :type, inclusion: {in: TYPES}
  belongs_to :user
  
  def disable!
    share = false
    save!
  end

  def enable!
    share = true
    save!
  end
end