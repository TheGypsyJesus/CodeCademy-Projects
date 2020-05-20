let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => {
  return Math.floor(Math.random() * 10);
};
//The is the shorthand of just "return userDiff <= cmpDiff" (Boolean)
const compareGuesses = (userGuess, cmpGuess, targetNum) => {
  const userDiff = Math.abs(targetNum - userGuess);
  const cmpDiff = Math.abs(targetNum - cmpGuess);

  if (userDiff < cmpDiff) {
    return true;
  } else if (cmpDiff < userDiff) {
    return false;
  } else {
    return true;
  }

};
//Experimanting with a switch rather than If/Else if
const updateScore = (winnerString) => {
  switch(winnerString){
    case 'human':
      humanScore++;
      break;
    case 'computer':
      computerScore++;
      break;
    default:
      //Tie
      break;
  }
};

const advanceRound = () => currentRoundNumber++;
