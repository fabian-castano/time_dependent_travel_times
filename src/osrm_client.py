import requests

class OSRMClient:
    def __init__(self, host):
        self.host = host


    def get_distance_matrix(self, coordinates,source):
        # ?annotations=distance,duratio
        url = f"http://{self.host}/table/v1/driving/{';'.join([f'{c[0]},{c[1]}' for c in coordinates])}?sources={source}&annotations=distance"
        #print(url)
        response = requests.get(url)
        return response.json()
        
    def get_nearest(self, coordinates):
        url = f"http://{self.host}/nearest/v1/driving/{coordinates[0]},{coordinates[1]}"
        response = requests.get(url)
        coordinates = response.json()["waypoints"][0]["location"]
        return coordinates
    
    def get_distance(self, x, y):

        # find the nearest point to the coordinates
        a=self.get_nearest(x)
        b=self.get_nearest(y)
        

        # get the distance between the two points just found
        url = f"http://{self.host}/route/v1/driving/{a[0]},{a[1]};{b[0]},{b[1]}"
        response = requests.get(url)
        return response.json()["routes"][0]["distance"]/1000