# NMO_net
Test on performance of inception v3 transfer learning on dataset

progress:

used about 100000 images to train for classifications of 1. body position; 2. scanning orientation; 3. scanning mode; using inception v3 net as initial weights; accuracy at about 96 percent.


export_procedure.py : export dicom data to jpeg, under correct directory path
label_image.py: go through all directories, use the trained net to identify if there is any mistake in categorizing. 



**Todo:**

Note 6/29/17:
- Until data better curated, check out other neural image dataset, and 3D convolutional NN; 
- Only mode T1, T1 Flair +C, T2, and T2 Flair need to be considered;
- test on Other_Patient dataset
- utilize 3D Neural Network to recognize if two MRI sets belong to the same person
- with multiple body parts, scanning orientation, and scanning mode, maybe consider multi-view 3D CNN?
- Need to understand what each scanning mode is 

1. label all scanning images according to body parts, scanning orientation, and scanning mode, and put them to corresponding folders;
2. for each folder, decide if that certain sequence of images have diagnostic evidence on NMO - and if so, which images, at about what part?
3. divide the images into 2 sets, one has observable NMO, and the other one does not.
4. create 3D CNN for every body part's every scanning orientation's every scanning mode (or just every body part and scanning orientation, this is about 6 of them), and use the 2 sets to train for binary classification. Use the resulting CNN's activation functions as feature extractor to train another fully connected NN/SVM, which outputs the result. 

**Question:**

what is each scanning mode, are all of them significant? 

do we have enough positive data sequences? need to pull the data on this one 

what structure should the 3D CNN be? 

what is the best implementation for the last NN? should we use SVM? 


~~Take stats on the dataset - how many images of each type exactly?~~

check test.txt


**Notes:**
dataset candidates:

- opensource MRI data:
https://openfmri.org/how-to-extract-data/

- kaggle lung cancer data:
https://www.kaggle.com/c/data-science-bowl-2017/data

- ADNI
http://adni.loni.usc.edu/data-samples/mri/

- multi-view 2D
https://arxiv.org/pdf/1505.00880.pdf

- skull stripping trained 3D CNN
https://github.com/GUR9000/Deep_MRI_brain_extraction


- 3D Neural Network:
VoxNet

**Apendix**
- FSE - Fast Spin Echo
- FS - Fat Suppressed
- SE - Spin Echo
- FSPGR - Fast spoiled Gradient Echo, faster scan, less false shadow
- Note, Fat and Water are high signal under T2
- TOP - From Neck to Chest
- LOC - locate, not meaningful
- FL:B T1P - can be considered T1
- WATER - can be considered as FS
- FAT - Fat image, not meaningful
- C stands for Cervical Vertebrae. It consists of 7 bones, from top to bottom, C1, C2, C3, C4, C5, C6 and C7.
- T stands for Thoracic Vertebrae, 12 of them.
- O stands for Oblique - a plane or section not perpendicular to the xyz coordinate system, such as long and short axis views of the heart - ala not Ax Cor or Sag

