import math
import pprint


def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def get_edges(places):
    """
        Decimal coordinates	Sexagesimal coordinates
        Latitude	Longitude	Latitude	Longitude
        0° to 90°	0° to 180°	N	E
        0° to 90°	0° to -180°	N	W
        0° to -90°	0° to 180°	S	E
        0° to -90°	0° to -180°	S	W
        """
    edges = dict(north=dict(lat=None, long=None, name=None, tfid=None),
                 south=dict(lat=None, long=None, name=None, tfid=None),
                 east=dict(lat=None, long=None, name=None, tfid=None),
                 west=dict(lat=None, long=None, name=None, tfid=None))
    for place in places:
        lat = place.coordinates[1]
        long = place.coordinates[0]
        name = place.name
        tfid = place.tfid
        if edges['north']['lat'] is None or edges['north']['lat'] < lat:
            edges['north'] = dict(lat=lat, long=long, name=name, tfid=tfid)
        if edges['south']['lat'] is None or edges['south']['lat'] > lat:
            edges['south'] = dict(lat=lat, long=long, name=name, tfid=tfid)
        if edges['east']['long'] is None or edges['east']['long'] < long:
            edges['east'] = dict(lat=lat, long=long, name=name, tfid=tfid)
        if edges['west']['long'] is None or edges['west']['long'] > long:
            edges['west'] = dict(lat=lat, long=long, name=name, tfid=tfid)
    return edges


def print_edges(places):
    edges = get_edges(places)
    import pprint
    with open('edges.txt', 'w') as f:
        f.write(pprint.pformat(edges))
        f.write('\nE->W {}'.format(haversine((edges['west']['lat'], edges['west']['long']),
                                           (edges['east']['lat'], edges['east']['long'])) * 0.00062137, 'miles'))
        f.write('\nN->S {}'.format(haversine((edges['north']['lat'], edges['north']['long']),
                                           (edges['south']['lat'], edges['south']['long'])) * 0.00062137, 'miles'))
