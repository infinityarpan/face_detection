# face_detection

This is a face_detection and locatization programme using dlib package. The first argument takes the image path. In the susequent arguments we could pass our desired model we want to use or we can pass multiple models, so that we can compare the performance of each model. We can use CNN and HOG as our model options.

1. clone the repo in to your system

	git clone https://github.com/infinityarpan/face_detection.git

2. cd into the directory

3. Create a anaconda virtual environment 

	conda create --name <environment_name> python=3

4. Activate the environment 

	conda activate <environment_name>
	
5. Install imutils(it will also install opencv along with it)

	conda install -c conda-forge imutils 

6. Download the dlib package inside with 

	git clone https://github.com/davisking/dlib.git
	
7. Then follow these steps

	cd dlib
	mkdir build
	cd build
	cmake .. ; cmake --build .
	sudo make install
	cd ..
	python setup.py install
	cd ..
	
8. Download the 'mmod_human_face_detector.dat.bz2' from https://github.com/davisking/dlib-models/blob/master/mmod_human_face_detector.dat.bz2

9. Extract the model in the directory at step 2

10. Run the code

	python face_detection.py <image_path> <model_name> <model_name>
