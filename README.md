# NMO_net
Test on performance of inception v3 transfer learning on dataset

progress:

used about 100000 images to train for classifications of 1. body position; 2. scanning orientation; 3. scanning mode; using inception v3 net as initial weights; accuracy at about 96 percent.


export_procedure.py : export dicom data to jpeg, under correct directory path
label_image.py: go through all directories, use the trained net to identify if there is any mistake in categorizing. 



**Todo:**

Note 6/29/17:
- Until data better curated, check out other neural image dataset, and 3D convolutional NN; 

dataset candidates:

opensource MRI data:
https://openfmri.org/how-to-extract-data/

kaggle lung cancer data:
https://www.kaggle.com/c/data-science-bowl-2017/data

3D Neural Network:




~~Take stats on the dataset - how many images of each type exactly? - ~~
check test.txt

- test on Other_Patient dataset
