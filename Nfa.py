class Nfa: 
    def __init__(
        self,
        alphabet,
        states,
        initial_states, 
        accepting_states,
        transitions
    ):
        self.alphabet = alphabet
        self.states = states
        self.initial_states = initial_states
        self.accepting_states = accepting_states
        self.transitions = transitions
    

    def get_next_states(self, current_states, action):
        """
        Get a list of the next states accepted for a given list of states and the current action.
        """
        next_states = set()
 
        for state in current_states:
                if (state, action) in self.transitions:
                    next_states.update(self.transitions[state, action])
        
        return next_states

    def match_word(self, word):
        current_level = set()
        current_level = current_level.union(self.initial_states)
        next_level = set()
        
        for action in word:
            next_level = self.get_next_states(current_level, action)
            if len(next_level) < 1:
                return False

            current_level = next_level
            next_level = set()
        if current_level.intersection(self.accepting_states):
            return True
        else:
            return False

    
