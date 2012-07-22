class ProfileController < ApplicationController
  def edit

  end

  def add_field
    p params
    field = current_user.add_field params[:field_type], params[:field_value]
    render :partial => 'shared/card-field', locals: {field: field}
  end

  def disable_field
    ShareField.find(params[:id]).disable!
  end

  def delete_field
    field = ShareField.find(params[:id])
    if field.user = current_user
      field.delete!
      render :status => 204
   else
     render :status => 403
   end
  end

end