class BumpController < ApplicationController

  def bump
    dict = [:timestamp, :lat, :lon, :acc].inject({}) do |hash, key|
      hash[key] = params[key].to_f
      hash
    end
    puts current_user.uid
    dict.merge!({uid: current_user.uid})
    dict[:timestamp] = dict[:timestamp]/1000

    resp = %x[python mongo/save_event.py '#{dict.to_json}']

    render :status => 200, :nothing => true
  end

  def hump
    uid = current_user.uid
    ids = %x[python mongo/get_group.py '#{uid}']
    
    array = JSON.parse(ids).map do |id|
      unless id == uid
        User.find_by_uid(id)
      end
    end.to_json
    render :json=> array
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
