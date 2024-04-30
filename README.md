# Named Entity Recognition

This project focuses on building a special type of artificial intelligence model called a Named Entity Recognition (NER) model. This model is designed to identify and classify specific entities related to the world of cinema within a given sentence. These entities can include actors, directors, film titles, and more.

- Training the Model: To train the NER model effectively, I developed a program called a "train generator." This program creates a large number of random sentences specifically tailored to the cinema domain. These sentences act as training examples for the model, helping it learn to recognize the relevant entities.

- Standardizing the Data:  I also implemented a "value standardizer." This component takes the entities identified by the NER model and ensures they are in the correct format. For instance, it might fix any typos or inconsistencies in the names of actors or directors found in the sentence. This step helps to improve the overall accuracy and consistency of the model's output.
