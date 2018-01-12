# Semi-automated marking for R notebooks

## Summary

I have implemented a system that does automatic grading of R Notebooks, a text / code format used in the R programming language.  This allowed me to mark 266 submissions relatively quickly.

This system is fairly easy to extend to other R homework submissions, and could be integrated into Canvas, to give the students hints about how to fix their code, before they submit.

## Background

This year (2018) I found myself with the task of designing a couple of short
independent study modules on statistics for BIO240.

I decided to ask the students to turn in their homework as [R
Notebooks](http://rmarkdown.rstudio.com/r_notebooks.html).  These are text
documents that contain delimited fragments of R code, called "Chunks".  For example, the following text is part of a notebook file, with a single chunk:

~~~~
Use your [Code School](http://tryr.codeschool.com) skills to do
a scatterplot with "root" on the x-axis and "wood" on the y-axis:

```{r}
#- Here you type the commands to plot wood against root

```

These data are for several different species.  The column "species" has the
identifier for each species.  When R loaded this dataset, it decided that
the "species" column was a `factor`.
~~~~

The notebook file can be executed to generate tables, plots and figures.
These render to high-quality output, such as HTML or PDF.  They are a good
example of technology that makes it easier to do reproducible analysis.

I gave the students a notebook to fill in, with instructions inside the
text. For example, their task was to fill in the text above like this:

~~~~
Use your [Code School](http://tryr.codeschool.com) skills to do
a scatterplot with "root" on the x-axis and "wood" on the y-axis:

```{r}
#- Here you type the commands to plot wood against root
plot(biomass$root, biomass$wood)
```

These data are for several different species.  The column "species" has the
identifier for each species.  When R loaded this dataset, it decided that
the "species" column was a `factor`.
~~~~

The actual notebook from the first semester had 7 questions (chunks) for them to fill in, with many variations as to how they could do it, and get the correct answer.

## Automated grading

To make my life easier, I wrote code to:

* load the R Notebook;
* run every code chunk;
* store the result in terms of text and graphic output.

This code is open-source and public at
https://github.com/matthew-brett/rnbgrader .

I then wrote some supporting code to:

* execute the solution Notebook, and store the results for each chunk;
* compare the solution results to the results from each student notebook, to
  give a score for each question (chunk).

This allowed me to do semi-automated grading by:

* downloading all student submissions as a zip file from Canvas;
* unpacking the zip file, and running the algorithm on each student
  notebook.

Here is the result of me running the algorithm on the solution notebook on my computer:

```
$ python3 bio240_grader.py grade bio240_r_1_solution.Rmd
100.0
```

For about 90% of students notebooks, this grading was correct.  I checked every notebook below the pass threshold of 70 / 100; there were about 6 of 266 that had used variations in plotting that I had not anticipated. I adjusted the marks by hand for those cases.

## Integration with Canvas

I would like to plumb this system into Canvas, so that the students could
click on a button in Canvas, and upload their file for automated grading,
returning a set of hints of type "I could not find a valid answer for
question 3" or "The plot does not right for question 5".  They could then modify their notebook until they have a pass grade before they submit.

This should be possible in principle.   Canvas allows integration of
[external
applications](https://canvas.instructure.com/doc/api/file.tools_intro.html).
These are applications running on some server, that send and receive
messages to Canvas, using a [standard protocol](http://www.imsglobal.org/activity/learning-tools-interoperability).  In my case, I would need to wrap my code inside an small web app that handles the communication with Canvas.  In the middle, my code might reply to a request like ('respond to this file upload') with ('please display the following feedback').  This should be a relatively small amount of work for me and a programmer experienced with using the Canvas API.  I think it would be an excellent test case for expanding the range of what we can do with Canvas, in terms of custom exercises and grading.
