class BumpController < ApplicationController

  def bump
    params.merge!({uid: current_user.uid})
    render :status => 200, :json=>%x[python mongo/save_event.py '#{params}']
  end

  def hump
    uid = current_user.uid
    render :json=>%x[python mongo/get_group.py '#{uid}']
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
    
  end

  def fake_get
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
