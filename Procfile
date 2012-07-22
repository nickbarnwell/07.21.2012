web: bundle exec rails server thin -p $PORT -e $RACK_ENV
eventer: python mongo/save_event.py $AGG_PORT
grouper: python mongo/get_group.py $GROUP_PORT
