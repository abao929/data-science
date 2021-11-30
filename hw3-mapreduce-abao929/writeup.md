# MapReduce Write Up

## Written questions

1. Your response to Question 1 here.

Potential issues while processing that much data could include just having memory issues. I personally ran into them while dealing with much smaller datasets, and in the graph above, the pipeline seems a bit messy. Having that much data and mapping it 4 times to 2 reducers creates what seems like 8 different combinations of map-reducers, whereas instead one should map something then reduce it twice, then map it a second time in order to streamline it.

2. Your response to Question 2 here.

The pipeline does not produce the correct output because at no point in time do you sort the words by the count, which means when you return the first 10 values, it is just the first ten words that were found rather than the most frequent words.

4. Your response to Question 5 here. You can also choose to *additionally* respond directly to the student's post on Piazza!

I like your suggestion about the idea of creating collaborative datasets, though I just worry that others might not be as careful in their methodology when collecting data, and that their contributions could lead to further bias added. Another issue might be that after enough iterations and augmentation that the new dataset no longer accurately represents the original intention and analysis on it could lead to unaccounted for bias. I’m not sure if I’m misinterpreting but I do not really see how someone else could add a column to the table. For example, if you were to sample a group of people and get some data, how could someone else go out and just add another column of information from those same people. This could potentially lead to a lot of mismatched results if enough people keep adding to it and the table might be filled with null values everywhere and be somewhat useless. Overall it’s a great suggestion, but I guess I’m just a bit more skeptical of other people.

## README

If you have anything to note to the TAs about your submission, please put it in this section.

When running the bash files provided to compare the json files, my json would match the ta_outputs, however when uploading to gradescope I would fail the autograder.