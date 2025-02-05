import random
import pickle

from pygame.locals import *

from Species import Species
from Trait import Trait
from Enemy import Enemy
from Player import Player
from Rune import Rune
from Encounter import Encounter
from Area import Area

# initialize pools
def choose_enemy_trait_pool():
    return [[Trait("Pesky", -2,-1,0),       (1/60)], 
            [Trait("Annoying", -2,0,-1),    (1/60)], 
            [Trait("Weak", -1,-2,0),        (1/60)], 
            [Trait("Frail", -1,0,-2),       (1/60)], 
            [Trait("Feeble", 0,-2,-1),      (1/60)], 
            [Trait("Sickly", 0,-1,-2),      (1/60)], 
            [Trait("Brash", -2,-1,1),       (1/60)], 
            [Trait("Irritating", -2,1,-1),  (1/60)], 
            [Trait("Cocky", -1,-2,1),       (1/60)], 
            [Trait("Lonely", -1,1,-2),      (1/60)], 
            [Trait("Desperate", 1,-2,-1),   (1/60)], 
            [Trait("Skittish", 1,-1,-2),    (1/60)], 
            [Trait("Shy", -2,-1,2),         (1/60)], 
            [Trait("Coy", -2,0,1),          (1/60)], 
            [Trait("Sheepish", -2,1,0),     (1/60)], 
            [Trait("Nervous", -2,2,-1),     (1/60)], 
            [Trait("Bashful", -1,-2,2),     (1/60)], 
            [Trait("Cautious", -1,2,-2),    (1/60)], 
            [Trait("Sloppy", 0,-2,1),       (1/60)], 
            [Trait("Stubborn", 0,1,-2),     (1/60)], 
            [Trait("Jittery", 1,-2,0),      (1/60)], 
            [Trait("Jumpy", 1,0,-2),        (1/60)], 
            [Trait("Stressed", 2,-2,-1),    (1/60)], 
            [Trait("Frantic", 2,-1,-2),     (1/60)], 
            [Trait("Nonchalant", -2,0,2),   (1/60)], 
            [Trait("Aloof", -2,2,0),        (1/60)], 
            [Trait("Haughty", -1,0,1),      (1/60)], 
            [Trait("Indifferent", -1,1,0),  (1/60)], 
            [Trait("Lazy", 0,-2,2),         (1/60)], 
            [Trait("Calm", 0,-1,1),         (1/60)], 
            [Trait("Reluctant", 0,1,-1),    (1/60)], 
            [Trait("Oblivious", 0,2,-2),    (1/60)], 
            [Trait("Casual", 1,-1,0),       (1/60)], 
            [Trait("Wary", 1,0,-1),         (1/60)], 
            [Trait("Careless", 2,-2,0),     (1/60)], 
            [Trait("Apathetic", 2,0,-2),    (1/60)], 
            [Trait("Placid", -2,1,2),       (1/60)], 
            [Trait("Gentle", -2,2,1),       (1/60)], 
            [Trait("Cool", -1,0,2),         (1/60)], 
            [Trait("Composed", -1,2,0),     (1/60)], 
            [Trait("Chipper", 0,-1,2),      (1/60)], 
            [Trait("Tough", 0,2,-1),        (1/60)], 
            [Trait("Reckless", 1,-2,2),     (1/60)], 
            [Trait("Bold", 1,2,-2),         (1/60)], 
            [Trait("Crazy", 2,-2,1),        (1/60)], 
            [Trait("Lively", 2,-1,0),       (1/60)], 
            [Trait("Vicious", 2,0,-1),      (1/60)], 
            [Trait("Bloodthirsty", 2,1,-2), (1/60)], 
            [Trait("Gritty", -1,1,2),       (1/60)], 
            [Trait("Gutsy", -1,2,1),        (1/60)], 
            [Trait("Daring", 1,-1,2),       (1/60)], 
            [Trait("Fierce", 1,2,-1),       (1/60)], 
            [Trait("Fearless", 2,-1,1),     (1/60)], 
            [Trait("Dangerous", 2,1,-1),    (1/60)], 
            [Trait("Burly", 0,1,2),         (1/60)], 
            [Trait("Sturdy", 0,2,1),        (1/60)], 
            [Trait("Buff", 1,0,2),          (1/60)], 
            [Trait("Mighty", 1,2,0),        (1/60)], 
            [Trait("Brawny", 2,0,1),        (1/60)], 
            [Trait("Heroic", 2,1,0),        (1/60)]]

def choose_enemy_health_pool(difficulty):
    if difficulty < 15:
        return [[5, 0.25],
                [6, 0.25],
                [7, 0.25],
                [8, 0.25],
                [9, 0.00]]
    if difficulty == 15:
        return [[5, 0.15],
                [6, 0.20],
                [7, 0.30],
                [8, 0.20],
                [9, 0.15]]
    if difficulty > 15:
        return [[5, 0.00],
                [6, 0.25],
                [7, 0.25],
                [8, 0.25],
                [9, 0.25]]

