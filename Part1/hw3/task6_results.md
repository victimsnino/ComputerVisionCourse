In all cases used **pattern_size = (9, 7)**

____________
python .\task6.py  ./data/GOPR0117000?.jpg 
```
Total count of objects: 9
RMS: 0.11888749869150379
camera matrix:
 [[412.31630028   0.         475.19092824]
 [  0.         420.9767259  273.9744743 ]
 [  0.           0.           1.        ]]
distortion coefficients:  [-3.50704433e-01  1.06618037e+00 -1.53269457e-02 -2.04792677e-03
 -2.53563048e+00]
```
 ___________________
python .\task6.py  ./data/GOPR011700[1,2]?.jpg 
 ```
Total count of objects: 20
RMS: 0.1086046556290967
camera matrix:
 [[421.03122995   0.         475.50513006]
 [  0.         437.94730073 280.18840567]
 [  0.           0.           1.        ]]
distortion coefficients:  [-2.57941063e-01 -9.19722278e-01 -1.48775534e-02 -5.99785121e-05
  1.16719731e+01]
  ```
  _______________
python .\task6.py  ./data/GOPR011700[1,2,3]?.jpg 
  ```
Total count of objects: 30
RMS: 0.11330631678923286
camera matrix:
 [[427.35987163   0.         474.37579545]
 [  0.         445.36316023 277.39570262]
 [  0.           0.           1.        ]]
distortion coefficients:  [-3.03554295e-01  1.82476327e-01 -1.37515854e-02  8.58918564e-04
  1.55543875e+00]
```
  ___________
  python .\task6.py  ./data/GOPR011700[1,2,3,4,5]?.jpg 
   ```
Total count of objects: 50
RMS: 0.11555684698637284
camera matrix:
 [[428.13165291   0.         472.91060336]
 [  0.         451.27528811 284.29194281]
 [  0.           0.           1.        ]]
distortion coefficients:  [-0.29580684  0.09380132 -0.01698056  0.00207134  1.4553116 ]
```
___________
python .\task6.py  ./data/GOPR011700??.jpg 
```
Total count of objects: 99
RMS: 0.11721576265392616
camera matrix:
 [[403.64115169   0.         480.9115181 ]
 [  0.         418.12247856 291.73573583]
 [  0.           0.           1.        ]]
distortion coefficients:  [-2.49626863e-01 -3.44686990e-03 -1.93542307e-02 -3.01924066e-04
  7.73509875e-01]
```

---------
I've tried to calculate params on the whole dataset, but it haven't ended after 4+ hours...
