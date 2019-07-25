default: slides

all: slides handout

SOURCE=yay_resampling

# Need gpp for conditional stuff
# `brew install gpp` on macOS

slides: $(SOURCE).md
	gpp -H $(SOURCE).md | pandoc \
	    --filter pandoc-citeproc \
	    -t beamer \
	    -o $(SOURCE)_slides.pdf

handout: $(SOURCE).md
	gpp -H -DHANDOUT=1 $(SOURCE).md | pandoc \
	    --filter pandoc-citeproc \
	    -o $(SOURCE)_handout.pdf

clean:
	rm *.pdf *.html
