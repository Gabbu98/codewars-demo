package kata
import (
  "fmt"
)
// SnakesLadders - Stucture that game is played on
type SnakesLadders struct {
  // Define Game Struct
  boxes map[int]int
  current1 int
  current2 int
  player1Turn bool
}

// NewGame - Method that starts a new game for the SnakesLadders struct
func (sl *SnakesLadders) NewGame() {
    sl.current1 = 0
    sl.current2 = 0
    sl.player1Turn = true    // Player 1 starts
    
    // Reinitialize the board (optional, if you want to reset everything)
    sl.boxes = map[int]int{
        2:  38,  7:  14,  8:  31,  15:  26,
        16: 6,  28: 84,  21: 42,  36: 44,  49: 11,
        46: 25, 51: 67,  62: 19,  64: 60,  71: 91,
        74: 53, 78: 98,  87: 94,  89: 68,  92: 88,
        95: 75, 99: 80, // End position
    }
}

// Play - Method that makes turn givem a doce roll from die1 and die2 for the SnakesLadders struct
// Player that dice is for should automatically be determined based on rules
func (sl *SnakesLadders) Play(die1, die2 int) string {
  if(sl.current1 == 100 || sl.current2 == 100 ) {
    return "Game over!"
  }
  
  var total int = die1 + die2
  isEqual := die1 == die2

  var negative bool
  var current *int
  
  // determine which player's turn and update current
  if(sl.player1Turn){
    current = &sl.current1
  } else {
    current = &sl.current2
  }
  
  // iterate current
  // each iteration check map,

  for i:=1; i <= total; i++ {
    var val int = 0
    var ok bool = false
    
    if !negative {
      (*current)++
    } else {
      // bounce back
      (*current)--
    }
    
    if i == total {
       val, ok = sl.boxes[*current]
    }

    // special move
    if ok {
      *current = val
    }
    
    if *current == 100 {
      negative = true
    }
    
    // no special move

  }
  
  // update next player's turn
  if sl.player1Turn {
    sl.current1 = *current
    
    // if die aren't equal flip turn
    if !isEqual {
      sl.player1Turn = !sl.player1Turn
    }
    if *current == 100 {
      return "Player 1 Wins!"
    }
    
    return fmt.Sprintf("Player 1 is on square %d", *current)
  }
  
  sl.current2 = *current
  
  // if die aren't equal flip turn
  if !isEqual {
    sl.player1Turn = !sl.player1Turn
  }
  if *current == 100 {
      return "Player 2 Wins!"
  }
  return fmt.Sprintf("Player 2 is on square %d", *current)
}

// - make a class SnakesLadders
// - triggerable = play(die1, die2)
// - die1 and die2 thrown in turn and both integers between 1-6

// Rules:
// 1. two player and both start from board square 0
// 2. Player 1 starts
// 3. Follow the numbers up the board in order 1=>100
// 4. Both die equals => another go
// 5. Ladders = climb and cont moving
// 6. Snakes = slide down and cont moving
// 7. last square = win, roll too high bounces off and roll back

