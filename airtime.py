from model import Model


class Labyrinth:"""
This is for the airtime code challenge. I have imported
created a model file to make the API calls, but did not
make a view file.

"""

  # needs_lights stores the rooms that need lights
  needs_lights = []
  # writings stores the order (key) and writing (value)
  writings = {}
  # order will take the orders to be sorted
  order = []
  # rooms_visited will list all of the rooms visited
  rooms_visited = []

  def __init__(self):
    # call self.model from model.py
    self.model = Model()


  def starting_room(self):
    """ This is the backbone function - run this.
    It takes in the initial room id and calls other functions
    to solve the problem. """
    room_id = self.model.start()
    self.move(room_id, "First")
    self.order_list()
    challenge = self.concatenate()
    body = {
    'roomIds': self.needs_lights,
    'challenge': challenge
    }
    responds = self.model.report(body)
    return responds.text

  def lights_report(self, room_id):
    """ Creates the reports. If the lights are out
    it will add that room id to the needs_lights array.
    If lights are on it adds to writings dic with order as key
    and writings as value.
    """
    answer = self.model.wall(room_id)
    writing = answer['writing']
    order = answer['order']
    if order == -1:
      self.needs_lights.append(room_id)
      return
    elif order >= 0:
      self.writings[order] = writing
      return
    else:
      return "problem"

  def move(self, room_id, direction):
    """
    Moves through the labyrinth and calls lights_report
    function to sort the room's info.
    """
    if room_id in self.rooms_visited:
      return False
    self.rooms_visited.append(room_id)
    self.lights_report(room_id)
    exits = self.model.exit(room_id)
    if exits == None:
      return False
    if 'north' in exits:
      next_room = self.model.move(room_id, 'north')
      self.move(next_room, 'north')

    if 'south' in exits:
      next_room = self.model.move(room_id, 'south')
      self.move(next_room, 'south')

    if 'east' in exits:
      next_room = self.model.move(room_id, 'east')
      self.move(next_room, 'east')

    if 'west' in exits:
      next_room = self.model.move(room_id, 'west')
      self.move(next_room, 'west')

    return 'Movement Completed'

  def order_list(self):
    """
    puts the key of writings in a list to be sorted
    """
    for key in self.writings:
      self.order.append(key)
    return self.order

  def concatenate(self):
    """
    sorts the ordered list
    """
    ordered = sorted(self.order)
    concat = []
    for i in ordered:
      concat.append(self.writings[i])
    challenge_code = "".join(concat)
    return challenge_code

run = Labyrinth()
run.starting_room()



