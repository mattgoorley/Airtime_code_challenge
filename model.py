import requests

class Model:
  """
  I decided to break this up into a MVC format (minus the V)

  I am calling the API and returning the responses here.
  """
  def __init__(self):
    self.url = "http://challenge2.airtime.com:7182/"
    self.headers = {"X-Labyrinth-Email": "mattgoorley@gmail.com"}

  def start(self):
    """ This function returns the starting room id """
    start_url = self.url + "start"
    room = requests.get(start_url, headers=self.headers).json()
    room_id = room['roomId']
    return room_id

  def exit(self, room):
    """ Returns the possible exits from a room """
    exit_url = self.url + "exits?roomId={a}".format(a=room)
    exit_list = requests.get(exit_url, headers=self.headers).json()
    exits = exit_list['exits']
    return exits

  def move(self, room, exit):
    """ Moves to a new room and returns new room id.

    Must put in room id that you are moving from and the exit
    you wish to leave from.
    """
    move_url = self.url + "move?roomId={a}&exit={b}".format(a=room, b=exit)
    move = requests.get(move_url, headers=self.headers).json()
    room_id = move['roomId']
    return room_id

  def wall(self, room):
    """ Returns what is on the wall """
    wall_url = self.url + "wall?roomId={a}".format(a=room)
    wall = requests.get(wall_url, headers=self.headers).json()
    return wall

  def report(self, body):
    """ Submits report and returns response """
    post_url = self.url + "report"
    r = requests.post(post_url, headers=self.headers, json=body)
    return r


