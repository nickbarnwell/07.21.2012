class User < ActiveRecord::Base
  validates_format_of(:email,
   :on => :create,
   :email => true,
   :with => /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\z/i,
   :allow_nil => true
  )
  validates :uid, :uniqueness => {:scope => :provider}, :on => :create
  validates_format_of :uid, :with => /\d+/, :on => :create

  validates :provider, :inclusion => {:in => %w(facebook)}

  serialize :raw, Hash

  has_many :share_fields
  alias :fields :share_fields
  alias :fields= :share_fields=

  def name
    "#{first_name} #{last_name}"
  end

  def token
    access_token
  end

  def update_token!(credentials)
    if token_expires_soon?
      self.access_token = credentials["token"]
      self.token_expiration = credentials["expires_at"]
      save!
    end
  end

  def token_expiration=(value)
    if value.class == Fixnum
      value = DateTime.strptime(value.to_s, '%s').utc #FIXME
    end
    self[:token_expiration] = value
  end

  def token_expires_soon?
    token_expiration.nil? || token_expiration < 5.days.from_now
  end

  def add_field(field_type, value)
    ShareField.create! do |field|
      field.field_type = field_type
      field.value = value
      field.share = true
      field.user = self
    end
  end

  class << self
    def create_with_omniauth(auth)
      user = create! do |user|
        user.provider = auth["provider"]
        user.uid = auth["uid"]
        user.name = auth["info"]["name"]
        user.first_name = auth["info"]["first_name"]
        user.last_name = auth["info"]["last_name"]
        user.raw = auth["extra"]["raw_info"]
        user.access_token = auth["credentials"]["token"]
        user.token_expiration = auth["credentials"]["expires_at"]
      end
      begin
        user.add_field 'mail-work', auth["info"]["email"]
      end
    end
  end

end