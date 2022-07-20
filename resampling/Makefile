default: slides

all: slides handout

SOURCE=yay_resampling

# Need gpp for conditional stuff
# `brew install gpp` on macOS

slides: $(SOURCE).md
	pandoc $(SOURCE).md \
	    --citeproc \
	    -t beamer \
	    -o $(SOURCE)_slides.pdf

handout: $(SOURCE).md
	pandoc $(SOURCE).md \
	    --citeproc \
	    -o $(SOURCE)_handout.pdf

clean:
	rm *.pdf *.html
