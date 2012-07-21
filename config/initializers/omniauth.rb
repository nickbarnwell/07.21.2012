Rails.application.config.middleware.use OmniAuth::Builder do
  provider :facebook, '445165405514649', 'bde3b8907422b58b4e9845aee6817aa9',
           :scope => 'email', :display => 'page'
end
