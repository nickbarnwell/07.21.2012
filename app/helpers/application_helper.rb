module ApplicationHelper
  def title
    (@content_for_title + " &mdash; " if @content_for_title).to_s + 'CallMeMae.Be'
  end
end
