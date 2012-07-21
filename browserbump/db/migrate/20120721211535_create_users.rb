class CreateUsers < ActiveRecord::Migration
  def change
    create_table :users do |t|
      t.string :provider
      t.string :uid
      t.string :name
      t.string :access_token
      t.datetime :token_expiration
      t.string :email
      t.string :first_name
      t.string :last_name
      t.text :raw

      t.timestamps
    end
  end
end
