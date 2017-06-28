# NMO_net
Test on performance of inception v3 transfer learning on dataset

progress:

used about 100000 images to train for classifications of 1. body position; 2. scanning orientation; 3. scanning mode; using inception v3 net as initial weights; accuracy at about 96 percent.


export_procedure.py : export dicom data to jpeg, under correct directory path
label_image.py: go through all directories, use the trained net to identify if there is any mistake in categorizing. 


to do:

Take stats on the dataset - how many images of each type exactly?
correction rate? 

test on Other_Patient dataset
