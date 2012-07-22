class SharesController < ApplicationController
  def save
    if Share.where(user_id: current_user.id, sharer_id:   params[:user_id]).nil?
      share = Share.create! do |s|
        s.user = current_user
        s.sharer = User.find(params[:user_id])
      end
    end
    render nothing: true
  end

  def destroy
    Share.destroy(params[:id])
    render nothing: true
  end

  def index
    @shares = Share.where(user_id: current_user.id).map do |share|
      User.find(share.sharer_id)
    end
    p @shares
  end

end