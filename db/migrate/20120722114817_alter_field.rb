class AlterField < ActiveRecord::Migration
  def up
    remove_column :share_fields, :type
    add_column :share_fields, :field_type, :string
  end

  def down
  end
end
