class CreateFields < ActiveRecord::Migration
  def change
    create_table :share_fields do |t|
      t.string :value
      t.string :field_type
      t.boolean :share
      t.references :user
    end
  end
end
