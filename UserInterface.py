#Kelly Pham 25384246. Project 3

import MapRequest
import Output

def JourneyInput():
    ''' takes in the users input for their desired journey'''
    journey = []
    NumberofJourney = int(input())
    for destination in range(NumberofJourney):
        destination = input()
        journey.append(destination)
    return journey

def DetailsInput():
    details = []
    NumberofDetails = int(input())
    for detail in range(NumberofDetails):
        detail = input()
        details.append(detail)
    for each in details:
        if each not in ["TOTALDISTANCE", "TOTALTIME", "LATLONG", "STEPS", "ELEVATION"]:
            print("Invalid output type: " + each)
            return None
    return details

def all_together(journey: list):
    all_parsed_urls = []
    parsed_elevation_url = []
    search_url = MapRequest.build_search_URL(journey)
    parsed_search_url = MapRequest.decode_the_map(search_url)
    all_parsed_urls.append(parsed_search_url)
    elevation_url = MapRequest.build_elevation_URL(search_url)
    for each_location in elevation_url:
        parsed_elevation_url.append( MapRequest.decode_the_map(each_location))
    all_parsed_urls.append(parsed_elevation_url)
    return all_parsed_urls

if __name__ == '__main__':
    journey = JourneyInput()
    details = DetailsInput()
    if details != None:
        try:
            all_parsed_urls = all_together(journey)
            Output._calculate_classes(details, all_parsed_urls)
            print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
        except KeyError or TypeError:
            print("NO ROUTE FOUND")
    # except:
    #     print("MAPQUEST ERROR")

