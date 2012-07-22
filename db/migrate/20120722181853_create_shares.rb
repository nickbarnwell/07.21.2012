class CreateShares < ActiveRecord::Migration
  def change
    create_table :shares do |t|
      t.references :user
      t.references :sharer
      t.timestamps
    end
  end
end
