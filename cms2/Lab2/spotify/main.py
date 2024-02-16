"""Lab_2.Ex_2"""
import os
import base64
import json
from dotenv import load_dotenv
from requests import post, get

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

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

def get_auth_headers(token:str)->str:
    """
    Creates a header for the request
    >>> get_auth_headers("BQBRcXEfkd_rpWefpFJIvPCPQYa58duCouQ0hIPxMPZV709b7xDx2M\
-oUq_Tv9hMOhp-HJqLAJIwwdCa2bUIeS0AQtrS556EnuTODOJfP8sSExBWizPZ")
    {'Authorization': 'Bearer BQBRcXEfkd_rpWefpFJIvPCPQYa58duCouQ0hIPxMPZV709b7xDx\
2M-oUq_Tv9hMOhp-HJqLAJIwwdCa2bUIeS0AQtrS556EnuTODOJfP8sSExBWizPZ'}
    """
    return {"Authorization" : "Bearer "+ token}

def search_of_artist(token: str, artist_name: str)->dict:
    """Finds information about the artist on the spotify"""
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_headers(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url+query
    solut = get(query_url, headers=headers)
    json_solut = json.loads(solut.content)["artists"]["items"]
    if len(json_solut)==0:
        print("No such artist...")
        return None
    return json_solut[0]

def get_songs_by_artist(token:str, artist_id:str)->dict:
    """Finds the 10 most popular songs on Spotify by the specified artist"""
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_headers(token)
    solut = get(url, headers=headers)
    json_solut = json.loads(solut.content)["tracks"]
    return json_solut

if __name__ == '__main__':
    # import doctest
    # print(doctest.testmod())
    token = get_token()
    print("Write name of an artist: ", end="\t")
    artist_name = str(input())
    info_about_artist = (search_of_artist(token, artist_name))
    print(f"\n---------- {info_about_artist['name']} ------------\n\
What do you want to know about the artist? (choose an option from the following)\n\
\n'id' - the artist's web address in Spotify\n'followers' - number of followers\n\
'genres' - genres belong to the artist\n'songs' - top 10 songs\n\
'exit' - if you wan't to exit")
    while True:
        print("\nChoose option:\t", end='')
        option = str(input())
        if option == 'id':
            print(info_about_artist['external_urls']['spotify'])
        elif option == 'followers':
            print(info_about_artist['followers']['total'])
        elif option == 'genres':
            for genre in info_about_artist['genres']:
                print(f"- {genre}", end='\n')
        elif option == 'songs':
            artist_id = info_about_artist["id"]
            songs = get_songs_by_artist(token, artist_id)
            for indx,song in enumerate(songs):
                print(f"{indx+1} - {song['name']}")
        elif option == 'exit':
            break
        else:
            print("You have selected an option that does not exist. Please choose another")
