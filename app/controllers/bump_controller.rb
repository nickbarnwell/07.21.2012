class BumpController < ApplicationController
  skip_before_filter :login_required

  def index
  end

  def fake
    dict = {
      timestamp: DateTime.now.utc.to_i,
      lat: 37.7763675 + georand,
      lon: -122.3926582 + georand,
      acc: intrange(0,100),
      uid: intrange(0,12313).to_s
    }.to_json
    puts dict
    puts %x[python mongo/save_event.py '#{dict}']
    #render :json => dict
    render :status => 200, :text=>nil
  end

  def fake_get
    uid = params[:uid]
    puts %x[python mongo/get_group.py '#{uid}']
    render :status => 200, :text=>nil
  end



  def range (min, max)
    (rand * (max-min) + min)
  end

  def intrange(min, max)
    range(min, max).to_i
  end

  def georand()
    ((range(-1,1) * rand/1000))
  end

end
