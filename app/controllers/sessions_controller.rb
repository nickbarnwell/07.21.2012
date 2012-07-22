class SessionsController < ApplicationController
  skip_before_filter :login_required, :only => [:create, :fake_create]

  def create
    auth = request.env["omniauth.auth"]
    user = User.find_by_provider_and_uid(auth["provider"], auth["uid"])
    if user.nil?
      user = User.create_with_omniauth(auth)
      session[:first_login] = true
    end
    user.update_token! auth['credentials']
    session[:user_id] = user.id
    redirect_to root_url, :notice => "Signed in!"
  end

  def destroy
    session[:user_id] = nil
    redirect_to root_url, :notice => "Signed out!"
  end

  def fake_create
    if params[:user] == '2'
      user = User.find_by_uid('692938647')
    else
      user = User.find_by_uid('692938645')
    end
    
    session[:user_id] = user.id
    redirect_to root_url, :notice => "Signed in!"
  end
end
