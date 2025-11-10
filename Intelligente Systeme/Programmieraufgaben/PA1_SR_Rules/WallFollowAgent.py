from is_sr.Agents import Agent8M

class WallFollowAgent(Agent8M):
    """
    Wall-Following Agent according to lecture
    """    
    def __init__(self, memory=False):
        """
        Constructor
        
        Defers construction to Baseclass
        """
        Agent8M.__init__(self, memory)

    @classmethod
    def sense(cls, sensors):
        """
        Generate features from environment using sensor input sensors
        s0 s1 s2
        s7 WF s3
        s6 s5 s4
        """

        """
            STUDENT CODE HERE
        """

        return ()

    @classmethod
    def action(cls, x, memory=None):
        """
        Select appropriate rule from rule set based on passed feature vector x

        In some levels memory may be allowed and will be filled with the last executed action.
        """

        """
            STUDENT CODE HERE
        """

        return "N"
