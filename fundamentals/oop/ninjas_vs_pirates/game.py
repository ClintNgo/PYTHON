from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.pirate import Captain

michelangelo = Ninja("Michelanglo", 15)

jack_sparrow = Pirate("Jack Sparrow", 20)

davey_Jones = Captain("Davey Jones", 50)


davey_Jones.show_stats()
michelangelo.show_stats()
jack_sparrow.show_stats()
davey_Jones.cannon_shot(michelangelo)
jack_sparrow.attack(michelangelo)
michelangelo.attack(jack_sparrow)
jack_sparrow.heal()
michelangelo.heal()
jack_sparrow.attack(michelangelo)
michelangelo.attack(jack_sparrow)
jack_sparrow.attack(michelangelo)
michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# jack_sparrow.heal()
# michelangelo.heal()
# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# jack_sparrow.heal()
# michelangelo.heal()
# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# jack_sparrow.heal()
# michelangelo.heal()
# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)

