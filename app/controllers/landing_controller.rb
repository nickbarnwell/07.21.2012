class LandingController < ApplicationController
  before_filter :logged_in_redirect
  skip_before_filter :logged_in_redirect, :only => [:test]
  skip_before_filter :login_required

  def index
  end

  def logged_in_redirect
    if logged_in? then redirect_to dashboard_path end
  end
end
