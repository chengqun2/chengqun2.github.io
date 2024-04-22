## Machine-learning
### Face-recognition
1. Making our image black and white because we don’t need color data to find faces.
2. We break up the image into small squares of 16x16 pixels each. Also called `Histogram of Oriented Gradients`.
3. Use `face landmark estimation` algorithm to solve `different directions look totally different` issue.
The basic idea is we will come up with 68 specific points (called landmarks) that exist on every face — the top of the chin, the outside edge of each eye, the inner edge of each eyebrow, etc.
4. Measure features of the face in 128 measurements for each person and save.
5. Looking at all the faces we’ve measured in the past, see which person has the closest measurements to our face’s measurements. 