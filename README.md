# Ascii-Portrait
Assignment Submission

This repository contains a Python-based project that renders a high-resolution (240x240) ASCII art portrait of Galileo Galilei. The project was developed as part of a Python programming assignment focusing on core concepts like loops, conditional statements, and logical thinking without the use of external image-processing libraries like Pillow.

The goal was to recreate a famous personality in ASCII format under strict constraints:

No Image Libraries: You cannot simply convert pixels to characters using a library.

Resolution: Exactly 240 x 240 characters.

Logic-Driven: The portrait must be constructed through mathematical functions or procedural generation.

The Approach: "Form Before Texture"

Inspired by traditional art techniques, the project follows a two-step process:

1. Building the Skeleton (The Form)Instead of manually placing thousands of characters, the structure is defined using mathematical equations. 

By utilizing the formulas for circles, ellipses, and parabolas, we created a "blueprint" of Galileo’s face, hair, and robe.
Circle: $(x - h)^2 + (y - k)^2 = r^2$

Ellipse: $\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1$

The file skeleton.py contains the logic for this basic architecture, mapping these geometric shapes onto a coordinate grid.

2. Adding Detail (The Texture)To avoid the "tedious task" of writing thousands of unique if-else statements for every pixel, this project utilizes a custom Encoding/Decoding system.The Problem: Pure math creates a "flat" look; manual placement is too high-maintenance.The Solution: We introduced a compression-style encoding (similar to Run-Length Encoding). For example, instead of storing ,,,,, we store 4,. This allowed for the addition of "randomized" shading and fine textures within the mathematical bounds without bloating the file size.


### Usage:

1. Clone the repository:
```bash
git clone [https://github.com/Uday10001/ascii-galileo.git](https://github.com/Uday10001/ascii-galileo.git)
```
2. View the detailed Output:
```bash
python main.py
```
3. View the Architechture behind the portrait:
```bash
python Skeleton.py
```
