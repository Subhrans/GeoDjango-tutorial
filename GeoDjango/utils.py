from django.contrib.gis.geoip2 import GeoIP2


def get_ip(ip):
    user_ip=GeoIP2()
    country=user_ip.country(ip)
    city=user_ip.city(ip)
    lat,long=user_ip.lat_lon(ip)

    return country,city,lat,long