def choose_enemy_power_pool(difficulty):
    if difficulty < 15:
        return [[2, 0.20],
                [3, 0.40],
                [4, 0.40]]
    if difficulty == 15:
        return [[3, 0.33],
                [4, 0.33],
                [5, 0.33]]
    if difficulty > 15:
        return [[4, 0.40],
                [5, 0.40],
                [6, 0.20]]

def choose_player_element_pool():
    return [["F", 0.23],
            ["S", 0.23],
            ["I", 0.23],
            ["E", 0.23],
            ["A", 0.08]]

def choose_player_power_pool():
    return [[1, 0.25],
            [2, 0.25],
            [3, 0.25],
            [4, 0.25]]

def choose_area_biome_pool():
    return ["Desert",
            "Cave",
            "Forest",
            "Swamp",
            "Grassland"]

def choose_from(pool):
    sample_list, weight_list = zip(*pool)
    choice = random.choices(sample_list, weight_list, k = 1)
    result = choice[0]
    return result

def generate_rune(element_pool, power_pool):
    element = choose_from(element_pool)
    power = choose_from(power_pool)
    if element == "A":
        power = "?"
    rune = Rune(element, power)
    return rune

def generate_enemy(level_pool, species_pool, trait_pool, health_pool, power_pool):
    level = choose_from(level_pool)
    species = choose_from(species_pool)
    trait = choose_from(trait_pool)

    health = choose_from(health_pool)
    health += choose_from(health_pool)
    health += species.get_health_mod(level)
    health += trait.get_health_mod()

    base_attack = species.get_attack_mod(level)
    base_attack += trait.get_attack_mod()

    base_defense = species.get_defense_mod(level)
    base_defense += trait.get_defense_mod()

    power = choose_from(power_pool)

    action = choose_from(species.get_action_pool())

    gold = species.get_gold_drop(level)
    gold += (trait.get_score() + 4)

    enemy = Enemy(level, species, trait, health, health, base_attack, base_defense, power, action, gold)
    return enemy

def generate_player_hand(current_player_hand, player_element_pool, player_power_pool):
    num_runes_needed = 5 - len(current_player_hand)
    new_player_hand = current_player_hand.copy()
    count = 0
    while count < num_runes_needed:
        new_rune = generate_rune(player_element_pool, player_power_pool)
        if new_rune not in new_player_hand:
            new_player_hand.append(new_rune)
            count += 1
    return new_player_hand

def string_to_spell(spell_str):
    rune_str_list = spell_str.split()
    spell = []
    for rune_str in rune_str_list:
        element = str(rune_str[0])
        power = 0
        if element == "A":
            power = "?"
        else:
            power = int(rune_str[1:])
        rune = Rune(element, power)
        spell.append(rune)
    return spell

def choose_seed():
    seedlist = open("seedlist.txt")
    words=seedlist.read().split('\n')
    game_seed = str(random.choice(words))
    return game_seed

