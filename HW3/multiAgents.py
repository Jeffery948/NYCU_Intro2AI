from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        """
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        minGhostDistance = min([manhattanDistance(newPos, state.getPosition()) for state in newGhostStates])

        scoreDiff = childGameState.getScore() - currentGameState.getScore()

        pos = currentGameState.getPacmanPosition()
        nearestFoodDistance = min([manhattanDistance(pos, food) for food in currentGameState.getFood().asList()])
        newFoodsDistances = [manhattanDistance(newPos, food) for food in newFood.asList()]
        newNearestFoodDistance = 0 if not newFoodsDistances else min(newFoodsDistances)
        isFoodNearer = nearestFoodDistance - newNearestFoodDistance

        direction = currentGameState.getPacmanState().getDirection()
        if minGhostDistance <= 1 or action == Directions.STOP:
            return 0
        if scoreDiff > 0:
            return 8
        elif isFoodNearer > 0:
            return 4
        elif action == direction:
            return 2
        else:
            return 1


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (Part 1)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        # Begin your code (Part 1)
        #raise NotImplementedError("To be implemented")
        def value(agent, state, depth): # Calculate the value of each node
            if state.isWin() or state.isLose() or depth == 0: # If game is over or reach the depth, return current value
                return self.evaluationFunction(state)
            
            next = (agent + 1) % state.getNumAgents() # Calculate next agent index
            if next == 0: # If next is zero, which means a single level search is done
                depth -= 1

            if agent == 0: # If agent is pacman, calculate its max value from its successors
                v = float("-inf")
                for a in state.getLegalActions(agent):
                    v = max(v, value(next, state.getNextState(agent, a), depth))
                return v
            else: # If agent is ghost, calculate its min value from its successors
                v = float("inf")
                for a in state.getLegalActions(agent):
                    v = min(v, value(next, state.getNextState(agent, a), depth))
                return v
                
        maximum = float("-inf")
        action = None
        for a in gameState.getLegalActions(0): # First agent is pacman, calculate its max value to get best action
            v = value(1, gameState.getNextState(0, a), self.depth)
            if v > maximum:
                maximum = v
                action = a

        return action
            
        # End your code (Part 1)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (Part 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        # Begin your code (Part 2)
        #raise NotImplementedError("To be implemented")
        '''
        '''
        def value(agent, state, depth, alpha, beta): # Calculate the value of each node
            if state.isWin() or state.isLose() or depth == 0: # If game is over or reach the depth, return current value
                return self.evaluationFunction(state)
            
            next = (agent + 1) % state.getNumAgents() # Calculate next agent index
            if next == 0: # If next is zero, which means a single level search is done
                depth -= 1

            if agent == 0: # If agent is pacman, calculate its max value from its successors
                v = float("-inf")
                for a in state.getLegalActions(agent):
                    v = max(v, value(next, state.getNextState(agent, a), depth, alpha, beta))
                    if v > beta: # If value is greater than beta, do pruning
                        return v
                    alpha = max(v, alpha) # Update alpha
                return v
            else: # If agent is ghost, calculate its min value from its successors
                v = float("inf")
                for a in state.getLegalActions(agent):
                    v = min(v, value(next, state.getNextState(agent, a), depth, alpha, beta))
                    if v < alpha: # If value is smaller than alpha, do pruning
                        return v
                    beta = min(v, beta) # Update beta
                return v
                
        maximum = float("-inf")
        action = None
        alpha = float("-inf")
        beta = float("inf")
        for a in gameState.getLegalActions(0): # First agent is pacman, calculate its max value to get best action
            v = value(1, gameState.getNextState(0, a), self.depth, alpha, beta)
            if v > maximum:
                maximum = v
                action = a
            # Value must be smaller than beta, so do not need pruning
            alpha = max(maximum, alpha) # Update alpha

        return action
        # End your code (Part 2)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (Part 3)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        # Begin your code (Part 3)
        #raise NotImplementedError("To be implemented")
        '''
        '''
        def value(agent, state, depth): # Calculate the value of each node
            if state.isWin() or state.isLose() or depth == 0: # If game is over or reach the depth, return current value
                return self.evaluationFunction(state)
            
            next = (agent + 1) % state.getNumAgents() # Calculate next agent index
            if next == 0: # If next is zero, which means a single level search is done
                depth -= 1

            if agent == 0: # If agent is pacman, calculate its max value from its successors
                v = float("-inf")
                for a in state.getLegalActions(agent):
                    v = max(v, value(next, state.getNextState(agent, a), depth))
                return v
            else: # If agent is ghost, calculate its mean value from its successors
                v = 0
                for a in state.getLegalActions(agent):
                    v += value(next, state.getNextState(agent, a), depth)
                return float(v / len(state.getLegalActions(agent)))
                
        maximum = float("-inf")
        action = None
        for a in gameState.getLegalActions(0): # First agent is pacman, calculate its max value to get best action
            v = value(1, gameState.getNextState(0, a), self.depth)
            if v > maximum:
                maximum = v
                action = a

        return action
        # End your code (Part 3)


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (Part 4).
    """
    # Begin your code (Part 4)
    #raise NotImplementedError("To be implemented")
    Pos = currentGameState.getPacmanPosition() # Get pacman position
    GhostStates = currentGameState.getGhostStates() # Get ghosts states
    Food = currentGameState.getFood() # Get food position
    Capsule = currentGameState.getCapsules() # Get capsules position
    numFood = currentGameState.getNumFood() # Get number of food
    numCapsules = len(Capsule) # Get number of capsules

    score = currentGameState.getScore() # Get current score
    scare = 0 # A flag to show whether a ghost is scared

    minGhostDistance = min([manhattanDistance(Pos, state.getPosition()) for state in GhostStates]) # Get closest ghost distance
    minCapsuleDistance = 0
    if numCapsules > 0: # If there exist capsule, get the closest capsule distance
        minCapsuleDistance = min([manhattanDistance(Pos, capsule) for capsule in Capsule])
    minScareDistance = float("inf")
    for state in GhostStates:
        if state.scaredTimer > 0: # If there exist scared ghost, set scare true, and get closest scared ghost distance
            minScareDistance = min(minScareDistance, manhattanDistance(Pos, state.getPosition()))
            scare = 1

    nearestFoodDistance = min([manhattanDistance(Pos, food) for food in Food]) # Get closest food distance
    
    if scare: # If some ghosts are scared, return the value below
        return 10 * score - 50 * minScareDistance
    elif minGhostDistance > 3: # If no ghost near pacman by 3 steps, return the value below
        return 10 * score + (-10 * nearestFoodDistance) + (-20 * minCapsuleDistance) + (-20 * numFood) + (-50 * numCapsules)
    else: # Else, return the value below
        return 10 * score + (10 * minGhostDistance) + (-1 * nearestFoodDistance) + (-20 * minCapsuleDistance) + (-10 * numFood) + (-25 * numCapsules)
    # End your code (Part 4)

# Abbreviation
better = betterEvaluationFunction
