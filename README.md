This is a reupload of a term project I developed during my time at graduate school at SDSU in 2024 to study the process of mathematical optimization on the process of color restoration in media. Within this example, a rudimentary optimizer is used without any machine learning processes involved, displaying the results by just using a gradient descent optimizer. 

The objective function utilized is the Delta E (CIE 2000) formula, implemented using the OpenCV library as ```colour.delta_E(image1_lab, image2_lab, method='CIE 2000')``` and implemented into a scipy optimizer. While additional ML-based processes would be used in the current day, I wanted to see the effect of using a simple optimizer. 

<img width="447" height="337" alt="image" src="https://github.com/user-attachments/assets/e0540023-ab38-49eb-9352-889608194270" />

To run the code, you can use the ```.ipynb``` file or run the ```.py``` file directly. 

Images used: 
[1] Flooded House, Creative Commons.
[2] J. Sato, Director, Pretty Soldier Sailor Moon. [Film]. Japan: Toei Animation, 1992. 
