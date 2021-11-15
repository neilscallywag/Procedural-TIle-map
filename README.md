## About The Project


Procedural Grid based dungeon map system coded in JS. Serves as preliminary step in the design thinking process in order to create a game-style portfolio website. 

## Design Thinking

Initially i decided to make the character movable throughout the viewport by just changing the pixel values of the character. 
However, this creates an issue with collision detection as the code required to create a complex collision detection between character and environment of different polygons.

### Solutions

There were multiple different solutions to the abovementioned problem used in the gaming industry. As such i came up with a few considerations before going for an implementation. 
 * The Portfolio will have simple graphics with not many vertices and polygons. 
 * The code is simple and not too complicated to implement. 
 * It needs to be modular to aid in addition of new environment elements. 
 
 Here are the solutions:-
 
 1. Bounding box implemention 
 * Where a simple a the bounding box has 4 attributes of X,Y coordinates and a length (h) and breadth (w) values. 
   Therefore a simple code like this could work. 
   ```javascript
   b1.x < b2.x + b2.w &&
   b1.x + b1.w > b2.x &&
   b1.y < b2.y + b2.h &&
   b1.h + b1.y > b2.y 

 2. Detection based on alpha channel values 
 * Similar to the bounding box approach however, we check the changes in alpha value as the bounding boxes are transparent.It yields a pretty accurate collision detection. However, we have no need for that as our sprites and images are low resolution. 
 
 3. Grid Based approach. 
 * Simple where the whole viewport is divided into a grid. and the grid matrix have values to indicate where the player can traverse and interact with.
 For example. We will set value '1' and any value more than '10000' as parts of the grid where the player can move. Hence the implementation would be 
  ```javascript
   if (
      typeof map[newY] !== "undefined" &&
      typeof map[newY][newX] !== "undefined" &&
      (map[newY][newX] == 1 || map[newY][newX] > 10000)
      ) {
    // Change the current pos of player with the new pos.
      x = newX; 
      y = newY;
    // Physically move the image 
      sprite.style.left = x * 40 + "px";
      sprite.style.top = y * 40 + "px";
        }
   ```
    
Furthermore, this makes it extremly modular as we just need to map different numbers to environment objects on the grid to have different interactions. 
The code will be much simpler as we would no longer have to create a bounding box for each object. Instead we can just overlay the image on top of the grid matrix. 
 
 

