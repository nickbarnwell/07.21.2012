class Share < ActiveRecord::Base
  validates_presence_of :user
  validates_presence_of :sharer
  belongs_to :sharer, class_name: 'User', foreign_key: 'sharer_id'
  belongs_to :user

end