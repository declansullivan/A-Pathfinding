# A-Pathfinding
A* Pathfinding algorithm in Python

<hr>

<h2>Write-Up</h2>

This A* pathfinding program was to help learn the basics behind pathfinding by following the algorithm on Wikipedia. I was also trying to learn the tkinter gui package for Python, and updating a grid of rectangles with their colors based on what kind of node they represent seemed like a good way to start.

<hr>

<h2>Versions</h2>

My first attempt at A* pathfinding is in the base file, main.py. Here, a Node object and all methods needed for the pathfinding algorithm are written. It was quite messy, but it worked, so my next goal was to clean it up.

<br>

The second attempt is in the Minigame directory. Here I wanted to try to have multiple Enemy objects that would chase the player as they tried to avoid the enemies as they found their way towards the player. This was a cleaner version with a Node, Enemy, and AStar object, as well as a main file to start the program.

This attempt works quite well, aside for some flaws I am currently trying to fix. You can have multiple enemies that will all
pathfind towards the player, although when the player moves a good amount quickly, their pathfinding can become flawed and they will freeze, likely because the endpoint has changed, which messes up the scoring system of each node.  Other than that, they can all pathfind straight to the point, updating the GUI every 'turn'.
