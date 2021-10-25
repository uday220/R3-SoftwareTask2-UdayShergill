# R3-SoftwareTask2-UdayShergill

The way this project works is with two python files, one called input and the other called output. The input file has three main tasks, first, it listens for any keyboard inputs, then when a key is pressed it figures out what key is pressed and what that key means in terms of how the rover is going to move ex. w key forward. Finally, it then sends the information to the output file to output to the rover.

The way I got the file to listen for key inputs was by using the pynput library and importing the keyboard from it. Then I created a function for the key input and with a function to listen for keys. It looked like this
![image](https://user-images.githubusercontent.com/91505369/138620732-0081a80d-5240-4a5f-9f51-763f2e55d2c0.png)

Then I had to find out what the pressed key was meant to do which I did by using key.char and if statements. When incorporated it looked like this
![image](https://user-images.githubusercontent.com/91505369/138620808-36e16bef-b48e-4a29-a690-885fa3a78092.png)

Then I started to create the client for the rover where this will all go. I imported the socket library to start with and then assigned values to the TCP_IP, TCP_PORT, and the BUFFER_SIZE. Then I converted my output from the code above into bytes and stored it in MESSAGE. Then the socket was connected with the corresponding TCP_IP and TCP_PORT from the server and which then allowed the message to be sent. 

After the client program was set up I began working on the server program which was similar to the client one. I imported the socket library and assigned the same values for the TCP_IP, TCP_PORT, and the BUFFER_SIZE. Then the server was bound to that TCP_IP and TCP_PORT and started to listen and accept connects. After that in a while loop, the data was received, decoded, and finally output. 

There was only one problem with my code which was the input would only listen for one type of input and send it before listening for others too. I attempted to overcome this problem but, I couldn't. When I broke apart the code for the TCP sending data and the keyboard listening, I found that the keyboard listener was listening for multiple inputs but the way I was sending data only sent the first input key. There is a closer on the server (output) code but, that was added later after failing to try to resolve the issue to have a way to close the program when it is done outputting. Otherwise, the code works as it successfully outputs the correct output when the specific command key is pressed. 

Example output of D and 5
![image](https://user-images.githubusercontent.com/91505369/138622321-9e99ae29-8ee1-48a4-94d0-3e34fe5b7018.png)

Video Link:
https://drive.google.com/file/d/1KQm1gy4oS12Rs6VDWFXhmnu591kpfrya/view?usp=sharing
 
