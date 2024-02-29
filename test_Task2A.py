from floodsystem.stationdata import build_station_list, update_water_levels

def test_update_water_levels():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print station and latest level for first 5 stations in list
    names = [
        'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge', 'Hemingford',
        'Swindon'
    ]
    x = []
    for station in stations:
        if station.name in names:
            x.append((station.name,station.latest_level))

    y=[]
    for i in x:
        y.append(i[1])

    assert len(x) == 5
    assert len(y) == 5
    assert type(y[0]) == float
                     