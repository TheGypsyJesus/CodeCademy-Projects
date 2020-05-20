using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    //This method will update the position of the player when a key is pressed
    public new static void UpdatePosition(string keyPress, out int x_ord, out int y_ord){

      //Setting variables
      x_ord = 0;
      y_ord = 0;

      //Switch statement to determine which key was pressed
      switch (keyPress){
        case "DownArrow":
          y_ord += 1;
          break;
        case "UpArrow":
          y_ord -= 1;
          break;
        case "RightArrow":
          x_ord += 1;
          break;
        case "LeftArrow":
          x_ord -= 1;
          break;
        default:
          Console.WriteLine("Invalid key!");
          break;
      }
    }
//This method will update the direction of the sprite(pointer)
    public new static char UpdateCursor(string keyPress){

      //Setting the variable to reduce errors
      char sprite = "o";

      switch (kewPress){
        case "LeftArrow":
          sprite = "<";
          break;
        case "RightArrow":
          sprite = ">";
          break;
        case "UpArrow":
          sprite = "^";
          break;
        case "DownArrow":
          sprite = "v";
          break;
      }
      return sprite; //Return desired direction
    }
//This method will set the outer bounds, of which we cannot cross
    public new static int KeepInBounds(int co_ord, int max_val){
      //If statement for ensuring coordinates are within bounds
      if (co_ord > max_val){
        return 0; //send player to the other side when crossing the bound (like the tunnel on pacman)
      } else if (co_ord < 0){
        return max_val; //this will do the same as the above, just the opposite way
      } else {
        return co_ord; //Current coordinates are fine for continuation
      }
    }

  //This will allow the score to increase after the @ symbol is hit
    public new static bool DidScore(int player_x, int player_y, int fruit_x, int fruit_y){
      //if statement to determine if the coordinates overlap
      if (player_x == fruit_x && player_y == fruit_y){
        return true;
      } else {
        return false;
      }
    }
  }
}
