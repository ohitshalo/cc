
class MonitoringStation:

    """This class represents a river level monitoring station"""

 

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""
        self.station_id = station_id
        self.measure_id = measure_id
        # Handle case of erroneous data where data system returns

        # '[label, label]' rather than 'label'

        self.name = label

        if isinstance(label, list):
            self.name = label[0]
        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.latest_level = None
        self.risk_factor = 0

 

   

    def typical_range_consistent(self):
        if self.typical_range == None:
            return False
        elif self.typical_range[0] < self.typical_range[1]:
            return True
        elif self.typical_range[1] < self.typical_range[0]:
            return False

    def __repr__(self):

        d = "Station name:     {}\n".format(self.name)

        d += "   id:            {}\n".format(self.station_id)

        d += "   measure id:    {}\n".format(self.measure_id)

        d += "   coordinate:    {}\n".format(self.coord)

        d += "   town:          {}\n".format(self.town)

        d += "   river:         {}\n".format(self.river)

        d += "   typical range: {}".format(self.typical_range)

        return d
    
    def relative_water_level(self):
        """
        returns current water level as a fraction of the typical range, 1 = typical high, 0 = typical low
        """
        if self.latest_level == None or self.typical_range == None:
            return None
        shift_max = self.typical_range[1] - self.typical_range[0]
        shift_level = self.latest_level - self.typical_range[0]
        return shift_level / shift_max

def inconsistent_typical_range_stations(stations):
    inconsistent_list = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) ==False:
            inconsistent_list.append(station)

    return inconsistent_list    