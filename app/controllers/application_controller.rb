class ApplicationController < ActionController::Base
  helper_method :current_user, :logged_in?


  def page_title(text)
    content_tag(:h1, content_for(:title){ text })
  end

  def current_user
    @current_user ||= User.find(session[:user_id]) if session[:user_id]
  end

  def logged_in?
    !session[:user_id].nil?
  end

  def render_403(exc = nil)
    render_error(403, "You are not authorized to view this page (403)", exc.try(:message))
  end

  def render_404(exc = nil)
    render_error(404, "The page you were looking for doesn't exist (404)", "You may have mistyped the address or the page may have moved.")
  end

  def render_500(exc = nil)
    log_error(exc)
    render_error(500, "We're sorry, but something went wrong (500)", exc.try(:message))
  end

  def render_error(status, title, message)
    @title = title
    @message = message || "Hmm, something went horribly wrong"
    render(:template => 'layouts/error', :status => status, :layout => false)

    true # to make 'render_404 and return' work
  end

  def login_required
    logged_in? || access_denied
  end

  def access_denied
    respond_to do |format|
      format.html do
        store_location
        redirect_to login_path, :notice => 'You need to be logged in to access this page'
      end
    end
  end

  def store_location
    session[:return_to] = request.url
  end

  def redirect_back_or_default(default)
    redirect_to(session[:return_to] || default)
    session[:return_to] = nil
  end
end
