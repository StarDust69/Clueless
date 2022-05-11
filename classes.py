class Detective:
  '''
  Class for prime detective.
  @param Name, intelligence, strength, stamina, and health.
  '''
  def __init__(self, name, intelligence, strength, stamina, health):
    self.name = name
    self.intelligence = intelligence
    self.strength = strength
    self.stamina = stamina
    self.health = health

  def __repr__(self):
    return self.name


class Riddle:
  '''
  Class for riddle.
  '''
  def __init__(self, description, intelligence, strength, stamina, health):
    self.description = description
    self.intelligence = intelligence
    self.strength = strength
    self.stamina = stamina
    self.health = health

  def __repr__(self):
    return self.description


class Loot:
  '''
  Class for Loot.
  '''
  def __init__(self, intelligence, strength, stamina, health):
    self.intelligence = intelligence
    self.strength = strength
    self.stamina = stamina
    self.health = health 
  
  def __repr__(self):
    return '''
    {intelligence} intelligence,
    {strength} strength,
    {stamina} stamina,
    {health} health'''.format(intelligence=self.intelligence, strength=self.strength, stamina=self.stamina, health=self.health)

class Story:
  '''
  Class for story.
  '''
  def __init__(self, clues, description, intelligence, strength, stamina, health):
    self.clues = clues
    self.description = description
    self.intelligence = intelligence
    self.strength = strength
    self.stamina = stamina 
    self.health = health

  def __repr__(self):
    return self.description
