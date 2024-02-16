"""Lab_2.Ex_3"""
import base64
import json
import pycountry
import folium
from requests import post, get
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search():
    token = get_token()
    artist_name = request.form['artist']
    info_about_artist = (search_of_artist(token, artist_name))
    artist_id = info_about_artist["id"]
    songs = get_songs_by_artist(token, artist_id)
    track_id = songs[0]['uri'].split(':')[-1]
    map = draw_on_map(countries_locations(get_song_info(token, track_id)))
    return map.get_root().render()


@app.route('/')
@app.route('/index')
def entry_page():
    return render_template('index.html')


client_id = "00098b27c0bb4078b6526b31e16b9391"
client_secret = "6c8955e1fb7c449990ad3cafe491a4ed"


def get_token():
    """
    return token from spotify website
    """
    auth_str = client_id + ":" + client_secret
    auth_bytes = auth_str.encode("utf-8")

    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    solut = post(url, headers=headers, data=data)
    json_solut = json.loads(solut.content)
    token = json_solut["access_token"]
    return token


def get_auth_headers(token: str) -> str:
    """
    Creates a header for the request
    >>> get_auth_headers("BQBRcXEfkd_rpWefpFJIvPCPQYa58duCouQ0hIPxMPZV709b7xDx2M\
-oUq_Tv9hMOhp-HJqLAJIwwdCa2bUIeS0AQtrS556EnuTODOJfP8sSExBWizPZ")
    {'Authorization': 'Bearer BQBRcXEfkd_rpWefpFJIvPCPQYa58duCouQ0hIPxMPZV709b7xDx\
2M-oUq_Tv9hMOhp-HJqLAJIwwdCa2bUIeS0AQtrS556EnuTODOJfP8sSExBWizPZ'}
    """
    return {"Authorization": "Bearer " + token}


def search_of_artist(token: str, artist_name: str) -> dict:
    """Finds information about the artist on the spotify"""
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_headers(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url+query
    solut = get(query_url, headers=headers)
    json_solut = json.loads(solut.content)["artists"]["items"]
    if len(json_solut) == 0:
        print("No such artist...")
        return None
    return json_solut[0]


def get_songs_by_artist(token: str, artist_id: str) -> dict:
    """Finds the 10 most popular songs on Spotify by the specified artist"""
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_headers(token)
    solut = get(url, headers=headers)
    json_solut = json.loads(solut.content)["tracks"]
    return json_solut


def get_song_info(token: str, song_id: str) -> dict:
    """Finds the available_markets of the track given as id"""
    url = f"https://api.spotify.com/v1/tracks/{song_id}"
    headers = get_auth_headers(token)
    solut = get(url, headers=headers)
    json_solut = json.loads(solut.content)["available_markets"]
    return json_solut


def available_markets_location(lst_of_countries: list) -> list:
    """finds coordinates of countries"""
    counries_locations = []
    for count_code in lst_of_countries:
        try:
            country_location = pycountry.countries.get(alpha_2=count_code)
            if ',' in country_location.name:
                counries_locations.append(country_location.name.split(',')[0])
            else:
                counries_locations.append(country_location.name)
        except AttributeError:
            continue
    return counries_locations


def countries_locations(countries: list) -> list[tuple]:
    """
    Func find position countries.
    """
    countries_with_locations = []
    countries_in_world = {}
    with open("countries.csv", 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.replace('\n', '').split(',')
            countries_in_world[line[0]] = [line[-1], line[1], line[2]]
    for country in countries:
        try:
            countries_with_locations.append(
                (countries_in_world[country][0], countries_in_world[country][1], countries_in_world[country][2]))
        except KeyError:
            continue
    return countries_with_locations


def draw_on_map(countries: list[tuple]):
    """
    this function draw points on a map
    """
    map_of_available_markets = folium.Map(
        location=[49.8171100, 24.0224973], zoom_start=5)

    fgroup1 = folium.FeatureGroup(
        name="Marks of available markets to your track")
    for country in countries:
        fgroup1.add_child(folium.Marker(
            location=[country[1], country[2]], popup=f"{country[0]}", icon=folium.Icon()))
    map_of_available_markets.add_child(fgroup1)
    map_of_available_markets.add_child(folium.TileLayer(
        'cartodbdark_matter', name='Black theme'))
    map_of_available_markets.add_child(folium.LayerControl())
    return map_of_available_markets


if __name__ == '__main__':
    app.run(debug=True)
