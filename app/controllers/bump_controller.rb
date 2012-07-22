class BumpController < ApplicationController

  def bump
    dict = [:timestamp, :lat, :lon, :acc].inject({}) do |hash, key|
      hash[key] = params[key].to_f
      hash
    end

    dict.merge!({uid: current_user.uid})
    dict[:timestamp] = DateTime.now.utc.to_i

    
    p dict
    resp = %x[python mongo/save_event.py '#{dict.to_json}']

    render :status => 200, :nothing => true
  end

  def field_render
    field = ShareField.find(params[:id])
    render :partial => 'shared/card-field', locals:{field: field}
  end

  def hump
    uid = current_user.uid
    ids = %x[python mongo/get_group.py '#{uid}']
    ids = JSON.parse(ids) - [uid]
    array = ids.map do |id|
      User.find_by_uid(id)
    end
    render :json=> array.to_json(include: :share_fields)
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
