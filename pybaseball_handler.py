import os
import sqlite3
import pandas as pd
from pybaseball import statcast, playerid_lookup, statcast_pitcher, statcast_batter


cache_dir = '.cache'
cache_db = os.path.join(cache_dir, 'lookup.db')

def find_player_by_id(name):
    conn = sqlite3.connect(cache_db)
    c = conn.cursor()
    id_ = c.execute('SELECT id FROM player WHERE name == "{}" LIMIT 1'.format(name)).fetchone()
    if id_ == None:
        id_ = playerid_lookup(name.split()[1], name.split()[0])['key_mlbam'].to_numpy()
        assert len(id_) != 0, 'Player not exists!'
        c.execute('INSERT INTO player (name, id) VALUES ("{}", {})'.format(name, id_[0]))
    conn.commit()
    conn.close()
    return id_[0]


def get_history_data(start_dt, end_dt, cols=['hc_x', 'hc_y'], batter=None, pitcher=None):
    assert not batter or not pitcher, 'you can only have general results or specify one batter or one pitcher'
    cache_path = os.path.join(cache_dir, '{}_{}_{}_{}.h5'.format(start_dt, end_dt, batter, pitcher))
    store = pd.HDFStore(cache_path)
    try:
        df = store['df']
    except:
        if batter: df = statcast_batter(start_dt=start_dt, end_dt=end_dt, player_id=batter)
        elif pitcher: df = statcast_batter(start_dt=start_dt, end_dt=end_dt, player_id=pitcher)
        else: df = statcast(start_dt=start_dt, end_dt=end_dt)
        store['df'] = df
    home = (130, 200)
    df['hc_x'] = df['hc_x'] - home[0]
    df['hc_y'] = home[1] - df['hc_y']
    return df[cols]