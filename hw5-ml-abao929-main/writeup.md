# Assignment 5 - Machine Learning!

  

## Part 3 - Written Questions

  

1.  **Question**: Explain your K-Means algorithm. What are the parts of your algorithm, and how do they work together to divide your samples into different clusters?

	KMeans is broken up into a few different functions: init_centroids, euclidean_dist, closest_centroids, compute_centroids, run, and inertia

	init_centroids, initializes the k centroids by sampling k random points from the unique set of points in X the dataset.

	euclidean_dist simply calculates the euclidean distance between two points and is used by other functions later on

	closest_centroids iterates through the dataset X, and computes the closest centroid to that point using the euclidean_dist function above. This function returns an array of the same length as X of the centroid index the corresponding X value is closest to. Let index_array be the output of closest_centroids, index_array[3] is the index of the closest centroid to the point self.X[3].

	compute_centroids essentially recomputes all the centroids so that the new centroids better fit the clusters. It does so by first taking in the list of centroid indices computed using closest_centroids, then groups together the X values based off of which centroid it is closest to, thus forming the clusters. compute_centroids does so by iterating through the possible centroid indices, then getting all the X values for a given index, thus grouping the points together. It then calculates the mean of the points for each group, creating a new centroid for a cluster. compute_centroids then returns a boolean indicating whether or not the kmeans has converged which just means whether or not the new centroids are the same as the old ones.

	run is just a function that does all the previous steps together. Run computes the centroids and new indices over and over until it converges or hits the max iterations.

	Lastly, inertia computes the total squared euclidean distance between each X and the closest centroid. This is just a measure of error and how close the centroids are to the clusters.

------------------------------  

2.

- **Question**: What is each data point that is being divided into clusters? what does each cluster represent?

	 In the context of the image, each data point represents the RGB tuple for a pixel. Centroids represent the average RGB of a bunch of similar RGB values, that way you can change a whole bunch of pixels into the centroid color, effectively compressing the image.
  

- **Question**: How does changing the number of clusters impact the result of the song dataset and the image compression dataset?
	Changing the number of clusters reduces the number of groupings, and thus would mean that the clusters are larger and less fitted. Having these larger clusters results in loss for the image and just makes it super compressed. For the songs the clusters would be broader groupings of songs so the songs in each cluster would not be as closely related.
	

------------------------------

3.

- **Question**: What is the difference between supervised classification, supervised regression, and unsupervised learning?

	Classification is putting data together and putting points into labels, whereas regression is correlating features to labels then using that to predict the output given an input.
	Unsurpervised learning is different since in supervised you havefeatures and labels and try to minimize loss given boss. In unsupervized there are no given labels and the model have to try and find structure in unlabeled data.

- **Question**: Give an example of an algorithm under each, specifying the type of data that the algorithm takes in and the goal of the algorithm, and an explanation for why they are a supervised classification/supervised regression/unsupervised algorithm.

	KNN is a form of supervised classification as it places things in close proximity in bins and will predict which bin new points will go into.

	Linear regression is a supervised regression as the times we have used it in labs and homeworks we feed a model X and Y values for train and test sets.

	KMeans that we did in this project would fall under the category of unsupervised learning as in this case, none of the data is labeled and we just have assorted data of features. In the case of the images, we only have different pixel values and we cluster the pixels without a specific end result in mind.

------------------------------

4. **Question**: Give an overview of how you would modify your Kmeans class to implement Fair K-Means in  `kmeans.py`. Describe any methods you would add and where you would call them. You don’t need to understand the mathematical details of the Fair K-Means algorithm to have a general idea of the key changes necessary to modify your solution.

	In order to implement a Fair K-Means, another function would need to be added to create a proportional mean for each cluster rather than a normal mean of the features. In order for this to be implemented, the data would need to be a bit different as different attributes would need to be classified beforehand as either sensitive (gender, ethnicity) or insensitive (perfomance), that way the algorithm can balance the sensitive information when forming the clusters. 

------------------------------

5. **Question**:  How does the Fair K-means algorithm define fairness? Describe a situation or context where this definition of fairness might not be appropriate, or match your own perception of fairness.

	Fair K-means algorithm defines fairness as creating clusters that generally represent the dataset as a whole in terms of sensitive information demographics. I assume this means that each cluster will strive to maintain the same demographic splits as the dataset so that there do not exist clusters where only one demographic is grouped together. This fairness might not be appropriate in the case where there are fewer sensitive points than clusters, so I am not sure how certain clusters would try and skew data to uphold the general data trend. This could lead to overfitted data though this is purely speculation as I do not know how the algorithm works.

------------------------------

6. **Question**: Are there any situations in which even a perfectly fair ML system might still cause or even exacerbate harm? Are there other metrics or areas of social impact you might consider? Justify your opinion.

	Defining fairness is virtually impossible. In the case of job hires, some consider fair to be purely merit based whereas others feel that certain demographics have not had the same opportunities in life and thus are deserving of the job. How this ML system defines fair could either exacerbate systemic biases in the first case, or hire a person who potentially underperforms relative to peers. Calling something as just fair seems so arbitrary. Does this mean equal, or equitable which could be vastly different in certain cases. Other metrics to consider would be family income, school district ranking in the area, and school funding. Collecting more and more data could give a better estimate of how one could have potentially done the best given a situation, but even then, there are too many factors to consider and thus a perfectly fair system does not exist.