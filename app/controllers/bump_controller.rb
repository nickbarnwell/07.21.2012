class BumpController < ApplicationController
  def index
  end

  def fake
    dict = {
      timestamp: DateTime.now.utc.to_i,
      lat: 37.7763675 + georand,
      lon: -122.3926582 + georand,
      acc: intrange(0,100),
      uid: intrange(0,12313)
    }
    render :json => dict
  end

  def range (min, max)
    (rand * (max-min) + min)
  end

  def intrange(min, max)
    range(min, max).to_i
  end

  def georand()
    ((range(-1,1) * rand/10))
  end

end
