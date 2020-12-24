This folder contains the python scripts and data that I (Pandula Priyadarshana) use in my final research project submission for the RL4NLP course (2020).

This folder contains the below 7 folders.

1. data 
 - contains the game frames (images) that I used to generate image sequences (zipped and unzipped files)
 - notebook used to unzip the zip data folder

2. generate_image_emd
 - contains the notebook used to create image embeddings
 - contains the image embedding vectors saved as a .json [removed due to size from GIT]

3. generate_text_emd
 - contains the notebook used to create sentence embeddings
 - contains the sentence embedding vectors saved as a .json [removed due to size from GIT]

4. generate_combined_emb
 - contains the notebook used to create combined embeddings
 - contains the `correct' and `incorrect' combined embedding vectors saved as .json files (correct: related image-sentence embeddings, incorrect: o/w) [removed due to size from GIT]

5. I-LEARN
 - contains the notebook in which I prepare the training data and train the I-LEARN model
 - contains the weights of the trained I-LEARN model (saved model) [removed due to size from GIT]

6. reward_generation_process
 - contains the notebook which contains the langugage-based intermediate (shaping) reward generating function
 - contains the saved I-LEARN model

7. q_learning_rl_training
 - contains the notebook which runs the core DQN algorithm (full experiment)
 - contains the saved model weights for the DQN (in train_dir)
 - contains the saved I-LEARN model
 
8. [Paper] Designing a sample-efficient RL Setup with NLP
 - a paper written on this research project
 