class GameState:
    def __init__(self, seed, difficulty, adaptive_difficulty):
        if seed == "":
            self.seed = choose_seed()
        else:
            self.seed = str(seed)

        random.seed(self.seed)

        if difficulty == "easy":
            self.difficulty = 0
        elif difficulty == "hard":
            self.difficulty = 30
        else:
            self.difficulty = 15

        if adaptive_difficulty == "1":
            self.adaptive_difficulty = True
        else:
            self.adaptive_difficulty = False

        self.enemy_trait_pool = choose_enemy_trait_pool()
        self.enemy_health_pool = choose_enemy_health_pool(self.difficulty)
        self.enemy_power_pool = choose_enemy_power_pool(self.difficulty)
        self.player_power_pool = choose_player_power_pool()
        self.player_element_pool = choose_player_element_pool()
        self.area_biome_pool = choose_area_biome_pool()
        self.player_state = Player(30, 5)
        self.spell_str = ""
        self.area_num = 0
        self.encounter_num = 0
        self.current_area = Area(self.area_num, "none")
        self.next_area1 = "none"
        self.next_area2 = "none"
        self.state = "title"
        self.random_state = random.getstate()
        self.turn_result = []
        self.rerolls = 1
        self.encounters_damage_dealt = []
        self.encounters_damage_taken = []
        self.encounters_damage_blocked = []
        self.encounters_num_turns = []
        self.enemies_defeated = []

    # game logic

    def set_seed(self, seed):
        self.seed = seed

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.enemy_health_pool = choose_enemy_health_pool(difficulty)
        self.enemy_power_pool = choose_enemy_power_pool(difficulty)

    def adapt_difficulty(self):
        total_damage_taken = sum(self.current_area.current_encounter.player_damage_taken)
        adjustment_factor = 10 - total_damage_taken
        old_difficulty = self.difficulty
        new_difficulty = old_difficulty + adjustment_factor
        self.set_difficulty(new_difficulty)

    def choose_next_area_fork(self):
        biomes = self.area_biome_pool.copy()
        if self.current_area.get_biome() in biomes:
            biomes.remove(self.current_area.get_biome())
        choices = random.sample(biomes, 2)
        self.next_area1 = choices[0]
        self.next_area2 = choices[1]

    def next_area(self, choice):
        biome = "none"
        if choice == 1:
            biome = self.next_area1
        if choice == 2:
            biome = self.next_area2
        if choice == 3:
            biome = "Cave"
        self.area_num += 1
        self.current_area = Area(self.area_num, biome)
        self.encounter_num = 0

    def log_battle(self):
        self.encounters_damage_dealt.append(sum(self.current_area.current_encounter.player_damage_dealt))
        self.encounters_damage_taken.append(sum(self.current_area.current_encounter.player_damage_taken))
        self.encounters_damage_blocked.append(sum(self.current_area.current_encounter.player_damage_blocked))
        self.encounters_num_turns.append(self.current_area.current_encounter.get_turn())
        self.enemies_defeated.append(self.current_area.current_encounter.get_enemy_state().get_species().get_name())

    def next_encounter(self):
        if self.encounter_num > 0 and self.adaptive_difficulty:
            self.adapt_difficulty()
        self.encounter_num += 1
        self.player_state.set_current_hand(generate_player_hand(self.player_state.get_current_hand(), self.player_element_pool, self.player_power_pool))
        if self.area_num > 5:
            enemy = Enemy(4, Species("Snake"), Trait("Slippery", 0, 0, 0), 30, 30, 6, 6, 5, "defend", 30)
        else:
            enemy = generate_enemy(self.current_area.get_enemy_level_pool(), self.current_area.get_enemy_species_pool(), self.enemy_trait_pool, self.enemy_health_pool, self.enemy_power_pool)
        self.current_area.next_encounter(self.player_state, enemy)

    def next_turn(self):
        self.player_state.cast_spell()
        self.current_area.current_encounter.do_turn(self.player_state)
        self.rerolls = 1
        self.turn_result = self.current_area.current_encounter.display_turn()
        self.current_area.current_encounter.choose_enemy_action()
        self.current_area.current_encounter.enemy_state.set_current_power(choose_from(self.enemy_power_pool))
        self.player_state.set_current_hand(generate_player_hand(self.player_state.get_current_hand(), self.player_element_pool, self.player_power_pool))
        self.player_state.set_current_spell([])

    def current_enemy_is_dead(self):
        return self.current_area.current_encounter.get_enemy_state().is_dead()

    def player_is_dead(self):
        return self.player_state.is_dead()

    def give_current_enemy_gold_to_player(self):
        self.player_state.change_current_gold(self.current_area.current_encounter.enemy_state.get_gold())

    def get_current_enemy_gold(self):
        return self.current_area.current_encounter.enemy_state.get_gold()

    def heal_player(self):
        if self.player_state.current_gold > 0 and self.player_state.current_health < 30:
            self.player_state.change_current_gold(-1)
            self.player_state.change_current_health(1)
        
    def heal_player_all(self):
        amount = 30 - self.player_state.get_current_health()
        if self.player_state.current_gold >= amount:
            self.player_state.change_current_gold(-amount)
            self.player_state.set_current_health(30)
        else:
            while self.player_state.current_gold > 0:
                self.heal_player()

    def reroll_hand(self):
        if self.rerolls > 0:
            self.player_state.set_current_hand([])
            self.player_state.set_current_spell([])
            self.player_state.set_current_hand(generate_player_hand(self.player_state.get_current_hand(), self.player_element_pool, self.player_power_pool))
            self.rerolls -= 1

    def get_current_enemy_species(self):
        return self.current_area.current_encounter.enemy_state.species.name

    def get_current_area_biome(self):
        return self.current_area.get_biome()

    def get_current_enemy_name(self):
        return self.current_area.current_encounter.enemy_state.print_name()

    def get_current_enemy_stats(self):
        return self.current_area.current_encounter.enemy_state.print_stats()

    def get_current_player_stats(self):
        return self.player_state.print_stats()

    def get_current_player_hand(self):
        return "Hand: " + str(' '.join([str(rune) for rune in self.player_state.get_current_hand()]))

    def get_turn_result(self):
        return self.turn_result

    def save(self):
        self.random_state = random.getstate()
        with open("save", "wb") as f:
            pickle.dump(self, f)

    def load(self):
        random.setstate(self.random_state)